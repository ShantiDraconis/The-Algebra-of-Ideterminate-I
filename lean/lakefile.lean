name = "IAlgebra"
version = "0.1.0"
keywords = ["mathematics", "algebra", "indeterminate", "formal-verification"]
description = "Formal verification of the Algebra of Indeterminate I"

[[lean_lib]]
name = "IAlgebra"

[dependencies]
mathlib = { git = "https://github.com/leanprover-community/mathlib4.git", rev = "master" }

[package]
moreLeanArgs = ["--threads=4"]
moreGlobalServerArgs = ["--threads=4"]
import Lake
open Lake DSL

package algebra_i {
  -- Add package configuration options here
}

lean_lib AlgebraI {
  -- Add library configuration options here
}

@[default_target]
lean_exe algebra_i {
  root := `Main
}

-- Mathlib dependency (commented out for now - uncomment when needed)
-- require mathlib from git
--   "https://github.com/leanprover-community/mathlib4.git"
