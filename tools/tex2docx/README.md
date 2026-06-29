# LaTeX → Word conversion

Builds an editable `Helge_Kminek_Lebenslauf.docx` from the LaTeX source
(`main.tex` + `sections/body.tex`).

`build_docx.py` parses the arasgungore CV macros directly and renders the Word
file with [python-docx](https://python-docx.readthedocs.io/), reproducing the
PDF's layout: a centered header, section titles underlined with a rule, and
two-column entry rows with the date right-aligned. The output is plain editable
Word text (borderless tables, no text boxes), so it can be edited without
touching LaTeX/Overleaf.

This is self-contained — no pandoc, no LaTeX install, no external template.

## Requirements

- Python 3
- `python-docx` (`pip3 install -r tools/tex2docx/requirements.txt`)

## Usage

From the repository root:

```bash
bash tools/tex2docx/convert_to_docx.sh
```

This writes `Helge_Kminek_Lebenslauf.docx` in the repo root. To choose a
different output path:

```bash
bash tools/tex2docx/convert_to_docx.sh /path/to/output.docx
```

Or call the builder directly:

```bash
python3 tools/tex2docx/build_docx.py [output.docx]
```

## Files

| File | Purpose |
|------|---------|
| `build_docx.py` | Parses the CV LaTeX and renders the `.docx` |
| `convert_to_docx.sh` | Convenience wrapper (checks deps, runs the builder) |
| `requirements.txt` | Python dependency (`python-docx`) |

## Supported macros

`build_docx.py` understands the arasgungore entry macros used in this CV:
`\resumeSubheading` (org / date / role / location → two-column row),
`\resumeSubSubheading` (italic sub-heading, e.g. a semester label),
`\resumeProjectHeading`, and `\resumeItem` / `\resumeSubItem` (bullets).
Inline `\textbf`/`\textit`/`\emph` and `\href` are preserved.

## Notes

- The Word layout closely mirrors the PDF but is not pixel-identical — Word and
  LaTeX paginate differently, so the page count may differ.
- For submission-quality PDF, compile `main.tex` with pdfLaTeX in Overleaf.
- Regenerate the `.docx` after any edit to `sections/body.tex` or `main.tex`.
