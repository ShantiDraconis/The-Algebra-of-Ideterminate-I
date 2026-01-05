import Lake
open Lake DSL

package «algebra-indeterminate» where
  -- add package configuration options here

lean_lib «AlgebraIndeterminate» where
  -- add library configuration options here

@[default_target]
lean_exe «algebra-indeterminate» where
  root := `Main
