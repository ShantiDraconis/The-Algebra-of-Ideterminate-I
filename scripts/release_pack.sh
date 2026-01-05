#!/usr/bin/env bash
set -euo pipefail

OUTDIR="${1:-release_pack}"
mkdir -p "$OUTDIR"

# Build artifacts (best-effort)
make latex || true
make python_test || true

# Copy key deliverables
cp -f README.md "$OUTDIR/" || true
cp -f LICENSE "$OUTDIR/" || true
cp -f CITATION.cff "$OUTDIR/" || true

if [[ -f latex/main.pdf ]]; then
    cp -f latex/main.pdf "$OUTDIR/" || true
fi
if [[ -f latex/build/main.pdf ]]; then
    cp -f latex/build/main.pdf "$OUTDIR/" || true
fi

echo "Release pack prepared in: $OUTDIR"
