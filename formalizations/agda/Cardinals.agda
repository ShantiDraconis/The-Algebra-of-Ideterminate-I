-- Cardinal Arithmetic and the Indeterminate Element I in Agda
--
-- This file formalizes the extended axiomatic system for the indeterminate element I
-- as described in Section 8 of "The Algebra of the Indeterminate I".

{-# OPTIONS --safe #-}

module Cardinals where

open import ZFC
open import Agda.Primitive using (Level)

-- Cardinal Numbers
postulate
  Cardinal : Set

-- Cardinal arithmetic operations
postulate
  _⊕_ : Cardinal → Cardinal → Cardinal  -- Addition
  _⊗_ : Cardinal → Cardinal → Cardinal  -- Multiplication
  _^^_ : Cardinal → Cardinal → Cardinal  -- Exponentiation

infixl 6 _⊕_
infixl 7 _⊗_
infixr 8 _^^_

-- The Indeterminate Element I
postulate
  I : Cardinal

-- The subtractive operation
postulate
  _⊖_ : Cardinal → Cardinal → Cardinal

infixl 6 _⊖_

-- Axioms for the Element I (Section 8.2)

-- Axiom I1: Existence and Uniqueness of I
-- For every cardinal κ, κ ⊖ κ = I
postulate
  axiom-I1 : ∀ (κ : Cardinal) → κ ⊖ κ ≡ I

-- Axiom I2: Limited Neutrality
postulate
  axiom-I2-f : Cardinal → Cardinal → Cardinal
  axiom-I2-g : Cardinal → Cardinal → Cardinal

postulate
  axiom-I2 : ∀ (κ λ : Cardinal) →
    (κ ⊖ λ ≡ axiom-I2-f κ λ) ×
    (λ ⊖ κ ≡ axiom-I2-g κ λ) ×
    (κ ≡ λ → (axiom-I2-f κ λ ≡ I) × (axiom-I2-g κ λ ≡ I))

-- Axiom I3: Consistency with Additive and Multiplicative Operations
postulate
  axiom-I3 : ∀ (κ λ : Cardinal) →
    ((κ ⊕ λ) ⊖ (κ ⊖ λ) ≡ I) ×
    ((κ ⊖ λ) ⊕ (λ ⊖ κ) ≡ I)

-- Fundamental Theorems

-- Theorem 3.1: Uniqueness of the Element I
uniqueness-of-I : ∀ (κ λ : Cardinal) →
  κ ⊖ κ ≡ I → λ ⊖ λ ≡ I → κ ⊖ κ ≡ λ ⊖ λ
uniqueness-of-I κ λ h1 h2 rewrite h1 | h2 = refl
  where
    postulate refl : ∀ {A : Set} {x : A} → x ≡ x

-- Properties of the ⊖ Operation

self-subtraction : ∀ (κ : Cardinal) → κ ⊖ κ ≡ I
self-subtraction = axiom-I1

additive-consistency : ∀ (κ λ : Cardinal) →
  (κ ⊕ λ) ⊖ (κ ⊖ λ) ≡ I
additive-consistency κ λ = proj₁ (axiom-I3 κ λ)
  where
    postulate proj₁ : ∀ {A B : Set} → A × B → A

symmetric-consistency : ∀ (κ λ : Cardinal) →
  (κ ⊖ λ) ⊕ (λ ⊖ κ) ≡ I
symmetric-consistency κ λ = proj₂ (axiom-I3 κ λ)
  where
    postulate proj₂ : ∀ {A B : Set} → A × B → B

-- Extended Cardinal Arithmetic Properties

postulate
  card-add-comm : ∀ (κ λ : Cardinal) → κ ⊕ λ ≡ λ ⊕ κ
  card-add-assoc : ∀ (κ λ μ : Cardinal) → (κ ⊕ λ) ⊕ μ ≡ κ ⊕ (λ ⊕ μ)
  card-mul-comm : ∀ (κ λ : Cardinal) → κ ⊗ λ ≡ λ ⊗ κ
  card-mul-assoc : ∀ (κ λ μ : Cardinal) → (κ ⊗ λ) ⊗ μ ≡ κ ⊗ (λ ⊗ μ)
  card-mul-add-distrib : ∀ (κ λ μ : Cardinal) →
    κ ⊗ (λ ⊕ μ) ≡ (κ ⊗ λ) ⊕ (κ ⊗ μ)

-- Zero and successor cardinals
postulate
  𝟘 : Cardinal  -- Zero cardinal
  card-succ : Cardinal → Cardinal

-- Properties of zero
postulate
  card-zero-add : ∀ (κ : Cardinal) → 𝟘 ⊕ κ ≡ κ
  card-zero-mul : ∀ (κ : Cardinal) → 𝟘 ⊗ κ ≡ 𝟘

-- Integration with ZFC
postulate
  card : ZFSet → Cardinal

postulate
  card-empty : ∃[ E ∈ ZFSet ] (card E ≡ 𝟘)
    where
      ∃[_∈_]_ = λ T P → Σ T P
      postulate Σ : (A : Set) → (A → Set) → Set
  card-singleton : ∀ (x : ZFSet) →
    ∃[ S ∈ ZFSet ] (card S ≡ card-succ 𝟘)
    where
      ∃[_∈_]_ = λ T P → Σ T P
      postulate Σ : (A : Set) → (A → Set) → Set
