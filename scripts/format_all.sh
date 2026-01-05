#!/usr/bin/env bash
set -euo pipefail

if command -v black >/dev/null; then
    (cd src/python && black .) || true
fi

if command -v ruff >/dev/null; then
    (cd src/python && ruff check . --fix) || true
fi

echo "Formatting complete."
