import Indet

/-!
# Benchmark: `Indet` (`indet_field` / `indet_ring`) × Mathlib (`field_simp` / `ring`)

Mesmas identidades nas duas formulações. Mede-se o esforço de elaboração com `#count_heartbeats in`
(rodar com `-DElab.async=false`, senão as provas são elaboradas em paralelo e a contagem só vê o enunciado).

* **F1** soma de k frações (k = 2…5): no Mathlib precisa de k hipóteses `bᵢ ≠ 0`; em `Indet`, nenhuma. Com k = 6 o
  `field_simp` do Mathlib v4.19 não termina de limpar os denominadores, e as duas formulações param no mesmo ponto.
* **F2** produto de k frações: nenhuma hipótese nas duas.
* **F3** quociente de quocientes: nenhuma hipótese no Mathlib; uma em `Indet`.
* **F4** produto de duas somas de k termos (só anel): nenhuma hipótese nas duas.
* **F5** uso em cadeia do lema de soma de frações: k − 1 reescritas; no Mathlib, com as hipóteses acumuladas.
-/

open Indet

namespace IndetBench

variable {K : Type*} [Field K] [DecidableEq K]

set_option linter.unusedSectionVars false

/-! ## F1: soma de k frações -/

#count_heartbeats in
theorem m_soma2 (a1 b1 a2 b2 : K) (h1 : b1 ≠ 0) (h2 : b2 ≠ 0) :
    a1 / b1 + a2 / b2 = ((a1) * b2 + (b1) * a2) / ((b1) * b2) := by field_simp; ring

#count_heartbeats in
theorem i_soma2 (a1 b1 a2 b2 : Indet K) :
    a1 / b1 + a2 / b2 = ((a1) * b2 + (b1) * a2) / ((b1) * b2) := by indet_field

#count_heartbeats in
theorem m_soma3 (a1 b1 a2 b2 a3 b3 : K) (h1 : b1 ≠ 0) (h2 : b2 ≠ 0) (h3 : b3 ≠ 0) :
    a1 / b1 + a2 / b2 + a3 / b3 = (((a1) * b2 + (b1) * a2) * b3 + ((b1) * b2) * a3) / (((b1) * b2) * b3) := by field_simp; ring

#count_heartbeats in
theorem i_soma3 (a1 b1 a2 b2 a3 b3 : Indet K) :
    a1 / b1 + a2 / b2 + a3 / b3 = (((a1) * b2 + (b1) * a2) * b3 + ((b1) * b2) * a3) / (((b1) * b2) * b3) := by indet_field

#count_heartbeats in
theorem m_soma4 (a1 b1 a2 b2 a3 b3 a4 b4 : K) (h1 : b1 ≠ 0) (h2 : b2 ≠ 0) (h3 : b3 ≠ 0) (h4 : b4 ≠ 0) :
    a1 / b1 + a2 / b2 + a3 / b3 + a4 / b4 = ((((a1) * b2 + (b1) * a2) * b3 + ((b1) * b2) * a3) * b4 + (((b1) * b2) * b3) * a4) / ((((b1) * b2) * b3) * b4) := by field_simp; ring

#count_heartbeats in
theorem i_soma4 (a1 b1 a2 b2 a3 b3 a4 b4 : Indet K) :
    a1 / b1 + a2 / b2 + a3 / b3 + a4 / b4 = ((((a1) * b2 + (b1) * a2) * b3 + ((b1) * b2) * a3) * b4 + (((b1) * b2) * b3) * a4) / ((((b1) * b2) * b3) * b4) := by indet_field

#count_heartbeats in
theorem m_soma5 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 : K) (h1 : b1 ≠ 0) (h2 : b2 ≠ 0) (h3 : b3 ≠ 0) (h4 : b4 ≠ 0) (h5 : b5 ≠ 0) :
    a1 / b1 + a2 / b2 + a3 / b3 + a4 / b4 + a5 / b5 = (((((a1) * b2 + (b1) * a2) * b3 + ((b1) * b2) * a3) * b4 + (((b1) * b2) * b3) * a4) * b5 + ((((b1) * b2) * b3) * b4) * a5) / (((((b1) * b2) * b3) * b4) * b5) := by field_simp; ring

#count_heartbeats in
theorem i_soma5 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 : Indet K) :
    a1 / b1 + a2 / b2 + a3 / b3 + a4 / b4 + a5 / b5 = (((((a1) * b2 + (b1) * a2) * b3 + ((b1) * b2) * a3) * b4 + (((b1) * b2) * b3) * a4) * b5 + ((((b1) * b2) * b3) * b4) * a5) / (((((b1) * b2) * b3) * b4) * b5) := by indet_field

/-! ## F2: produto de k frações -/

#count_heartbeats in
theorem m_prod2 (a1 b1 a2 b2 : K) :
    (a1 / b1) * (a2 / b2) = (a1 * a2) / (b1 * b2) := by ring

#count_heartbeats in
theorem i_prod2 (a1 b1 a2 b2 : Indet K) :
    (a1 / b1) * (a2 / b2) = (a1 * a2) / (b1 * b2) := by indet_field

#count_heartbeats in
theorem m_prod3 (a1 b1 a2 b2 a3 b3 : K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) = (a1 * a2 * a3) / (b1 * b2 * b3) := by ring

#count_heartbeats in
theorem i_prod3 (a1 b1 a2 b2 a3 b3 : Indet K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) = (a1 * a2 * a3) / (b1 * b2 * b3) := by indet_field

#count_heartbeats in
theorem m_prod4 (a1 b1 a2 b2 a3 b3 a4 b4 : K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) * (a4 / b4) = (a1 * a2 * a3 * a4) / (b1 * b2 * b3 * b4) := by ring

#count_heartbeats in
theorem i_prod4 (a1 b1 a2 b2 a3 b3 a4 b4 : Indet K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) * (a4 / b4) = (a1 * a2 * a3 * a4) / (b1 * b2 * b3 * b4) := by indet_field

#count_heartbeats in
theorem m_prod5 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 : K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) * (a4 / b4) * (a5 / b5) = (a1 * a2 * a3 * a4 * a5) / (b1 * b2 * b3 * b4 * b5) := by ring

#count_heartbeats in
theorem i_prod5 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 : Indet K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) * (a4 / b4) * (a5 / b5) = (a1 * a2 * a3 * a4 * a5) / (b1 * b2 * b3 * b4 * b5) := by indet_field

#count_heartbeats in
theorem m_prod6 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 a6 b6 : K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) * (a4 / b4) * (a5 / b5) * (a6 / b6) = (a1 * a2 * a3 * a4 * a5 * a6) / (b1 * b2 * b3 * b4 * b5 * b6) := by ring

#count_heartbeats in
theorem i_prod6 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 a6 b6 : Indet K) :
    (a1 / b1) * (a2 / b2) * (a3 / b3) * (a4 / b4) * (a5 / b5) * (a6 / b6) = (a1 * a2 * a3 * a4 * a5 * a6) / (b1 * b2 * b3 * b4 * b5 * b6) := by indet_field

/-! ## F3: quociente de quocientes -/

#count_heartbeats in
theorem m_quoc (a b c d : K) : (a / b) / (c / d) = (a * d) / (b * c) := by rw [div_div_div_eq]

#count_heartbeats in
theorem i_quoc (a b c d : Indet K) (hd : v d ≠ 0) : (a / b) / (c / d) = (a * d) / (b * c) := by indet_field

/-! ## F4: produto de duas somas de k termos -/

#count_heartbeats in
theorem m_anel2 (x1 x2 y1 y2 : K) :
    (x1 + x2) * (y1 + y2) = x1 * y1 + x1 * y2 + x2 * y1 + x2 * y2 := by ring

#count_heartbeats in
theorem i_anel2 (x1 x2 y1 y2 : Indet K) :
    (x1 + x2) * (y1 + y2) = x1 * y1 + x1 * y2 + x2 * y1 + x2 * y2 := by indet_ring

#count_heartbeats in
theorem m_anel3 (x1 x2 x3 y1 y2 y3 : K) :
    (x1 + x2 + x3) * (y1 + y2 + y3) = x1 * y1 + x1 * y2 + x1 * y3 + x2 * y1 + x2 * y2 + x2 * y3 + x3 * y1 + x3 * y2 + x3 * y3 := by ring

#count_heartbeats in
theorem i_anel3 (x1 x2 x3 y1 y2 y3 : Indet K) :
    (x1 + x2 + x3) * (y1 + y2 + y3) = x1 * y1 + x1 * y2 + x1 * y3 + x2 * y1 + x2 * y2 + x2 * y3 + x3 * y1 + x3 * y2 + x3 * y3 := by indet_ring

#count_heartbeats in
theorem m_anel4 (x1 x2 x3 x4 y1 y2 y3 y4 : K) :
    (x1 + x2 + x3 + x4) * (y1 + y2 + y3 + y4) = x1 * y1 + x1 * y2 + x1 * y3 + x1 * y4 + x2 * y1 + x2 * y2 + x2 * y3 + x2 * y4 + x3 * y1 + x3 * y2 + x3 * y3 + x3 * y4 + x4 * y1 + x4 * y2 + x4 * y3 + x4 * y4 := by ring

#count_heartbeats in
theorem i_anel4 (x1 x2 x3 x4 y1 y2 y3 y4 : Indet K) :
    (x1 + x2 + x3 + x4) * (y1 + y2 + y3 + y4) = x1 * y1 + x1 * y2 + x1 * y3 + x1 * y4 + x2 * y1 + x2 * y2 + x2 * y3 + x2 * y4 + x3 * y1 + x3 * y2 + x3 * y3 + x3 * y4 + x4 * y1 + x4 * y2 + x4 * y3 + x4 * y4 := by indet_ring

#count_heartbeats in
theorem m_anel5 (x1 x2 x3 x4 x5 y1 y2 y3 y4 y5 : K) :
    (x1 + x2 + x3 + x4 + x5) * (y1 + y2 + y3 + y4 + y5) = x1 * y1 + x1 * y2 + x1 * y3 + x1 * y4 + x1 * y5 + x2 * y1 + x2 * y2 + x2 * y3 + x2 * y4 + x2 * y5 + x3 * y1 + x3 * y2 + x3 * y3 + x3 * y4 + x3 * y5 + x4 * y1 + x4 * y2 + x4 * y3 + x4 * y4 + x4 * y5 + x5 * y1 + x5 * y2 + x5 * y3 + x5 * y4 + x5 * y5 := by ring

#count_heartbeats in
theorem i_anel5 (x1 x2 x3 x4 x5 y1 y2 y3 y4 y5 : Indet K) :
    (x1 + x2 + x3 + x4 + x5) * (y1 + y2 + y3 + y4 + y5) = x1 * y1 + x1 * y2 + x1 * y3 + x1 * y4 + x1 * y5 + x2 * y1 + x2 * y2 + x2 * y3 + x2 * y4 + x2 * y5 + x3 * y1 + x3 * y2 + x3 * y3 + x3 * y4 + x3 * y5 + x4 * y1 + x4 * y2 + x4 * y3 + x4 * y4 + x4 * y5 + x5 * y1 + x5 * y2 + x5 * y3 + x5 * y4 + x5 * y5 := by indet_ring

/-! ## F5: uso em cadeia de um lema de soma de frações (k frações)

No Mathlib cada reescrita pede as hipóteses do denominador acumulado (`mul_ne_zero`); em `Indet` não há condições. -/

#count_heartbeats in
theorem m_uso3 (a b c d e f : K) (hb : b ≠ 0) (hd : d ≠ 0) (hf : f ≠ 0) :
    a / b + c / d + e / f = ((a * d + b * c) * f + (b * d) * e) / ((b * d) * f) := by
  rw [div_add_div _ _ hb hd, div_add_div _ _ (mul_ne_zero hb hd) hf]

#count_heartbeats in
theorem i_uso3 (a b c d e f : Indet K) :
    a / b + c / d + e / f = ((a * d + b * c) * f + (b * d) * e) / ((b * d) * f) := by
  rw [div_add_div', div_add_div']

#count_heartbeats in
theorem m_uso5 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 : K) (h1 : b1 ≠ 0) (h2 : b2 ≠ 0) (h3 : b3 ≠ 0) (h4 : b4 ≠ 0)
    (h5 : b5 ≠ 0) :
    a1 / b1 + a2 / b2 + a3 / b3 + a4 / b4 + a5 / b5 =
      ((((a1 * b2 + b1 * a2) * b3 + (b1 * b2) * a3) * b4 + (b1 * b2 * b3) * a4) * b5 + (b1 * b2 * b3 * b4) * a5) /
        (b1 * b2 * b3 * b4 * b5) := by
  rw [div_add_div _ _ h1 h2, div_add_div _ _ (mul_ne_zero h1 h2) h3,
    div_add_div _ _ (mul_ne_zero (mul_ne_zero h1 h2) h3) h4,
    div_add_div _ _ (mul_ne_zero (mul_ne_zero (mul_ne_zero h1 h2) h3) h4) h5]

#count_heartbeats in
theorem i_uso5 (a1 b1 a2 b2 a3 b3 a4 b4 a5 b5 : Indet K) :
    a1 / b1 + a2 / b2 + a3 / b3 + a4 / b4 + a5 / b5 =
      ((((a1 * b2 + b1 * a2) * b3 + (b1 * b2) * a3) * b4 + (b1 * b2 * b3) * a4) * b5 + (b1 * b2 * b3 * b4) * a5) /
        (b1 * b2 * b3 * b4 * b5) := by
  rw [div_add_div', div_add_div', div_add_div', div_add_div']

end IndetBench
