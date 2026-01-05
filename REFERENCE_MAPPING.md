# Reference Mapping to Repository Sections

This document maps the references in REFERENCES.md to the specific parts of the repository where they are relevant or cited.

## Map by Repository Section

### Set Theory Formalizations (ZF/AC + I)

**Primary References:**
- [1] Jech (2003) - Set Theory
- [2] Kunen (1980) - Independence Proofs
- [3] Bell & Machover (1977) - Mathematical Logic

**Files:**
- `formalizations/lean/AlgebraIndeterminate/ZFC.lean`
- `formalizations/coq/ZFC.v`
- `formalizations/isabelle/ZFC.thy`
- `formalizations/agda/ZFC.agda`
- `docs/theory/01_zf_ac_indeterminate/`

### Ultrapowers and Nonstandard Analysis

**Primary References:**
- [4] Goldblatt (1998) - Lectures on the Hyperreals
- [5] Bell & Slomson (2006) - Models and Ultraproducts
- [6] Robinson (1996) - Non-standard Analysis

**Files:**
- `formalizations/lean/AlgebraIndeterminate/Ultrapowers.lean`
- `formalizations/coq/Ultrapowers.v`
- `formalizations/python/ultrapowers.py`
- `docs/theory/02_ultrapowers/`

### Wheel Theory (Division by Zero)

**Primary References:**
- [7] Carlström (2004) - Wheels – On Division by Zero

**Files:**
- `docs/theory/03_wheel_theory/`
- `formalizations/lean/AlgebraIndeterminate/WheelAlgebra.lean`
- Implementation notes in axiom files

### Cardinal Arithmetic with I

**Primary References:**
- [1] Jech (2003) - Cardinal arithmetic chapters
- [49] Bourbaki (1994) - Historical context

**Files:**
- `formalizations/lean/AlgebraIndeterminate/Cardinals.lean`
- `formalizations/coq/Cardinals.v`
- `formalizations/python/cardinal_arithmetic.py`
- `data/axioms/axioms.yaml` (Axiom I1: κ ⊖ κ = I)

### Special Functions and Analysis

**Primary References:**
- [9] Artin (1964) - The Gamma Function
- [11] NIST Handbook (2010) - Mathematical Functions
- [12] Whittaker & Watson (1927) - Modern Analysis
- [13] Andrews, Askey & Roy (1999) - Special Functions

**Files:**
- References for extending factorial and gamma to indeterminate values
- `docs/theory/04_axioms/` - Discussion of gamma extensions

### Calculus and I-Calculus

**Primary References:**
- [14] Rudin (1976) - Principles of Mathematical Analysis
- [15] Spivak (2006) - Calculus
- [50] de l'Hôpital (1696) - Historical: Indeterminate forms

**Files:**
- `docs/theory/06_i_calculus/`
- Notes on limits, derivatives, and integrals with I
- Historical context of 0/0 indeterminate forms

### Physical Interpretations

**Quantum Gravity:**
- [21] Penrose (2004) - The Road to Reality
- [35] Rovelli (2004) - Quantum Gravity
- [36] Rovelli (2014) - Loop Quantum Gravity
- [32] Tawfik & Diab (2014) - Generalized Uncertainty Principle
- [31] Das & Vagenas (2008) - Quantum Gravity Corrections

**General Relativity:**
- [19] Einstein (1916) - Die Grundlage der allgemeinen Relativitätstheorie
- [20] Einstein (1922) - The Meaning of Relativity
- [22] Penrose (1979) - Singularities and Time-Asymmetry
- [23] Hawking (1975) - Particle Creation by Black Holes

**Cosmology:**
- [25] Riess et al. (1998) - Supernova evidence for acceleration
- [26] Perlmutter et al. (1999) - Measurements of Ω and Λ
- [27] Planck Collaboration (2020) - Cosmological parameters
- [28] Scolnic et al. (2018) - Pantheon supernova sample
- [29] Spergel et al. (2003) - WMAP observations

**Files:**
- `docs/PHYSICAL_INTERPRETATIONS.md`
- `docs/theory/07_physics/`

### Fundamental Constants

**Primary References:**
- [33] Uzan (2003) - Variation of fundamental constants
- [34] Flambaum & Tedesco (2006) - Temporal variation tests
- [46] Barrow (2002) - The Constants of Nature

**Files:**
- `docs/PHYSICAL_INTERPRETATIONS.md` - Section on Planck scale

### Quantum Field Theory

**Primary References:**
- [37] Lancaster & Blundell (2014) - QFT for the Gifted Amateur
- [38] Colombeau (1984) - Generalized Functions
- [39] Cartier & DeWitt-Morette (2006) - Functional Integration
- [40] Feynman (2006) - QED

**Files:**
- `docs/theory/07_physics/` - Discussion of I-field theory

### Formal Verification Infrastructure

**Lean 4:**
- [52] de Moura & Ullrich (2021) - The Lean 4 Theorem Prover
- [53] mathlib Community (2020) - The Lean Mathematical Library

**Coq:**
- [54] Bertot & Castéran (2004) - Interactive Theorem Proving

**Isabelle/HOL:**
- [55] Nipkow, Paulson & Wenzel (2002) - Isabelle/HOL

**Agda:**
- [56] Norell (2009) - Dependently Typed Programming in Agda

**Files:**
- `formalizations/lean/README.md` - Cite Lean 4 paper
- `formalizations/coq/README.md` - Cite Coq'Art
- `formalizations/isabelle/README.md` - Cite Isabelle book
- `formalizations/agda/README.md` - Cite Agda paper
- `formalizations/DETAILED_GUIDE.md` - Mentions all four systems

### Computational Methods

**Primary References:**
- [57] Dean & Ghemawat (2008) - MapReduce
- [58] Burgin (2010) - Non-Diophantine Arithmetics

**Files:**
- `formalizations/python/` - Computational implementation
- Discussion of alternative arithmetic systems

### Philosophy and Foundations

**Primary References:**
- [44] Deutsch (1997) - The Fabric of Reality
- [45] Tegmark (2008) - The Mathematical Universe
- [47] Zeh (2007) - The Physical Basis of the Direction of Time
- [48] Varela, Thompson & Rosch (2017) - The Embodied Mind

**Files:**
- `docs/theory/` - Philosophical discussions
- Context for mathematical universe hypothesis

### History of Mathematics

**Primary References:**
- [49] Bourbaki (1994) - Elements of the History of Mathematics
- [50] de l'Hôpital (1696) - Analyse des Infiniment Petits
- [51] Kline (1990) - Mathematical Thought

**Files:**
- Historical context throughout documentation
- `docs/theory/04_axioms/` - Historical development

## Map by Research Question

### Q: How do we formalize I in set theory?
**Answer:** Using ZFC + Axiom I1 (κ ⊖ κ = I)
**References:** [1] Jech, [2] Kunen, [3] Bell & Machover

### Q: What is the model-theoretic foundation?
**Answer:** Ultrapowers and ultraproduct constructions
**References:** [4] Goldblatt, [5] Bell & Slomson, [6] Robinson

### Q: How do we handle division by zero algebraically?
**Answer:** Wheel structures
**References:** [7] Carlström (2004)

### Q: What are the physical applications?
**Answer:** Quantum gravity at Planck scale, singularity resolution
**References:** [21] Penrose, [23] Hawking, [35-36] Rovelli, [31-32] QG corrections

### Q: How do we verify the formalization?
**Answer:** Multiple proof assistants (Lean, Coq, Isabelle, Agda)
**References:** [52-56] Proof assistant papers

### Q: What is the historical precedent for indeterminate forms?
**Answer:** Dating back to early calculus (de l'Hôpital)
**References:** [50] de l'Hôpital (1696), [49] Bourbaki

## Usage Guidelines

### For Paper Writing

When writing about specific aspects, cite appropriate references:

```latex
% For ZFC formalization
The extended set theory is based on standard ZFC axioms \cite{jech2003,kunen1980}.

% For ultrapowers
We use ultrapower constructions \cite{goldblatt1998,bell2006} to model indeterminacy.

% For wheel theory
Division by zero is handled via wheel structures \cite{carlstrom2004}.

% For formal verification
Our work is formalized in Lean 4 \cite{moura2021} using Mathlib \cite{mathlib2020}.

% For physical applications
The I-field theory connects to quantum gravity \cite{penrose2004,rovelli2004} 
and Planck-scale physics \cite{tawfik2014}.
```

### For Code Comments

```lean
-- Based on Jech (2003), Chapter on Cardinal Arithmetic
axiom I1 : ∀ κ : Cardinal, κ ⊖ κ = I

-- Ultrapower construction following Goldblatt (1998)
def ultrapower (U : Ultrafilter α) : ...

-- Wheel axioms from Carlström (2004)
axiom wheel_div_zero : ∀ n : ℕ, n / 0 = I
```

### For Documentation

Include references in markdown:

```markdown
## Theoretical Foundation

The algebra of indeterminate I is built on:

1. **Set Theory**: Standard ZFC axioms [Jech 2003, Kunen 1980]
2. **Ultrapowers**: Model-theoretic constructions [Goldblatt 1998]
3. **Wheel Theory**: Division by zero structures [Carlström 2004]

See [REFERENCES.md](../REFERENCES.md) for complete bibliography.
```

## Verification Status

All references have been:
- ✅ Verified for existence and correct attribution
- ✅ Checked for proper DOI/ISBN where available
- ✅ Cross-referenced with repository usage
- ✅ Organized by research area
- ✅ Cleaned of phantom references

## Updates

To add a new reference:

1. Verify it exists (check DOI, ISBN, or archive)
2. Add to `REFERENCES.md` in the appropriate category
3. Add to `references.bib` with proper BibTeX format
4. Update this mapping document with usage locations
5. Commit with message describing the addition

## Notes on Removed References

The following commonly cited but problematic references were explicitly removed:

- **Smith, J.D. Non-Diophantine Arithmetics (2020)** - Non-existent; replaced with actual Burgin (2010)
- **Misattributed Penrose titles** - Corrected to proper book titles and chapters
- **Incorrect Einstein publisher** - Corrected to original Annalen der Physik (1916) and Princeton (1922)
- **Phantom gamma function papers** - Covered by standard references (Artin, Whittaker & Watson)

These corrections ensure scientific integrity and prevent citation of non-existent sources.

---

**Last Updated**: 2026-01-05  
**Maintained by**: Repository contributors  
**See also**: [REFERENCES.md](REFERENCES.md), [references.bib](references.bib)
