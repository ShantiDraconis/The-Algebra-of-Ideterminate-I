import Batteries.Data.Rat.Basic

/-!
# Benchmark de execução: exato (ℚ), ponto flutuante e híbrido

Tarefa: para `m` cadeias de `n` quocientes `aₖ/bₖ` (`aₖ ∈ [-10, 10]`, `bₖ ∈ [0, 10]`), decidir **exatamente** o sinal
da soma de cada cadeia, ou `𝕀` se algum denominador for nulo. Uma fração das cadeias é construída para somar
exatamente 0 (trios `a/10 + c/10 − (a+c)/10`), o caso em que o ponto flutuante erra o sinal.

* **Q** — exato em `ℚ` com o indeterminado absorvente (para no primeiro denominador nulo).
* **F** — só ponto flutuante (rápido, sem garantia: o sinal pode sair errado perto de 0).
* **H** — híbrido: soma em `Float` com a cota de erro de arredondamento `γ·Σ|tₖ|`; se `|s|` passa da cota, o sinal
  está certo e não se faz conta exata; se não, refaz a cadeia em `ℚ`. O resultado é sempre igual ao de **Q**.

`ℚ` aqui é o `Rat` do Batteries, o mesmo tipo do `ℚ` do Mathlib.
-/

namespace Hibrido

inductive Sinal where
  | neg | zero | pos | I
  deriving BEq, Repr

def Sinal.mostra : Sinal → String
  | .neg => "-" | .zero => "0" | .pos => "+" | .I => "I"

def sinalRat (q : Rat) : Sinal := if q.num < 0 then .neg else if q.num == 0 then .zero else .pos

/-- Q: exato, com o indeterminado absorvente (para no primeiro denominador nulo). -/
@[noinline] def exato (xs : Array (Int × Nat)) : Sinal := Id.run do
  let mut s : Rat := 0
  for (a, b) in xs do
    if b == 0 then return .I
    s := s + (a : Rat) / (b : Rat)
  return sinalRat s

/-- Uma cadeia nas duas representações: exata (para a conta em `ℚ`) e em ponto flutuante, sem caixas
(`FloatArray` com `a₀, b₀, a₁, b₁, …`), para a passada rápida. -/
structure Cadeia where
  ex : Array (Int × Nat)
  fl : FloatArray

/-- F: só ponto flutuante. -/
@[noinline] def flutuante (c : Cadeia) : Sinal := Id.run do
  let mut s : Float := 0
  let n := c.fl.size / 2
  for i in [0:n] do
    let b := c.fl[2 * i + 1]!
    if b == 0 then return .I
    s := s + c.fl[2 * i]! / b
  return if s < 0 then .neg else if s == 0 then .zero else .pos

/-- H: ponto flutuante com cota de erro; conta exata só quando o sinal não está garantido. -/
@[noinline] def hibrido (c : Cadeia) : Sinal × Bool := Id.run do
  let mut s : Float := 0
  let mut abs : Float := 0
  let n := c.fl.size / 2
  for i in [0:n] do
    let b := c.fl[2 * i + 1]!
    if b == 0 then return (.I, false)
    let t := c.fl[2 * i]! / b
    s := s + t
    abs := abs + t.abs
  -- |fl(Σ) − Σ| ≤ γ_{n+1} Σ|tₖ| (soma recursiva, mais o arredondamento de cada divisão), com folga de 2×
  let u : Float := 1.1102230246251565e-16
  let k := Float.ofNat (n + 1)
  let cota := 2.0 * (k * u / (1.0 - k * u)) * abs
  if s.abs > cota then
    return (if s < 0 then .neg else .pos, false)
  else
    return (exato c.ex, true)

/-- Gerador congruencial (determinístico). -/
structure Gen where
  s : UInt64

def Gen.prox (g : Gen) (m : Nat) : Nat × Gen :=
  let s := g.s * 6364136223846793005 + 1442695040888963407
  ((s >>> 33).toNat % m, ⟨s⟩)

/-- `m` cadeias de `n` termos; `zerosPorMil` denominadores nulos por mil; `fracNula` cadeias por mil que somam 0. -/
def gera (m n zerosPorMil fracNula : Nat) (semente : UInt64) : Array Cadeia := Id.run do
  let mut g : Gen := ⟨semente⟩
  let mut out := Array.mkEmpty m
  for _ in [0:m] do
    let (sel, g1) := g.prox 1000; g := g1
    let mut xs := Array.mkEmpty n
    if sel < fracNula then
      -- trios a/10 + c/10 − (a+c)/10: a soma exata é 0, mas em ponto flutuante sobra arredondamento
      -- (por exemplo 1/10 + 2/10 − 3/10 ≈ 5,6·10⁻¹⁷), e o sinal pelo `Float` sai errado
      for _ in [0:n / 3] do
        let (a, g2) := g.prox 21; let (c, g3) := g2.prox 21; g := g3
        let a : Int := (a : Int) - 10
        let c : Int := (c : Int) - 10
        xs := xs.push (a, 10)
        xs := xs.push (c, 10)
        xs := xs.push (-(a + c), 10)
    else
      for _ in [0:n] do
        let (a, g2) := g.prox 21; let (z, g3) := g2.prox 1000; let (b, g4) := g3.prox 10; g := g4
        xs := xs.push ((a : Int) - 10, if z < zerosPorMil then 0 else b + 1)
    let fl := xs.foldl (fun acc (a, b) => (acc.push (Float.ofInt a)).push (Float.ofNat b)) (FloatArray.mkEmpty (2 * n))
    out := out.push ⟨xs, fl⟩
  return out

def mediana (v : Array Nat) : Nat := let w := v.qsort (· < ·); w[w.size / 2]!

end Hibrido

open Hibrido in
def main (args : List String) : IO Unit := do
  let m := (args.getD 0 "1000").toNat!
  let n := (args.getD 1 "1000").toNat!
  let reps := (args.getD 2 "5").toNat!
  IO.println "zeros_por_mil,cadeias_nulas_por_mil,variante,mediana_ms,ns_por_op,refeitas_em_Q,erros_de_sinal"
  for (z, f) in [(0, 0), (0, 10), (1, 10), (100, 10)] do
    let r ← IO.mkRef (gera m n z f 42)
    -- referência exata
    let ref := (← r.get).map (fun c => exato c.ex)
    let mut linhas : Array String := #[]
    for nome in ["Q_exato", "F_flutuante", "H_hibrido"] do
      let mut ts : Array Nat := #[]
      let mut refeitas := 0
      let mut erros := 0
      for _ in [0:reps] do
        let t0 ← IO.monoNanosNow
        let cs ← r.get
        let mut res : Array Sinal := Array.mkEmpty cs.size
        let mut rf := 0
        for c in cs do
          match nome with
          | "Q_exato" => res := res.push (exato c.ex)
          | "F_flutuante" => res := res.push (flutuante c)
          | _ =>
            let (s, refez) := hibrido c
            res := res.push s
            if refez then rf := rf + 1
        let t1 ← IO.monoNanosNow
        ts := ts.push (t1 - t0)
        refeitas := rf
        erros := (res.zip ref).foldl (fun acc (x, y) => if x == y then acc else acc + 1) 0
      let t := mediana ts
      linhas := linhas.push s!"{z},{f},{nome},{Float.ofNat t / 1.0e6},{Float.ofNat t / Float.ofNat (m * n)},{refeitas},{erros}"
    for l in linhas do IO.println l
