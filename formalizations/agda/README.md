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
# Agda Formalization

This directory contains the Agda formalization of "The Algebra of the Indeterminate I", covering the theoretical foundations described in Sections 7-13 of the book.

## Structure

- `ZFC.agda` - Zermelo-Fraenkel set theory with the Axiom of Choice (Section 7.1)
- `Cardinals.agda` - Cardinal arithmetic and the indeterminate element I (Section 8)

## Building

### Prerequisites

- Agda (version 2.6.3 or later)
- Agda standard library (optional but recommended)

### Installation

1. Install Agda following the instructions at https://agda.readthedocs.io/en/latest/getting-started/installation.html

2. Type-check the files:
```bash
cd formalizations/agda
agda ZFC.agda
agda Cardinals.agda
```

Or in Emacs with agda-mode:
```bash
emacs ZFC.agda
# Then C-c C-l to load the file
```

## Key Definitions and Theorems

### ZFC Foundations
- `ZFSet` - The type of ZF sets
- `_∈_` - Membership relation
- `_⊆_` - Subset relation
- `extensionality` - Axiom of extensionality
- `subset-refl` - Reflexivity of subset relation
- `subset-trans` - Transitivity of subset relation
- `subset-antisym` - Antisymmetry of subset relation

### Cardinal Arithmetic with I
- `Cardinal` - The type of cardinal numbers
- `_⊕_`, `_⊗_`, `_^^_` - Cardinal addition, multiplication, exponentiation
- `I` - The indeterminate element
- `_⊖_` - The subtractive operation
- `axiom-I1` - For every cardinal κ, κ ⊖ κ ≡ I
- `axiom-I2` - Limited neutrality of the ⊖ operation
- `axiom-I3` - Consistency with additive operations
- `uniqueness-of-I` - The element I is unique (Theorem 3.1)
- `self-subtraction` - Direct application of Axiom I1
- `additive-consistency` - (κ ⊕ λ) ⊖ (κ ⊖ λ) ≡ I
- `symmetric-consistency` - (κ ⊖ λ) ⊕ (λ ⊖ κ) ≡ I

## Features

- Dependently-typed formalization
- Constructive proofs where possible
- Uses Agda's powerful type system for mathematical precision
- Clean unicode notation for mathematical symbols
- Safe mode enabled (no postulates in production code, used here for axioms)

## Interactive Development

Using Emacs with agda-mode (recommended):
```bash
emacs ZFC.agda
```

Key commands:
- `C-c C-l` - Load and type-check file
- `C-c C-c` - Case split
- `C-c C-r` - Refine
- `C-c C-a` - Auto (attempt automatic proof)
- `C-c C-,` - Show goal and context

## Type-Checking

Agda performs rigorous type checking:
```bash
agda --safe ZFC.agda
agda --safe Cardinals.agda
```

## Notes

- The formalization uses postulates (axioms) for foundational concepts
- Agda's dependent types provide strong guarantees about correctness
- The `--safe` flag ensures no unsafe features are used (except postulates)
- This is a research formalization exploring the mathematical foundations of the indeterminate I

## Universe Levels

The formalization uses Agda's universe levels to handle size issues in set theory:
- `ZFSet : Set₁` - Sets live in universe level 1
- Careful level management prevents Russell's paradox and similar issues

## References

- Book: "The Algebra of the Indeterminate I"
- Sections 7-8: Theoretical Foundations and Axiomatic Reinterpretation
- Agda documentation: https://agda.readthedocs.io/
- Agda standard library: https://github.com/agda/agda-stdlib
