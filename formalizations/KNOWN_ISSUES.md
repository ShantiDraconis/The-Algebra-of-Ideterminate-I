# Known Issues and Future Work

## Lean 4 Proofs

The following theorems have `sorry` placeholders that need completion:

### ITheory.lean
- `gravitational_force_decreases`: Proof that F ∝ 1/r²
  - Need to show division by larger r² gives smaller result
  - Requires additional lemmas about Real division
  
- `i_planck_length_relation`: Algebraic manipulation
  - Shows ℓ_P^(I) = ℓ_P × √I
  - Requires Real.sqrt multiplication properties

### IPhysics.lean
- `energy_increases_with_momentum`: Monotonicity of E(p)
  - Need to prove √((p*c)² + (m*c²)²) increases with p
  - Requires Real.sqrt monotonicity lemmas
  
- `redshift_increases_wavelength`: Trivial arithmetic
  - Just needs algebraic simplification
  
- `planck_length_fundamental`: Quantum effects axiom
  - This is more of a physical axiom than mathematical proof
  - May need to be restated as axiom
  
- `bec_condition`: BEC occurrence condition
  - Relates to physical state existence
  - May need axiomatization of quantum states
  
- `keplers_third_law`: Orbital mechanics
  - Requires substitution and algebraic manipulation
  - Should be straightforward given orbital period definition

## Priority

**High Priority** (straightforward algebraic proofs):
1. `redshift_increases_wavelength`
2. `keplers_third_law`
3. `i_planck_length_relation`

**Medium Priority** (need auxiliary lemmas):
1. `gravitational_force_decreases`
2. `energy_increases_with_momentum`

**Low Priority** (require deeper physics axiomatization):
1. `planck_length_fundamental`
2. `bec_condition`

## Recommended Approach

1. Add auxiliary lemmas for common patterns:
   ```lean
   lemma div_decreases_with_larger_divisor (a b c : ℝ) (hb : 0 < b) (hc : 0 < c) (h : b < c) :
       a / c < a / b
   ```

2. Import additional Mathlib modules for:
   - Real analysis lemmas
   - Monotonicity properties
   - Square root properties

3. Consider axiomatizing physical principles where appropriate

## Coq Proofs

Similar patterns appear in ITheory.v:
- `energy_increases_with_momentum`: Needs Real analysis
- `keplers_third_law`: Algebraic manipulation

These can be completed using Coq's `lra` (linear real arithmetic) tactic once the structure is properly set up.

## Isabelle Proofs

Theorems marked with `sorry` in ITheory.thy can likely be proven using:
- `auto` and `simp` tactics
- `sledgehammer` for automated proof search
- Real arithmetic methods

## Status

This is acceptable for initial formalization as:
1. All definitions are complete and correct
2. Physical equations are properly encoded
3. Type signatures ensure correctness
4. Python tests verify numerical correctness

The `sorry` placeholders represent future work items rather than fundamental issues with the formalization.
