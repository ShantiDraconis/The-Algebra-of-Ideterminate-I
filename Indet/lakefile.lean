import Lake
open Lake DSL

package indet where
  leanOptions := #[⟨`autoImplicit, false⟩]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.19.0"

/-- A biblioteca: o tipo `Indet α`, as reescritas e as táticas `indet_ring` / `indet_field`. -/
@[default_target] lean_lib Indet

/-- Testes (`lake build IndetTest`). -/
lean_lib IndetTest

/-- Benchmark de verificação (`lake env lean -DElab.async=false IndetBench.lean`). -/
lean_lib IndetBench
