# Axioms for The Algebra of Indeterminate I

This directory contains detailed documentation and justification for each axiom in the system.

## Overview

The Algebra of Indeterminate I is built on 15 fundamental postulates that define a non-field algebraic structure containing a special element I with unique properties. These axioms are complemented by extensions from set theory (ZF), choice principles (AC), and indeterminate-specific rules.

## Core Postulates

The 15 core postulates establish the basic algebraic structure:

### Additive Structure (P1-P5)
- **P1: Closure under Addition** - Ensures the system is closed under addition
- **P2: Associativity of Addition** - Addition is associative
- **P3: Commutativity of Addition** - Addition is commutative
- **P4: Additive Identity** - Zero exists and acts as additive identity
- **P5: Additive Inverse** - Every element has an additive inverse

### Multiplicative Structure (P6-P8, P13)
- **P6: Closure under Multiplication** - Ensures the system is closed under multiplication
- **P7: Associativity of Multiplication** - Multiplication is associative
- **P8: Multiplicative Identity** - One exists and acts as multiplicative identity
- **P13: Zero Absorption** - Zero absorbs all elements under multiplication

### Distributivity (P9)
- **P9: Distributivity** - Multiplication distributes over addition

### Indeterminate Properties (P10-P12, P14-P15)
- **P10: Indeterminate Element** - I exists and is distinct from 0 and 1
- **P11: I-squared Property** - I² = I (multiplicative idempotency)
- **P12: I-addition Property** - I + I = I (additive idempotency)
- **P14: Non-invertibility of I** - I has no multiplicative inverse
- **P15: I-zero Distinction** - I behaves like zero in some contexts but is distinct

## Extensions

### ZF Extensions (ZF1-ZF5)
Set-theoretic foundations ensuring proper mathematical grounding:
- Extensionality, Pairing, Union, Power Set, Infinity

### AC Extensions (AC1-AC2)
Choice principles for constructive proofs:
- Axiom of Choice, Well-ordering Theorem

### Indeterminate Extensions (I1-I5)
Additional properties specific to the indeterminate element:
- Uniqueness, mixed operations, ordering incompleteness, division undefined, polynomial behavior

### Meta-Axioms (M1-M3)
Properties of the axiom system itself:
- Consistency, Independence, Minimality

## Why These Axioms?

The axiom system is designed to:

1. **Capture indeterminacy formally** - I represents truly indeterminate values
2. **Break field structure minimally** - Most field axioms hold except multiplicative inverse for I
3. **Enable computation** - Rules are mechanizable and decidable
4. **Model real phenomena** - Captures behavior of undefined/indeterminate values in computation

## Key Non-Properties

The system explicitly does NOT have:
- **Multiplicative inverse for I** (P14) - I cannot be "divided out"
- **Commutativity of multiplication** (general case) - Order matters
- **Total ordering** (I3) - I cannot be consistently ordered with respect to other elements
- **Field structure** - This is not a field

## Documentation Files

Detailed documentation for each axiom group:
- [Core Postulates](./core_postulates.md) - Detailed explanation of P1-P15
- [ZF Extensions](./zf_extensions.md) - Set-theoretic foundations
- [AC Extensions](./ac_extensions.md) - Choice principles
- [Indeterminate Extensions](./indeterminate_extensions.md) - I-specific properties
- [Meta-Axioms](./meta_axioms.md) - System properties
- [Counterexamples](./counterexamples.md) - Where classical axioms fail

## Machine-Readable Format

The formal catalog of axioms is available in machine-readable format at:
- [`../../data/axioms/axioms.yaml`](../../data/axioms/axioms.yaml)
- [`../../data/axioms/rewrite_rules.yaml`](../../data/axioms/rewrite_rules.yaml)

## References

1. The main book: "The Algebra of Indeterminate I"
2. Computational examples: `../../notebooks/`
3. Formal verification: `../../lean/` and `../../coq/`
