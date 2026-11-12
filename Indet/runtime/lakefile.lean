import Lake
open Lake DSL

-- Benchmark de execução (exato × ponto flutuante × híbrido). O Batteries é o do Mathlib v4.19.0.
package indetRuntime where
  moreLeancArgs := #["-O3"]

require batteries from git
  "https://github.com/leanprover-community/batteries" @ "f5d04a9c4973d401c8c92500711518f7c656f034"

@[default_target] lean_exe hibrido where
  root := `Main

-- Diagnóstico: o erro some (divisão total), aparece (Option, NaN, 𝕀) ou aparece com a posição (𝕀 com origem).
lean_exe origem where
  root := `Origem
