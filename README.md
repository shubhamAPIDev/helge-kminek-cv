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

Word export — earlier pandoc attempt:

- Pandoc could not read the custom arasgungore macros (`\resumeSubheading`, `\resumeProjectHeading`, `\resumeItem`), so the macros had to be expanded first.
- Even after expansion, pandoc produced a flat layout: left-aligned header, no section rules, and dates crammed inline rather than right-aligned. It did not look like the PDF.
- Off-the-shelf LaTeX→docx repos (`jay-dennis/tex2docx`, `wmvanvliet/pandoc-tutorial`) were built around academic papers (equations, figures, citations) and did not fit a resume template.

Word export — current workflow:

- Replaced pandoc with a small, self-contained renderer, `tools/tex2docx/build_docx.py`, that parses the arasgungore macros and writes the `.docx` directly with `python-docx`.
- It reproduces the PDF layout — centered header, section titles with a bottom rule, and two-column entry rows with **right-aligned dates** — while keeping the output as plain editable Word text (borderless tables, no text boxes).
- No pandoc, no LaTeX install, and no external reference template are needed; the only dependency is `python-docx`.

## Repository Structure

| File | Role |
|------|------|
| `main.tex` | arasgungore preamble, commands, header, and document wrapper |
| `sections/body.tex` | Helge's CV content using `\resumeSubheading`, `\resumeItem`, etc. |
| `Helge_Kminek_Lebenslauf.docx` | Generated editable Word version |
| `tools/tex2docx/` | Self-contained LaTeX→Word renderer (`build_docx.py`, python-docx) |

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

The Word export is produced by `tools/tex2docx/build_docx.py`, a small
self-contained renderer that parses the arasgungore CV macros and writes the
`.docx` directly with [python-docx](https://python-docx.readthedocs.io/). No
pandoc, LaTeX install, or external template is required.

Install the one dependency once:

```bash
pip3 install -r tools/tex2docx/requirements.txt
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

- The Word layout mirrors the PDF — centered header, section rules, and
  right-aligned dates — and stays plain editable text (no text boxes).
- It is not pixel-identical: Word and LaTeX paginate differently.
- The PDF (pdfLaTeX in Overleaf) remains the source for exact visual formatting.

## Credits

- **Template:** [arasgungore/arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) (MIT)
- **Word export:** `tools/tex2docx/build_docx.py`, built on [python-docx](https://python-docx.readthedocs.io/)
- **Content:** Dr. Helge Kminek
