# Indet — exact arithmetic with an absorbing indeterminate, for Lean 4 / Mathlib

`Indet α` is `α` plus one element `𝕀`:

- on determined values (`val a`) the operations are those of `α`;
- `𝕀` absorbs `+`, `·`, `−` (including `0 · 𝕀 = 𝕀`);
- division by zero gives `𝕀`, so `0 / 0 = 𝕀`.

There are no axioms in this library: `𝕀 ≠ val a` is a theorem.

**Status.** Lean v4.19.0, Mathlib v4.19.0. The workflow `.github/workflows/indet.yml` builds the library and the tests. It also builds the decision theorems and checks that `#print axioms` lists only `propext`, `Classical.choice` and `Quot.sound` and never `sorryAx`. Then it runs both execution benchmarks at a reduced size and asserts their results. Finally it runs the blind batch test with a fresh seed. There is no `sorry` and no `axiom` in `Indet/`.

## Better and worse, side by side

| Where `Indet` is better | Measured | Where `Indet` is worse | Measured |
|---|---|---|---|
| Field identities with no hypotheses | sum of k fractions: Mathlib needs k hypotheses `≠ 0`, Indet needs 0 | Proof cost of the identities themselves | sum 1.5–1.8×, product 4.5–4.9×, ring 2.2–2.4×, quotient of quotients 21.7× **and** 1 hypothesis |
| Chained use of a hypothesis-free lemma | 676 vs 1 248 heartbeats (3 fractions), 1 328 vs 2 751 (5): **0.54× and 0.48×** | Not a ring | `0 · 𝕀 = 𝕀 ≠ 0`; `ring`/`field_simp` only through `indet_ring`/`indet_field` |
| The error stays visible | with total division (`x/0 = 0`), 96 of 96 decisions with a zero denominator were decided silently, 53 of them "approve"; with `𝕀`, 96 of 96 flagged | Plain execution speed | 10⁶ quotients in ~395 ms, a tie with `ℚ` and `Option ℚ` |
| The error has an address (`𝕀` with origin) | 96 of 96 located at the first zero denominator, 0 false alarms, cost within noise of plain `𝕀` | Hardware speed | `Float` is ~75× faster (5 ms vs 390 ms, 96 errors in 1 000) and also flags the error, but only because the code checks `isFinite` (a bare `s ≥ 0` approves `+∞` silently), and without the address and without exactness |
| Exact sign at near-float speed (hybrid) | 43 ms vs 416 ms exact on the workload with chains that sum exactly to 0, 0 wrong signs; `Float` alone: 4 wrong out of those 4 chains | Not unique | plain `𝕀` = `Option`; `𝕀` with origin = `Except Nat ℚ`; the absorbing element is IEEE NaN / wheel `⊥` / SQL `NULL` |

Prototypes that were measured and dropped: tactics by case split over `2ⁿ` cases cost 12 % to 31 % more than the plain rewriting version. A reflection prototype cut 6 variables from 3 998 to 1 241 heartbeats (−69 %), still 2.6× Mathlib's 485.

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
| chains summing exactly to 0 (rate 1 %; seed 42 gives 4 of them) | 416 ms | 21 ms, **4 wrong signs out of 4** | 43 ms, **0 wrong signs** (the 4 chains recomputed exactly) |
| plus 0.1 % zero divisors | 258 ms | 13 ms, 4 wrong | 27 ms, 0 wrong |
| plus 10 % zero divisors | 5.0 ms | 0.3 ms, 4 wrong | 2.1 ms, 0 wrong |

The hybrid computes in hardware floating point and keeps a rounding-error bound `γ·Σ|tₖ|`. Only when `|s|` falls under that bound does it recompute the sum in ℚ. Its results equal the exact ones, and it runs about 10× faster. The table gives the median of three runs (`resultados_1000x1000.csv` also has the minimum and maximum). The hybrid is a technique demonstrated in `runtime/`, not part of the library's API.

### Diagnostics: is the error silent, visible, or located? (`runtime/Origem.lean`)

The workload is 1 000 decisions of the form "approve if `Σ aₖ/bₖ ≥ 0`", 1 000 quotients each. In a fraction of the decisions, one or two denominators are set to 0 (a specification error, such as an empty weight). Five repetitions per formulation:

| Errors injected | Formulation | Median | Decided silently (of which "approve") | Flagged | Located at the first zero | False alarms |
|---|---|---|---|---|---|---|
| 96 of 1 000 | total division (`x/0 = 0`) | 397 ms | **96 (53)** | 0 | 0 | 0 |
| 96 of 1 000 | `Option ℚ` | 391 ms | 0 | 96 | 0 | 0 |
| 96 of 1 000 | `Float` (NaN/∞) | 5 ms | 0 | 96 | 0 | 0 |
| 96 of 1 000 | plain `𝕀` | 388 ms | 0 | 96 | 0 | 0 |
| 96 of 1 000 | `𝕀` with origin | 390 ms | 0 | 96 | **96** | 0 |
| 1 000 of 1 000 | total division | 406 ms | **1 000 (483)** | 0 | 0 | 0 |
| 1 000 of 1 000 | `𝕀` with origin | 170 ms | 0 | 1 000 | **1 000** | 0 |

The other rows (0 and 8 errors) are in `resultados_origem_1000x1000.csv`. On error-free input, all five agree and plain `𝕀` and `𝕀` with origin cost the same within noise.

Two caveats. The origin is a runtime feature: inside the algebra, an `𝕀` that keeps "the first origin" would make addition non-commutative (`𝕀₁ + 𝕀₂ ≠ 𝕀₂ + 𝕀₁`), so the library's `𝕀` carries none. Also, `𝕀` with origin is exactly `Except Nat ℚ`. What gives the address is carrying the origin, not the symbol `𝕀`.

### Deciding with no human in the loop: proved for every input, then tested blind

The decision rule is written by a person: approve if `Σ aₖ/bₖ ≥ 0`, otherwise reject. The program applies it with no help. For each input it returns `aprova`, `reprova` or `erro k`. The program does not invent rules. A new rule means new code.

**Proved for every input** (`IndetDecisao.lean`; `#print axioms` shows only the three standard axioms):

| Theorem | Statement |
|---|---|
| `decidir_eq` | the one-pass program equals its specification |
| `nunca_em_silencio` | if some denominator is 0, the output is `erro k`, where `k` is the first index with a zero denominator |
| `sem_alarme_falso` | if no denominator is 0, the output is the exact decision in `ℚ` |
| `decidir_erro_iff_indet` | the output is an error exactly when the sum in `Indet ℚ` is `𝕀` |
| `total_aprova_em_silencio` | with total division (`x/0 = 0`), any one-term decision with a zero denominator is approved, whatever the numerator |
| `decidirNulo_eq_total` | the SQL decision (`x/0` is `NULL`, `SUM` skips `NULL`) equals the total-division decision, for every input |
| `nulo_nunca_avisa` | the SQL decision never returns an error |
| `nulo_ignora_nulo` | in the SQL decision, a term with a zero denominator, any numerator, at any position, does not change the result |

**Tested blind** (`lote_cego.py` + `LoteCego.lean`). The protocol has four steps:

1. A generator draws 10 000 decisions of 99 quotients from an operating-system seed. It sets zero denominators in 5 % of them (one or two each, sometimes at the first or last position). It also makes 1 % of them sum to exactly 0.
2. The decider receives only the cases. It never sees the truth or the seed, and it runs the same `decidir` as the theorems.
3. A checker compares the outputs with the truth. It computes the expected decision independently, in Python with `fractions.Fraction`.
4. Negative controls must fail the same test: total division and `Float` in Lean, and the idiomatic one-line rule in SQLite, NumPy, pandas, Python and JavaScript (`adaptadores/`). A hand-written Python version of the same contract must pass. A test that cannot fail proves nothing.

CI runs all of this on every push with a fresh seed.

Local run, seed 16480616440769979998 (`resultados_lote_cego.json`):

| Decider | Silent on error (approved / rejected) | Flagged | Located | Wrong decisions without error | False alarms | Verdict |
|---|---|---|---|---|---|---|
| `decidir` (`𝕀` with origin) | 0 / 0 of 512 | 512 | 512 | 0 of 9 488 | 0 | passes |
| total division | 230 / 282 of 512 | 0 | 0 | 0 of 9 488 | 0 | fails |
| `Float` | 0 / 0 of 512 | 512 | 0 | 28 of 9 488, all 28 among the 81 sums that are exactly 0 | 0 | fails |

The test covers 10 000 cases; the theorems cover all of them.

### Common stacks on the same batch (`adaptadores/`)

Each decider below is the idiomatic way to write "approve if `Σ aₖ/bₖ ≥ 0`" in that stack. It reads the same cases file and never sees the truth. Same seed, 16480616440769979998 (`adaptadores/resultados_stacks.json`; Python 3.13, NumPy 2.5.3, pandas 3.0.5, SQLite 3.53.1, Node 22):

| Decider | Silent on error (approved / rejected) | Flagged | Located | Wrong decisions without error | Verdict |
|---|---|---|---|---|---|
| SQLite: `SUM(a * 1.0 / b) >= 0` | 230 / 282 of 512 | 0 | 0 | 40 of 9 488 | fails |
| NumPy: `np.sum(a / b) >= 0` | 169 / 343 of 512 | 0 | 0 | 25 of 9 488 | fails |
| pandas: `(df.a / df.b).sum() >= 0` | 184 / 328 of 512 | 0 | 0 | 29 of 9 488 | fails |
| JavaScript: `reduce((s, [a, b]) => s + a / b, 0) >= 0` | 169 / 343 of 512 | 0 | 0 | 28 of 9 488 | fails |
| Python `float`, `try/except ZeroDivisionError` | 0 / 0 of 512 | 512 | 0 | 40 of 9 488 | fails |
| Python `Fraction`, `try/except ZeroDivisionError` | 0 / 0 of 512 | 512 | 0 | 0 of 9 488 | fails |
| Python `Fraction`, returns the first zero index | 0 / 0 of 512 | 512 | 512 | 0 of 9 488 | passes |

Every wrong decision without error is among the 81 sums that are exactly 0.

What this shows:

- **SQL fails exactly like total division.** SQLite turns `x / 0` into `NULL`, and `SUM` skips it, so the term disappears. Its 230 / 282 split is the same as Lean's total division on the same batch. `decidirNulo_eq_total` proves the two decisions are equal for every input, and CI checks it on every blind batch.
- **NumPy and JavaScript fail by IEEE 754 rules.** `a / 0` is `±∞` and `0 / 0` is `NaN`; `NaN >= 0` is false, so those decisions are rejected silently.
- **pandas differs from NumPy** because `sum` skips `NaN` by default, so `0 / 0` terms disappear as in SQL.
- **The contract is easy to meet by hand once it is written down.** The last row passes. What Lean adds is the proof that `decidir` meets it for every input, not only the 10 000 tested.

## The AEI correction (`formalizations/lean/AlgebraIndeterminate/AEI.lean`)

- **The old rule was inconsistent.** The original text set `0 · 𝕀 = 1`. Together with associativity it gives `0 = 1`, and the theorem `KI.regra_antiga_colapsa` records this.
- **The new rule is `0 · 𝕀 = 𝕀`.** With it, multiplication is associative and commutative and distributes over addition.
- **No axioms are left.** `I_not_zero` and `I_not_field_element` are now theorems.
- **Still pending: `0 / a = 𝕀`.** The text's rule `0 / a = 𝕀` for `a ≠ 0` is kept as written. It is the author's decision and is not changed here. The library `Indet` uses the usual `0 / a = 0`.

## What this library does not claim

- **That `𝕀` is faster.** See the tables above.
- **That the idea of an absorbing error element is new.** The contribution is the proof technique (`Det`/`v`, `ext_iff'`, the two tactics, the hypothesis-free lemmas) and the measurements.
- **Anything about open problems.** Nothing here touches any Millennium problem.

## Files

- `Indet.lean`: the library (type, simp set, structure instances, `Det`/`v`, `ext_iff'`, tactics, hypothesis-free field lemmas).
- `IndetTest.lean`: tests. Every theorem prints only the standard axioms under `#print axioms`.
- `IndetBench.lean`: the verification benchmark. The numbers are in `resultados_heartbeats.json`.
- `runtime/Main.lean`: the execution benchmark (exact, Float, hybrid); results in `resultados_1000x1000.csv`.
- `runtime/Origem.lean`: the diagnostics benchmark (silent, flagged, located); results in `resultados_origem_1000x1000.csv`.
- `IndetDecisao.lean`: the decision program and the theorems that it never decides silently.
- `LoteCego.lean`, `lote_cego.py`: the blind batch test (generator, decider, independent checker, negative controls); a local run in `resultados_lote_cego.json`.
- `adaptadores/`: the same rule written idiomatically in SQLite, NumPy, pandas, Python and JavaScript, run on the same blind batch; a local run in `resultados_stacks.json`.

## Build

```
lake exe cache get              # Mathlib v4.19.0 cache
lake build                      # Indet
lake build IndetTest            # tests
lake build IndetDecisao         # the decision and its theorems
lake env lean -DElab.async=false IndetBench.lean
python3 lote_cego.py gera casos.txt verdade.json
lake env lean --run LoteCego.lean O casos.txt saidas_O.txt
python3 lote_cego.py confere verdade.json saidas_O.txt
cd runtime && lake build hibrido origem
.lake/build/bin/hibrido 1000 1000 5
.lake/build/bin/origem 1000 1000 5
```
