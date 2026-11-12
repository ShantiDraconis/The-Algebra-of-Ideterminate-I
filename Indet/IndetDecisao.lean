import Indet

/-!
# Decisão sem humano no laço: a especificação, provada para todas as entradas

Uma decisão recebe uma lista de quocientes `aₖ / bₖ` e devolve uma de três saídas: `aprova` (se `Σ aₖ/bₖ ≥ 0`),
`reprova` (se `Σ aₖ/bₖ < 0`) ou `erro k`, onde `k` é o índice do primeiro denominador nulo.

`decidir` é o programa: uma passada só, que acumula a soma e para no primeiro denominador nulo, como o
`runtime/Origem.lean`. Os teoremas abaixo valem para **toda** lista, não só para as do teste de lote cego
(`lote_cego.py`, que roda este mesmo `decidir`):

* `decidir_eq`: o programa é igual à especificação;
* `nunca_em_silencio`: se algum denominador é nulo, a saída é `erro k` com `k` o primeiro índice nulo;
* `sem_alarme_falso`: se nenhum denominador é nulo, a saída é a decisão exata em `ℚ`;
* `decidir_erro_iff_indet`: a saída é um erro exatamente quando a soma em `Indet ℚ` dá `𝕀`;
* `total_aprova_em_silencio`: com a divisão total do Mathlib (`x / 0 = 0`), toda decisão de um termo só com
  denominador nulo é aprovada, qualquer que seja o numerador;
* `decidirNulo_eq_total`: a decisão em SQL (`x / 0` é `NULL`, `SUM` ignora `NULL`) é, para toda lista, a mesma
  da divisão total;
* `nulo_nunca_avisa`, `nulo_ignora_nulo`: a decisão em SQL nunca devolve erro, e um termo com denominador nulo,
  com qualquer numerador e em qualquer posição, não muda a decisão.
-/

open Indet

namespace IndetDecisao

/-- As três saídas de uma decisão. -/
inductive Saida where
  | aprova
  | reprova
  | erro (k : ℕ)
  deriving DecidableEq, Repr

/-- O programa: uma passada; no primeiro denominador nulo para e devolve o índice dele. -/
def passada : List (ℚ × ℚ) → ℕ → ℚ → Saida
  | [], _, s => if 0 ≤ s then .aprova else .reprova
  | (a, b) :: r, i, s => if b = 0 then .erro i else passada r (i + 1) (s + a / b)

/-- A decisão. -/
def decidir (l : List (ℚ × ℚ)) : Saida := passada l 0 0

/-- A mesma decisão com a divisão total do Mathlib (`x / 0 = 0`): sempre decide. -/
def decidirTotal (l : List (ℚ × ℚ)) : Saida :=
  if 0 ≤ (l.map fun p => p.1 / p.2).sum then .aprova else .reprova

/-! ## A especificação -/

/-- Índice do primeiro denominador nulo. -/
def primeiroZero : List (ℚ × ℚ) → Option ℕ
  | [] => none
  | (_, b) :: r => if b = 0 then some 0 else (primeiroZero r).map (· + 1)

/-- A soma exata (só tem sentido quando nenhum denominador é nulo). -/
def soma (l : List (ℚ × ℚ)) : ℚ := (l.map fun p => p.1 / p.2).sum

/-- A soma no indeterminado da biblioteca. -/
def somaI (l : List (ℚ × ℚ)) : Indet ℚ := (l.map fun p => (val p.1 : Indet ℚ) / val p.2).sum

theorem passada_eq (l : List (ℚ × ℚ)) (i : ℕ) (s : ℚ) :
    passada l i s = match primeiroZero l with
      | some k => .erro (i + k)
      | none => if 0 ≤ s + soma l then .aprova else .reprova := by
  induction l generalizing i s with
  | nil => simp [passada, primeiroZero, soma]
  | cons p r ih =>
    obtain ⟨a, b⟩ := p
    by_cases hb : b = 0
    · simp [passada, primeiroZero, hb]
    · simp only [passada, primeiroZero, hb, if_false, ih]
      cases h : primeiroZero r with
      | none => simp [soma, add_assoc]
      | some k => simp [Nat.add_assoc, Nat.add_comm 1 k]

/-- O programa é igual à especificação. -/
theorem decidir_eq (l : List (ℚ × ℚ)) :
    decidir l = match primeiroZero l with
      | some k => .erro k
      | none => if 0 ≤ soma l then .aprova else .reprova := by
  rw [decidir, passada_eq]
  cases primeiroZero l <;> simp

theorem primeiroZero_none_iff (l : List (ℚ × ℚ)) : primeiroZero l = none ↔ ∀ p ∈ l, p.2 ≠ 0 := by
  induction l with
  | nil => simp [primeiroZero]
  | cons p r ih =>
    obtain ⟨a, b⟩ := p
    by_cases hb : b = 0 <;> simp [primeiroZero, hb, ih]

theorem primeiroZero_some_iff (l : List (ℚ × ℚ)) (k : ℕ) :
    primeiroZero l = some k ↔
      (∃ p, l[k]? = some p ∧ p.2 = 0) ∧ ∀ j < k, ∀ p, l[j]? = some p → p.2 ≠ 0 := by
  induction l generalizing k with
  | nil => simp [primeiroZero]
  | cons p r ih =>
    obtain ⟨a, b⟩ := p
    by_cases hb : b = 0
    · cases k with
      | zero => simp [primeiroZero, hb]
      | succ k =>
        simp only [primeiroZero, hb, if_true, Option.some.injEq]
        constructor
        · intro h; omega
        · rintro ⟨_, h⟩
          exact absurd rfl (h 0 (by omega) (a, 0) rfl)
    · cases k with
      | zero => simp [primeiroZero, hb]
      | succ k =>
        simp only [primeiroZero, hb, if_false, Option.map_eq_some_iff, Nat.add_right_cancel_iff,
          exists_eq_right, ih, List.getElem?_cons_succ]
        constructor
        · rintro ⟨h1, h2⟩
          refine ⟨h1, fun j hj q hq => ?_⟩
          cases j with
          | zero => simp at hq; subst hq; exact hb
          | succ j => exact h2 j (by omega) q (by simpa using hq)
        · rintro ⟨h1, h2⟩
          exact ⟨h1, fun j hj q hq => h2 (j + 1) (by omega) q (by simpa using hq)⟩

/-- **Nunca em silêncio.** Se algum denominador é nulo, a saída é `erro k`, e `k` é o primeiro índice nulo. -/
theorem nunca_em_silencio (l : List (ℚ × ℚ)) (h : ∃ p ∈ l, p.2 = 0) :
    ∃ k, decidir l = .erro k ∧ (∃ p, l[k]? = some p ∧ p.2 = 0) ∧
      ∀ j < k, ∀ p, l[j]? = some p → p.2 ≠ 0 := by
  cases hz : primeiroZero l with
  | none =>
    obtain ⟨p, hp, h0⟩ := h
    exact absurd h0 ((primeiroZero_none_iff l).1 hz p hp)
  | some k => exact ⟨k, by rw [decidir_eq, hz], (primeiroZero_some_iff l k).1 hz⟩

/-- **Sem alarme falso.** Sem denominador nulo, a saída é a decisão exata em `ℚ`. -/
theorem sem_alarme_falso (l : List (ℚ × ℚ)) (h : ∀ p ∈ l, p.2 ≠ 0) :
    decidir l = if 0 ≤ soma l then .aprova else .reprova := by
  rw [decidir_eq, (primeiroZero_none_iff l).2 h]

/-- A soma no indeterminado é `𝕀` exatamente quando algum denominador é nulo; senão é a soma exata. -/
theorem somaI_eq (l : List (ℚ × ℚ)) :
    somaI l = if ∃ p ∈ l, p.2 = 0 then 𝕀 else val (soma l) := by
  induction l with
  | nil => simp [somaI, soma, zero_def]
  | cons p r ih =>
    obtain ⟨a, b⟩ := p
    simp only [somaI, soma, List.map_cons, List.sum_cons] at ih ⊢
    rw [ih]
    by_cases hb : b = 0
    · simp [hb]
    · by_cases hr : ∃ p ∈ r, p.2 = 0
      · simp [hb, hr]
      · simp [hb, hr]

/-- A saída é um erro exatamente quando a soma em `Indet ℚ` dá `𝕀`. -/
theorem decidir_erro_iff_indet (l : List (ℚ × ℚ)) : (∃ k, decidir l = .erro k) ↔ somaI l = 𝕀 := by
  rw [somaI_eq]
  by_cases h : ∃ p ∈ l, p.2 = 0
  · simp only [h, if_true, iff_true]
    obtain ⟨k, hk, -⟩ := nunca_em_silencio l h
    exact ⟨k, hk⟩
  · simp only [h, if_false, reduceCtorEq, iff_false, not_exists]
    push_neg at h
    intro k
    rw [sem_alarme_falso l h]
    split <;> simp

/-- **A divisão total aprova em silêncio.** Um termo só, denominador nulo, qualquer numerador: aprovado. -/
theorem total_aprova_em_silencio (a : ℚ) : decidirTotal [(a, 0)] = .aprova := by
  simp [decidirTotal]

/-- E a decisão com o indeterminado, na mesma entrada, devolve o erro no índice 0. -/
example (a : ℚ) : decidir [(a, 0)] = .erro 0 := by simp [decidir, passada]

/-! ## SQL: `x / 0` é `NULL` e `SUM` ignora `NULL`

No SQLite (e no MySQL fora do modo estrito), `x / 0` é `NULL`, e `SUM` pula os `NULL`. A decisão
"aprova se `SUM(a / b) ≥ 0`" vira a soma só dos termos com denominador não nulo. -/

/-- A decisão em SQL: soma só os termos com denominador não nulo. -/
def decidirNulo (l : List (ℚ × ℚ)) : Saida :=
  if 0 ≤ ((l.filter fun p => p.2 ≠ 0).map fun p => p.1 / p.2).sum then .aprova else .reprova

theorem soma_sem_nulos (l : List (ℚ × ℚ)) :
    ((l.filter fun p => p.2 ≠ 0).map fun p => p.1 / p.2).sum = (l.map fun p => p.1 / p.2).sum := by
  induction l with
  | nil => rfl
  | cons p r ih =>
    obtain ⟨a, b⟩ := p
    by_cases hb : b = 0
    · simpa [List.filter_cons, hb] using ih
    · simpa [List.filter_cons, hb] using ih

/-- **SQL decide como a divisão total.** Pular os `NULL` dá a mesma decisão que `x / 0 = 0`, para toda lista. -/
theorem decidirNulo_eq_total (l : List (ℚ × ℚ)) : decidirNulo l = decidirTotal l := by
  unfold decidirNulo decidirTotal
  rw [soma_sem_nulos]

/-- A decisão em SQL nunca devolve erro. -/
theorem nulo_nunca_avisa (l : List (ℚ × ℚ)) (k : ℕ) : decidirNulo l ≠ .erro k := by
  unfold decidirNulo
  split_ifs <;> simp

theorem soma_meio_zero (l₁ l₂ : List ℚ) : (l₁ ++ 0 :: l₂).sum = (l₁ ++ l₂).sum := by
  induction l₁ with
  | nil => simp
  | cons x r ih => simp [ih]

/-- Com a divisão total, um termo com denominador nulo some: qualquer numerador, em qualquer posição. -/
theorem total_ignora_nulo (l₁ l₂ : List (ℚ × ℚ)) (a : ℚ) :
    decidirTotal (l₁ ++ (a, 0) :: l₂) = decidirTotal (l₁ ++ l₂) := by
  simp [decidirTotal, soma_meio_zero]

/-- **Em SQL, o termo com denominador nulo some.** A decisão é a da lista sem ele. -/
theorem nulo_ignora_nulo (l₁ l₂ : List (ℚ × ℚ)) (a : ℚ) :
    decidirNulo (l₁ ++ (a, 0) :: l₂) = decidirNulo (l₁ ++ l₂) := by
  rw [decidirNulo_eq_total, decidirNulo_eq_total, total_ignora_nulo]

end IndetDecisao

#print axioms IndetDecisao.decidir_eq
#print axioms IndetDecisao.nunca_em_silencio
#print axioms IndetDecisao.sem_alarme_falso
#print axioms IndetDecisao.decidir_erro_iff_indet
#print axioms IndetDecisao.total_aprova_em_silencio
#print axioms IndetDecisao.decidirNulo_eq_total
#print axioms IndetDecisao.nulo_nunca_avisa
#print axioms IndetDecisao.nulo_ignora_nulo
