# Coq Formalization

This directory contains the Coq formalization of "The Algebra of the Indeterminate I", covering the theoretical foundations described in Sections 7-13 of the book.

## Structure

- `ZFC.v` - Zermelo-Fraenkel set theory with the Axiom of Choice (Section 7.1)
- `Cardinals.v` - Cardinal arithmetic and the indeterminate element I (Section 8)

## Building

### Prerequisites

- Coq (version 8.16 or later)
- CoqIDE or ProofGeneral (optional, for interactive development)

### Installation

1. Install Coq following the instructions at https://coq.inria.fr/download

2. Compile the files:
```bash
cd formalizations/coq
coqc ZFC.v
coqc Cardinals.v
```

Or using a Makefile (if created):
```bash
make
```

### Interactive Development

Using CoqIDE:
```bash
coqide ZFC.v
```

Using Proof General in Emacs:
```bash
emacs ZFC.v
```

## Key Theorems

### ZFC Foundations
- `subset_refl` - Reflexivity of subset relation
- `subset_trans` - Transitivity of subset relation
- `subset_antisym` - Antisymmetry of subset relation (proved using extensionality)

### Cardinal Arithmetic with I
- `axiom_I1` - For every cardinal κ, κ ⊖ κ = I
- `axiom_I2` - Limited neutrality of the ⊖ operation
- `axiom_I3` - Consistency with additive operations
- `uniqueness_of_I` - The element I is unique (Theorem 3.1)
- `self_subtraction` - Direct application of Axiom I1
- `additive_consistency` - (κ ⊕ λ) ⊖ (κ ⊖ λ) = I (proved)
- `symmetric_consistency` - (κ ⊖ λ) ⊕ (λ ⊖ κ) = I (proved)
- `I_unique` - Corollary: Any element satisfying the I property equals I (proved)

## Features

- Uses Coq's classical logic (`Classical`, `ClassicalChoice`)
- Axiomatic approach for set theory foundations
- Proven theorems where possible, axioms for foundational assumptions
- Clean notation using Coq's notation system

## Notes

- The formalization builds incrementally from ZFC to the extended system with I
- Proofs are constructive where possible, classical where necessary
- This is a research formalization exploring the mathematical foundations of the indeterminate I

## References

- Book: "The Algebra of the Indeterminate I"
- Sections 7-8: Theoretical Foundations and Axiomatic Reinterpretation
