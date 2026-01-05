import Lake
open Lake DSL

package «i-theory» where
  -- add package configuration options here

lean_lib «ITheory» where
  -- add library configuration options here

lean_lib «IPhysics» where
  -- add library configuration options here

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

@[default_target]
lean_exe «i-theory» where
  root := `Main
