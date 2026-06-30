# Dr. Helge Kminek — Lebenslauf

The academic curriculum vitae (Lebenslauf) of **Dr. Helge Kminek**, maintained as
a single, consistent source from which both an editable Word document and a PDF
are produced.

The CV covers his qualifications, professional career, teaching record,
publications, talks, event organisation, editorial and reviewing roles,
third-party funding, committee work, fellowships, and memberships.

---

## Deliverables

| File | Purpose |
|------|---------|
| **`Helge_Kminek_Lebenslauf.docx`** | The editable Word version. This is the working document — open it in Microsoft Word and edit the text directly. |
| **`Helge_Kminek_Lebenslauf.pdf`** | A PDF generated **from the Word file**, so it always matches the Word version exactly (same fonts, spacing, and alignment). |

Both files are kept in sync: the PDF is simply the Word document exported to PDF.

---

## How to edit and update

**To change the content:** open `Helge_Kminek_Lebenslauf.docx` in Word and type
your edits. No special software, no LaTeX, no Overleaf required.

**To refresh the PDF after editing:** in Word, choose
**File → Save As** (or **Print**) and select **PDF** as the format. The PDF will
then reflect the latest Word content.

> Three teaching semesters (Wintersemester 2024/25, Sommersemester 2025,
> Wintersemester 2025/26) currently show the placeholder bullet
> *"Lehrveranstaltungen werden ergänzt."* Replace each placeholder with the
> actual course titles, then remove any that remain unused before sending the CV.

---

## Document design

The layout follows a clean, single-column academic style:

- Centred header with name (small caps), title, addresses, and contact details.
- Section headings in small caps, underlined with a horizontal rule.
- Each entry shows its description on the left and its **date right-aligned** on
  the same line; longer entries place the role/subtitle in italics beneath.
- A serif typeface (**Times New Roman**) throughout, with consistent spacing.

---

## Changes made

### Content updates (based on Dr. Kminek's confirmations)

1. **Herausgeberband Holz/Singer-Brodowski** — updated from "in Vorbereitung" to
   the published 2024 citation:
   *Kminek, H./Singer-Brodowski, M./Holz, V. (Hrsg.) (2024): Bildung für eine
   nachhaltige Entwicklung im Umbruch? … DOI: 10.3224/84742736.*
2. **Duplicate editor roles removed** — the two "Editor (seit 04/2024)" entries
   were appearing under both *Herausgeberschaften* and *Funktionen und
   Gutachtertätigkeiten*. They are now kept only under *Herausgeberschaften*.
3. **Editor start-date corrected** — the book series
   *Wissenschaftliche Beiträge zur Philosophiedidaktik und Bildungsphilosophie*
   now consistently reads **seit 2016** (with Christian Thein); the conflicting
   "04/2024" entry was removed with the duplicate above.
4. **Marburg teaching entry removed** — the Wintersemester 2023/2024 course at
   Universität Marburg was deleted entirely (it had been cancelled at short
   notice).
5. **Outdated "Ausblick" labels removed** — from both the teaching list and the
   Vorträge section.
6. **AAU Klagenfurt teaching expanded** — Sommersemester 2026 listed with its
   courses; headings added for **Wintersemester 2024/2025, Sommersemester 2025,
   and Wintersemester 2025/2026** (with placeholder bullets to be completed); and
   Sommersemester 2024 noted as having no teaching.
7. **Works "in Vorbereitung" retained** — the monograph and several
   working-title articles were kept in, per Dr. Kminek's request to review them
   himself.

### Layout and formatting

8. **Consistent serif typography** — Times New Roman with small-caps headings,
   matching the original PDF style.
9. **Uniform entry alignment** — every single-item entry (qualifications,
   editorial/reviewing roles, committee work, fellowships, etc.) is rendered as
   one line with the text on the left and the date right-aligned, eliminating
   earlier "floating dates" and inconsistent bold/italic styling.
10. **Long descriptions no longer wrap awkwardly** — role descriptions in the
    event-organisation section were moved to the wide left column instead of the
    narrow date column, so they no longer break into a ragged stack.
11. **Even spacing throughout** — tightened gaps between entries, added space
    above section sub-labels, and removed stray blank lines.
12. **Flush-left alignment** — entry text now lines up exactly with the section
    labels above it (table padding removed).
13. **Entries kept together** — an entry's title, date, and role no longer split
    across a page break.

### Production workflow

14. **Editable Word output** — Dr. Kminek requested an editable Word file rather
    than working in Overleaf, so the CV is delivered as `.docx`.
15. **PDF from Word** — the PDF is produced directly from the Word document,
    guaranteeing the two are always visually identical.

---

## Repository structure

| Path | Role |
|------|------|
| `Helge_Kminek_Lebenslauf.docx` | Editable Word version (the deliverable) |
| `main.tex`, `sections/body.tex` | LaTeX source the Word file is generated from |
| `tools/tex2docx/build_docx.py` | Self-contained generator (LaTeX source → Word, via python-docx) |
| `tools/tex2docx/convert_to_docx.sh` | Convenience wrapper for the generator |
| `tools/tex2docx/requirements.txt` | Sole dependency (`python-docx`) |

### Regenerating the Word file from source (optional, for maintainers)

The Word document can be rebuilt from the LaTeX source at any time:

```bash
pip3 install -r tools/tex2docx/requirements.txt   # once
bash tools/tex2docx/convert_to_docx.sh            # writes Helge_Kminek_Lebenslauf.docx
```

This is only needed if the content is edited in the LaTeX source. Day to day, the
Word file is edited directly.

---

## Credits

- **Layout** adapted from the [arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) template (MIT License).
- **Word generation** by `tools/tex2docx/build_docx.py`, built on [python-docx](https://python-docx.readthedocs.io/).
- **Content** © Dr. Helge Kminek.
