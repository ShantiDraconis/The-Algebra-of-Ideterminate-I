# Copilot Prompt Templates for I-Algebra Development

This file contains ready-to-use prompts for GitHub Copilot to generate proofs and lemmas for the Algebra of Indeterminate I.

## Table of Contents
1. [Advanced Lemma Generation](#advanced-lemma-generation)
2. [Forcing Proofs](#forcing-proofs)
3. [Physical Applications](#physical-applications)
4. [Integration Theory](#integration-theory)
5. [Category Theory](#category-theory)

---

## Advanced Lemma Generation

### Prompt 1: Absorption Properties Expansion

```
I am working in Lean 4 on the file nexus_core.lean which defines an Indeterminate 
structure for the algebra of I = 0/0. 

Generate 10 new lemmas (lemma_I_56 through lemma_I_65) that prove advanced 
absorption properties of I in the following contexts:

1. Nested operations with arbitrary depth
2. Mixed algebraic/transcendental operations
3. Composition with standard mathematical functions
4. Absorption in tensor products
5. Absorption in direct sums

Each lemma should:
- Follow the naming convention lemma_I_[number]_[property_name]
- Include a docstring with /-- ... -/
- Use @[simp] attribute where appropriate
- Have a complete proof using tactics like simp, cases, or rfl
- Build on the existing lemmas 1-55

Start with the structure:
```lean
/-- Lemma 56: [Description] -/
@[simp]
theorem lemma_I_56_[name] (parameters) :
    statement := by
  proof_tactics
```

### Prompt 2: Limit Theory Expansion

```
Based on the NexusCore module in nexus_core.lean, generate 15 lemmas about 
limit behavior of I in advanced contexts:

Topics to cover:
- Double limits and Fubini-style theorems
- Uniform continuity with I
- Equicontinuity in families of I-valued functions
- Arzela-Ascoli theorem adaptations
- Compactness in function spaces with I

Use the existing Indeterminate structure and follow the style of lemmas 11-15.
Each proof should be complete with no sorry statements.
Include references to relevant mathematical theorems in comments.
```

### Prompt 3: Measure Theory and Integration

```
You are formalizing measure-theoretic properties of I in Lean 4. 

Create 20 lemmas about:
1. Measurability of I-valued functions
2. Integration of I-valued functions (Lebesgue)
3. Dominated convergence with I
4. Fatou's lemma adaptations
5. Monotone convergence with I
6. Fubini's theorem for I-valued integrands
7. Change of variables with I
8. Radon-Nikodym theorem considerations

Base your work on the Indeterminate structure in nexus_core.lean.
Use Mathlib.MeasureTheory.* imports.
Each lemma should have a complete proof or a well-documented sorry explaining 
what needs to be established.
```

---

## Forcing Proofs

### Prompt 4: Complete Generic Filter Construction

```
In the file theory_independence.lean, I have outlined forcing-based independence 
proofs for I = 0/0 from ZF axioms. 

Complete the proof of the theorem generic_meets_distinct which shows that a 
generic filter meets all dense sets. 

The context is:
- BaseModel satisfies ZF axioms
- GenericFilter is a filter of ForcingConditions
- dense_distinct is a dense set ensuring I behaves distinctly
- We need to show G.filter ∩ dense_distinct is nonempty

Use standard forcing arguments. The proof should:
1. Assume G is generic (meets all dense sets)
2. Show dense_distinct is dense in the forcing poset
3. Apply genericity to conclude G meets dense_distinct

Provide a complete proof with no sorry statements.
```

### Prompt 5: Forcing Preserves Arithmetic

```
Complete the proof of arithmetic_preservation in theory_independence.lean.

We need to show that in the forced model M[G], standard arithmetic operations 
on rationals remain unchanged. That is, for rationals a and b:
- (a + b in M[G]) = (a + b in M)
- (a * b in M[G]) = (a * b in M)  
- Adding I doesn't collapse standard arithmetic

Use the forcing framework established in the file. The proof should show that:
1. Names for rationals in the forcing extension remain standard
2. Operations on standard names yield standard results
3. I is genuinely new (not equal to any standard number)

Provide rigorous Lean 4 proof steps.
```

### Prompt 6: Independence Theorem Completion

```
In theory_independence.lean, complete the proof of independence_from_zf.

This theorem states that I = 0/0 is independent of ZF, similar to how the 
Continuum Hypothesis is independent.

The proof requires constructing two models:
- M₁[G₁] where I exists as 0/0
- M₂[G₂] where I is not required to exist

Both models satisfy ZF axioms but differ on the existence of I.

Structure the proof following Cohen's technique:
1. Start with a model M of ZF
2. For M₁, use forcing to add I as a generic object
3. For M₂, use the base model without forcing
4. Verify both satisfy ZF
5. Show they differ on the existence of I

Use standard set theory and forcing tactics from Mathlib.
```

---

## Physical Applications

### Prompt 7: I-Field Quantum Gravity

```
Create a new file lean/physical_applications.lean that formalizes I-field 
theory for quantum gravity.

Include:

1. I-field structure:
```lean
structure IField where
  field_value : ℝ → ℝ → ℝ → ℝ → Indeterminate  -- Spacetime → I
  coupling : ℝ  -- Coupling constant
  action : ℝ  -- Action integral value
```

2. Theorems about:
- I-field Lagrangian
- Equations of motion for I-field
- Coupling to standard matter
- Singularity resolution properties
- Planck scale behavior

3. Connection to observational constraints:
- Dark energy equation of state
- Dark matter rotation curves
- Cosmological constant problem

Use the Indeterminate structure from nexus_core.lean.
Include physics references in comments.
```

### Prompt 8: Dark Sector Phenomena

```
Extend physical_applications.lean with dark sector modeling using I.

Create structures and theorems for:

1. Dark matter as I-coupled field:
```lean
def dark_matter_density (I : Indeterminate) (r : ℝ) : ℝ :=
  -- Density profile with I-coupling
```

2. Dark energy from I-vacuum:
```lean  
theorem dark_energy_equation_of_state :
  ∀ I : Indeterminate, ∃ w : ℝ, w = -1 -- Cosmological constant
```

3. Observable predictions:
- Modified rotation curves
- Structure formation with I
- CMB power spectrum modifications

Include dimensional analysis and unit checks.
Reference observational papers in comments.
```

---

## Integration Theory

### Prompt 9: Fundamental Theorem of I-Calculus

```
In nexus_core.lean or a new file icalculus.lean, formalize the fundamental 
theorem of calculus for I-valued functions.

Define:
1. I-derivative: deriv_I (f : ℝ → Indeterminate) (x : ℝ) : Indeterminate
2. I-integral: integral_I (f : ℝ → Indeterminate) (a b : ℝ) : Indeterminate

Prove:
theorem fundamental_theorem_I :
  ∀ (f : ℝ → Indeterminate) (a b : ℝ),
  continuous_I f →
  integral_I (deriv_I f) a b = f b ⊖ f a

where ⊖ is the extended subtraction operation on Indeterminate.

Handle special cases where:
- f(x) = I for some x
- The derivative is I
- The integral yields I

Use Mathlib's calculus framework as a foundation.
```

### Prompt 10: Contour Integration with I

```
Formalize contour integration for I-valued complex functions.

Define:
```lean
structure ComplexIndeterminate where
  real_part : Indeterminate
  imag_part : Indeterminate

def contour_integral_I 
  (f : ℂ → ComplexIndeterminate) 
  (γ : ℝ → ℂ) 
  (a b : ℝ) : ComplexIndeterminate
```

Prove I-versions of:
1. Cauchy's theorem
2. Residue theorem
3. Maximum modulus principle (adapted)
4. Liouville's theorem (adapted)

Each theorem should handle:
- Functions that take I-values
- Contours passing through I-singularities
- Residues at I-poles

Use complex analysis from Mathlib as foundation.
```

---

## Category Theory

### Prompt 11: I as Categorical Object

```
Formalize I-Algebra as a category in Lean 4.

Define:
```lean
structure IAlgebraCategory where
  objects : Type
  morphisms : objects → objects → Type
  composition : ∀ {X Y Z}, morphisms Y Z → morphisms X Y → morphisms X Z
  identity : ∀ X, morphisms X X
  -- Category axioms
  
  indeterminate_object : objects
  indeterminate_properties : -- I-specific properties
```

Prove:
1. I forms a terminal object in a suitable category
2. Functoriality of I-operations
3. Natural transformations involving I
4. Adjunctions related to I
5. Monoidal structure on I-Algebra

Use Mathlib.CategoryTheory.* imports.
Follow category theory conventions from Mathlib.
```

### Prompt 12: Functorial Properties of I

```
Based on NexusCore.Indeterminate, prove that I satisfies functorial properties.

Define a functor F : Set → IAlgebra where:
- F sends sets to I-extended sets
- F sends functions to I-extended functions
- F preserves I-operations

Prove:
1. F preserves composition
2. F preserves identities  
3. F is faithful (injective on morphisms)
4. F creates I-limits
5. F has a left adjoint

Connect this to:
- Universal properties of I
- Free constructions with I
- Colimit constructions

Use category theory tactics from Mathlib.
Include diagrams in comments.
```

---

## Usage Instructions

### How to Use These Prompts

1. **Copy the prompt** for your desired task
2. **Paste into GitHub Copilot Chat** or include as comments in your Lean file
3. **Review the generated code** carefully
4. **Adjust and refine** based on your specific needs
5. **Test with `lake build`** to ensure compilation
6. **Iterate** until proofs are complete

### Best Practices

- Start with simpler prompts (lemma generation) before complex ones (forcing proofs)
- Test each generated lemma individually
- Build incrementally - don't try to generate 50 lemmas at once
- Review mathematical correctness, not just syntactic correctness
- Cross-reference with existing mathematical literature

### Customization

Feel free to modify these prompts to:
- Target specific mathematical properties
- Adjust difficulty level
- Focus on particular proof techniques
- Connect to your research interests

---

## Additional Prompt Ideas

### For Beginners
- "Generate simple examples showing I + I = I"
- "Create test cases for Indeterminate operations"
- "Prove basic commutativity properties with I"

### For Advanced Users
- "Formalize Grothendieck universe with I"
- "Prove I-cohomology theories"
- "Connect I-Algebra to derived categories"

### For Physicists
- "Model black hole singularities with I"
- "Formalize renormalization with I"
- "Create cosmological models using I"

---

## Feedback and Iteration

After using these prompts:
1. Note which prompts were most effective
2. Identify patterns in successful proof generation
3. Refine prompts based on results
4. Share improvements with the community

---

**Version**: 1.0  
**Date**: 2026-01-05  
**Author**: Tiago Fagliari  
**Status**: Ready for Sea Day and Port Day development

---

## License

These prompts are released as part of "The Algebra of the Indeterminate" project.
Free to use and modify for research and educational purposes.
