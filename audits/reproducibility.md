# Reproducibility Guide

This document describes how to reproduce all computational results in The Algebra of Indeterminate I repository.

## Overview

The repository is designed for full reproducibility of:
1. Operation tables and axiom verification
2. Counterexamples to field axioms
3. Formal verification attempts
4. All computational claims in the associated book

## Environment Setup

### Requirements

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Required Python packages (see `requirements.txt`)

### Installation

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I.git
cd The-Algebra-of-Ideterminate-I

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Reproducing Results

### Layer A: Axiom Catalog

The formal axiom catalog is machine-readable and requires no execution:

```bash
# View axioms
cat data/axioms/axioms.yaml

# View rewrite rules
cat data/axioms/rewrite_rules.yaml
```

**Verification**: 
- Axioms are declarative and self-documenting
- Cross-reference with `docs/theory/axioms/` for human-readable explanations
- Each axiom has a unique ID for traceability

### Layer B: Operation Tables and Counterexamples

#### Operation Tables

Execute the operation tables notebook:

```bash
jupyter notebook notebooks/02_operations_tables.ipynb
```

Or run all cells:

```bash
jupyter nbconvert --to notebook --execute notebooks/02_operations_tables.ipynb
```

**Expected outputs**:
- `data/examples/addition_table.csv` - Addition table for basic elements
- `data/examples/multiplication_table.csv` - Multiplication table for basic elements
- Console output showing axiom verification results

**Verification checklist**:
- [ ] Addition table is commutative (symmetric)
- [ ] I + I = I appears in table
- [ ] I · I = I appears in table
- [ ] All identity and inverse properties verified
- [ ] Zero absorption verified

#### Counterexamples

Execute the counterexamples notebook:

```bash
jupyter notebook notebooks/04_counterexamples_field_axioms.ipynb
```

**Expected outputs**:
- `data/examples/counterexamples.jsonl` - Machine-readable counterexamples
- `data/examples/counterexamples_summary.json` - Summary statistics
- Console output verifying each counterexample

**Verification checklist**:
- [ ] CE1: I has no multiplicative inverse (proof by contradiction)
- [ ] CE2: Cancellation law fails (I·I = I·1 but I ≠ 1)
- [ ] CE4: Additive idempotency breaks group reasoning
- [ ] CE7: Polynomial x² = x has 3 roots (0, 1, I)
- [ ] CE9: All powers of I equal I

### Layer C: Reproducibility Report

Execute the reproducibility report notebook:

```bash
jupyter notebook notebooks/09_reproducibility_report.ipynb
```

This notebook automatically:
1. Re-runs all other notebooks
2. Verifies outputs match expected results
3. Checks for regressions
4. Generates a reproducibility certificate

**Expected outputs**:
- Console report of all verification steps
- Reproducibility certificate (if all checks pass)

### Layer D: Formal Verification

#### Lean Formalization

```bash
cd lean
lake build
```

**Status**: Incremental proofs in progress
- Basic type definitions: ✓ Complete
- Axiom declarations: ✓ Complete
- Basic lemmas: ⚠ In progress
- Full proofs: ⚠ In progress

#### Coq Formalization

```bash
cd coq
make
```

**Status**: Optional mirror for second verification
- Project structure: ✓ Complete
- Axiom formalization: ⚠ In progress
- Proofs: ⚠ In progress

## Regression Testing

### Running All Tests

To verify nothing has broken:

```bash
# Run all notebooks in sequence
./scripts/run_all_notebooks.sh

# Or manually:
jupyter nbconvert --to notebook --execute notebooks/02_operations_tables.ipynb
jupyter nbconvert --to notebook --execute notebooks/04_counterexamples_field_axioms.ipynb
jupyter nbconvert --to notebook --execute notebooks/09_reproducibility_report.ipynb
```

### Comparing Results

```bash
# Compare current counterexamples with baseline
diff data/examples/counterexamples.jsonl data/examples/counterexamples.baseline.jsonl

# Compare operation tables
diff data/examples/addition_table.csv data/examples/addition_table.baseline.csv
diff data/examples/multiplication_table.csv data/examples/multiplication_table.baseline.csv
```

## Data Integrity

### Checksums

Verify data file integrity:

```bash
# Generate checksums
sha256sum data/axioms/axioms.yaml
sha256sum data/axioms/rewrite_rules.yaml
sha256sum data/examples/counterexamples.jsonl

# Compare with published checksums (see CHECKSUMS.txt)
sha256sum -c CHECKSUMS.txt
```

### Version Control

All computational artifacts are version-controlled:
- Axiom definitions in `data/axioms/`
- Counterexample database in `data/examples/`
- Notebooks in `notebooks/`

Check the git history to see when any result changed:

```bash
git log --follow data/examples/counterexamples.jsonl
```

## Verification Levels

The repository provides multiple levels of verification:

### Level 1: Axiom Consistency (Static)
- **Method**: Manual review of axiom definitions
- **Location**: `data/axioms/axioms.yaml`
- **Effort**: 15 minutes
- **Status**: ✓ Complete

### Level 2: Computational Verification (Dynamic)
- **Method**: Execute notebooks
- **Location**: `notebooks/02_*.ipynb`, `notebooks/04_*.ipynb`
- **Effort**: 5 minutes
- **Status**: ✓ Complete

### Level 3: Formal Verification (Proof)
- **Method**: Lean/Coq type checking and proof verification
- **Location**: `lean/`, `coq/`
- **Effort**: Ongoing research
- **Status**: ⚠ In progress

## Known Limitations

See `audits/model_limitations.md` for:
- Open questions
- Unproven conjectures
- Computational limitations
- Known edge cases

## Continuous Integration

The repository includes CI configuration (`.github/workflows/`) that automatically:
1. Runs all notebooks on each commit
2. Verifies axiom consistency
3. Checks for regressions in counterexamples
4. Attempts Lean/Coq builds

View CI results at: [GitHub Actions](https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/actions)

## Troubleshooting

### Notebook Execution Fails

**Problem**: Notebook fails to execute
**Solution**: 
1. Check Python version (3.8+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Clear notebook outputs: `jupyter nbconvert --clear-output notebooks/*.ipynb`
4. Try again

### Lean Build Fails

**Problem**: Lean formalization doesn't build
**Solution**:
1. Update Lean: `elan update`
2. Clean build: `lake clean`
3. Rebuild: `lake build`
4. Check `lean/README.md` for version requirements

### Different Results Than Expected

**Problem**: Your results differ from published results
**Solution**:
1. Check git branch: `git branch` (should be on main)
2. Check for uncommitted changes: `git status`
3. Pull latest: `git pull`
4. Verify environment matches requirements
5. Report issue at: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/issues

## Citation

If you reproduce these results in your work, please cite:

```bibtex
@misc{algebra-indeterminate-i-repo,
  author = {[Author Name]},
  title = {The Algebra of Indeterminate I: Computational Repository},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I}
}
```

## Contact

For questions about reproducibility:
- Open an issue: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/issues
- Email: [contact information]

## Audit Trail

| Date | Version | Verified By | Status |
|------|---------|-------------|--------|
| 2024-XX-XX | 1.0.0 | [Name] | ✓ All checks pass |

Last updated: 2024-XX-XX
