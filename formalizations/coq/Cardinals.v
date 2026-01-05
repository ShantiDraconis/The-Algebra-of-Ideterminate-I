(*
  Cardinal Arithmetic and the Indeterminate Element I in Coq
  
  This file formalizes the extended axiomatic system for the indeterminate element I
  as described in Section 8 of "The Algebra of the Indeterminate I".
*)

Require Import ZFC.

Module CardinalArithmetic.

Import ZFC.

(** * Cardinal Numbers *)

Parameter Cardinal : Type.

(** Cardinal arithmetic operations *)
Parameter card_add : Cardinal -> Cardinal -> Cardinal.
Parameter card_mul : Cardinal -> Cardinal -> Cardinal.
Parameter card_exp : Cardinal -> Cardinal -> Cardinal.

Notation "κ ⊕ λ" := (card_add κ λ) (at level 50, left associativity).
Notation "κ ⊗ λ" := (card_mul κ λ) (at level 40, left associativity).
Notation "κ ^^ λ" := (card_exp κ λ) (at level 30, right associativity).

(** * The Indeterminate Element I *)

Parameter I : Cardinal.

(** The subtractive operation *)
Parameter card_sub : Cardinal -> Cardinal -> Cardinal.

Notation "κ ⊖ λ" := (card_sub κ λ) (at level 50, left associativity).

(** * Axioms for the Element I (Section 8.2) *)

(** Axiom I1: Existence and Uniqueness of I *)
Axiom axiom_I1 : forall (κ : Cardinal), κ ⊖ κ = I.

(** Axiom I2: Limited Neutrality *)
Parameter axiom_I2_f : Cardinal -> Cardinal -> Cardinal.
Parameter axiom_I2_g : Cardinal -> Cardinal -> Cardinal.

Axiom axiom_I2 : forall (κ λ : Cardinal),
  κ ⊖ λ = axiom_I2_f κ λ /\
  λ ⊖ κ = axiom_I2_g κ λ /\
  (κ = λ -> axiom_I2_f κ λ = I /\ axiom_I2_g κ λ = I).

(** Axiom I3: Consistency with Additive and Multiplicative Operations *)
Axiom axiom_I3 : forall (κ λ : Cardinal),
  (κ ⊕ λ) ⊖ (κ ⊖ λ) = I /\ (κ ⊖ λ) ⊕ (λ ⊖ κ) = I.

(** * Fundamental Theorems *)

(** Theorem 3.1: Uniqueness of the Element I *)
Theorem uniqueness_of_I : forall (κ λ : Cardinal),
  κ ⊖ κ = I -> λ ⊖ λ = I -> κ ⊖ κ = λ ⊖ λ.
Proof.
  intros κ λ H1 H2.
  rewrite H1. rewrite H2. reflexivity.
Qed.

(** Corollary: I is unique *)
Theorem I_unique : forall (J : Cardinal),
  (forall (κ : Cardinal), κ ⊖ κ = J) -> J = I.
Proof.
  intros J H.
  specialize (H I).
  rewrite axiom_I1 in H.
  symmetry. exact H.
Qed.

(** * Properties of the ⊖ Operation *)

Theorem self_subtraction : forall (κ : Cardinal), κ ⊖ κ = I.
Proof.
  exact axiom_I1.
Qed.

Theorem additive_consistency : forall (κ λ : Cardinal),
  (κ ⊕ λ) ⊖ (κ ⊖ λ) = I.
Proof.
  intros κ λ.
  destruct (axiom_I3 κ λ) as [H _].
  exact H.
Qed.

Theorem symmetric_consistency : forall (κ λ : Cardinal),
  (κ ⊖ λ) ⊕ (λ ⊖ κ) = I.
Proof.
  intros κ λ.
  destruct (axiom_I3 κ λ) as [_ H].
  exact H.
Qed.

(** * Extended Cardinal Arithmetic Properties *)

Axiom card_add_comm : forall (κ λ : Cardinal), κ ⊕ λ = λ ⊕ κ.
Axiom card_add_assoc : forall (κ λ μ : Cardinal), (κ ⊕ λ) ⊕ μ = κ ⊕ (λ ⊕ μ).
Axiom card_mul_comm : forall (κ λ : Cardinal), κ ⊗ λ = λ ⊗ κ.
Axiom card_mul_assoc : forall (κ λ μ : Cardinal), (κ ⊗ λ) ⊗ μ = κ ⊗ (λ ⊗ μ).
Axiom card_mul_add_distrib : forall (κ λ μ : Cardinal),
  κ ⊗ (λ ⊕ μ) = (κ ⊗ λ) ⊕ (κ ⊗ μ).

(** Zero and successor cardinals *)
Parameter card_zero : Cardinal.
Parameter card_succ : Cardinal -> Cardinal.

Notation "𝟘" := card_zero.

(** Properties of zero *)
Axiom card_zero_add : forall (κ : Cardinal), 𝟘 ⊕ κ = κ.
Axiom card_zero_mul : forall (κ : Cardinal), 𝟘 ⊗ κ = 𝟘.

(** * Integration with ZFC *)

Parameter card : Set -> Cardinal.

Axiom card_empty : exists (E : Set), card E = 𝟘.
Axiom card_singleton : forall (x : Set),
  exists (S : Set), card S = card_succ 𝟘.

End CardinalArithmetic.
