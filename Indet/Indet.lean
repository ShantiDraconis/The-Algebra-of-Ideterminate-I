import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Tauto
import Mathlib.Tactic.CasesM

/-!
# `Indet α`: aritmética com um indeterminado absorvente

`Indet α` é `α` acrescido de um elemento `𝕀`:

* na parte determinada (`val a`), as operações são as de `α`;
* `𝕀` absorve soma, produto, oposto e subtração (`𝕀 + x = 𝕀`, `0 · 𝕀 = 𝕀`);
* a divisão por zero dá `𝕀` (em particular `0 / 0 = 𝕀`).

Não há axiomas: `𝕀 ≠ val a` é um teorema (construtores distintos). Como estrutura de dados, `Indet α` é
`Option α` com as operações levantadas (`toOption_add` etc.); o que a biblioteca acrescenta é a maneira de provar.

## O que a biblioteca oferece

* um conjunto fechado de reescritas `@[simp]` para o absorvente;
* `Det x` (determinado) e `v x` (valor, `0` em `𝕀`) com o teorema de extensionalidade `ext_iff'`:
  `x = y ↔ (Det x ↔ Det y) ∧ (Det x → v x = v y)`;
* as táticas `indet_ring` e `indet_field`: uma identidade em `Indet α` vira (i) uma equivalência proposicional entre
  as condições de determinação dos dois lados (`tauto`) e (ii) a mesma identidade em `α` sob essas condições
  (`ring` / `field_simp`). Não se abrem `2ⁿ` casos.

Identidades em que os dois lados viram `𝕀` nos casos degenerados valem **sem hipóteses** (por exemplo
`a/b + c/d = (a·d + b·c)/(b·d)`); onde só um dos lados vira `𝕀`, a hipótese continua necessária (por exemplo
`(a/b)/(c/d) = (a·d)/(b·c)` precisa de `d` determinado e não nulo, que no Mathlib vale sem hipótese).
-/

/-- `α` com um indeterminado absorvente `𝕀`. -/
inductive Indet (α : Type*) where
  /-- um valor determinado -/
  | val : α → Indet α
  /-- o indeterminado -/
  | I : Indet α
  deriving DecidableEq, Repr

@[inherit_doc] notation "𝕀" => Indet.I

namespace Indet

variable {α : Type*}

instance : Coe α (Indet α) := ⟨val⟩
instance [Inhabited α] : Inhabited (Indet α) := ⟨I⟩

/-- `𝕀` não é valor nenhum. No AEI isto era axioma; aqui é teorema. -/
@[simp] theorem I_ne_val (a : α) : (𝕀 : Indet α) ≠ val a := nofun
@[simp] theorem val_ne_I (a : α) : val a ≠ (𝕀 : Indet α) := nofun

/-! ## Operações -/

section Ops

/-- soma, com `𝕀` absorvente -/
protected def add [Add α] : Indet α → Indet α → Indet α
  | val a, val b => val (a + b)
  | _, _ => I

/-- produto, com `𝕀` absorvente (inclusive `0 · 𝕀 = 𝕀`) -/
protected def mul [Mul α] : Indet α → Indet α → Indet α
  | val a, val b => val (a * b)
  | _, _ => I

/-- oposto -/
protected def neg [Neg α] : Indet α → Indet α
  | val a => val (-a)
  | I => I

/-- subtração -/
protected def sub [Sub α] : Indet α → Indet α → Indet α
  | val a, val b => val (a - b)
  | _, _ => I

/-- divisão: dividir por zero dá `𝕀` -/
protected def div [Div α] [Zero α] [DecidableEq α] : Indet α → Indet α → Indet α
  | val a, val b => if b = 0 then I else val (a / b)
  | _, _ => I

instance [Add α] : Add (Indet α) := ⟨Indet.add⟩
instance [Mul α] : Mul (Indet α) := ⟨Indet.mul⟩
instance [Neg α] : Neg (Indet α) := ⟨Indet.neg⟩
instance [Sub α] : Sub (Indet α) := ⟨Indet.sub⟩
instance [Div α] [Zero α] [DecidableEq α] : Div (Indet α) := ⟨Indet.div⟩
instance [Zero α] : Zero (Indet α) := ⟨val 0⟩
instance [One α] : One (Indet α) := ⟨val 1⟩

end Ops

/-! ## Reescritas -/

section Simp

@[simp] theorem val_add_val [Add α] (a b : α) : (val a : Indet α) + val b = val (a + b) := rfl
@[simp] theorem I_add [Add α] (x : Indet α) : 𝕀 + x = 𝕀 := rfl
@[simp] theorem add_I [Add α] (x : Indet α) : x + 𝕀 = 𝕀 := by cases x <;> rfl
@[simp] theorem val_mul_val [Mul α] (a b : α) : (val a : Indet α) * val b = val (a * b) := rfl
@[simp] theorem I_mul [Mul α] (x : Indet α) : 𝕀 * x = 𝕀 := rfl
@[simp] theorem mul_I [Mul α] (x : Indet α) : x * 𝕀 = 𝕀 := by cases x <;> rfl
@[simp] theorem neg_val [Neg α] (a : α) : -(val a : Indet α) = val (-a) := rfl
@[simp] theorem neg_I [Neg α] : -(𝕀 : Indet α) = 𝕀 := rfl
@[simp] theorem val_sub_val [Sub α] (a b : α) : (val a : Indet α) - val b = val (a - b) := rfl
@[simp] theorem I_sub [Sub α] (x : Indet α) : 𝕀 - x = 𝕀 := rfl
@[simp] theorem sub_I [Sub α] (x : Indet α) : x - 𝕀 = 𝕀 := by cases x <;> rfl
@[simp] theorem val_div_val [Div α] [Zero α] [DecidableEq α] (a b : α) :
    (val a : Indet α) / val b = if b = 0 then 𝕀 else val (a / b) := rfl
@[simp] theorem I_div [Div α] [Zero α] [DecidableEq α] (x : Indet α) : 𝕀 / x = 𝕀 := rfl
@[simp] theorem div_I [Div α] [Zero α] [DecidableEq α] (x : Indet α) : x / 𝕀 = 𝕀 := by cases x <;> rfl
theorem zero_def [Zero α] : (0 : Indet α) = val 0 := rfl
theorem one_def [One α] : (1 : Indet α) = val 1 := rfl

/-- `0/0 = 𝕀`. -/
theorem zero_div_zero [DivisionRing α] [DecidableEq α] : (0 : Indet α) / 0 = 𝕀 := by
  simp [zero_def]

/-- `0 · 𝕀 = 𝕀`: o absorvente vence o zero. Por isso `Indet α` não é anel (não vale `0 · x = 0`). -/
theorem zero_mul_I [Zero α] [Mul α] : (0 : Indet α) * 𝕀 = 𝕀 := rfl

theorem not_zero_mul [Zero α] [Mul α] : ¬ ∀ x : Indet α, 0 * x = 0 := fun h =>
  absurd (h 𝕀) (by simp [zero_def])

end Simp

/-! ## Estrutura algébrica

Monoide comutativo para a soma e para o produto, com distributividade; não é semianel (falha `0 · 𝕀 = 0`). -/

section Estrutura

instance [AddCommMonoid α] : AddCommMonoid (Indet α) where
  add_assoc a b c := by cases a <;> cases b <;> cases c <;> simp [add_assoc]
  zero_add a := by cases a <;> simp [zero_def]
  add_zero a := by cases a <;> simp [zero_def]
  add_comm a b := by cases a <;> cases b <;> simp [add_comm]
  nsmul := nsmulRec

instance [CommMonoid α] : CommMonoid (Indet α) where
  mul_assoc a b c := by cases a <;> cases b <;> cases c <;> simp [mul_assoc]
  one_mul a := by cases a <;> simp [one_def]
  mul_one a := by cases a <;> simp [one_def]
  mul_comm a b := by cases a <;> cases b <;> simp [mul_comm]

theorem left_distrib' [Distrib α] (a b c : Indet α) : a * (b + c) = a * b + a * c := by
  cases a <;> cases b <;> cases c <;> simp [left_distrib]

theorem right_distrib' [Distrib α] (a b c : Indet α) : (a + b) * c = a * c + b * c := by
  cases a <;> cases b <;> cases c <;> simp [right_distrib]

end Estrutura

/-! ## Determinação e valor -/

section DetV

/-- `x` é determinado (não é `𝕀`). -/
def Det : Indet α → Prop
  | val _ => True
  | I => False

/-- o valor de `x` (`0` em `𝕀`) -/
def v [Zero α] : Indet α → α
  | val a => a
  | I => 0

@[simp] theorem det_val (a : α) : Det (val a) := trivial
@[simp] theorem not_det_I : ¬ Det (𝕀 : Indet α) := id
@[simp] theorem det_zero [Zero α] : Det (0 : Indet α) := trivial
@[simp] theorem det_one [One α] : Det (1 : Indet α) := trivial
@[simp] theorem v_val [Zero α] (a : α) : v (val a) = a := rfl
@[simp] theorem v_I [Zero α] : v (𝕀 : Indet α) = 0 := rfl
@[simp] theorem v_zero [Zero α] : v (0 : Indet α) = 0 := rfl
@[simp] theorem v_one [Zero α] [One α] : v (1 : Indet α) = 1 := rfl

theorem det_iff_ne (x : Indet α) : Det x ↔ x ≠ 𝕀 := by cases x <;> simp [Det]

@[simp] theorem det_add [Add α] {x y : Indet α} : Det (x + y) ↔ Det x ∧ Det y := by
  cases x <;> cases y <;> simp [Det]
@[simp] theorem det_mul [Mul α] {x y : Indet α} : Det (x * y) ↔ Det x ∧ Det y := by
  cases x <;> cases y <;> simp [Det]
@[simp] theorem det_neg [Neg α] {x : Indet α} : Det (-x) ↔ Det x := by
  cases x <;> simp [Det]
@[simp] theorem det_sub [Sub α] {x y : Indet α} : Det (x - y) ↔ Det x ∧ Det y := by
  cases x <;> cases y <;> simp [Det]
@[simp] theorem det_div [Div α] [Zero α] [DecidableEq α] {x y : Indet α} :
    Det (x / y) ↔ Det x ∧ Det y ∧ v y ≠ 0 := by
  cases x <;> cases y <;> simp [Det] <;> split_ifs <;> simp_all [Det]

/-- No produto o valor é sempre o produto dos valores (onde há `𝕀`, os dois lados dão `0`). -/
@[simp] theorem v_mul [MulZeroClass α] (x y : Indet α) : v (x * y) = v x * v y := by
  cases x <;> cases y <;> simp
@[simp] theorem v_neg [NegZeroClass α] (x : Indet α) : v (-x) = -v x := by
  cases x <;> simp
/-- Num anel de divisão o valor do quociente é sempre o quociente dos valores (`a / 0 = 0` em `α`). -/
@[simp] theorem v_div [DivisionRing α] [DecidableEq α] (x y : Indet α) : v (x / y) = v x / v y := by
  cases x <;> cases y <;> simp <;> split_ifs <;> simp_all

theorem v_add [AddZeroClass α] {x y : Indet α} (hx : Det x) (hy : Det y) : v (x + y) = v x + v y := by
  cases x <;> cases y <;> simp_all [Det]
theorem v_sub [SubNegZeroMonoid α] {x y : Indet α} (hx : Det x) (hy : Det y) : v (x - y) = v x - v y := by
  cases x <;> cases y <;> simp_all [Det]

theorem det_iff_exists {x : Indet α} : Det x ↔ ∃ a, x = val a := by cases x <;> simp [Det]

/-- **Extensionalidade**: dois elementos são iguais quando têm a mesma determinação e, determinados, o mesmo
valor. É o que permite provar uma identidade sem abrir os `2ⁿ` casos das variáveis. -/
theorem ext_iff' [Zero α] {x y : Indet α} : x = y ↔ (Det x ↔ Det y) ∧ (Det x → v x = v y) := by
  cases x <;> cases y <;> simp [Det]

end DetV

/-! ## Equivalência com `Option` -/

section Option

/-- `Indet α` e `Option α` são o mesmo tipo de dados (`𝕀 ↦ none`). -/
def toOption : Indet α → Option α
  | val a => some a
  | I => none

def ofOption : Option α → Indet α
  | some a => val a
  | none => I

def equivOption : Indet α ≃ Option α where
  toFun := toOption
  invFun := ofOption
  left_inv x := by cases x <;> rfl
  right_inv o := by cases o <;> rfl

/-- A soma de `Indet` é a soma levantada de `Option` (`Option.map₂`). -/
theorem toOption_add [Add α] (x y : Indet α) :
    toOption (x + y) = Option.map₂ (· + ·) (toOption x) (toOption y) := by
  cases x <;> cases y <;> rfl

theorem toOption_mul [Mul α] (x y : Indet α) :
    toOption (x * y) = Option.map₂ (· * ·) (toOption x) (toOption y) := by
  cases x <;> cases y <;> rfl

end Option

end Indet

/-! ## Táticas

As duas táticas seguem o mesmo roteiro, sem abrir `2ⁿ` casos:

1. `ext_iff'` separa a identidade em determinação e valor;
2. determinação: as condições dos dois lados viram conjunções de átomos (`Det x`, `v y ≠ 0`); cada lado é
   montado a partir das hipóteses do outro, em tempo linear (com `tauto` de reserva);
3. valor: com todos os átomos determinados, cada variável é substituída por `val a` e a identidade cai em `α`,
   onde `ring` (ou `field_simp` + `ring`) fecha. -/

/-- conjunto de reescritas da determinação -/
macro "indet_det_simp" : tactic =>
  `(tactic| simp only [Indet.det_add, Indet.det_mul, Indet.det_neg, Indet.det_sub, Indet.det_div, Indet.det_val,
    Indet.det_zero, Indet.det_one, Indet.v_mul, Indet.v_div, Indet.v_neg, Indet.v_val, Indet.v_zero, Indet.v_one,
    mul_ne_zero_iff, div_ne_zero_iff, ne_eq, true_and, and_true])

/-- fecha `A ↔ B` entre conjunções de átomos em tempo linear (abre as hipóteses, monta as conjunções por
`assumption`); se a forma não for essa, recorre a `tauto` -/
macro "indet_iff_conj" : tactic =>
  `(tactic| first
    | (constructor <;> (intro hc; casesm* _ ∧ _; constructorm* _ ∧ _ <;> assumption))
    | tauto)

/-- passa ao valor: com todas as variáveis determinadas, troca cada uma por `val a` -/
macro "indet_para_valor" : tactic =>
  `(tactic| (
    try simp only [Indet.det_add, Indet.det_mul, Indet.det_neg, Indet.det_sub, Indet.det_div, Indet.det_val,
      Indet.det_zero, Indet.det_one, Indet.v_mul, Indet.v_div, Indet.v_neg, Indet.v_val, mul_ne_zero_iff,
      div_ne_zero_iff, ne_eq, true_and, and_true] at *
    casesm* _ ∧ _
    try simp only [Indet.det_iff_exists] at *
    casesm* ∃ _, _
    subst_vars
    try simp only [Indet.v_val] at *
    try simp only [Indet.val_add_val, Indet.val_mul_val, Indet.neg_val, Indet.val_sub_val, Indet.val_div_val,
      Indet.zero_def, Indet.one_def, Indet.v_val, Indet.v_mul, Indet.v_neg, Indet.v_div, mul_eq_zero, div_eq_zero_iff,
      or_self, or_false, false_or, if_false, ↓reduceIte, *]))

/-- Identidade de anel comutativo em `Indet α` (`+`, `·`, `-`, `0`, `1`). -/
macro "indet_ring" : tactic =>
  `(tactic| (
    rw [Indet.ext_iff']
    refine ⟨?_, fun h => ?_⟩
    · (try indet_det_simp) <;> indet_iff_conj
    · indet_para_valor
      ring))

/-- Identidade de corpo em `Indet α` (com `/`): a divisão por zero é `𝕀`, então as condições `v y ≠ 0` entram na
determinação; o valor é resolvido por `ring` e, se não bastar, por `field_simp` e `ring`. -/
macro "indet_field" : tactic =>
  `(tactic| (
    rw [Indet.ext_iff']
    refine ⟨?_, fun h => ?_⟩
    · (try indet_det_simp) <;> indet_iff_conj
    · indet_para_valor
      first
        | ring1
        | (field_simp; try ring)))

/-! ## Lemas de corpo sem hipóteses

O ganho da formulação: nos casos degenerados os dois lados viram `𝕀`, então a identidade vale sem `b ≠ 0`.
No uso em cadeia (reescrever várias vezes) não há condições laterais para carregar. -/

namespace Indet

variable {K : Type*} [Field K] [DecidableEq K]

/-- `a/b + c/d = (a·d + b·c)/(b·d)`, sem hipóteses (no Mathlib: `div_add_div` com `b ≠ 0` e `d ≠ 0`). -/
theorem div_add_div' (a b c d : Indet K) : a / b + c / d = (a * d + b * c) / (b * d) := by indet_field

/-- `a/b − c/d = (a·d − b·c)/(b·d)`, sem hipóteses. -/
theorem div_sub_div' (a b c d : Indet K) : a / b - c / d = (a * d - b * c) / (b * d) := by indet_field

/-- `(a/b)·(c/d) = (a·c)/(b·d)`, sem hipóteses (como no Mathlib). -/
theorem div_mul_div' (a b c d : Indet K) : (a / b) * (c / d) = (a * c) / (b * d) := by indet_field

/-- `(a/b)/(c/d) = (a·d)/(b·c)` precisa de `v d ≠ 0` (no Mathlib vale sem hipótese). -/
theorem div_div_div' (a b c d : Indet K) (hd : v d ≠ 0) : (a / b) / (c / d) = (a * d) / (b * c) := by
  indet_field

/-- `(a/b)·b = a` precisa de `b` determinado e não nulo (como no Mathlib). -/
theorem div_mul_cancel' (a b : Indet K) (hb : Det b) (hb0 : v b ≠ 0) : a / b * b = a := by indet_field

end Indet
