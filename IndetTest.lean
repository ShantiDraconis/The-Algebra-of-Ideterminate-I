import Indet

/-!
# Testes da biblioteca `Indet`

Cada teorema abaixo é verificado pelo kernel; os `#print axioms` no fim mostram que só aparecem os axiomas padrão
(`propext`, `Classical.choice`, `Quot.sound`).
-/

open Indet

namespace IndetTest

variable {K : Type*} [Field K] [DecidableEq K]

set_option linter.unusedSectionVars false

/-! ## Valores concretos -/

example : ((0 : Indet ℚ) / 0) = 𝕀 := by simp [zero_def]
example : ((val 1 : Indet ℚ) / val 0) = 𝕀 := by simp
example : ((val 6 : Indet ℚ) / val 3) = val 2 := by norm_num
example : (0 : Indet ℚ) * 𝕀 = 𝕀 := rfl

/-! ## Identidades de corpo sem hipóteses

Nos casos degenerados (algum denominador nulo ou alguma variável `𝕀`) os dois lados viram `𝕀`. -/

theorem soma_fracoes (a b c d : Indet K) : a / b + c / d = (a * d + b * c) / (b * d) := by
  indet_field

theorem tres_fracoes (a b c d e f : Indet K) :
    a / b + c / d + e / f = ((a * d + b * c) * f + (b * d) * e) / ((b * d) * f) := by
  indet_field

theorem produto_fracoes (a b c d : Indet K) : (a / b) * (c / d) = (a * c) / (b * d) := by
  indet_field

theorem diferenca_fracoes (a b c d : Indet K) : a / b - c / d = (a * d - b * c) / (b * d) := by
  indet_field

/-! ## Identidades de anel (sem divisão), sem abrir `2ⁿ` casos -/

theorem distrib (x y z : Indet K) : x * (y + z) = x * y + x * z := by indet_ring

theorem quatro_termos (x y z w : Indet K) : (x + y) * (z + w) = x * z + x * w + y * z + y * w := by indet_ring

theorem nove_termos (x y z u v w : Indet K) :
    (x + y + z) * (u + v + w) = x*u + x*v + x*w + y*u + y*v + y*w + z*u + z*v + z*w := by indet_ring

theorem quadrado (x y : Indet K) : (x + y) * (x + y) = x * x + (1 + 1) * (x * y) + y * y := by indet_ring

/-! ## Onde a hipótese continua necessária

`(a/b)/(c/d) = (a·d)/(b·c)` vale no Mathlib sem hipótese; em `Indet` falha quando `d = 0`
(lado esquerdo `𝕀`, lado direito determinado). Com `v d ≠ 0` (que já obriga `d` a ser determinado), vale. -/

theorem quociente_falso_sem_hipotese :
    ¬ ∀ a b c d : Indet ℚ, (a / b) / (c / d) = (a * d) / (b * c) := by
  intro h
  have := h 1 1 1 0
  simp [zero_def, one_def] at this

theorem quociente (a b c d : Indet K) (hd0 : v d ≠ 0) :
    (a / b) / (c / d) = (a * d) / (b * c) := by
  indet_field

theorem cancelamento (a b : Indet K) (hb : Det b) (hb0 : v b ≠ 0) : a / b * b = a := by
  indet_field

/-! ## O que `Indet` não é -/

/-- Não é anel: `0 · 𝕀 = 𝕀 ≠ 0`. -/
example : ¬ ∀ x : Indet ℚ, 0 * x = 0 := not_zero_mul

/-- Não há inverso aditivo para `𝕀`. -/
example : ∀ y : Indet ℚ, 𝕀 + y ≠ 0 := by intro y; simp [zero_def]

end IndetTest

#print axioms IndetTest.soma_fracoes
#print axioms IndetTest.tres_fracoes
#print axioms IndetTest.nove_termos
#print axioms IndetTest.quociente
#print axioms IndetTest.cancelamento
#print axioms IndetTest.quociente_falso_sem_hipotese
