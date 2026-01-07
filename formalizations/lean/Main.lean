import ITheory
import IPhysics

-- Main entry point for I-Theory Lean project

def main : IO Unit := do
  IO.println "I-Theory Lean 4 Formalization"
  IO.println "=============================="
  IO.println ""
  IO.println "This project contains formal definitions and proofs for:"
  IO.println "  - Basic I-algebra structures"
  IO.println "  - Physical constants and Planck units"
  IO.println "  - Fundamental equations from sections 22-28"
  IO.println "  - Quantum gravity and cosmology"
  IO.println ""
  IO.println "To explore the formalization, examine:"
  IO.println "  - ITheory.lean: Foundation definitions"
  IO.println "  - IPhysics.lean: Physical applications"
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
import AlgebraIndeterminate.CentralHypothesis

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
def main : IO Unit := do
  IO.println "The Algebra of the Indeterminate I - Lean 4 Formalization"
  IO.println "Central Hypothesis (AEI) formalized and verified"
import AlgebraIndeterminate.FlexibleResolution

def main : IO Unit :=
  IO.println "The Algebra of the Indeterminate I - Lean 4 Formalization with Flexible Resolution"
