# The Algebra of Indeterminate I

A computational and formal verification repository for "The Algebra of Indeterminate I" — providing more calculations, formal proofs, and reproducible results than the book alone.

## Overview

This repository materializes the algebraic framework presented in the book through multiple computational and formal layers:

- **Layer A**: Machine-readable axiom catalog and rewrite rules
- **Layer B**: Operation tables and counterexamples to classical field axioms
- **Layer C**: Reproducibility reports and honest limitation documentation
- **Layer D**: Formal verification in Lean and Coq

## Quick Start

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I.git
cd The-Algebra-of-Ideterminate-I

# View axioms
cat data/axioms/axioms.yaml

# Run notebooks (requires Python 3.8+)
pip install -r requirements.txt
jupyter notebook notebooks/
```

## Repository Structure

```
├── data/
│   ├── axioms/              # Layer A: Formal axiom catalog
│   │   ├── axioms.yaml      # 15 postulates + extensions (ZF/AC/I)
│   │   └── rewrite_rules.yaml  # Simplification rules
│   └── examples/            # Computational examples
│       └── counterexamples.jsonl  # Field axiom violations
│
├── docs/
│   └── theory/
│       └── axioms/          # Human-readable axiom docs
│           ├── README.md
│           ├── core_postulates.md
│           └── counterexamples.md
│
├── notebooks/               # Layer B: Jupyter notebooks
│   ├── 02_operations_tables.ipynb
│   ├── 04_counterexamples_field_axioms.ipynb
│   └── 09_reproducibility_report.ipynb
│
├── audits/                  # Layer C: Reproducibility & limitations
│   ├── reproducibility.md
│   └── model_limitations.md
│
├── lean/                    # Layer D: Lean 4 formalization
│   ├── README.md
│   ├── lakefile.lean
│   └── AlgebraI/
│       └── Basic.lean
│
└── coq/                     # Layer D: Coq formalization
    ├── README.md
    ├── Makefile
    └── theories/
        └── Basic.v
```

## The Algebra

The Algebra of Indeterminate I is a non-field algebraic structure built on 15 postulates, featuring a special element **I** with these unique properties:

- **I² = I** (multiplicative idempotency)
- **I + I = I** (additive idempotency)
- **I ≠ 0, I ≠ 1** (distinct from identities)
- **I has no multiplicative inverse** (not a field)

This structure models truly indeterminate values while maintaining algebraic coherence.

## Key Features

### ✓ Machine-Readable Axioms

Formal catalog in YAML format for computational use:
- 15 core postulates
- ZF set theory extensions
- Axiom of Choice extensions
- Indeterminate-specific properties
- Meta-axioms about the system

### ✓ Computational Verification

Jupyter notebooks demonstrating:
- Operation tables for basic elements
- Axiom verification for finite cases
- Counterexamples to field axioms (with proofs)
- Reproducibility checks

### ✓ Honest Limitations

Explicit documentation of:
- What is proven vs. conjectured
- Open questions
- Known issues
- Research roadmap

### ✓ Formal Verification (In Progress)

Dual formalization in:
- **Lean 4**: Primary formalization target
- **Coq**: Secondary verification path

## Usage

### Exploring Axioms

```bash
# View the formal axiom catalog
cat data/axioms/axioms.yaml

# View rewrite rules
cat data/axioms/rewrite_rules.yaml

# Read human documentation
open docs/theory/axioms/README.md
```

### Running Notebooks

```bash
# Install dependencies
pip install jupyter pandas pyyaml numpy

# Start Jupyter
jupyter notebook

# Open and run:
# - notebooks/02_operations_tables.ipynb
# - notebooks/04_counterexamples_field_axioms.ipynb
# - notebooks/09_reproducibility_report.ipynb
```

### Formal Verification

#### Lean 4

```bash
cd lean
lake build
```

#### Coq

```bash
cd coq
make
```

## Documentation

- **[Axiom Documentation](docs/theory/axioms/README.md)** - Detailed explanation of all axioms
- **[Core Postulates](docs/theory/axioms/core_postulates.md)** - The 15 fundamental axioms
- **[Counterexamples](docs/theory/axioms/counterexamples.md)** - Where field axioms fail
- **[Reproducibility Guide](audits/reproducibility.md)** - How to reproduce all results
- **[Model Limitations](audits/model_limitations.md)** - Open questions and limitations
- **[Lean README](lean/README.md)** - Lean formalization guide
- **[Coq README](coq/README.md)** - Coq formalization guide

## Why This Matters

Traditional mathematical books present results; this repository provides:

1. **Verifiable computations** - Run the notebooks, check the results
2. **Formal proofs** - Machine-checked correctness (in progress)
3. **Regression testing** - Ensure consistency over time
4. **Reproducibility** - Anyone can verify the claims
5. **Educational resource** - Learn through executable examples

## Contributing

We welcome contributions in several areas:

- **Proofs**: Complete the Lean/Coq formalizations
- **Examples**: Add more computational examples
- **Documentation**: Improve explanations
- **Testing**: Add regression tests
- **Applications**: Explore practical uses

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Status

| Component | Status |
|-----------|--------|
| Axiom Catalog (Layer A) | ✓ Complete |
| Operation Tables (Layer B) | ✓ Complete |
| Counterexamples (Layer B) | ✓ Complete |
| Reproducibility Docs (Layer C) | ✓ Complete |
| Model Limitations (Layer C) | ✓ Complete |
| Lean Formalization (Layer D) | ⚠ In Progress |
| Coq Formalization (Layer D) | ⚠ In Progress |
| Formal Proofs | ❌ Not Started |

## Citations

If you use this work, please cite:

```bibtex
@misc{algebra-indeterminate-i,
  title = {The Algebra of Indeterminate I: Computational Repository},
  author = {[Author Name]},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I}
}
```

## License

[To be determined - see LICENSE file]

## Contact

- **Issues**: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/issues
- **Discussions**: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/discussions
- **Email**: [contact information]

## Acknowledgments

This repository demonstrates that modern mathematics can be:
- Computational
- Reproducible
- Formally verified
- Openly documented

We thank the Lean and Coq communities for their proof assistant tools, and the Jupyter community for computational notebooks.

---

**"Mais cálculos do que o livro"** — More calculations than the book.