# Coq Formalization of I-Algebra

Formalization of the I-Algebra framework in the Coq proof assistant.

## Files

- `IAlgebra.v` - Complete formalization with:
  - Core definitions
  - Extended operations
  - Proven theorems
  - I-Calculus module
  - ZF extension axioms

## Features

### Type System
- `ExtendedReal` inductive type with three constructors:
  - `Real : R -> ExtendedReal`
  - `Indeterminate` (I)
  - `RecipIndeterminate` (J)

### Operations
- `eadd` (⊕) - Extended addition
- `esub` (⊖) - Extended subtraction  
- `emul` (⊗) - Extended multiplication
- `ediv` (⊘) - Extended division

### Proven Theorems
- `indeterminate_invariance` - Full proof of Theorem 14.1
- `self_sub_is_indeterminate` - Proof that x ⊖ x = I
- `eadd_comm` - Commutativity of addition
- `i_absorbs_add_left/right` - I absorption lemmas
- `i_absorbs_mul_left/right` - I multiplication lemmas

### Axioms
- `axiom_i1` - Cardinal self-subtraction
- `axiom_i2` - I distinct from zero
- `axiom_i3` - Operation preservation

### I-Calculus Module
- `ilimit` - I-limit definition
- `icontinuous` - Continuity predicate
- `ideriv` - Derivative operator
- Calculus rules (chain, product)

## Dependencies

- Coq (version 8.13 or later recommended)
- Standard library `Reals`, `Setoid`, `Classical`

## Installation

```bash
# Install Coq
opam install coq

# Or use system package manager
apt-get install coq  # Debian/Ubuntu
brew install coq     # macOS
```

## Compilation

```bash
coqc IAlgebra.v
```

Or use CoqIDE:
```bash
coqide IAlgebra.v
```

## Structure

The file is organized into modules:
1. `IAlgebra` - Main module with core definitions
2. `ZF_I_Extension` - Model-theoretic consistency
3. `ICalculus` - Calculus operations

## Example Usage

```coq
Require Import IAlgebra.

(* Create extended reals *)
Definition x := Real 3.14.
Definition I := Indeterminate.

(* Use operations *)
Compute (x ⊕ I).  (* Results in I *)
Compute (x ⊖ x).  (* Results in I *)

(* Apply theorems *)
Theorem my_theorem : x ⊕ I = I.
Proof.
  apply (indeterminate_invariance x).
Qed.
```

## Verification Status

All core theorems are **fully proven** without `admit` or `Admitted`:
- ✓ Indeterminate invariance
- ✓ Self-subtraction property
- ✓ Commutativity (with conditions)
- ✓ Absorption properties

Axiomatic parts:
- Calculus rules (axiomatized)
- Model theory (axiomatized with consistency outline)

## Future Work

- Complete formalization of limit theory
- Ultrapower construction details
- Integration with MathComp or Coquelicot for analysis
- Automation tactics for I-algebra proofs

## Notes

- Uses `Req_EM_T` for decidable real equality
- Classical logic for some proofs
- Compatible with `ssreflect` tactics

---

*Formalized: January 5, 2026*
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
