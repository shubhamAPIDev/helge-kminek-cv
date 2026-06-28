#!/usr/bin/env python3
"""Prepare Helge Kminek CV LaTeX for pandoc -> DOCX conversion."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PREAMBLE = r"""% Auto-generated for pandoc conversion. Do not edit by hand.
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[ngerman]{babel}
\usepackage[hidelinks]{hyperref}

"""

HEADER = r"""
\begin{center}
\textbf{\Large Dr.\ Helge Kminek}\par
\textit{Lebenslauf}\par\vspace{6pt}
AAU Klagenfurt, Sterneckstra{\ss}e 15, A-9020 Klagenfurt \textbar\
Mathildenstra{\ss}e 5, 55116 Mainz\par
\href{mailto:HelgeKminek@posteo.de}{HelgeKminek@posteo.de} \textbar\
\href{mailto:Helge.Kminek@aau.at}{Helge.Kminek@aau.at}\par
Geboren am 10.02.1980, Offenbach am Main
\end{center}

"""

MACRO_ALIASES = {
    r"\resumeSubHeadingListStart": r"\begin{itemize}",
    r"\resumeSubHeadingListEnd": r"\end{itemize}",
    r"\resumeItemListStart": r"\begin{itemize}",
    r"\resumeItemListEnd": r"\end{itemize}",
}

CLEANUP_PATTERNS = [
    (re.compile(r"\\faMapMarker\s*\\hspace\{[^}]+\}"), ""),
    (re.compile(r"\\faAt\s*\\hspace\{[^}]+\}"), ""),
    (re.compile(r"\$\|$"), r"\\textbar\\"),
    (re.compile(r"\\vspace\{[^}]+\}"), ""),
    (re.compile(r"\\scshape"), ""),
    (re.compile(r"\\Huge"), r"\\Large"),
    (re.compile(r"\\small"), ""),
    (re.compile(r"\\hspace\{[^}]+\}"), " "),
    (re.compile(r"^%.*$", re.MULTILINE), ""),
    (re.compile(r"\{\s*\\itshape\\bfseries\\small\s+([^}]+)\}"), r"\\textbf{\\textit{\1}}"),
    (re.compile(r"\\par\\vspace\{[^}]+\}"), ""),
    (re.compile(r"\n{3,}"), "\n\n"),
]


def read_body(repo_root: Path) -> str:
    body_path = repo_root / "sections" / "body.tex"
    if not body_path.exists():
        raise FileNotFoundError(f"Missing body file: {body_path}")
    return body_path.read_text(encoding="utf-8")


def parse_brace_groups(text: str, start: int) -> tuple[list[str], int]:
    """Parse consecutive {..} groups beginning at or after start."""
    args: list[str] = []
    pos = start
    length = len(text)
    while pos < length:
        while pos < length and text[pos].isspace():
            pos += 1
        if pos >= length or text[pos] != "{":
            break
        depth = 0
        begin = pos
        pos += 1
        while pos < length:
            ch = text[pos]
            if ch == "{":
                depth += 1
            elif ch == "}":
                if depth == 0:
                    args.append(text[begin + 1 : pos])
                    pos += 1
                    break
                depth -= 1
            pos += 1
    return args, pos


def strip_outer(text: str) -> str:
    return text.strip()


def expand_subheading(args: list[str]) -> str:
    a, b, c, d = (strip_outer(x) for x in (args + ["", "", "", ""])[:4])
    lines: list[str] = ["\\item"]
    if a:
        line = f"\\textbf{{{a}}}"
        if b:
            line += f" (\\textit{{{b}}})"
        lines.append(line)
    elif b:
        lines.append(f"\\textit{{{b}}}")
    if c:
        lines.append(c)
    if d:
        lines.append(f"\\textit{{{d}}}")
    return "\n".join(lines) + "\n"


def expand_sub_subheading(args: list[str]) -> str:
    a, b = (strip_outer(x) for x in (args + ["", ""])[:2])
    if b:
        return f"\\item[] \\textbf{{{a}}} (\\textit{{{b}}})\n"
    return f"\\item[] \\textbf{{{a}}}\n"


def expand_project_heading(args: list[str]) -> str:
    a = strip_outer(args[0]) if args else ""
    return f"\\item[] {a}\n"


def expand_simple_macro(name: str, args: list[str]) -> str:
    if name == r"\resumeItem":
        return f"\\item {strip_outer(args[0])}\n"
    if name == r"\resumeSubItem":
        return f"\\item {strip_outer(args[0])}\n"
    if name == r"\resumeSubheading":
        return expand_subheading(args)
    if name == r"\resumeSubSubheading":
        return expand_sub_subheading(args)
    if name == r"\resumeProjectHeading":
        return expand_project_heading(args)
    joined = "".join(f"{{{strip_outer(arg)}}}" for arg in args)
    return f"{name}{joined}\n"


def expand_macros(text: str) -> str:
    known = sorted(
        [
            r"\resumeItemListStart",
            r"\resumeItemListEnd",
            r"\resumeSubHeadingListStart",
            r"\resumeSubHeadingListEnd",
            r"\resumeSubSubheading",
            r"\resumeProjectHeading",
            r"\resumeSubheading",
            r"\resumeSubItem",
            r"\resumeItem",
        ],
        key=len,
        reverse=True,
    )
    out: list[str] = []
    pos = 0
    length = len(text)
    while pos < length:
        match = None
        for name in known:
            if text.startswith(name, pos):
                match = name
                break
        if match is None:
            out.append(text[pos])
            pos += 1
            continue
        pos += len(match)
        if match in MACRO_ALIASES:
            out.append(MACRO_ALIASES[match] + "\n")
            continue
        args, pos = parse_brace_groups(text, pos)
        out.append(expand_simple_macro(match, args))
    return "".join(out)


def apply_aliases_and_cleanup(text: str) -> str:
    for pattern, repl in CLEANUP_PATTERNS:
        text = pattern.sub(repl, text)
    return text


def build_docx_tex(body_tex: str) -> str:
    body_tex = expand_macros(body_tex)
    body_tex = apply_aliases_and_cleanup(body_tex)
    return PREAMBLE + "\\begin{document}\n" + HEADER + body_tex + "\n\\end{document}\n"


def preprocess(repo_root: Path, output_path: Path) -> None:
    body_tex = read_body(repo_root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_docx_tex(body_tex), encoding="utf-8")
    print(f"Wrote {output_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Path to helge-kminek-cv repository root",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "main-docx.tex",
        help="Output preprocessed .tex file",
    )
    args = parser.parse_args()
    preprocess(args.repo_root, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
