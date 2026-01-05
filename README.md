# The Algebra of Indeterminate I

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
