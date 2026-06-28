#!/usr/bin/env bash
# Convert Helge Kminek CV from LaTeX to Word using pandoc.
# Based on workflows from:
#   https://github.com/jay-dennis/tex2docx
#   https://github.com/wmvanvliet/pandoc-tutorial
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PREPROCESSED="$SCRIPT_DIR/main-docx.tex"
OUTPUT="${1:-$REPO_ROOT/Helge_Kminek_Lebenslauf.docx}"
TEMPLATE="$SCRIPT_DIR/template.docx"

command -v pandoc >/dev/null 2>&1 || {
  echo "pandoc is required. Install with: brew install pandoc" >&2
  exit 1
}

python3 "$SCRIPT_DIR/preprocess_cv.py" --repo-root "$REPO_ROOT" --output "$PREPROCESSED"

PANDOC_ARGS=(
  -s "$PREPROCESSED"
  -f latex+raw_tex
  -o "$OUTPUT"
)

if [[ -f "$TEMPLATE" ]]; then
  PANDOC_ARGS+=(--reference-doc="$TEMPLATE")
fi

pandoc "${PANDOC_ARGS[@]}"
echo "Wrote $OUTPUT"
