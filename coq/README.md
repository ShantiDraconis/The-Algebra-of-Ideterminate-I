# Coq Formalization of The Algebra of Indeterminate I

This directory contains a Coq formalization of The Algebra of Indeterminate I, serving as an optional mirror and second verification path alongside the Lean formalization.

## Overview

The Coq formalization provides:
1. **Alternative verification** - Independent check of proofs
2. **Different proof tactics** - Coq's automation may succeed where Lean's doesn't
3. **Cross-validation** - Results proven in both systems have higher confidence
4. **Learning resource** - Compare proof styles across systems

## Project Structure

```
coq/
├── README.md           # This file
├── _CoqProject         # Coq project configuration
├── Makefile            # Build configuration
└── theories/           # Formalization files
    ├── Basic.v         # Basic definitions and axioms
    ├── Operations.v    # Operation properties
    ├── Counterexamples.v  # Field axiom counterexamples
    └── Theorems.v      # Main theorems
```

## Status

### Completed ✓
- Project structure
- Documentation

### In Progress ⚠
- Basic definitions

## Prerequisites

### Install Coq

```bash
# Via opam (OCaml package manager)
opam install coq

# Or via system package manager
# Ubuntu/Debian:
sudo apt-get install coq

# macOS:
brew install coq

# Verify installation
coqc --version
```

### Recommended Tools

```bash
# CoqIDE - graphical interface
opam install coqide

# Proof General - Emacs mode
# (requires Emacs installed)

# VSCode extension
# Install "VSCoq" from VSCode marketplace
```

## Building

```bash
cd coq
make
```

## Usage

### Interactive Development

```bash
# Open in CoqIDE
coqide theories/Basic.v

# Or in Emacs with Proof General
emacs theories/Basic.v

# Or in VS Code with VSCoq extension
code theories/Basic.v
```

### Compilation

```bash
# Compile all files
make

# Compile specific file
coqc theories/Basic.v

# Clean build artifacts
make clean
```

### Documentation Generation

```bash
# Generate HTML documentation
coqdoc theories/*.v -d docs/

# View documentation
open docs/index.html
```

## Formalization Strategy

### Phase 1: Mirror Lean (Current)

Translate the Lean formalization to Coq:
- Define the algebra as a `Record` or `Module Type`
- Declare axioms using `Parameter` or `Axiom`
- State theorems using `Theorem` (with `Admitted` initially)

### Phase 2: Independent Proofs

Develop proofs using Coq-specific tactics:
- `auto`, `omega`, `lia` for automation
- `ring`, `field` for algebraic reasoning
- Custom tactics for I-specific properties

### Phase 3: Comparison

Compare with Lean proofs:
- Identify which proofs are easier in each system
- Cross-validate critical results
- Document differences in approach

## File Descriptions

### `_CoqProject`

Project configuration listing:
- Coq version requirements
- Source files
- Build flags

### `Makefile`

Generated from `_CoqProject` by:
```bash
coq_makefile -f _CoqProject -o Makefile
```

### `theories/Basic.v`

Core definitions:
```coq
(* The algebra structure *)
Module Type ALGEBRA_I.
  Parameter Carrier : Type.
  
  (* Elements *)
  Parameter zero : Carrier.
  Parameter one : Carrier.
  Parameter i : Carrier.
  
  (* Operations *)
  Parameter add : Carrier -> Carrier -> Carrier.
  Parameter mul : Carrier -> Carrier -> Carrier.
  Parameter neg : Carrier -> Carrier.
  
  (* Axioms *)
  Axiom i_squared : mul i i = i.
  Axiom i_plus_i : add i i = i.
  (* ... etc *)
End ALGEBRA_I.
```

### `theories/Operations.v`

Properties of operations:
- Closure, associativity, commutativity
- Identity and inverse properties
- Distributivity

### `theories/Counterexamples.v`

Formalized counterexamples:
```coq
Theorem i_no_inverse : ~exists x, mul i x = one.
Proof.
  (* proof by contradiction *)
Admitted.
```

### `theories/Theorems.v`

Main results and theorems.

## Development Guidelines

### Naming Conventions

- Types: `CamelCase` (e.g., `AlgebraI`)
- Definitions: `snake_case` (e.g., `i_squared`)
- Theorems: `descriptive_name` (e.g., `i_no_inverse`)
- Axioms: `axiom_name` (e.g., `add_comm`)

### Proof Style

```coq
Theorem example : forall a b, add a b = add b a.
Proof.
  intros a b.
  (* Use tactics: intro, destruct, apply, rewrite *)
  (* Document complex steps *)
  apply add_comm.
Qed.
```

### Using Automation

```coq
(* For arithmetic goals *)
Require Import Lia.
Goal forall n m : nat, n + m = m + n.
Proof. intros. lia. Qed.

(* For propositional logic *)
Require Import Tauto.
Goal forall P Q : Prop, P /\ Q -> Q /\ P.
Proof. tauto. Qed.
```

## Known Limitations

### Current Limitations

1. **No proofs yet** - Most theorems `Admitted`
2. **Basic structure only** - Minimal definitions
3. **No automation** - No custom tactics yet
4. **No extraction** - Can't execute computations

### Comparison with Lean

**Coq Advantages:**
- More mature proof automation (`auto`, `omega`)
- Richer standard library
- Better documentation generation
- Extraction to OCaml/Haskell

**Coq Disadvantages:**
- Less modern syntax
- More verbose in some cases
- Smaller community than Lean (currently)
- No metaprogramming (Lean has tactics written in Lean)

## Differences from Lean Formalization

| Aspect | Lean 4 | Coq |
|--------|--------|-----|
| Type Theory | Dependent Type Theory + Quotients | Calculus of Inductive Constructions |
| Syntax | More concise | More explicit |
| Tactics | `simp`, `ring`, `omega` | `auto`, `ring`, `omega`, `lia` |
| Modules | Namespaces | Modules |
| Notation | Unicode-friendly | ASCII-focused (but Unicode possible) |
| Metaprogramming | Lean 4 metaprogramming | Ltac, Ltac2 |

## Contributing

### Adding Definitions

1. Add to `theories/Basic.v`
2. Update `_CoqProject` if needed
3. Regenerate Makefile: `coq_makefile -f _CoqProject -o Makefile`
4. Update this README

### Adding Proofs

1. Find theorem with `Admitted`
2. Replace with actual proof ending in `Qed`
3. Document proof strategy in comments
4. Update status in README

## Resources

### Coq Documentation

- [Coq Reference Manual](https://coq.inria.fr/refman/)
- [Software Foundations](https://softwarefoundations.cis.upenn.edu/)
- [Certified Programming with Dependent Types](http://adam.chlipala.net/cpdt/)

### Learning Resources

- [Coq Discord](https://discord.gg/coq)
- [Coq Zulip](https://coq.zulipchat.com/)
- [Coq Tutorial](https://coq.inria.fr/tutorial)

### Related Formalizations

- Mathematical Components
- Formalizations in algebra
- Standard Library

## Contact

For questions about the Coq formalization:
- Open an issue: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I/issues
- Tag with `coq` label

## License

See main repository LICENSE file.

## Relationship to Lean Formalization

This Coq formalization is secondary to the Lean formalization in `../lean/`. The Lean version is the primary formalization target. This Coq version serves as:
1. An independent verification path
2. A learning resource for comparing proof assistants
3. An alternative for those more familiar with Coq

Critical results should be proven in both systems when possible.

---

Last updated: 2024-XX-XX
