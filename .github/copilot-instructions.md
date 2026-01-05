# Copilot Instructions — Algebra of the Indeterminate Hub

Implement an extended algebra with an indeterminate element `I = 0/0` and optional dual element `J`.

## Global constraints

Never change mathematical semantics without updating:
- `data/axioms/axioms.yaml`
- `docs/theory/axioms/*`
- unit tests in `src/python/tests/`

Every operation must have:
- docstring with formal signature
- at least 5 tests (including edge cases with I and 0)

Prefer deterministic rules; if context-dependence exists, implement explicit "semantics modes".

## Implementation order (mandatory)

### Phase 1 — Core datatypes and printing
- Implement `ialgebra/types.py`, `exceptions.py`, `printing.py`

### Phase 2 — Operations
- Implement `operations.py` with `⊕ ⊖ ⊗ ⊘` and classical `+ - * /` mapped where appropriate.
- Implement invariants and safety checks in `validation/invariants.py`

### Phase 3 — Rewrite/simplification
- Implement `simplify.py` driven by `data/axioms/rewrite_rules.yaml`

### Phase 4 — Wheel of Fractions
- Implement `wheel.py` and notebook `03_wheel_geometry.ipynb`

### Phase 5 — I-Calculus
- Implement `calculus.py` + examples notebook `06_I_calculus_examples.ipynb`

## Definition of Done (DoD)
- `make python_test` passes
- `ialgebra` package exposes a stable API
- CLI REPL works: `python -m cli.main repl`
- Minimal Lean build passes: `lake build`

## Do NOT
- Do not implement "magic" simplifications not listed in `rewrite_rules.yaml`
- Do not remove failing tests; document limitations in `audits/model_limitations.md`
