# Dr. Helge Kminek — Lebenslauf

Academic CV for **Dr. Helge Kminek**, using the [arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) LaTeX template **strictly** (same macros and layout code), filled with Helge's data.

## Structure

| File | Role |
|------|------|
| `main.tex` | arasgungore preamble, commands, and header (unchanged template code) |
| `sections/body.tex` | Helge's CV content using `\resumeSubheading`, `\resumeItem`, etc. |

## arasgungore macros used

- `\resumeSubheading` — Qualifikationen, Berufliche Laufbahn, Gutachtertätigkeiten, …
- `\resumeSubSubheading` — semester groups, subsections
- `\resumeProjectHeading` — publication subsections (Monographien, Poster, …)
- `\resumeItem` / `\resumeItemListStart` — course lists, publications, talks, memberships

## Compile (Overleaf)

1. Upload `main.tex` + `sections/body.tex`
2. Compiler: **pdfLaTeX**
3. Recompile

```bash
pdflatex main.tex
pdflatex main.tex
```

## Word export (.docx)

Helge can edit the CV in Microsoft Word without Overleaf. Regenerate after any content change:

```bash
brew install pandoc   # once
bash tools/tex2docx/convert_to_docx.sh
```

Output: `Helge_Kminek_Lebenslauf.docx` in the repo root.

See `tools/tex2docx/README.md` for details. Conversion uses [Pandoc](https://pandoc.org/) with a CV-specific preprocessor (inspired by [tex2docx](https://github.com/jay-dennis/tex2docx) and [pandoc-tutorial](https://github.com/wmvanvliet/pandoc-tutorial)).

## Note

Helge's full academic CV is long (~many pages). arasgungore's original template is a short 2-page résumé; the **same code patterns** are applied throughout, but the document is longer because of the amount of content.

## Credits

- **Template:** [arasgungore/arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) (MIT)
- **Content:** Dr. Helge Kminek
