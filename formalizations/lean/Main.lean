/-
  Main entry point for the Algebra of the Indeterminate I formalization
  
  This includes both the original cardinal-based formalization and the new
  AEI (Algebraic Extension of Indeterminacy) system.
-/

-- Original formalization
import AlgebraIndeterminate.ZFC
import AlgebraIndeterminate.Cardinals
import AlgebraIndeterminate.Ultrapowers
import AlgebraIndeterminate.Algebra
import AlgebraIndeterminate.Consistency

-- New AEI formalization
import AlgebraIndeterminate.AEI
import AlgebraIndeterminate.ExtendedOperators
import AlgebraIndeterminate.Transitions

def main : IO Unit := do
  IO.println "The Algebra of the Indeterminate I - Lean 4 Formalization"
  IO.println "=========================================================="
  IO.println ""
  IO.println "Modules loaded:"
  IO.println "  - ZFC Set Theory"
  IO.println "  - Cardinal Arithmetic"
  IO.println "  - Ultrapowers"
  IO.println "  - Algebraic Structures"
  IO.println "  - Consistency Proofs"
  IO.println ""
  IO.println "AEI System:"
  IO.println "  - Core AEI Framework (I = 1/0)"
  IO.println "  - Extended Operators & Numeric Classes"
  IO.println "  - Classical ↔ AEI Transitions"
  IO.println ""
  IO.println "For more information, see the documentation in docs/"
