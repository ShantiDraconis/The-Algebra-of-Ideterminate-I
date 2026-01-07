# Requirements and Installation Guide

## System Requirements

### For LaTeX Compilation

- **TeX Distribution**: TeX Live 2020 or later (or MiKTeX on Windows)
- **Required Packages**:
  - amsmath, amssymb, amsthm
  - mathtools
  - hyperref
  - geometry

Install on Ubuntu/Debian:
```bash
sudo apt-get install texlive-full
```

Install on macOS:
```bash
brew install --cask mactex
```

### For Coq Formalization

- **Coq Version**: 8.15 or later
- **Dependencies**: Standard library (included with Coq)

Install on Ubuntu/Debian:
```bash
sudo apt-get install coq
```

Install via opam:
```bash
opam install coq
```

### For Isabelle Formalization

- **Isabelle Version**: Isabelle2021 or later
- **Components**: HOL and Main theories

Download from: https://isabelle.in.tum.de/

### For Lean Formalization

- **Lean Version**: Lean 4.0 or later
- **Dependencies**: Mathlib4

Install via elan:
```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```

### For Python Implementation

- **Python Version**: 3.8 or later
- **Required Packages**:
  - matplotlib >= 3.3.0
  - numpy >= 1.19.0

Install dependencies:
```bash
pip install -r python/requirements.txt
```

Or manually:
```bash
pip install matplotlib numpy
```

## Building Instructions

### LaTeX Document

```bash
cd latex
pdflatex main.tex
pdflatex main.tex  # Second run for cross-references
```

Output: `main.pdf` with complete mathematical exposition

### Coq Verification

```bash
cd coq
coqc Indeterminate.v
```

This will:
- Compile the Coq file
- Verify all proofs
- Generate `.vo` object file

Expected output: No errors, all definitions and theorems accepted

### Isabelle Verification

```bash
cd isabelle
isabelle build -D .
```

Or open in Isabelle/jEdit:
```bash
isabelle jedit Indeterminate.thy
```

### Lean Verification

First, set up the project:
```bash
cd lean
lake new indeterminate
cd indeterminate
# Copy Indeterminate.lean to the src directory
lake build
```

### Python Execution

```bash
cd python
python indeterminate.py
```

Expected output:
- Axiom verification results
- Theorem demonstrations
- Cayley tables
- Visualization plot (saved as PNG)

## Testing

### Coq Tests

Run all theorems:
```bash
coqc Indeterminate.v && echo "All tests passed!"
```

### Python Tests

The Python script includes self-tests. Run:
```bash
python indeterminate.py
```

Look for:
- ✓ marks indicating passed axiom verifications
- Successful theorem demonstrations
- Generated visualization file

## Troubleshooting

### LaTeX Issues

**Problem**: Missing packages  
**Solution**: Install full TeX distribution or individual packages via `tlmgr`

**Problem**: Bibliography not showing  
**Solution**: Run `bibtex main` between pdflatex runs

### Coq Issues

**Problem**: "Cannot find library"  
**Solution**: Ensure Coq standard library is installed

**Problem**: Compilation timeout  
**Solution**: Increase Coq's timeout limit in settings

### Isabelle Issues

**Problem**: "Theory not found"  
**Solution**: Ensure you're in the correct directory

**Problem**: Slow processing  
**Solution**: Increase Isabelle's heap memory in settings

### Lean Issues

**Problem**: "Mathlib not found"  
**Solution**: Run `lake exe cache get` to download Mathlib

**Problem**: Timeout during compilation  
**Solution**: Increase memory limit or compile in stages

### Python Issues

**Problem**: Import errors  
**Solution**: Install required packages via pip

**Problem**: Matplotlib backend errors  
**Solution**: Set backend explicitly:
```python
import matplotlib
matplotlib.use('Agg')
```

## Development Setup

For contributing or modifying the formalizations:

1. Clone the repository:
```bash
git clone https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I.git
cd The-Algebra-of-Ideterminate-I
```

2. Set up your preferred proof assistant (see above)

3. Make modifications to the relevant files

4. Verify your changes compile/run successfully

5. Submit a pull request with description of changes

## Performance Notes

- **Coq compilation**: ~5-10 seconds on modern hardware
- **Isabelle verification**: ~10-20 seconds
- **Lean compilation**: ~30-60 seconds (first time with Mathlib)
- **Python execution**: ~1-2 seconds
- **LaTeX compilation**: ~5-10 seconds

## Platform Support

All components are tested and verified on:
- Ubuntu 20.04 LTS and later
- macOS 11 (Big Sur) and later
- Windows 10/11 (via WSL or native tools)

## Additional Resources

- Coq documentation: https://coq.inria.fr/documentation
- Isabelle documentation: https://isabelle.in.tum.de/documentation.html
- Lean documentation: https://leanprover.github.io/documentation/
- Python matplotlib: https://matplotlib.org/stable/index.html
