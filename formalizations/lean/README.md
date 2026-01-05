# Lean 4 Formalization

This directory contains the Lean 4 formalization of "The Algebra of the Indeterminate I", covering the theoretical foundations described in Sections 7-13 of the book.

## Structure

- `ZFC.lean` - Zermelo-Fraenkel set theory with the Axiom of Choice (Section 7.1)
- `Cardinals.lean` - Cardinal arithmetic and the indeterminate element I (Section 8)
- `Ultrapowers.lean` - Ultrapowers and nonstandard analysis (Section 9)
- `Algebra.lean` - Algebraic structures with I (Section 10)
- `Consistency.lean` - Model constructions and consistency proofs (Section 11)
- `Main.lean` - Main entry point

## Building

### Prerequisites

- Lean 4 (version 4.3.0 or later)
- Lake (Lean's package manager, included with Lean 4)

### Installation

1. Install Lean 4 following the instructions at https://leanprover.github.io/lean4/doc/setup.html

2. Build the project:
```bash
cd formalizations/lean
lake build
```

### Running

To run the main executable:
```bash
lake exe algebra-indeterminate
```

## Key Theorems

### ZFC Foundations
- `subset_refl` - Reflexivity of subset relation
- `subset_trans` - Transitivity of subset relation
- `subset_antisym` - Antisymmetry of subset relation

### Cardinal Arithmetic with I
- `axiom_I1` - For every cardinal κ, κ ⊖ κ = I
- `axiom_I2` - Limited neutrality of the ⊖ operation
- `axiom_I3` - Consistency with additive operations
- `uniqueness_of_I` - The element I is unique (Theorem 3.1)
- `additive_consistency` - (κ ⊕ λ) ⊖ (κ ⊖ λ) = I
- `symmetric_consistency` - (κ ⊖ λ) ⊕ (λ ⊖ κ) = I

### Ultrapowers and Nonstandard Analysis
- `los_theorem` - Łoś's Theorem for ultrapowers
- `transfer_principle` - Standard properties extend to nonstandard models
- `ultrapower_indeterminacy` - Ultrapowers capture indeterminacy via I

### Algebraic Structures
- `algebraic_compatibility` - Theorem 5.1: Algebraic compatibility
- `hom_preserves_indeterminacy` - Homomorphisms preserve indeterminacy
- `I_invariant_under_iso` - I is invariant under isomorphisms

### Consistency Proofs
- `relative_consistency` - If ZFC is consistent, then ZFC + I is consistent (Lemma 6.1)
- `extended_model_satisfies_I1/I2/I3` - Extended models satisfy the I axioms
- `no_contradictions` - The extended axioms don't create contradictions

## Notes

- Many theorems contain `sorry` placeholders indicating proof obligations that require full development
- The formalization uses axioms extensively to capture the theoretical framework
- This is a research formalization exploring the mathematical foundations of the indeterminate I

## References

- Book: "The Algebra of the Indeterminate I"
- Sections 7-13: Theoretical Foundations, Axiomatic Reinterpretation, Ultrapowers, Cardinal Arithmetic, and Consistency Proofs
