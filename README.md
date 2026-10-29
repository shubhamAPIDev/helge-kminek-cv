# Dr. Helge Kminek — Lebenslauf

The academic curriculum vitae (Lebenslauf) of **Dr. Helge Kminek**, maintained as
a single, consistent source from which both an editable Word document and a PDF
are produced.

The CV covers his qualifications, professional career, teaching record,
publications, talks, event organisation, editorial and reviewing roles,
third-party funding, committee work, fellowships, and memberships.

**Latest version:** 26.10.2026 (updated from the version shared by Dr. Kminek on 26.10.2026).

Teaching gaps for AAU Klagenfurt have been filled from the shared CV:
- **Wintersemester 2026/2027**: Aktuelle Herausforderungen in Schule und Unterricht; Planetary Boundaries and (Non-)Sustainability
- **Wintersemester 2025/2026**: Sustainable Development I; Sustainable Development I (Parallelgruppe); Planetary Boundaries and (Non-)Sustainability
- **Sommersemester 2025**: Forschungskolloquium I; Sustainable Development II; Sustainability and Fake News; Gebundene Wahlfächer: Schul- und Unterrichtsanalyse entlang und mit der Romanreihe Harry Potter
- **Wintersemester 2024/2025**: Cultural Sustainability; Sustainable Development I

The LaTeX source is up to date. To generate a fresh DOCX + PDF that includes these changes, run the commands below.

---

## Deliverables

| File | Purpose |
|------|---------|
| **`Helge_Kminek_Lebenslauf.docx`** | The editable Word version. This is the working document — open it in Microsoft Word and edit the text directly. |
| **`Helge_Kminek_Lebenslauf.pdf`** | A PDF generated **from the Word file**, so it always matches the Word version exactly (same fonts, spacing, and alignment). |

Both files are kept in sync: the PDF is simply the Word document exported to PDF.

---

## How to generate / update the CV

**To generate a fresh Word + PDF from the LaTeX source** (includes the filled teaching data):

```bash
pip3 install -r tools/tex2docx/requirements.txt   # once
bash tools/tex2docx/convert_to_docx.sh            # writes .docx and .pdf
```

Requires LibreOffice (`soffice`) for the PDF export step.

This rebuilds `Helge_Kminek_Lebenslauf.docx` and then exports
`Helge_Kminek_Lebenslauf.pdf` directly from that Word file, so the two always match.

**To change content later:**
- Edit `sections/body.tex` (or the generated `.docx` in Word), then re-run the same command above.
- Or edit the `.docx` directly and export PDF from Word (`File → Save As → PDF`).

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
6. **AAU Klagenfurt teaching filled** — placeholders for WS 2024/25, SS 2025, WS 2025/26 replaced with actual courses from the 26.10.2026 CV; WS 2026/27 added.
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

### Regenerating Word + PDF from source

```bash
pip3 install -r tools/tex2docx/requirements.txt   # once
bash tools/tex2docx/convert_to_docx.sh            # writes .docx and .pdf
```

Requires LibreOffice (`soffice`) for the automatic PDF export step.

---

## Credits

- **Layout** adapted from the [arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) template (MIT License).
- **Word generation** by `tools/tex2docx/build_docx.py`, built on [python-docx](https://python-docx.readthedocs.io/).
- **Content** © Dr. Helge Kminek.
