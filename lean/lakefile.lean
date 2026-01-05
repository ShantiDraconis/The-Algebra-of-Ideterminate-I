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
