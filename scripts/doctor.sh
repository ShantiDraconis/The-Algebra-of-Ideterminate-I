#!/usr/bin/env bash
set -euo pipefail

echo "== Doctor =="
command -v python >/dev/null && python --version || (echo "python missing" && exit 1)
command -v git >/dev/null && git --version || (echo "git missing" && exit 1)

if command -v latexmk >/dev/null; then
    latexmk -v | head -n 1
else
    echo "latexmk not found (LaTeX build will fail unless installed)."
fi

if command -v lake >/dev/null; then
    lake --version || true
else
    echo "Lean lake not found (Lean build will fail unless installed)."
fi

echo "Doctor finished."
