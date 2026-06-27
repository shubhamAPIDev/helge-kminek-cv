# Dr. Helge Kminek — Lebenslauf

Academic curriculum vitae (Lebenslauf) for **Dr. Helge Kminek**, typeset in LaTeX.

The layout is based on [arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) (MIT License). All biographical and academic content belongs to Dr. Helge Kminek.

## Repository structure

```
helge-kminek-cv/
├── main.tex              # Document preamble, header, CV commands
├── sections/
│   └── body.tex          # CV sections (education, career, publications, …)
├── LICENSE               # MIT (layout template)
└── README.md
```

## Compile

### Overleaf

1. Upload this repository (or `main.tex` + `sections/` folder).
2. Compiler: **XeLaTeX** (required for the TeX Gyre Heros font).
3. Recompile twice if references/tables need a second pass.

### Local (TeX Live / MacTeX)

```bash
xelatex main.tex
xelatex main.tex
```

Output: `main.pdf`

## Sections included

- Qualifikationen
- Berufliche Laufbahn
- Verzeichnis der Lehrveranstaltungen
- Publikationsverzeichnis
- Vorträge
- Veranstaltungen — Organisation und Mitwirkung
- Funktionen und Gutachtertätigkeiten
- Eingeworbene Dritt- und Fördermittel
- Gremienarbeit
- Fellowships
- Mitgliedschaften und außeruniversitäres Engagement

## Credits

| Component | Source |
|-----------|--------|
| LaTeX layout | [arasgungore/arasgungore-CV](https://github.com/arasgungore/arasgungore-CV) |
| CV content | Dr. Helge Kminek |

## License

- **Layout / template code:** MIT — see [LICENSE](LICENSE)
- **CV content:** © Dr. Helge Kminek
