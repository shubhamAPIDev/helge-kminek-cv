#!/usr/bin/env bash
# Build Word (.docx) and PDF from the LaTeX source in one step.
# 1. build_docx.py renders Helge_Kminek_Lebenslauf.docx from main.tex + sections/body.tex
# 2. LibreOffice exports the PDF directly from that Word file
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DOCX_OUTPUT="${1:-$REPO_ROOT/Helge_Kminek_Lebenslauf.docx}"
PDF_OUTPUT="${DOCX_OUTPUT%.docx}.pdf"

python3 -c "import docx" 2>/dev/null || {
  echo "python-docx is required. Install with: pip3 install -r $SCRIPT_DIR/requirements.txt" >&2
  exit 1
}

python3 "$SCRIPT_DIR/build_docx.py" "$DOCX_OUTPUT"
echo "Wrote $DOCX_OUTPUT"

SOFFICE=$(command -v soffice || true)
if [[ -z "$SOFFICE" ]]; then
  echo "LibreOffice (soffice) not found; skipped PDF export." >&2
  echo "Install LibreOffice to auto-generate the matching PDF." >&2
  exit 0
fi

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT
cp "$DOCX_OUTPUT" "$tmpdir/"
"$SOFFICE" --headless --convert-to pdf --outdir "$tmpdir" "$tmpdir/$(basename "$DOCX_OUTPUT")" >/dev/null 2>&1
mv "$tmpdir/$(basename "$PDF_OUTPUT")" "$PDF_OUTPUT"
echo "Wrote $PDF_OUTPUT"
