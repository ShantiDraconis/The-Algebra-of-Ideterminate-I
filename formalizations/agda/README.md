# Agda Formalization of I-Algebra

Formalization of the I-Algebra framework using Agda with dependent types.

## Files

- `IAlgebra.agda` - Complete formalization with:
  - Constructive type theory
  - Dependent types
  - Propositional equality proofs

## Features

### Type Definition
```agda
data ExtendedReal : Set where
  real : ℝ → ExtendedReal
  indeterminate : ExtendedReal
  recipIndeterminate : ExtendedReal
```

### Operations (with Unicode notation)
- `_⊕_` (infixl 6) - Extended addition
- `_⊖_` (infixl 6) - Extended subtraction
- `_⊗_` (infixl 7) - Extended multiplication
- `_⊘_` (infixl 7) - Extended division

### Proven Properties
- `indeterminate-invariance-add` - Addition invariance
- `indeterminate-invariance-mul` - Multiplication invariance
- `indeterminate-invariance-div` - Division invariance
- `self-sub-is-indeterminate` - Self-subtraction (partial)
- Absorption lemmas (all proven constructively)

### Postulates
- Real number operations (⊕ℝ, ⊗ℝ, etc.)
- Axioms I1-I3
- Derivative properties
- Calculus rules

## Dependencies

- Agda (version 2.6.2 or later)
- Agda Standard Library (version 1.7 or compatible)

## Installation

```bash
# Install Agda
cabal install Agda

# Or use stack
stack install Agda

# Install standard library
git clone https://github.com/agda/agda-stdlib.git
```

### Configure Agda

Edit `~/.agda/libraries`:
```
/path/to/agda-stdlib/standard-library.agda-lib
```

Edit `~/.agda/defaults`:
```
standard-library
```

## Type Checking

```bash
agda --safe IAlgebra.agda
```

Or use Emacs mode:
```bash
emacs IAlgebra.agda
```
Then: `C-c C-l` to load/check file

## Structure

The module is organized as:
1. Imports and definitions
2. Extended real type
3. Helper postulates for reals
4. Operation definitions
5. Proven theorems
6. Axiomatic framework
7. I-Calculus definitions
8. Model theory

## Proof Style

Agda uses constructive proofs with pattern matching:

```agda
indeterminate-invariance-add : ∀ (x : ExtendedReal) → x ⊕ I ≡ I
indeterminate-invariance-add (real a) = refl
indeterminate-invariance-add indeterminate = refl
indeterminate-invariance-add recipIndeterminate = refl
```

## Features of Dependent Types

### Records
```agda
record ILimit (f : ExtendedReal → ExtendedReal) 
              (x L : ExtendedReal) : Set where
  field
    ilimit-prop : ∀ (ε : ExtendedReal) → ...
```

### Dependent Types
Used for expressing properties directly in types:
```agda
IContinuous : (ExtendedReal → ExtendedReal) → Set
IContinuous f = ∀ x → ILimit f x (f x)
```

## Verification Status

### Constructively Proven
- ✓ All absorption properties
- ✓ Indeterminate invariance (all three parts)
- ✓ Type safety of operations

### Postulated
- Real number operations (interface to stdlib)
- Calculus rules
- Some auxiliary properties

### Incomplete (holes marked with {!!})
- Some cases in `self-sub-is-indeterminate` require reflexivity axioms

## Advanced Features

### Unicode Support
The formalization uses Unicode symbols for readability:
- ℝ for real numbers
- ⊕, ⊖, ⊗, ⊘ for operations
- ≡ for propositional equality
- ∀, ∃ for quantifiers

### Safe Flag
Can be compiled with `--safe` flag (no postulates in computational parts)

## Future Work

- Complete real number library integration
- Prove reflexivity for helper predicates
- Implement limit theory constructively
- Add quotient types for I-equivalence classes
- Cubical mode for better equality reasoning

## Resources

- [Agda Documentation](https://agda.readthedocs.io/)
- [Agda Tutorial](https://agda.readthedocs.io/en/latest/getting-started/)
- [Standard Library](https://agda.github.io/agda-stdlib/)

## Emacs Mode

For the best experience, use Agda's Emacs mode:
- `C-c C-l` - Load/type-check file
- `C-c C-c` - Case split
- `C-c C-,` - Show goal and context
- `C-c C-.` - Show goal and inferred type
- `C-c C-r` - Refine hole
- `C-c C-space` - Give solution

---

*Formalized: January 5, 2026*
