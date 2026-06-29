#!/usr/bin/env bash
# Build an editable Word (.docx) version of the CV from the LaTeX source.
# Self-contained: parses main.tex + sections/body.tex and renders with python-docx.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT="${1:-$REPO_ROOT/Helge_Kminek_Lebenslauf.docx}"

python3 -c "import docx" 2>/dev/null || {
  echo "python-docx is required. Install with: pip3 install -r $SCRIPT_DIR/requirements.txt" >&2
  exit 1
}

python3 "$SCRIPT_DIR/build_docx.py" "$OUTPUT"
