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