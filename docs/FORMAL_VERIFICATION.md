# Correction: formal verification status

This document previously described the repository as providing comprehensive formal verification of a “Theory of I = 0/0.” That wording is withdrawn.

The repository explores custom formal models. Any symbol (I) introduced with project-specific axioms is not thereby equal to the ordinary arithmetic expression (0/0), which is indeterminate. A theorem derived in such a model is conditional on its definitions and assumptions.

The existence of Lean, Coq, Isabelle, Agda, or Python files does not establish that each system verifies the same theorem. No claim of cross-assistant verification, consistency with standard arithmetic, or application to physics is made by this document.

To report a result as verified, document its exact statement, source revision, toolchain, dependencies, assumptions, and reproducible successful build. The earlier description is preserved in Git history for audit.
