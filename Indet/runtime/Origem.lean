import Batteries.Data.Rat.Basic

/-!
# Benchmark de diagnóstico: o erro some, aparece, ou aparece com endereço?

Tarefa: `m` decisões, cada uma do tipo "aprova se `Σ aₖ/bₖ ≥ 0`", com `n` quocientes (`aₖ ∈ [-10, 10]`,
`bₖ ∈ [1, 10]`). Numa fração das decisões injeta-se um erro de especificação: um ou dois denominadores viram 0
(o "peso vazio"). Para cada formulação mede-se o tempo e conta-se:

* **decididas em silêncio**: decisões com erro injetado que saíram como "aprova" ou "rejeita", sem aviso;
* **aprovadas em silêncio**: entre essas, as que saíram "aprova";
* **detectadas**: decisões com erro injetado que saíram marcadas como indeterminadas;
* **localizadas**: detectadas com a posição exata do **primeiro** denominador nulo;
* **alarmes falsos**: decisões sem erro marcadas como indeterminadas.

Formulações:

* **A** — divisão total do Mathlib (`x / 0 = 0`): sempre decide.
* **B** — `Option ℚ`: detecta, não diz onde.
* **F** — `Float` (IEEE 754): `a/0 = ±∞`, `0/0 = NaN`; detecta por `¬ isFinite`, não diz onde.
* **C** — `𝕀` puro (`val q | 𝕀`): detecta, não diz onde.
* **O** — `𝕀` com origem (`val q | 𝕀 k`, `k` = índice do primeiro denominador nulo): detecta e diz onde.

A origem é um recurso de execução. Na álgebra da biblioteca `Indet` o `𝕀` não carrega origem: com origem "a
primeira que apareceu", a soma deixaria de ser comutativa (`𝕀₁ + 𝕀₂ = 𝕀₁ ≠ 𝕀₂ = 𝕀₂ + 𝕀₁`).
-/

namespace Origem

inductive QI where
  | val (q : Rat)
  | I

inductive QO where
  | val (q : Rat)
  | I (termo : Nat)

/-- Resultado de uma decisão, comum às cinco formulações. -/
inductive Saida where
  | aprova | rejeita | indet | indetEm (termo : Nat)
  deriving BEq

structure Caso where
  ex : Array (Int × Nat)
  fl : FloatArray
  /-- índice do primeiro denominador nulo injetado, se houver -/
  erro : Option Nat

@[noinline] def somaA (xs : Array (Int × Nat)) : Rat :=
  xs.foldl (fun s (a, b) => s + (a : Rat) / (b : Rat)) 0

@[noinline] def somaB (xs : Array (Int × Nat)) : Option Rat := Id.run do
  let mut s : Rat := 0
  for (a, b) in xs do
    if b == 0 then return none
    s := s + (a : Rat) / (b : Rat)
  return some s

@[noinline] def somaC (xs : Array (Int × Nat)) : QI := Id.run do
  let mut s : Rat := 0
  for (a, b) in xs do
    if b == 0 then return .I
    s := s + (a : Rat) / (b : Rat)
  return .val s

@[noinline] def somaO (xs : Array (Int × Nat)) : QO := Id.run do
  let mut s : Rat := 0
  for i in [0:xs.size] do
    let (a, b) := xs[i]!
    if b == 0 then return .I i
    s := s + (a : Rat) / (b : Rat)
  return .val s

@[noinline] def somaF (fl : FloatArray) : Float := Id.run do
  let mut s : Float := 0
  for i in [0:fl.size / 2] do
    s := s + fl[2 * i]! / fl[2 * i + 1]!
  return s

def decideRat (q : Rat) : Saida := if q.num < 0 then .rejeita else .aprova

def decidir (nome : String) (c : Caso) : Saida :=
  match nome with
  | "A_mathlib_total" => decideRat (somaA c.ex)
  | "B_option" => match somaB c.ex with
    | some q => decideRat q
    | none => .indet
  | "F_float_NaN" =>
    let s := somaF c.fl
    if !s.isFinite then .indet else if s < 0 then .rejeita else .aprova
  | "C_I_puro" => match somaC c.ex with
    | .val q => decideRat q
    | .I => .indet
  | _ => match somaO c.ex with
    | .val q => decideRat q
    | .I k => .indetEm k

structure Gen where
  s : UInt64

def Gen.prox (g : Gen) (m : Nat) : Nat × Gen :=
  let s := g.s * 6364136223846793005 + 1442695040888963407
  ((s >>> 33).toNat % m, ⟨s⟩)

/-- `m` casos de `n` termos; em `errosPorMil` casos por mil, um ou dois denominadores viram 0. -/
def gera (m n errosPorMil : Nat) (semente : UInt64) : Array Caso := Id.run do
  let mut g : Gen := ⟨semente⟩
  let mut out := Array.mkEmpty m
  for _ in [0:m] do
    let mut xs : Array (Int × Nat) := Array.mkEmpty n
    for _ in [0:n] do
      let (a, g1) := g.prox 21; let (b, g2) := g1.prox 10; g := g2
      xs := xs.push ((a : Int) - 10, b + 1)
    let (sel, g1) := g.prox 1000; g := g1
    let mut erro : Option Nat := none
    if sel < errosPorMil then
      let (i, g2) := g.prox n; let (j, g3) := g2.prox n; let (dois, g4) := g3.prox 2; g := g4
      xs := xs.set! i (xs[i]!.1, 0)
      if dois == 1 then xs := xs.set! j (xs[j]!.1, 0)
      erro := some (if dois == 1 then min i j else i)
    let fl := xs.foldl (fun acc (a, b) => (acc.push (Float.ofInt a)).push (Float.ofNat b)) (FloatArray.mkEmpty (2 * n))
    out := out.push ⟨xs, fl, erro⟩
  return out

def mediana (v : Array Nat) : Nat := let w := v.qsort (· < ·); w[w.size / 2]!

end Origem

open Origem in
def main (args : List String) : IO Unit := do
  let m := (args.getD 0 "1000").toNat!
  let n := (args.getD 1 "1000").toNat!
  let reps := (args.getD 2 "5").toNat!
  IO.println ("erros_por_mil,casos_com_erro,variante,mediana_ms,min_ms,max_ms," ++
    "decididas_em_silencio,aprovadas_em_silencio,detectadas,localizadas,alarmes_falsos")
  for e in [0, 10, 100, 1000] do
    let r ← IO.mkRef (gera m n e 42)
    let comErro := (← r.get).foldl (fun k c => if c.erro.isSome then k + 1 else k) 0
    for nome in ["A_mathlib_total", "B_option", "F_float_NaN", "C_I_puro", "O_I_com_origem"] do
      let mut ts : Array Nat := #[]
      let mut res : Array Saida := #[]
      for _ in [0:reps] do
        let t0 ← IO.monoNanosNow
        let cs ← r.get
        let mut out : Array Saida := Array.mkEmpty cs.size
        for c in cs do out := out.push (decidir nome c)
        let t1 ← IO.monoNanosNow
        ts := ts.push (t1 - t0)
        res := out
      let cs ← r.get
      let mut silencio := 0; let mut aprovadas := 0; let mut detect := 0; let mut loc := 0; let mut falsos := 0
      for (c, s) in cs.zip res do
        match c.erro, s with
        | some _, .aprova => silencio := silencio + 1; aprovadas := aprovadas + 1
        | some _, .rejeita => silencio := silencio + 1
        | some _, .indet => detect := detect + 1
        | some k, .indetEm k' => detect := detect + 1; if k == k' then loc := loc + 1
        | none, .indet => falsos := falsos + 1
        | none, .indetEm _ => falsos := falsos + 1
        | none, _ => pure ()
      let w := ts.qsort (· < ·)
      let ms (x : Nat) := Float.ofNat x / 1.0e6
      IO.println s!"{e},{comErro},{nome},{ms (mediana ts)},{ms w[0]!},{ms w[w.size - 1]!},{silencio},{aprovadas},{detect},{loc},{falsos}"
