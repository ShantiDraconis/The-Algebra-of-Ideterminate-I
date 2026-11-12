# Indet — exact arithmetic with an absorbing indeterminate, for Lean 4 / Mathlib

`Indet α` is `α` plus one element `𝕀`:

- on determined values (`val a`) the operations are those of `α`;
- `𝕀` absorbs `+`, `·`, `−` (including `0 · 𝕀 = 𝕀`);
- division by zero gives `𝕀`, so `0 / 0 = 𝕀`.

There are no axioms in this library: `𝕀 ≠ val a` is a theorem.

## Where it stands, honestly

- **Data representation.** As a data type `Indet α` is `Option α` with the operations lifted (`Indet.equivOption`, `toOption_add`, `toOption_mul`).
- **Prior art.** The absorbing element itself is not new: IEEE 754 NaN, wheel theory (`0/0 = ⊥`), Kleene's three-valued logic and SQL `NULL` all have it.
- **Mathlib's convention.** Mathlib makes division total in a different way, with `x / 0 = 0` (`div_zero`).
- **What the library adds is a way of proving:**
  - the predicates `Det x` (determined) and `v x` (value);
  - the extensionality theorem `Indet.ext_iff'`: `x = y ↔ (Det x ↔ Det y) ∧ (Det x → v x = v y)`;
  - the tactics `indet_ring` and `indet_field`, which split an identity into its determinacy part and its value part, without the `2ⁿ` case split over the variables.
- **Identities that hold with no hypotheses.** These are identities where both sides become `𝕀` in every degenerate case. Example: `Indet.div_add_div' : a/b + c/d = (a·d + b·c)/(b·d)` holds unconditionally; Mathlib's `div_add_div` needs `b ≠ 0` and `d ≠ 0`.
- **Where it loses.** Some identities that are free in Mathlib need a hypothesis here. Example: `(a/b)/(c/d) = (a·d)/(b·c)` needs `v d ≠ 0`.
- **It is not a ring.** `0 · 𝕀 = 𝕀 ≠ 0`, so `ring` and `field_simp` do not apply to `Indet α` directly. The two tactics route through `α`.

## Benchmarks

Measured on Lean v4.19.0 with Mathlib v4.19.0, on a 2-core machine.

### Verification effort (`#count_heartbeats`, `-DElab.async=false`)

| Family | Mathlib (proof) | Hypotheses in Mathlib | Indet | Hypotheses in Indet | Indet / Mathlib |
|---|---|---|---|---|---|
| Sum of k fractions, k = 2…5 (`field_simp; ring`) | 2 721 – 14 713 | k | 4 873 – 21 636 | 0 | 1.8× → 1.5× |
| Product of k fractions, k = 2…6 (`ring`) | 389 – 1 179 | 0 | 1 897 – 5 317 | 0 | ~4.5× |
| Quotient of quotients (`div_div_div_eq`) | 256 | 0 | 5 546 | 1 | 21.7× |
| (Σ k terms)·(Σ k terms), k = 2…5 (`ring`) | 659 – 3 304 | 0 | 1 570 – 7 300 | 0 | ~2.2× |
| **Chained use** of the sum lemma, 3 fractions | 1 248 | 3, plus `mul_ne_zero` | **676** | **0** | **0.54×** |
| **Chained use** of the sum lemma, 5 fractions | 2 751 | 5, plus nested `mul_ne_zero` | **1 328** | **0** | **0.48×** |

The tactics cost more than Mathlib's own automation. A hypothesis-free lemma, proved once, is then cheaper to use: about half the heartbeats, and no side conditions to carry through a chain.

With 6 fractions, Mathlib v4.19's `field_simp` stops clearing denominators, and both formulations stop at the same point.

### Execution (compiled, `-O3`)

- **Sum of 10⁶ quotients, ℚ versus `Option ℚ` versus `Indet ℚ`:** the three are equal within noise, about 390 ns/op. The cost is rational normalisation, not the wrapper.
- **Absorbing early exit:** after the first `𝕀` the sum stops; the same holds for `Option`.
- **Decide the exact sign of 1 000 sums of 1 000 quotients each** (`runtime/`):

| Workload | Exact ℚ | Float only | Hybrid (Float + error bound, ℚ only when unsure) |
|---|---|---|---|
| no zero divisors | 418 ms | 21 ms | 41 ms |
| 1 % of chains summing exactly to 0 | 416 ms | 21 ms, **4 wrong signs** | 43 ms, **0 wrong signs** (4 chains recomputed exactly) |
| plus 0.1 % zero divisors | 258 ms | 13 ms, 4 wrong | 27 ms, 0 wrong |
| plus 10 % zero divisors | 5.0 ms | 0.3 ms, 4 wrong | 2.1 ms, 0 wrong |

The hybrid computes in hardware floating point and keeps a rounding-error bound `γ·Σ|tₖ|`. Only when `|s|` falls under that bound does it recompute the sum in ℚ. Its results equal the exact ones, and it runs about 10× faster.

## Files

- `Indet.lean`: the library (type, simp set, structure instances, `Det`/`v`, `ext_iff'`, tactics, hypothesis-free field lemmas).
- `IndetTest.lean`: tests. Every theorem prints only the standard axioms under `#print axioms`.
- `IndetBench.lean`: the verification benchmark. The numbers are in `resultados_heartbeats.json`.
- `runtime/`: the execution benchmark (exact, Float, hybrid) and `resultados_1000x1000.csv`.

## Build

```
lake build                      # Indet
lake build IndetTest            # tests
lake env lean -DElab.async=false IndetBench.lean
cd runtime && lake build && .lake/build/bin/hibrido 1000 1000 5
```
