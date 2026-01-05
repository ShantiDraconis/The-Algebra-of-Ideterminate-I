# The Algebra of Indeterminate I

## Formal Mathematical Framework for I = 0/0

This repository contains comprehensive formalizations of the Algebra of Indeterminate I across multiple proof assistants (Lean 4, Coq, Isabelle/HOL, and Agda).

## Overview

The framework introduces **I**, the indeterminate form 0/0, as a foundational element of an extended number system:

**K_I = ℝ ∪ {I, J}**

where:
- **I** represents the indeterminate form 0/0
- **J** is the dual element emerging from I-symmetry breaking
- Modified operations: ⊕, ⊖, ⊗, ⊘
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
├── lean/               # Lean 4 formalization
│   ├── IAlgebra.lean
│   └── ExtendedAnalysis.lean
├── coq/                # Coq formalization
│   ├── IAlgebra.v
│   └── ExtendedAnalysis.v
├── isabelle/           # Isabelle/HOL formalization
│   └── IAlgebra.thy
├── agda/               # Agda formalization
│   └── IAlgebra.agda
└── docs/               # Comprehensive documentation
    └── README.md
```

## Key Features

### 1. **15 Fundamental Postulates**
Complete axiomatic foundation for the extended number system

### 2. **Modified Algebraic Operations**
- Division by zero: a/0 = I
- Self-consistency: I + I = I, I × I = I
- Zero absorption: 0 × I = 0

### 3. **Wheel of Fractions**
Algebraic structure naturally accommodating division by zero

### 4. **Physical Interpretations**
- Quantum gravity framework
- Dark sector phenomena
- Singularity resolution

### 5. **Mathematical Connections**
- Ultrapowers and nonstandard analysis
- Cardinal arithmetic
- Set theory extensions

## Formalization Status

| Proof Assistant | Core Framework | Extended Analysis | Status |
|----------------|----------------|-------------------|---------|
| **Lean 4** | ✓ Complete | ✓ Complete | 🟢 Ready |
| **Coq** | ✓ Complete | ✓ Complete | 🟢 Ready |
| **Isabelle/HOL** | ✓ Complete | ⏳ In Progress | 🟡 Beta |
| **Agda** | ✓ Complete | ⏳ In Progress | 🟡 Beta |

## Quick Start

See [docs/README.md](docs/README.md) for detailed documentation, examples, and usage instructions.

## Main Theorems

1. **Non-existence of multiplicative inverse**: ¬∃x. I ⊗ x = 1
2. **Collapse contradiction**: I = 0 → ⊥
3. **Wheel division**: ∀n. wheel_div(n, 0) = I
4. **Context resolution**: ∃ctx. resolve(ctx, I) ≠ I
5. **System consistency**: The extended system is logically consistent

## Physical Applications

- **Quantum Gravity**: I-field theory framework
- **Dark Matter/Energy**: Modified gravitational interactions
- **Singularity Resolution**: Black holes and Big Bang
- **Planck Scale Physics**: Quantum-cosmic connections

## Building

### Lean 4
```bash
cd lean && lake build
```

### Coq
```bash
cd coq && coqc IAlgebra.v && coqc ExtendedAnalysis.v
```

### Isabelle
```bash
cd isabelle && isabelle build -D .
```

### Agda
```bash
cd agda && agda --safe IAlgebra.agda
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

Full mathematical framework, proofs, and examples available in [docs/README.md](docs/README.md)

## Contributing

This is a research framework. Contributions welcome for:
- Proof completions
- Extended theorems
- Physical models
- Computational implementations

## License

Academic and research use.

## Citation

```bibtex
@software{algebra_indeterminate_i,
  title={The Algebra of Indeterminate I: Formal Verification},
  year={2026},
  url={https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I}
}
```

---

**Note**: This framework represents theoretical mathematical structures requiring careful analysis and empirical validation for physical applications.
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


## Citations

If you use this work, please cite:

```bibtex
@misc{algebra-indeterminate-i,
  title = {The Algebra of Indeterminate I: Computational Repository},
  author = {[Author Name]},
  year = {2024},
  publisher = {GitHub},
A computational algebra system for exploring the properties and operations of the indeterminate unit **I**, extending traditional algebraic structures with novel calculus and rewriting systems.

## Overview

This project implements a formal system for working with the indeterminate **I**, providing:

- Type system for algebraic expressions involving I
- Operations and transformations
- Rewrite rules and normalization
- The Wheel of Fractions framework
- I-Calculus examples and applications

## Project Structure

```
.
├── ialgebra/          # Python implementation
├── lean/              # Lean 4 formal proofs
├── docs/              # Documentation and papers
├── data/              # Axioms and rules in YAML format
├── examples/          # Example computations
└── tests/             # Test suite
```

## Installation

### Python Package

```bash
pip install -e .
```

### Lean 4

```bash
lake build
```

## Usage

```python
from ialgebra import Indeterminate, Expression

# Create expressions with I
expr = Expression("x + I")
# ... perform operations
```

## Development

Build and test:

```bash
make build
make test
```

## Citation

If you use this work in your research, please cite:

```bibtex
@software{algebra_indeterminate_i,
  title = {The Algebra of Indeterminate I},
  author = {...},
  year = {2026},
  url = {https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I}
}
```

## License

[To be determined - see LICENSE file]

## Contact

- **Issues**: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/issues
- **Discussions**: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/discussions
- **Email**: [Shanti.Draconis@icloud.com]

## Acknowledgments

This repository demonstrates that modern mathematics can be:
- Computational
- Reproducible
- Formally verified
- Openly documented

We thank the Lean and Coq communities for their proof assistant tools, and the Jupyter community for computational notebooks.

---

**"Mais cálculos do que o livro"** — More calculations than the book.
See `CITATION.cff` for more details.

## License

[To be determined]

## Contributing

Contributions are welcome! Please see the open issues for areas that need work.
# The Algebra of the Indeterminate I

This repository contains the official reference materials and documentation for **"The Algebra of the Indeterminate I"** book.

## Quick Links

- **Book Reference PDF**: [`book/source/the_algebra_of_the_indeterminate.pdf`](book/source/the_algebra_of_the_indeterminate.pdf)
- **Chapter-to-Folder Mapping**: [`book/extracted/section_map.json`](book/extracted/section_map.json)
- **Structural Overview**: [`docs/theory/overview.md`](docs/theory/overview.md)

## Repository Structure

This repository maintains a direct correspondence with the book's structure:

```
book/
├── source/                    # Book PDF reference
│   └── the_algebra_of_the_indeterminate.pdf
└── extracted/                 # Book metadata
    └── section_map.json      # Chapter-to-folder mappings

docs/
└── theory/                    # Documentation for each chapter
    └── overview.md           # Structural overview

latex/
└── sections/                  # LaTeX sources for each section
```

## Book Content

The book covers eight major areas:

1. **ZF/AC + I** - ZF Set Theory with Axiom of Choice and the Indeterminate
2. **Ultrapowers** - Non-Standard Analysis and Ultrapowers
3. **Wheel Theory** - Division by Zero and Wheel Algebraic Structures
4. **Axioms** - Axiomatic Foundation of I
5. **Field Axioms** - Failures and Corrections
6. **I-Calculus** - Differential and Integral Operations
7. **Physics** - Physical Applications of the Indeterminate
8. **Computation** - Computational Aspects and Implementations

For detailed structural information, see [`docs/theory/overview.md`](docs/theory/overview.md).

## Navigation

The [`section_map.json`](book/extracted/section_map.json) file provides precise mappings from book chapters to their corresponding documentation and LaTeX folders in this repository, ensuring an unambiguous correspondence between the published book and repository materials.
