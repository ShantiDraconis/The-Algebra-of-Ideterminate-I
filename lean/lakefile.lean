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
