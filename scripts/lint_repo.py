#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = [
    "README.md",
    "Makefile",
    "src/python/pyproject.toml",
    "formal/lean/lakefile.lean",
    "latex/main.tex",
    ".github/copilot-instructions.md",
]

missing = [p for p in REQUIRED if not Path(p).exists()]
if missing:
    print("Missing required files:")
    for p in missing:
        print("  -", p)
    sys.exit(1)

print("lint_repo: OK")
