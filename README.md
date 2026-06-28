# Dr. Helge Kminek - Lebenslauf

Academic CV for **Dr. Helge Kminek**, using the [arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) LaTeX template with Helge's content.

The working version is the long academic CV in this repository. Helge said he likes this **version 3** layout best compared with the earlier color and black-and-white XeLaTeX drafts.

## Current Status

Completed:

- Created the GitHub/pdfLaTeX CV version using the arasgungore-style layout.
- Applied Helge's latest content corrections and pushed them to GitHub.
- Kept the PDF workflow compatible with **pdfLaTeX / Overleaf**.
- Added a Word conversion workflow because Helge prefers an editable `.docx` and does not want to work directly in Overleaf.
- Generated `Helge_Kminek_Lebenslauf.docx` from the current LaTeX content.
- Pushed the Word conversion tooling and generated Word file to GitHub.

Latest relevant commits:

- `3aabd7f` - Add pandoc-based LaTeX to Word conversion for Helge's CV.
- `bd22cc6` - Apply Helge's content updates.
- `236236e` - Revert a previous alignment/README change that looked worse.
- `4a6d50f` - Fix text overflow with wrapping table columns.

## What Helge Replied

Helge's layout choice:

- He prefers **version 3**, the GitHub/pdfLaTeX version in this repository.

Helge's answer about the Holz/Singer-Brodowski Herausgeberband:

- He sent the published PDF.
- The CV was updated from "in Vorbereitung" to the published 2024 citation:
  `Kminek, H./Singer-Brodowski, M./Holz, V. (Hrsg.) (2024): Bildung für eine nachhaltige Entwicklung im Umbruch?... DOI: 10.3224/84742736.`

Helge's answer about teaching and talks:

- He confirmed **no teaching in Sommersemester 2024**.
- AAU Klagenfurt teaching was added for **Sommersemester 2026**.
- The outdated "Ausblick" wording was removed from teaching and talks.

Helge's Word-file preference:

- He wants a Word file he can edit, instead of having to use Overleaf.
- The generated file is `Helge_Kminek_Lebenslauf.docx`.

## Still Pending

Editorial-role duplication:

- Helge did not yet decide where to keep the two "Editor seit 04/2024" entries.
- They currently overlap between `Herausgeberschaften` and `Funktionen und Gutachtertätigkeiten`.
- Text to clarify with him:
  - `Editor - datum & diskurs` (seit 04/2024): Zeitschrift für Komplementär-, Sekundär- und Reanalysen im Feld der qualitativen Schul- und Unterrichtsforschung.
  - `Editor` (seit 04/2024): Wissenschaftliche Beiträge zur Philosophiedidaktik und Bildungsphilosophie (Scientific Contributions to Philosophy Didactics and Educational Philosophy).

Remaining "in Vorbereitung" entries:

- Helge only resolved the Holz/Singer-Brodowski Herausgeberband.
- Still to confirm:
  - Monographie: `Zu den Aporien der Bildung für eine nachhaltige Entwicklung`.
  - Several article/manuscript entries still marked `(Arbeitstitel, in Vorbereitung)`.

AAU teaching details:

- The AAU Campus data only showed the visible **Sommersemester 2026** courses.
- German titles and any missing semesters such as WS 2024/2025, SS 2025, or WS 2025/2026 should be confirmed with Helge.

Final delivery:

- Recompile the final PDF in Overleaf with pdfLaTeX.
- Send Helge the updated PDF and `Helge_Kminek_Lebenslauf.docx`.
- In the reply, ask him to resolve the open editorial duplication and remaining "in Vorbereitung" entries.

## Issues Encountered

arasgungore CV template:

- The template is designed for a short resume, but Helge's academic CV is much longer.
- Several long German academic entries overflowed in the original table layout.
- This was fixed by changing the internal `\resumeSubheading` table columns to wrapping `p{...}` columns while keeping the same visual style.
- A later alignment/README cleanup looked worse in the PDF, so it was reverted in commit `236236e`.

Direct pandoc conversion:

- Running pandoc directly on `main.tex` did not work well.
- Pandoc could read the header, but it could not understand the custom arasgungore macros such as `\resumeSubheading`, `\resumeProjectHeading`, and `\resumeItem`.
- Pandoc also does not reproduce the exact PDF layout, especially right-aligned date columns.

`jay-dennis/tex2docx` reference repo:

- Useful idea: preprocess LaTeX before sending it to pandoc.
- Not directly usable for this CV because it is built around papers with equations, figures, tables, citations, `refs.bib`, and `pandoc-xnos`.
- Its script defaults to `Example.tex` and does not know the arasgungore CV macros.
- We reused the general preprocessing approach, not the script as-is.

`wmvanvliet/pandoc-tutorial` reference repo:

- Useful idea: use pandoc with a Word reference template and customize conversion around pandoc's limits.
- Not directly usable because its Python filters are specific to one academic paper, with acronyms, figures, citations, and paper-specific commands.
- The `template.docx` was useful as a Word reference document.
- Installing extra filter dependencies was unnecessary for this CV because the main problem was macro expansion, not citations or figures.

Current Word conversion workflow:

- Local pandoc was missing at first, so it was installed with Homebrew.
- Local LaTeX was still not required because the Word export is pandoc-based.
- The first macro approach using TeX conditionals produced bad Word output with stray `&` characters.
- The final approach expands the CV macros in Python before running pandoc.
- The generated Word file is editable and complete, but it is not a pixel-perfect copy of the PDF. Dates are inline rather than right-aligned.

## Repository Structure

| File | Role |
|------|------|
| `main.tex` | arasgungore preamble, commands, header, and document wrapper |
| `sections/body.tex` | Helge's CV content using `\resumeSubheading`, `\resumeItem`, etc. |
| `Helge_Kminek_Lebenslauf.docx` | Generated editable Word version |
| `tools/tex2docx/` | Pandoc-based Word conversion workflow |

## LaTeX / PDF Workflow

Use Overleaf for the final PDF.

1. Upload `main.tex` and `sections/body.tex`.
2. Set compiler to **pdfLaTeX**.
3. Recompile twice.

```bash
pdflatex main.tex
pdflatex main.tex
```

## Word Export Workflow

The Word export uses [Pandoc](https://pandoc.org/) plus a CV-specific preprocessor. It is inspired by:

- [jay-dennis/tex2docx](https://github.com/jay-dennis/tex2docx)
- [wmvanvliet/pandoc-tutorial](https://github.com/wmvanvliet/pandoc-tutorial)

Pandoc cannot read the custom arasgungore macros directly, so `tools/tex2docx/preprocess_cv.py` expands them into pandoc-friendly LaTeX first.

Install pandoc once:

```bash
brew install pandoc
```

Regenerate Word after any content edit:

```bash
bash tools/tex2docx/convert_to_docx.sh
```

Output:

```text
Helge_Kminek_Lebenslauf.docx
```

Notes:

- The Word file preserves the CV content and section structure.
- The Word layout is intentionally more editable than the PDF layout.
- The PDF remains the best source for exact visual formatting.

## Credits

- **Template:** [arasgungore/arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) (MIT)
- **Conversion references:** [jay-dennis/tex2docx](https://github.com/jay-dennis/tex2docx), [wmvanvliet/pandoc-tutorial](https://github.com/wmvanvliet/pandoc-tutorial)
- **Content:** Dr. Helge Kminek
