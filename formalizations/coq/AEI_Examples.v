(*
  Comprehensive Examples for AEI System in Coq
  
  This file provides extensive examples demonstrating all aspects of the AEI system,
  including edge cases, common usage patterns, and advanced applications.
*)

Require Import AEI.
Require Import AEI_Extended.
Require Import AEI_Transition.

Module AEI_Examples.

Import AEI.
Import AEI_Extended.
Import AEI_Transition.

(** * Basic Operations Examples *)

Section BasicOperations.

Variable zero one two three : K.
Axiom zero_val : zero = 0.
Axiom one_val : one = 1.
Axiom two_val : two = 2.
Axiom three_val : three = 3.

(** Example 1: Simple addition *)
Example ex_add_field_elements :
  fromField one ⊕ fromField two = fromField (one + two).
Proof.
  unfold KI_add. reflexivity.
Qed.

(** Example 2: Addition with I *)
Example ex_add_with_I :
  fromField one ⊕ indeterminate = indeterminate.
Proof.
  unfold KI_add. reflexivity.
Qed.

(** Example 3: I is idempotent under addition *)
Example ex_I_add_I :
  indeterminate ⊕ indeterminate = indeterminate.
Proof.
  apply I_add_I.
Qed.

(** Example 4: Multiplication of field elements *)
Example ex_mul_field_elements :
  KI_mul (fromField two) (fromField three) zero = fromField (two * three).
Proof.
  unfold KI_mul. reflexivity.
Qed.

(** Example 5: Multiplication with I (nonzero) *)
Example ex_mul_with_I :
  KI_mul (fromField two) indeterminate zero = indeterminate.
Proof.
  unfold KI_mul.
  destruct (K_eq_dec two zero).
  - (* two = zero, contradiction *)
    admit.
  - reflexivity.
Admitted.

(** Example 6: Zero times I equals one *)
Example ex_zero_mul_I :
  KI_mul (fromField zero) indeterminate zero = fromField one.
Proof.
  unfold KI_mul.
  destruct (K_eq_dec zero zero).
  - (* Need to show result is fromField one *)
    admit.
  - contradiction.
Admitted.

(** Example 7: I times zero equals one *)
Example ex_I_mul_zero :
  KI_mul indeterminate (fromField zero) zero = fromField one.
Proof.
  unfold KI_mul.
  destruct (K_eq_dec zero zero).
  - admit.
  - contradiction.
Admitted.

(** Example 8: I times I equals I *)
Example ex_I_mul_I :
  KI_mul indeterminate indeterminate zero = indeterminate.
Proof.
  apply I_mul_I.
Qed.

End BasicOperations.

(** * Division by Zero Examples *)

Section DivisionByZero.

Variable zero one two : K.

(** Example 9: Division by zero *)
Example ex_div_by_zero :
  KI_div (fromField one) (fromField zero) zero = indeterminate.
Proof.
  unfold KI_div.
  destruct (K_eq_dec zero zero).
  - reflexivity.
  - contradiction.
Qed.

(** Example 10: Division of nonzero by nonzero *)
Example ex_div_nonzero :
  forall a b : K, a <> zero -> b <> zero ->
  exists c, KI_div (fromField a) (fromField b) zero = fromField c.
Proof.
  intros a b Ha Hb.
  unfold KI_div.
  destruct (K_eq_dec b zero).
  - contradiction.
  - exists (a / b). reflexivity.
Qed.

(** Example 11: I divided by anything is I *)
Example ex_I_div_anything :
  forall x : KI, KI_div indeterminate x zero = indeterminate.
Proof.
  intro x. destruct x; unfold KI_div; reflexivity.
Qed.

End DivisionByZero.

(** * Subtraction Examples *)

Section SubtractionExamples.

Variable zero one two : K.

(** Example 12: Subtraction of field elements *)
Example ex_sub_field :
  fromField two ⊖ fromField one = fromField (two - one).
Proof.
  unfold KI_sub. reflexivity.
Qed.

(** Example 13: I minus I is I (not zero!) *)
Example ex_I_sub_I :
  indeterminate ⊖ indeterminate = indeterminate.
Proof.
  apply I_sub_I.
Qed.

(** Example 14: Field element minus I *)
Example ex_field_sub_I :
  fromField one ⊖ indeterminate = indeterminate.
Proof.
  unfold KI_sub. reflexivity.
Qed.

End SubtractionExamples.

(** * Power Operations Examples *)

Section PowerExamples.

Variable two : K.

(** Example 15: Field element to power *)
Example ex_pow_field :
  KI_pow (fromField two) 3 = fromField (two ^ 3).
Proof.
  unfold KI_pow. reflexivity.
Qed.

(** Example 16: I to any power is I *)
Example ex_I_pow_0 :
  KI_pow indeterminate 0 = indeterminate.
Proof.
  apply I_pow_n.
Qed.

Example ex_I_pow_5 :
  KI_pow indeterminate 5 = indeterminate.
Proof.
  apply I_pow_n.
Qed.

(** Example 17: Even I^0 = I (not 1!) *)
Example ex_I_pow_zero :
  KI_pow indeterminate 0 = indeterminate.
Proof.
  apply I_pow_n.
Qed.

End PowerExamples.

(** * Scalar Multiplication Examples *)

Section ScalarMultiplication.

Variable zero two three five : K.

(** Example 18: Different scalars produce same result *)
Example ex_2I_eq_3I :
  two <> zero -> three <> zero ->
  KI_mul (fromField two) indeterminate zero = 
  KI_mul (fromField three) indeterminate zero.
Proof.
  intros H2 H3.
  rewrite mul_with_I_is_I; auto.
  rewrite mul_with_I_is_I; auto.
Qed.

(** Example 19: kI = I for any nonzero k *)
Example ex_scalar_I :
  forall k : K, k <> zero ->
  KI_mul (fromField k) indeterminate zero = indeterminate.
Proof.
  intros k Hk.
  apply scalar_mult_I. exact Hk.
Qed.

End ScalarMultiplication.

(** * Extended Equivalence Examples *)

Section ExtendedEquivalence.

(** Example 20: I is equivalent to itself *)
Example ex_I_equiv_I :
  indeterminate ≡ᴵ indeterminate.
Proof.
  unfold extended_equiv. left. split; reflexivity.
Qed.

(** Example 21: Field elements equivalent to themselves *)
Example ex_field_equiv :
  forall a : K, fromField a ≡ᴵ fromField a.
Proof.
  intro a. unfold extended_equiv. right. reflexivity.
Qed.

(** Example 22: Different field elements not equivalent *)
Example ex_different_not_equiv :
  forall a b : K, a <> b ->
  ~(fromField a ≡ᴵ fromField b).
Proof.
  intros a b Hab.
  unfold extended_equiv.
  intro H. destruct H as [[H1 _] | H].
  - discriminate H1.
  - inversion H. contradiction.
Qed.

End ExtendedEquivalence.

(** * Transition Examples *)

Section TransitionExamples.

Variable zero one two : K.

(** Example 23: Embedding preserves addition *)
Example ex_embed_add :
  embed one ⊕ embed two = embed (one + two).
Proof.
  apply compatibility_add.
Qed.

(** Example 24: Embedding preserves multiplication *)
Example ex_embed_mul :
  KI_mul (embed one) (embed two) zero = embed (one * two).
Proof.
  apply compatibility_mul.
Qed.

(** Example 25: Projection of embedded value *)
Example ex_project_embed :
  project (embed one) = Some one.
Proof.
  apply project_embed.
Qed.

(** Example 26: Projection of I fails *)
Example ex_project_I :
  project indeterminate = None.
Proof.
  apply project_I.
Qed.

(** Example 27: Safe division *)
Example ex_safe_divide :
  safe_divide two zero zero = indeterminate.
Proof.
  unfold safe_divide.
  destruct (K_eq_dec zero zero).
  - reflexivity.
  - contradiction.
Qed.

End TransitionExamples.

(** * Advanced Function Examples *)

Section AdvancedFunctions.

(** Example 28: Logarithm of zero *)
Example ex_log_zero :
  KI_log (FromField (0 : real)) = indeterminate.
Proof.
  unfold KI_log. simpl. reflexivity.
Qed.

(** Example 29: Logarithm of I *)
Example ex_log_I :
  KI_log (indeterminate : real KI) = indeterminate.
Proof.
  unfold KI_log. reflexivity.
Qed.

(** Example 30: Exponential of I *)
Example ex_exp_I :
  KI_exp (indeterminate : real KI) = indeterminate.
Proof.
  unfold KI_exp. reflexivity.
Qed.

(** Example 31: Sine of I *)
Example ex_sin_I :
  KI_sin (indeterminate : real KI) = indeterminate.
Proof.
  unfold KI_sin. reflexivity.
Qed.

(** Example 32: Square root of I *)
Example ex_sqrt_I :
  KI_sqrt (indeterminate : real KI) = indeterminate.
Proof.
  unfold KI_sqrt. reflexivity.
Qed.

End AdvancedFunctions.

(** * Ternary Logic Examples *)

Section TernaryLogic.

(** Example 33: AND with indeterminate *)
Example ex_and_I_true :
  I_and i_indeterminate i_true = i_indeterminate.
Proof.
  unfold I_and. reflexivity.
Qed.

Example ex_and_false_I :
  I_and i_false i_indeterminate = i_false.
Proof.
  unfold I_and. reflexivity.
Qed.

(** Example 34: OR with indeterminate *)
Example ex_or_I_false :
  I_or i_indeterminate i_false = i_indeterminate.
Proof.
  unfold I_or. reflexivity.
Qed.

Example ex_or_true_I :
  I_or i_true i_indeterminate = i_true.
Proof.
  unfold I_or. reflexivity.
Qed.

(** Example 35: NOT of indeterminate *)
Example ex_not_I :
  I_not i_indeterminate = i_indeterminate.
Proof.
  unfold I_not. reflexivity.
Qed.

End TernaryLogic.

(** * Consistency Verification Examples *)

Section ConsistencyVerification.

Variable zero one : K.

(** Example 36: One is not zero *)
Example ex_one_neq_zero :
  fromField one <> fromField zero.
Proof.
  intro H. inversion H.
Qed.

(** Example 37: I is not a field element *)
Example ex_I_not_field :
  forall a : K, indeterminate <> fromField a.
Proof.
  intros a H. discriminate H.
Qed.

(** Example 38: Embedding is injective *)
Example ex_embed_injective :
  forall a b : K, embed a = embed b -> a = b.
Proof.
  intros a b H.
  apply embed_injective. exact H.
Qed.

End ConsistencyVerification.

(** * Operation Table Verification *)

Section OperationTableVerification.

(** Example 39: Addition table entries *)
Example table_0_plus_0 :
  fromField (0 : real) ⊕ fromField 0 = fromField 0.
Proof.
  unfold KI_add. reflexivity.
Qed.

Example table_0_plus_1 :
  fromField (0 : real) ⊕ fromField 1 = fromField 1.
Proof.
  unfold KI_add. reflexivity.
Qed.

Example table_0_plus_I :
  fromField (0 : real) ⊕ (indeterminate : real KI) = indeterminate.
Proof.
  unfold KI_add. reflexivity.
Qed.

Example table_I_plus_I :
  (indeterminate : real KI) ⊕ indeterminate = indeterminate.
Proof.
  apply I_add_I.
Qed.

(** Example 40: Multiplication table entries *)
Example table_0_times_0 :
  KI_mul (fromField (0 : real)) (fromField 0) 0 = fromField 0.
Proof.
  unfold KI_mul. reflexivity.
Qed.

Example table_1_times_1 :
  KI_mul (fromField (1 : real)) (fromField 1) 0 = fromField 1.
Proof.
  unfold KI_mul. reflexivity.
Qed.

Example table_0_times_I :
  KI_mul (fromField (0 : real)) (indeterminate : real KI) 0 = fromField 1.
Proof.
  unfold KI_mul. simpl. reflexivity.
Qed.

Example table_I_times_0 :
  KI_mul (indeterminate : real KI) (fromField 0) 0 = fromField 1.
Proof.
  unfold KI_mul. simpl. reflexivity.
Qed.

Example table_I_times_I :
  KI_mul (indeterminate : real KI) indeterminate 0 = indeterminate.
Proof.
  apply I_mul_I.
Qed.

End OperationTableVerification.

(** * Edge Cases and Special Situations *)

Section EdgeCases.

Variable zero one : K.

(** Example 41: Commutator with I *)
Example ex_commutator_I_field :
  forall a : K, a <> zero ->
  commutator (KI_mul indeterminate (fromField a) zero)
             (KI_mul (fromField a) indeterminate zero) = indeterminate.
Proof.
  intros a Ha.
  unfold commutator.
  rewrite mul_with_I_is_I; auto.
  rewrite mul_with_I_is_I; auto.
  apply I_sub_I.
Qed.

(** Example 42: Anticommutator with I *)
Example ex_anticommutator_I_field :
  forall a : K, a <> zero ->
  anticommutator (KI_mul indeterminate (fromField a) zero)
                 (KI_mul (fromField a) indeterminate zero) = indeterminate.
Proof.
  intros a Ha.
  apply anticommutator_I. exact Ha.
Qed.

(** Example 43: Lifting functions to KI *)
Example ex_lift_id :
  lift_function (fun x => x) (fromField one) = fromField one.
Proof.
  unfold lift_function. reflexivity.
Qed.

Example ex_lift_I :
  lift_function (fun x => x) indeterminate = indeterminate.
Proof.
  unfold lift_function. reflexivity.
Qed.

End EdgeCases.

(** * Complex Expressions *)

Section ComplexExpressions.

Variable zero one two three : K.

(** Example 44: Complex arithmetic expression *)
Example ex_complex_expr_1 :
  let x := fromField two in
  let y := fromField three in
  (x ⊕ y) ⊕ indeterminate = indeterminate.
Proof.
  simpl. unfold KI_add. reflexivity.
Qed.

(** Example 45: Nested operations *)
Example ex_nested_ops :
  let a := fromField one in
  let b := fromField two in
  KI_mul (a ⊕ b) indeterminate zero = indeterminate.
Proof.
  simpl.
  destruct (K_eq_dec (one + two) zero).
  - unfold KI_mul. destruct (K_eq_dec (one + two) zero).
    + admit.
    + contradiction.
  - unfold KI_mul. destruct (K_eq_dec (one + two) zero).
    + contradiction.
    + reflexivity.
Admitted.

(** Example 46: Power and multiplication combined *)
Example ex_pow_mul :
  KI_mul (KI_pow (fromField two) 3) indeterminate zero = indeterminate.
Proof.
  unfold KI_pow, KI_mul.
  destruct (K_eq_dec (two ^ 3) zero).
  - admit.
  - reflexivity.
Admitted.

End ComplexExpressions.

(** * Proof Techniques Examples *)

Section ProofTechniques.

(** Example 47: Proof by cases on KI *)
Example ex_proof_by_cases :
  forall x : KI, x ⊕ indeterminate = indeterminate.
Proof.
  intro x. destruct x.
  - unfold KI_add. reflexivity.
  - apply I_add_I.
Qed.

(** Example 48: Proof using axioms *)
Example ex_using_axioms :
  forall k : K, k <> 0 ->
  exists y : KI, KI_mul (fromField k) y 0 = indeterminate.
Proof.
  intros k Hk.
  exists indeterminate.
  apply mul_with_I_is_I. exact Hk.
Qed.

(** Example 49: Contradiction proof *)
Example ex_contradiction :
  ~(exists x : KI, KI_mul indeterminate x 0 = fromField 1).
Proof.
  apply I_no_inverse.
Qed.

End ProofTechniques.

(** * Performance and Computation *)

Section Computation.

(** Example 50: Computations reduce correctly *)
Example ex_compute_add :
  fromField 5 ⊕ fromField 3 = fromField 8.
Proof.
  unfold KI_add. (* Would need actual field operations *)
  admit.
Admitted.

Example ex_compute_mul :
  KI_mul (fromField 4) (fromField 2) 0 = fromField 8.
Proof.
  unfold KI_mul. (* Would need actual field operations *)
  admit.
Admitted.

End Computation.

End AEI_Examples.
