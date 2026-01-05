#!/usr/bin/env bash
# bootstrap_repo.sh
# Creates the full repository structure + core files for:
# "The Algebra of the Indeterminate — Buyer Hub & Formalization Repository"
# Usage (inside Codespace):
#   chmod +x bootstrap_repo.sh
#   ./bootstrap_repo.sh algebra-of-the-indeterminate-hub
#
# Optional:
#   ./bootstrap_repo.sh .   # generate in current folder (must be empty or you accept merges)

set -euo pipefail

ROOT="${1:-algebra-of-the-indeterminate-hub}"

# If ROOT is ".", work in current directory. Else create and enter it.
if [[ "$ROOT" != "." ]]; then
  mkdir -p "$ROOT"
fi

cd "$ROOT"

# ---------- helpers ----------
write_file() {
  local path="$1"
  shift
  mkdir -p "$(dirname "$path")"
  cat > "$path" <<EOF
$*
EOF
}

# More robust heredoc writer (keeps exact content).
write_file_hd() {
  local path="$1"
  mkdir -p "$(dirname "$path")"
  cat > "$path"
}

# ---------- directory tree ----------
mkdir -p \
  docker \
  scripts/ci \
  .github/ISSUE_TEMPLATE \
  .github/DISCUSSION_TEMPLATE \
  .github/workflows \
  docs/theory/axioms \
  docs/theory/algebra \
  docs/theory/calculus \
  docs/theory/wheel \
  docs/theory/logic_model_theory \
  docs/theory/physics \
  docs/theory/computation \
  docs/tutorials \
  docs/governance/decision_records \
  book/source \
  book/extracted \
  book/errata \
  latex/sections \
  latex/appendices \
  latex/figures/wheel \
  latex/figures/flowcharts \
  latex/figures/physics \
  formal/lean/IAlgebra/ModelTheory \
  formal/lean/Tests \
  formal/lean/scripts \
  formal/coq \
  src/python/ialgebra/validation \
  src/python/cli \
  src/python/experiments/cosmology \
  src/python/experiments/numerical \
  src/python/tests \
  src/js/playground/src \
  notebooks \
  data/axioms \
  data/examples \
  data/benchmarks \
  data/results \
  hub/buyers \
  hub/research_calls \
  hub/templates \
  audits

# ---------- root files ----------
write_file_hd README.md <<'EOF'
# The Algebra of the Indeterminate — Buyer Hub & Formalization Repository

This repository is the **expanded technical companion** to the book:

**"The Algebra of the Indeterminate: Ultra Advanced Theory Starting from I = 0/0"**

## What this repo is
- A **reproducible, auditable** implementation and formalization of the book's framework.
- A **buyer hub**: issues, discussions, errata, replication reports, and extensions.
- A **Copilot-first engineering spec**: the repository is structured so GitHub Copilot can implement
  modules in a controlled, test-driven way.

## Quick start (Codespaces recommended)

### Option A — Docker (most reliable)
```bash
docker compose up -d
docker compose exec app bash
make doctor
make all
```

### Option B — Local Python/Node
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
make test
```

## Repository structure
```
├── docker/              # Container definitions
├── scripts/             # Automation and CI/CD scripts
├── .github/             # Issue templates, workflows, discussions
├── docs/                # Theory documentation
│   ├── theory/          # Mathematical theory sections
│   ├── tutorials/       # User guides and tutorials
│   └── governance/      # Decision records and governance
├── book/                # Book companion materials
│   ├── source/          # Source content
│   ├── extracted/       # Extracted code/proofs
│   └── errata/          # Corrections and clarifications
├── latex/               # LaTeX source for papers/book
├── formal/              # Formal verification
│   ├── lean/            # Lean 4 proofs
│   └── coq/             # Coq proofs
├── src/                 # Implementation code
│   ├── python/          # Python library
│   └── js/              # JavaScript playground
├── notebooks/           # Jupyter notebooks
├── data/                # Datasets and benchmarks
├── hub/                 # Buyer hub materials
└── audits/              # Security and correctness audits
```

## Key files
- `Makefile`: Common development tasks
- `docker-compose.yml`: Container orchestration
- `requirements.txt`: Python dependencies
- `package.json`: Node.js dependencies
- `lakefile.lean`: Lean build configuration

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
See [LICENSE](LICENSE) for details.
EOF

write_file_hd .gitignore <<'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
venv/
ENV/
env/
.venv

# Jupyter
.ipynb_checkpoints
*.ipynb_checkpoints

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
.eslintcache

# Lean
build/
.lake/
lake-packages/

# LaTeX
*.aux
*.log
*.out
*.toc
*.bbl
*.blg
*.synctex.gz
*.fdb_latexmk
*.fls

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Temporary files
tmp/
temp/
*.tmp

# Results
data/results/*.json
data/results/*.csv
!data/results/.gitkeep
EOF

write_file_hd LICENSE <<'EOF'
MIT License

Copyright (c) 2026 The Algebra of the Indeterminate Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

write_file_hd CONTRIBUTING.md <<'EOF'
# Contributing to The Algebra of the Indeterminate

Thank you for your interest in contributing!

## Getting Started
1. Fork the repository
2. Clone your fork
3. Create a branch for your work
4. Make your changes
5. Run tests: `make test`
6. Submit a pull request

## Code Standards
- Python: Follow PEP 8, use type hints
- JavaScript: Follow standard.js conventions
- Lean: Follow mathlib4 conventions
- Documentation: Use clear, precise language

## Testing
All contributions must include appropriate tests.

## Issues
Use the issue templates in `.github/ISSUE_TEMPLATE/` for:
- Bug reports
- Feature requests
- Theoretical questions
- Errata submissions

## Discussions
For open-ended topics, use GitHub Discussions.
EOF

write_file_hd Makefile <<'EOF'
.PHONY: help doctor all clean test lint format build

help:
	@echo "Available targets:"
	@echo "  doctor      - Check system dependencies"
	@echo "  all         - Build everything"
	@echo "  clean       - Remove build artifacts"
	@echo "  test        - Run all tests"
	@echo "  lint        - Run linters"
	@echo "  format      - Format code"
	@echo "  build       - Build all components"

doctor:
	@echo "Checking dependencies..."
	@command -v python3 >/dev/null 2>&1 || { echo "Python 3 required"; exit 1; }
	@command -v node >/dev/null 2>&1 || { echo "Node.js required"; exit 1; }
	@command -v lean >/dev/null 2>&1 || { echo "Warning: Lean not found"; }
	@echo "Dependencies OK"

all: build test

clean:
	rm -rf build/ dist/ .lake/ lake-packages/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name node_modules -exec rm -rf {} + 2>/dev/null || true

test:
	pytest src/python/tests/ -v
	npm test --prefix src/js/playground

lint:
	flake8 src/python/
	mypy src/python/
	npm run lint --prefix src/js/playground

format:
	black src/python/
	isort src/python/
	npm run format --prefix src/js/playground

build:
	@echo "Building Python package..."
	pip install -e src/python/
	@echo "Building JavaScript playground..."
	npm run build --prefix src/js/playground
	@echo "Building Lean proofs..."
	cd formal/lean && lake build || echo "Lean build skipped"
EOF

# ---------- Docker files ----------
write_file_hd docker-compose.yml <<'EOF'
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: docker/Dockerfile
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: sleep infinity
    environment:
      - PYTHONUNBUFFERED=1
    ports:
      - "8888:8888"  # Jupyter
      - "3000:3000"  # Playground

  lean:
    image: leanprover/lean4:latest
    volumes:
      - ./formal/lean:/workspace
    working_dir: /workspace
    command: lake build
EOF

write_file_hd docker/Dockerfile <<'EOF'
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    nodejs \
    npm \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Lean 4
RUN curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y
ENV PATH="/root/.elan/bin:${PATH}"

WORKDIR /workspace

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY package.json .
RUN npm install

CMD ["/bin/bash"]
EOF

# ---------- Python setup ----------
write_file_hd requirements.txt <<'EOF'
numpy>=1.24.0
scipy>=1.10.0
sympy>=1.12
matplotlib>=3.7.0
jupyter>=1.0.0
pytest>=7.4.0
pytest-cov>=4.1.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.4.0
isort>=5.12.0
EOF

write_file_hd src/python/setup.py <<'EOF'
from setuptools import setup, find_packages

setup(
    name="ialgebra",
    version="0.1.0",
    description="Implementation of the Algebra of the Indeterminate",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "sympy>=1.12",
    ],
    python_requires=">=3.9",
)
EOF

write_file_hd src/python/ialgebra/__init__.py <<'EOF'
"""
The Algebra of the Indeterminate (I-Algebra)

A Python implementation of the algebraic framework starting from I = 0/0.
"""

__version__ = "0.1.0"
EOF

write_file_hd src/python/ialgebra/core.py <<'EOF'
"""
Core algebraic structures for I-Algebra.
"""

from typing import Any, Optional


class Indeterminate:
    """
    Represents the indeterminate I = 0/0.
    """
    
    def __init__(self):
        self.value = None  # Represents 0/0
    
    def __repr__(self) -> str:
        return "I"
    
    def __str__(self) -> str:
        return "I"


def create_indeterminate() -> Indeterminate:
    """Create an instance of the indeterminate."""
    return Indeterminate()
EOF

write_file_hd src/python/tests/__init__.py <<'EOF'
"""Tests for ialgebra package."""
EOF

write_file_hd src/python/tests/test_core.py <<'EOF'
"""Tests for core I-Algebra functionality."""

import pytest
from ialgebra.core import Indeterminate, create_indeterminate


def test_indeterminate_creation():
    """Test creating an indeterminate."""
    i = create_indeterminate()
    assert isinstance(i, Indeterminate)
    assert str(i) == "I"


def test_indeterminate_repr():
    """Test string representation."""
    i = Indeterminate()
    assert repr(i) == "I"
EOF

# ---------- JavaScript setup ----------
write_file_hd package.json <<'EOF'
{
  "name": "ialgebra-playground",
  "version": "0.1.0",
  "description": "Interactive playground for I-Algebra",
  "main": "src/js/playground/src/index.js",
  "scripts": {
    "test": "jest",
    "lint": "eslint src/js/playground/src",
    "format": "prettier --write 'src/js/playground/src/**/*.js'",
    "build": "webpack --config src/js/playground/webpack.config.js",
    "dev": "webpack serve --config src/js/playground/webpack.config.js"
  },
  "keywords": ["algebra", "mathematics", "indeterminate"],
  "author": "The Algebra of the Indeterminate Project",
  "license": "MIT",
  "devDependencies": {
    "eslint": "^8.45.0",
    "jest": "^29.6.0",
    "prettier": "^3.0.0",
    "webpack": "^5.88.0",
    "webpack-cli": "^5.1.0",
    "webpack-dev-server": "^4.15.0"
  },
  "dependencies": {
    "mathjs": "^11.9.0"
  }
}
EOF

write_file_hd src/js/playground/src/index.js <<'EOF'
/**
 * I-Algebra Playground
 * Interactive environment for exploring the Algebra of the Indeterminate
 */

class Indeterminate {
  constructor() {
    this.type = 'indeterminate';
  }
  
  toString() {
    return 'I';
  }
}

function createIndeterminate() {
  return new Indeterminate();
}

module.exports = { Indeterminate, createIndeterminate };
EOF

# ---------- Lean setup ----------
write_file_hd formal/lean/lakefile.lean <<'EOF'
import Lake
open Lake DSL

package «IAlgebra» {
  -- add package configuration options here
}

lean_lib «IAlgebra» {
  -- add library configuration options here
}

@[default_target]
lean_exe «ialgebra» {
  root := `Main
}
EOF

write_file_hd formal/lean/Main.lean <<'EOF'
-- Main entry point for I-Algebra formalization

import IAlgebra.Basic

def main : IO Unit :=
  IO.println "I-Algebra Formalization"
EOF

write_file_hd formal/lean/IAlgebra/Basic.lean <<'EOF'
-- Basic definitions for the Algebra of the Indeterminate

/-- The indeterminate I = 0/0 -/
axiom I : ℚ

/-- Axiom: I represents 0/0 -/
axiom I_def : I = 0 / 0
EOF

# ---------- GitHub templates ----------
write_file_hd .github/ISSUE_TEMPLATE/bug_report.md <<'EOF'
---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. 
2. 
3. 

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.11]
- Package version: [e.g., 0.1.0]

**Additional context**
Add any other context about the problem here.
EOF

write_file_hd .github/ISSUE_TEMPLATE/feature_request.md <<'EOF'
---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
EOF

write_file_hd .github/ISSUE_TEMPLATE/theoretical_question.md <<'EOF'
---
name: Theoretical question
about: Ask about the mathematical theory
title: '[THEORY] '
labels: question, theory
assignees: ''
---

**Question**
State your theoretical question clearly.

**Context**
- Book section/page reference (if applicable):
- Related concepts:

**What you've tried**
Describe any research or attempts to answer this yourself.

**Additional context**
Any additional mathematical context or references.
EOF

write_file_hd .github/workflows/ci.yml <<'EOF'
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test-python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -e src/python/
      - name: Lint
        run: |
          flake8 src/python/ --count --select=E9,F63,F7,F82 --show-source --statistics
      - name: Test
        run: |
          pytest src/python/tests/ -v --cov=ialgebra

  test-lean:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Lean
        run: |
          curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y
          echo "$HOME/.elan/bin" >> $GITHUB_PATH
      - name: Build Lean
        run: |
          cd formal/lean
          lake build
EOF

# ---------- Documentation ----------
write_file_hd docs/theory/axioms/README.md <<'EOF'
# Axioms of I-Algebra

This directory contains the fundamental axioms of the Algebra of the Indeterminate.

## Core Axiom
The foundation is: **I = 0/0**

## Derived Properties
(To be documented)
EOF

write_file_hd docs/tutorials/getting_started.md <<'EOF'
# Getting Started with I-Algebra

## Installation

### Using Docker
```bash
docker compose up -d
docker compose exec app bash
```

### Local Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e src/python/
```

## First Steps

### Python
```python
from ialgebra.core import create_indeterminate

i = create_indeterminate()
print(i)  # Output: I
```

### JavaScript
```javascript
const { createIndeterminate } = require('./src/js/playground/src/index.js');

const i = createIndeterminate();
console.log(i.toString());  // Output: I
```

## Next Steps
- Explore the [theory documentation](../theory/)
- Try the example notebooks in `notebooks/`
- Read the book companion materials in `book/`
EOF

write_file_hd hub/buyers/README.md <<'EOF'
# Buyer Hub

Welcome to the buyer hub for "The Algebra of the Indeterminate" book.

## Resources for Buyers
- **Errata**: See `book/errata/` for corrections and clarifications
- **Code examples**: All code from the book is in `book/extracted/`
- **Issues**: Report problems or ask questions via GitHub Issues
- **Discussions**: Join theoretical discussions via GitHub Discussions

## Getting Help
1. Check the [FAQ](../docs/FAQ.md)
2. Search existing issues
3. Create a new issue using the appropriate template

## Contributing
See [CONTRIBUTING.md](../../CONTRIBUTING.md) for how to contribute corrections or extensions.
EOF

write_file_hd notebooks/example_01_basic.ipynb <<'EOF'
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Example 1: Basic I-Algebra\n",
    "\n",
    "This notebook demonstrates the basic concepts of the Algebra of the Indeterminate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "from ialgebra.core import create_indeterminate\n",
    "\n",
    "i = create_indeterminate()\n",
    "print(f\"The indeterminate: {i}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Properties\n",
    "\n",
    "I represents 0/0, the fundamental indeterminate form."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
EOF

# ---------- Data placeholder files ----------
write_file_hd data/axioms/.gitkeep <<'EOF'
EOF

write_file_hd data/examples/.gitkeep <<'EOF'
EOF

write_file_hd data/benchmarks/.gitkeep <<'EOF'
EOF

write_file_hd data/results/.gitkeep <<'EOF'
EOF

# ---------- Success message ----------
echo ""
echo "✅ Repository structure created successfully!"
echo ""
echo "Next steps:"
echo "  1. cd $ROOT"
echo "  2. git init (if not already a repo)"
echo "  3. git add ."
echo "  4. git commit -m 'Initial structure from bootstrap'"
echo "  5. docker compose up -d  # or install dependencies locally"
echo "  6. make doctor"
echo "  7. make test"
echo ""
echo "Happy coding! 🚀"
