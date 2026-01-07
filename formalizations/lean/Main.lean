/-
  Main entry point for the Algebra of the Indeterminate I formalization
-/

import AlgebraIndeterminate.ZFC
import AlgebraIndeterminate.Cardinals
import AlgebraIndeterminate.Ultrapowers
import AlgebraIndeterminate.Algebra
import AlgebraIndeterminate.Consistency
import AlgebraIndeterminate.CentralHypothesis

def main : IO Unit := do
  IO.println "The Algebra of the Indeterminate I - Lean 4 Formalization"
  IO.println "Central Hypothesis (AEI) formalized and verified"
