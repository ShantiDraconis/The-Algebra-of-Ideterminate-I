# Isabelle/HOL Formalization

This directory contains the Isabelle/HOL formalization of "The Algebra of the Indeterminate I", covering the theoretical foundations described in Sections 7-13 of the book.

## Structure

- `ZFC.thy` - Zermelo-Fraenkel set theory with the Axiom of Choice (Section 7.1)
- `Cardinals.thy` - Cardinal arithmetic and the indeterminate element I (Section 8)

## Building

### Prerequisites

- Isabelle (version 2023 or later)
- Poly/ML (usually bundled with Isabelle)

### Installation

1. Install Isabelle from https://isabelle.in.tum.de/

2. Open the theories in Isabelle/jEdit:
```bash
isabelle jedit ZFC.thy
```

Or process from command line:
```bash
isabelle build -D .
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

## Features

- Built on Isabelle/HOL (Higher-Order Logic)
- Uses Isabelle's powerful automated proof methods (auto, simp, etc.)
- Clean mathematical notation using Isabelle's syntax
- Integrates with Isabelle's extensive library

## Interactive Development

Using Isabelle/jEdit (recommended):
```bash
isabelle jedit ZFC.thy Cardinals.thy
```

The IDE provides:
- Continuous proof checking
- Proof state visualization
- Sledgehammer for automated proof search
- Auto-completion and documentation

## Proof Methods

The formalization uses various Isabelle proof methods:
- `auto` - Automatic proof search
- `simp` - Simplification using rewrite rules
- `rule` - Apply a rule or axiom
- Manual proof construction with `unfolding` and explicit steps

## Notes

- Theorems are proven using Isabelle's powerful automation where possible
- Axiomatization is used for foundational set theory concepts
- The formalization is designed to be readable and maintainable
- This is a research formalization exploring the mathematical foundations of the indeterminate I

## References

- Book: "The Algebra of the Indeterminate I"
- Sections 7-8: Theoretical Foundations and Axiomatic Reinterpretation
- Isabelle documentation: https://isabelle.in.tum.de/documentation.html
