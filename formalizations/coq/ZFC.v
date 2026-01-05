(*
  ZF Set Theory with Axiom of Choice in Coq
  
  This file formalizes the Zermelo-Fraenkel axioms with the Axiom of Choice (ZFC)
  as described in Section 7.1 of "The Algebra of the Indeterminate I".
*)

Require Import Classical.
Require Import ClassicalChoice.

Module ZFC.

(** * Basic Set Type *)

Parameter Set : Type.

(** * ZF Axioms *)

(** Axiom of Extensionality *)
Axiom extensionality : forall (A B : Set),
  (forall (x : Set), x ∈ A <-> x ∈ B) -> A = B
where "x ∈ S" := (mem x S).

(** Axiom of Empty Set *)
Axiom empty_set : exists (E : Set), forall (x : Set), ~ (x ∈ E).

(** Axiom of Pairing *)
Axiom pairing : forall (a b : Set),
  exists (p : Set), forall (x : Set), x ∈ p <-> (x = a \/ x = b).

(** Axiom of Union *)
Axiom union : forall (F : Set),
  exists (U : Set), forall (x : Set),
    x ∈ U <-> exists (s : Set), s ∈ F /\ x ∈ s.

(** Axiom of Power Set *)
Axiom power_set : forall (S : Set),
  exists (P : Set), forall (x : Set),
    x ∈ P <-> (forall (y : Set), y ∈ x -> y ∈ S).

(** Axiom of Infinity *)
Axiom infinity : exists (I : Set),
  (exists (e : Set), e ∈ I /\ forall (x : Set), ~ (x ∈ e)) /\
  (forall (x : Set), x ∈ I ->
    exists (s : Set), s ∈ I /\
      forall (y : Set), y ∈ s <-> (y ∈ x \/ y = x)).

(** Axiom Schema of Replacement *)
Axiom replacement : forall (F : Set -> Set -> Prop),
  (forall (x : Set), exists! (y : Set), F x y) ->
  forall (A : Set), exists (B : Set),
    forall (y : Set), y ∈ B <-> exists (x : Set), x ∈ A /\ F x y.

(** Axiom of Regularity (Foundation) *)
Axiom regularity : forall (S : Set),
  (exists (x : Set), x ∈ S) ->
  exists (x : Set), x ∈ S /\ ~ exists (y : Set), y ∈ x /\ y ∈ S.

(** Axiom Schema of Comprehension *)
Axiom comprehension : forall (A : Set) (P : Set -> Prop),
  exists (B : Set), forall (x : Set), x ∈ B <-> (x ∈ A /\ P x).

(** * Axiom of Choice *)

Axiom choice : forall (F : Set),
  (forall (s : Set), s ∈ F -> exists (x : Set), x ∈ s) ->
  exists (f : Set -> Set), forall (s : Set), s ∈ F -> f s ∈ s.

(** * Membership and Basic Relations *)

Parameter mem : Set -> Set -> Prop.

Notation "x ∈ S" := (mem x S) (at level 50).

Definition subset (A B : Set) : Prop :=
  forall (x : Set), x ∈ A -> x ∈ B.

Notation "A ⊆ B" := (subset A B) (at level 50).

(** * Basic Theorems *)

Theorem subset_refl : forall A : Set, A ⊆ A.
Proof.
  intros A x H. exact H.
Qed.

Theorem subset_trans : forall A B C : Set,
  A ⊆ B -> B ⊆ C -> A ⊆ C.
Proof.
  intros A B C H1 H2 x Hx.
  apply H2. apply H1. exact Hx.
Qed.

Theorem subset_antisym : forall A B : Set,
  A ⊆ B -> B ⊆ A -> A = B.
Proof.
  intros A B H1 H2.
  apply extensionality.
  intro x. split.
  - apply H1.
  - apply H2.
Qed.

End ZFC.
