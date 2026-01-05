(*
  Ultrapowers and Nonstandard Analysis in Coq
  
  This file formalizes ultrapowers and their role in nonstandard analysis
  as described in Section 9 of "The Algebra of the Indeterminate I".
*)

Require Import ZFC.
Require Import Cardinals.
Require Import Classical.

Module Ultrapowers.

Import ZFC.
Import CardinalArithmetic.

(** * Index Sets and Filters *)

Parameter IndexSet : Type.

(** A filter on an index set *)
Record Filter (I : Type) : Type := mkFilter {
  filter_sets : Set -> Prop;
  filter_proper : exists (S : Set), ~ filter_sets S;
  filter_upward_closed : forall (A B : Set),
    filter_sets A -> A ⊆ B -> filter_sets B;
  filter_closed_intersection : forall (A B : Set),
    filter_sets A -> filter_sets B -> filter_sets (A ∩ B)
}.

(** An ultrafilter is a maximal filter *)
Record Ultrafilter (I : Type) : Type := mkUltrafilter {
  ultra_base :> Filter I;
  ultra_maximal : forall (S : Set),
    filter_sets ultra_base S \/ filter_sets ultra_base (Sᶜ)
}.

(** * Mathematical Structures *)

Record Structure : Type := mkStructure {
  carrier : Type;
  relations : list (carrier -> carrier -> Prop);
  functions : list (carrier -> carrier)
}.

(** * Ultrapower Construction *)

Definition ultrapower (M : Structure) (I : Type) (U : Ultrafilter I) : Structure.
Admitted.

Notation "M ^ U" := (ultrapower M U) (at level 30).

(** * First-Order Formulas *)

Inductive Formula : Type :=
  | Atom : nat -> Formula
  | Neg : Formula -> Formula
  | And : Formula -> Formula -> Formula
  | Exists : Formula -> Formula.

(** Truth in a structure *)
Parameter satisfies : Structure -> Formula -> Prop.

Notation "M ⊨ φ" := (satisfies M φ) (at level 50).

(** * Łoś's Theorem *)

Axiom los_theorem : forall (M : Structure) (I : Type) (U : Ultrafilter I) (φ : Formula),
  (M ^ U) ⊨ φ <-> M ⊨ φ.

(** * Nonstandard Reals *)

Parameter R_structure : Structure.

Definition nonstandard_reals (I : Type) (U : Ultrafilter I) : Structure :=
  R_structure ^ U.

Notation "⋆R" := nonstandard_reals.

(** Infinitesimals and infinite elements *)
Definition is_infinitesimal (M : Structure) (x : carrier M) : Prop.
Admitted.

Definition is_infinite (M : Structure) (x : carrier M) : Prop.
Admitted.

(** * Role of I in Nonstandard Analysis *)

(** I represents indeterminate limits between infinitesimal elements *)
Axiom I_as_infinitesimal_difference :
  forall (κ λ : Cardinal),
  exists (I_type : Type) (U : Ultrafilter I_type)
         (x y : carrier (⋆R I_type U)),
    is_infinitesimal (⋆R I_type U) x /\
    is_infinitesimal (⋆R I_type U) y /\
    κ ⊖ λ = I.

(** Transfer principle *)
Axiom transfer_principle :
  forall (φ : Formula) (I_type : Type) (U : Ultrafilter I_type),
  R_structure ⊨ φ -> (⋆R I_type U) ⊨ φ.

End Ultrapowers.
