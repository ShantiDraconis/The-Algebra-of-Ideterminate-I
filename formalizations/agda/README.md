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
