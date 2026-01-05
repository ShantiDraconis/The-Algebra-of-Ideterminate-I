# Lean Formalization of The Algebra of Indeterminate I

This directory contains a Lean 4 formalization of The Algebra of Indeterminate I.

## Overview

The formalization follows an incremental approach:
1. **Type definitions** - Define the algebraic structure
2. **Axiom declarations** - Declare the 15 core postulates
3. **Basic lemmas** - Prove simple properties
4. **Counterexamples** - Formalize why field axioms fail
5. **Advanced theorems** - Prove deeper properties

## Project Structure

```
lean/
├── README.md                 # This file
├── lakefile.lean            # Lake build configuration
├── lean-toolchain           # Lean version specification
└── AlgebraI/                # Main formalization
    ├── Basic.lean           # Basic definitions and axioms
    ├── Operations.lean      # Operation properties
    ├── Counterexamples.lean # Field axiom counterexamples
    └── Theorems.lean        # Main theorems
```

## Status

### Completed ✓
- Project structure setup
- Documentation

### In Progress ⚠
- Type definitions
- Axiom declarations
- Basic lemmas

### Not Started ❌
- Consistency proof (if possible)
- Independence proofs
- Complete theorem library

## Prerequisites

### Install Lean 4

```bash
# Install elan (Lean version manager)
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh

# Verify installation
lean --version
```

### Install Lake (Lean build tool)

Lake comes with Lean 4 by default.

## Building

```bash
cd lean
lake build
```

## Usage

### Interactive Development

```bash
# Open in VS Code with Lean extension
code AlgebraI/Basic.lean
```

### Type Checking

```bash
# Check all files
lake build

# Check specific file
lean AlgebraI/Basic.lean
```

### REPL

```bash
# Start Lean REPL
lean --run
```

## Formalization Strategy

### Phase 1: Typecheck First (Current)

Focus on getting the definitions and axioms to typecheck correctly:
- Define the carrier type `AlgebraI`
- Declare elements: `zero`, `one`, `i`
- Declare operations: `add`, `mul`
- State axioms as theorems (without proofs)

### Phase 2: Basic Proofs

Prove simple properties:
- Commutativity of addition
- Identity laws
- I-specific properties (I² = I, I + I = I)

### Phase 3: Counterexamples

Formalize why field axioms fail:
- No multiplicative inverse for I
- Cancellation law fails
- Polynomial degree doesn't bound roots

### Phase 4: Advanced Theorems

Prove deeper properties:
- Consistency (if possible)
- Independence (if possible)
- Categorical characterization

## File Descriptions

### `lakefile.lean`

Lake build configuration. Specifies:
- Package name: `algebra_i`
- Lean version requirement
- Dependencies (mathlib4 eventually)

### `lean-toolchain`

Specifies the Lean version to use. Currently targeting Lean 4.

### `AlgebraI/Basic.lean`

Core definitions:
```lean
-- The algebra type
structure AlgebraI where
  carrier : Type

-- Elements
axiom zero : AlgebraI
axiom one : AlgebraI
axiom i : AlgebraI

-- Operations
axiom add : AlgebraI → AlgebraI → AlgebraI
axiom mul : AlgebraI → AlgebraI → AlgebraI

-- Core axioms
axiom i_squared : mul i i = i
axiom i_plus_i : add i i = i
-- ... etc
```

### `AlgebraI/Operations.lean`

Properties of operations:
- Closure
- Associativity
- Commutativity (for addition)
- Identity elements
- Inverses

### `AlgebraI/Counterexamples.lean`

Formalized counterexamples:
```lean
-- I has no multiplicative inverse
theorem i_no_inverse : ¬∃ x, mul i x = one := by
  -- proof by contradiction
  sorry
```

### `AlgebraI/Theorems.lean`

Main results and theorems about the algebra.

## Development Guidelines

### Naming Conventions

- Types: `PascalCase` (e.g., `AlgebraI`)
- Functions: `snake_case` (e.g., `i_squared`)
- Axioms: `axiom_name` (e.g., `add_comm`)
- Theorems: `descriptive_name` (e.g., `i_no_inverse`)

### Proof Strategy

1. Start with `sorry` for unproven theorems
2. Replace with actual proofs incrementally
3. Use tactics: `intro`, `cases`, `contradiction`, `simp`
4. Document complex proofs with comments

### Testing

```bash
# Run all checks
lake build

# Check specific theorem
lean --run scripts/check_theorem.lean
```

## Known Limitations

### Current Limitations

1. **No mathlib4 integration yet** - Will add when needed
2. **Proofs incomplete** - Many theorems have `sorry`
3. **No computation** - Pure specification, not executable
4. **Limited automation** - Few custom tactics

### Theoretical Limitations

1. **Consistency unprovable** - Gödel's theorem may apply
2. **Independence hard** - Requires model construction
3. **Categoricity unknown** - May not uniquely determine algebra

## Related Work

### Relevant Lean Libraries

- `Mathlib4.Algebra.Group` - Group theory
- `Mathlib4.Algebra.Ring` - Ring theory (for contrast)
- `Mathlib4.Algebra.Field` - Field theory (for counterexamples)

### Similar Formalizations

- Non-standard arithmetic
- Boolean algebras
- Tropical algebras

## Contributing

### Adding Definitions

1. Add to `AlgebraI/Basic.lean`
2. Update this README
3. Add tests if applicable

### Adding Proofs

1. Find theorem with `sorry`
2. Replace with actual proof
3. Document proof strategy
4. Update status in README

### Adding Theorems

1. State theorem in appropriate file
2. Add proof (or `sorry`)
3. Update documentation
4. Add to index

## Resources

### Lean 4 Documentation

- [Lean 4 Manual](https://leanprover.github.io/lean4/doc/)
- [Theorem Proving in Lean 4](https://leanprover.github.io/theorem_proving_in_lean4/)
- [Mathlib4 Documentation](https://leanprover-community.github.io/mathlib4_docs/)

### Learning Resources

- [Lean Zulip Chat](https://leanprover.zulipchat.com/)
- [Natural Number Game](https://adam.math.hhu.de/#/g/leanprover-community/NNG4)
- [Functional Programming in Lean](https://leanprover.github.io/functional_programming_in_lean/)

## Contact

For questions about the Lean formalization:
- Open an issue: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/issues
- Tag with `lean` label

## License

See main repository LICENSE file.

## Acknowledgments

This formalization is inspired by:
- Lean mathlib community
- Formal verification of algebraic structures
- The main book: "The Algebra of Indeterminate I"

---

Last updated: 2024-XX-XX
