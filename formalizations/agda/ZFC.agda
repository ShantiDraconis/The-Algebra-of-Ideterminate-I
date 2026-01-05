-- ZF Set Theory with Axiom of Choice in Agda
--
-- This file formalizes the Zermelo-Fraenkel axioms with the Axiom of Choice
-- as described in Section 7.1 of "The Algebra of the Indeterminate I".

{-# OPTIONS --safe #-}

module ZFC where

open import Agda.Primitive using (Level; _⊔_)

-- Universe levels for size issues
private
  variable
    ℓ : Level

-- Basic Set Type (axiomatic)
postulate
  ZFSet : Set₁

-- Membership relation
postulate
  _∈_ : ZFSet → ZFSet → Set

-- Subset relation
_⊆_ : ZFSet → ZFSet → Set
A ⊆ B = ∀ (x : ZFSet) → x ∈ A → x ∈ B

-- ZF Axioms

-- Axiom of Extensionality: Two sets are equal if they have the same elements
postulate
  extensionality : ∀ (A B : ZFSet) →
    (∀ (x : ZFSet) → x ∈ A → x ∈ B) →
    (∀ (x : ZFSet) → x ∈ B → x ∈ A) →
    A ≡ B

-- Axiom of Empty Set
postulate
  empty-set : ∃[ E ∈ ZFSet ] (∀ (x : ZFSet) → ¬ (x ∈ E))
    where
      ∃[_∈_]_ = Σ

-- Axiom of Pairing
postulate
  pairing : ∀ (a b : ZFSet) →
    ∃[ p ∈ ZFSet ] (∀ (x : ZFSet) → x ∈ p ↔ (x ≡ a ⊎ x ≡ b))
    where
      _↔_ : Set → Set → Set
      A ↔ B = (A → B) × (B → A)

-- Axiom of Union
postulate
  union : ∀ (F : ZFSet) →
    ∃[ U ∈ ZFSet ] (∀ (x : ZFSet) →
      x ∈ U ↔ (∃[ s ∈ ZFSet ] (s ∈ F × x ∈ s)))

-- Axiom of Power Set
postulate
  power-set : ∀ (S : ZFSet) →
    ∃[ P ∈ ZFSet ] (∀ (x : ZFSet) →
      x ∈ P ↔ (∀ (y : ZFSet) → y ∈ x → y ∈ S))

-- Axiom of Infinity
postulate
  infinity : ∃[ I ∈ ZFSet ]
    ((∃[ e ∈ ZFSet ] (e ∈ I × (∀ (x : ZFSet) → ¬ (x ∈ e)))) ×
     (∀ (x : ZFSet) → x ∈ I →
       ∃[ s ∈ ZFSet ] (s ∈ I × (∀ (y : ZFSet) → y ∈ s ↔ (y ∈ x ⊎ y ≡ x)))))

-- Axiom Schema of Replacement
postulate
  replacement : ∀ (F : ZFSet → ZFSet → Set) →
    (∀ (x : ZFSet) → ∃![ y ∈ ZFSet ] F x y) →
    ∀ (A : ZFSet) →
    ∃[ B ∈ ZFSet ] (∀ (y : ZFSet) →
      y ∈ B ↔ (∃[ x ∈ ZFSet ] (x ∈ A × F x y)))
    where
      ∃![_∈_]_ = λ T P → Σ T (λ x → P x × (∀ y → P y → x ≡ y))

-- Axiom of Regularity (Foundation)
postulate
  regularity : ∀ (S : ZFSet) →
    (∃[ x ∈ ZFSet ] x ∈ S) →
    ∃[ x ∈ ZFSet ] (x ∈ S × ¬ (∃[ y ∈ ZFSet ] (y ∈ x × y ∈ S)))

-- Axiom Schema of Comprehension (Specification)
postulate
  comprehension : ∀ (A : ZFSet) (P : ZFSet → Set) →
    ∃[ B ∈ ZFSet ] (∀ (x : ZFSet) → x ∈ B ↔ (x ∈ A × P x))

-- Axiom of Choice
postulate
  choice : ∀ (F : ZFSet) →
    (∀ (s : ZFSet) → s ∈ F → ∃[ x ∈ ZFSet ] x ∈ s) →
    ∃[ f ∈ (ZFSet → ZFSet) ] (∀ (s : ZFSet) → s ∈ F → f s ∈ s)

-- Basic Theorems

subset-refl : ∀ (A : ZFSet) → A ⊆ A
subset-refl A x x∈A = x∈A

subset-trans : ∀ (A B C : ZFSet) → A ⊆ B → B ⊆ C → A ⊆ C
subset-trans A B C A⊆B B⊆C x x∈A = B⊆C x (A⊆B x x∈A)

subset-antisym : ∀ (A B : ZFSet) → A ⊆ B → B ⊆ A → A ≡ B
subset-antisym A B A⊆B B⊆A = extensionality A B A⊆B B⊆A
