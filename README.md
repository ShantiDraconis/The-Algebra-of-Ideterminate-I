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
    ├── overview.md           # Structural overview
    └── 07_physics/           # Physics applications documentation

latex/
└── sections/                  # LaTeX sources for each section
    └── 07_physics/           # Complete physics formalization (sections 22-28)
        ├── physics_applications.tex
        ├── 22_physical_realization/
        ├── 23_lithium_atoms/
        ├── 24_redshift/
        ├── 25_planck_era/
        ├── 26_universal_principles/
        ├── 27_fundamental_equations/
        └── 28_wavefunction/

formalizations/                # Formal verification and implementations
├── lean/                      # Lean 4 proofs
├── coq/                       # Coq verification
├── isabelle/                  # Isabelle/HOL theorems
├── agda/                      # Agda dependent types
└── python/                    # Python implementations and tests
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

## New: Formal Verification and Implementations

This repository now includes comprehensive formalizations of I-theory physics:

### LaTeX Formalization (Sections 22-28)

Complete mathematical treatment of physical applications:
- **Section 22**: Quantum Gravity Lagrangian and Field Equations
- **Section 23**: Ultra-Cold Lithium Atoms and BEC
- **Section 24**: Cosmological Redshift and Expansion
- **Section 25**: Planck Era and Quantum-Cosmological Connections
- **Section 26**: Universal Principles of Observation
- **Section 27**: Fundamental I-Particle Equations
- **Section 28**: Wavefunction Description and Quantum Mechanics

📄 [View LaTeX Documentation](latex/sections/07_physics/README.md)

### Proof Assistant Formalizations

Rigorous mathematical verification in multiple systems:

- **Lean 4**: Type-checked definitions, theorems, and proofs
- **Coq**: Verified physical equations with formal proofs
- **Isabelle/HOL**: Higher-order logic formalization
- **Agda**: Dependent type theory implementation

### Python Implementation

Practical computational framework with complete test coverage:

```python
from formalizations.python.i_theory_physics import IParticle, PlanckUnits

# Create I-particle
particle = IParticle(mass=1.78e-27)  # 1 GeV/c²

# Calculate physical properties
print(f"Energy: {particle.energy:.3e} J")
print(f"Gravitational force near Sun: {particle.gravitational_force(1.989e30, 1.496e11):.3e} N")

# Planck scale physics
planck = PlanckUnits()
print(f"Planck length: {planck.length:.3e} m")
```

**Features:**
- Complete implementation of all physical equations (sections 22-28)
- 30 comprehensive unit tests (100% passing)
- Classes for particles, wavefunctions, cosmology, dark matter, and BEC physics

📚 [View Formalization Documentation](formalizations/README.md)

## Quick Start

### LaTeX Compilation

```bash
cd latex/sections/07_physics
pdflatex physics_applications.tex
```

### Python Tests

```bash
pip install numpy
cd formalizations/python
python test_i_theory.py
```

### Lean Verification

```bash
cd formalizations/lean
lake build
```

## Navigation

The [`section_map.json`](book/extracted/section_map.json) file provides precise mappings from book chapters to their corresponding documentation and LaTeX folders in this repository, ensuring an unambiguous correspondence between the published book and repository materials.