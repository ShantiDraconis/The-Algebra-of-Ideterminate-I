import Lake
open Lake DSL

package ialgebra where
  moreServerArgs := #["-Ktrace.Elab.definition=false"]

lean_lib IAlgebra where
  roots := #[`IAlgebra]
