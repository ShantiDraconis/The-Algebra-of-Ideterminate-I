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