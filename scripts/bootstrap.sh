#!/usr/bin/env bash
set -euo pipefail

python -m pip install -U pip
python -m pip install -U "pytest>=8" "ruff>=0.5" "mypy>=1.10" "black>=24.0"

echo "Bootstrap complete."
