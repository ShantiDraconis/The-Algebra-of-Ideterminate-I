import IndetDecisao

/-!
# Teste de lote cego: o decisor

Lê só o arquivo de casos (uma decisão por linha: `a₀ b₀ a₁ b₁ …`) e escreve uma saída por linha. Não recebe a
verdade nem a semente. Uso:

```
lake env lean --run LoteCego.lean <O|A|F> casos.txt saidas.txt
```

* `O` — `IndetDecisao.decidir`, o mesmo programa dos teoremas (`aprova`, `reprova` ou `erro k`);
* `A` — `IndetDecisao.decidirTotal`, a divisão total do Mathlib (controle negativo: decide em silêncio);
* `F` — ponto flutuante (controle negativo: detecta por NaN/∞, mas não diz onde, e erra o sinal perto de 0);
* `N` — `IndetDecisao.decidirNulo`, o modelo da decisão em SQL (`x / 0` é `NULL`, `SUM` ignora `NULL`). O CI
  confere que a saída é idêntica à de `A`, como diz `decidirNulo_eq_total`.
-/

open IndetDecisao

def pares : List Int → List (Int × Int)
  | a :: b :: r => (a, b) :: pares r
  | _ => []

def mostra : Saida → String
  | .aprova => "aprova"
  | .reprova => "reprova"
  | .erro k => s!"erro {k}"

def decidirFloat (l : List (Int × Int)) : String :=
  let s := l.foldl (fun s (p : Int × Int) => s + Float.ofInt p.1 / Float.ofInt p.2) 0
  if !s.isFinite then "erro ?" else if s < 0 then "reprova" else "aprova"

def main (args : List String) : IO Unit := do
  let [variante, entrada, saida] := args
    | throw (IO.userError "uso: LoteCego.lean <O|A|F> casos.txt saidas.txt")
  let linhas ← IO.FS.lines entrada
  let h ← IO.FS.Handle.mk saida .write
  for linha in linhas do
    let l := pares (((linha.splitOn " ").filter (· ≠ "")).map String.toInt!)
    let q : List (ℚ × ℚ) := l.map fun (a, b) => ((a : ℚ), (b : ℚ))
    let r := match variante with
      | "O" => mostra (decidir q)
      | "A" => mostra (decidirTotal q)
      | "N" => mostra (decidirNulo q)
      | _ => decidirFloat l
    h.putStrLn r
