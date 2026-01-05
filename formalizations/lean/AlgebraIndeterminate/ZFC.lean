/-
  ZF Set Theory with Axiom of Choice
  
  This file formalizes the Zermelo-Fraenkel axioms with the Axiom of Choice (ZFC)
  as described in Section 7.1 of "The Algebra of the Indeterminate I".
-/

namespace ZFC

/-! ## Basic Set Type -/

axiom Set : Type

/-! ## ZF Axioms -/

-- Axiom of Extensionality: Two sets are equal if they contain exactly the same elements
axiom extensionality : ∀ (A B : Set), (∀ (x : Set), x ∈ A ↔ x ∈ B) → A = B

-- Axiom of Empty Set: There exists a set with no elements
axiom empty_set : ∃ (E : Set), ∀ (x : Set), x ∉ E

-- Axiom of Pairing: For any two sets, there exists a set containing exactly those two sets
axiom pairing : ∀ (a b : Set), ∃ (p : Set), ∀ (x : Set), x ∈ p ↔ (x = a ∨ x = b)

-- Axiom of Union: For any set of sets, there exists a set of all elements in those sets
axiom union : ∀ (F : Set), ∃ (U : Set), ∀ (x : Set), x ∈ U ↔ ∃ (s : Set), s ∈ F ∧ x ∈ s

-- Axiom of Power Set: For any set, there exists the set of all its subsets
axiom power_set : ∀ (S : Set), ∃ (P : Set), ∀ (x : Set), x ∈ P ↔ (∀ (y : Set), y ∈ x → y ∈ S)

-- Axiom of Infinity: There exists an infinite set
axiom infinity : ∃ (I : Set), (∃ (e : Set), e ∈ I ∧ (∀ (x : Set), x ∉ e)) ∧ 
                 (∀ (x : Set), x ∈ I → ∃ (s : Set), s ∈ I ∧ (∀ (y : Set), y ∈ s ↔ (y ∈ x ∨ y = x)))

-- Axiom Schema of Replacement: Images of sets under functions are sets
axiom replacement : ∀ (F : Set → Set → Prop), 
  (∀ (x : Set), ∃! (y : Set), F x y) → 
  ∀ (A : Set), ∃ (B : Set), ∀ (y : Set), y ∈ B ↔ ∃ (x : Set), x ∈ A ∧ F x y

-- Axiom of Regularity (Foundation): Every non-empty set contains a member disjoint from it
axiom regularity : ∀ (S : Set), (∃ (x : Set), x ∈ S) → 
                   ∃ (x : Set), x ∈ S ∧ ¬∃ (y : Set), y ∈ x ∧ y ∈ S

-- Axiom Schema of Comprehension (Specification): Can form subsets using predicates
axiom comprehension : ∀ (A : Set) (P : Set → Prop), 
  ∃ (B : Set), ∀ (x : Set), x ∈ B ↔ (x ∈ A ∧ P x)

/-! ## Axiom of Choice -/

-- Axiom of Choice: For any set of non-empty sets, there exists a choice function
axiom choice : ∀ (F : Set), 
  (∀ (s : Set), s ∈ F → ∃ (x : Set), x ∈ s) →
  ∃ (f : Set → Set), ∀ (s : Set), s ∈ F → f s ∈ s

/-! ## Basic Properties and Operations -/

-- Membership relation (assumed primitive)
axiom mem : Set → Set → Prop

notation:50 x " ∈ " S => mem x S
notation:50 x " ∉ " S => ¬(mem x S)

-- Subset relation
def subset (A B : Set) : Prop := ∀ (x : Set), x ∈ A → x ∈ B

notation:50 A " ⊆ " B => subset A B

-- Basic theorems derivable from axioms

theorem subset_refl (A : Set) : A ⊆ A := fun _ h => h

theorem subset_trans (A B C : Set) (h1 : A ⊆ B) (h2 : B ⊆ C) : A ⊆ C :=
  fun x hx => h2 x (h1 x hx)

theorem subset_antisym (A B : Set) (h1 : A ⊆ B) (h2 : B ⊆ A) : A = B :=
  extensionality A B (fun x => ⟨h1 x, h2 x⟩)

end ZFC
