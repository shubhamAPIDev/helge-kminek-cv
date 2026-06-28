# LaTeX → Word conversion

Converts `main.tex` + `sections/body.tex` to an editable `.docx` file using [Pandoc](https://pandoc.org/).

This workflow combines ideas from:

- [jay-dennis/tex2docx](https://github.com/jay-dennis/tex2docx) — LaTeX preprocessing before pandoc
- [wmvanvliet/pandoc-tutorial](https://github.com/wmvanvliet/pandoc-tutorial) — pandoc filters and reference templates

The CV uses custom arasgungore macros that pandoc cannot read directly, so `preprocess_cv.py` expands them into a pandoc-friendly `.tex` file first.

## Requirements

- [Pandoc](https://pandoc.org/) 3.x (`brew install pandoc`)
- Python 3

## Usage

From the repository root:

```bash
bash tools/tex2docx/convert_to_docx.sh
```

This writes `Helge_Kminek_Lebenslauf.docx` in the repo root.

To choose a different output path:

```bash
bash tools/tex2docx/convert_to_docx.sh /path/to/output.docx
```

## Files

| File | Purpose |
|------|---------|
| `preprocess_cv.py` | Inlines body content and rewrites CV macros for pandoc |
| `convert_to_docx.sh` | Runs preprocess + pandoc |
| `template.docx` | Optional Word reference styles (from pandoc-tutorial) |
| `main-docx.tex` | Generated intermediate file (gitignored) |

## Notes

- The Word file preserves all CV **content** and section structure. Layout differs slightly from the PDF (no two-column date alignment).
- For submission-quality PDF, compile `main.tex` with pdfLaTeX in Overleaf as before.
- Regenerate the `.docx` after any edit to `sections/body.tex` or `main.tex`.
