(*
  Cardinal Arithmetic and the Indeterminate Element I in Isabelle/HOL
  
  This theory formalizes the extended axiomatic system for the indeterminate element I
  as described in Section 8 of "The Algebra of the Indeterminate I".
*)

theory Cardinals
  imports ZFC
begin

(* Cardinal Numbers *)
typedecl Cardinal

(* Cardinal arithmetic operations *)
consts
  card_add :: "Cardinal \<Rightarrow> Cardinal \<Rightarrow> Cardinal" (infixl "\<oplus>" 65)
  card_mul :: "Cardinal \<Rightarrow> Cardinal \<Rightarrow> Cardinal" (infixl "\<otimes>" 70)
  card_exp :: "Cardinal \<Rightarrow> Cardinal \<Rightarrow> Cardinal" (infixl "^^" 80)

(* The Indeterminate Element I *)
consts I :: Cardinal

(* The subtractive operation *)
consts card_sub :: "Cardinal \<Rightarrow> Cardinal \<Rightarrow> Cardinal" (infixl "\<ominus>" 65)

(* Axioms for the Element I (Section 8.2) *)

(* Axiom I1: Existence and Uniqueness of I *)
axiomatization where
  axiom_I1: "\<kappa> \<ominus> \<kappa> = I"

(* Axiom I2: Limited Neutrality *)
consts
  axiom_I2_f :: "Cardinal \<Rightarrow> Cardinal \<Rightarrow> Cardinal"
  axiom_I2_g :: "Cardinal \<Rightarrow> Cardinal \<Rightarrow> Cardinal"

axiomatization where
  axiom_I2: "\<kappa> \<ominus> \<lambda> = axiom_I2_f \<kappa> \<lambda> \<and>
             \<lambda> \<ominus> \<kappa> = axiom_I2_g \<kappa> \<lambda> \<and>
             (\<kappa> = \<lambda> \<longrightarrow> axiom_I2_f \<kappa> \<lambda> = I \<and> axiom_I2_g \<kappa> \<lambda> = I)"

(* Axiom I3: Consistency with Additive Operations *)
axiomatization where
  axiom_I3: "(\<kappa> \<oplus> \<lambda>) \<ominus> (\<kappa> \<ominus> \<lambda>) = I \<and> (\<kappa> \<ominus> \<lambda>) \<oplus> (\<lambda> \<ominus> \<kappa>) = I"

(* Fundamental Theorems *)

(* Theorem 3.1: Uniqueness of the Element I *)
theorem uniqueness_of_I:
  assumes "\<kappa> \<ominus> \<kappa> = I" and "\<lambda> \<ominus> \<lambda> = I"
  shows "\<kappa> \<ominus> \<kappa> = \<lambda> \<ominus> \<lambda>"
  using assms by simp

(* Properties of the \<ominus> Operation *)

theorem self_subtraction: "\<kappa> \<ominus> \<kappa> = I"
  by (rule axiom_I1)

theorem additive_consistency: "(\<kappa> \<oplus> \<lambda>) \<ominus> (\<kappa> \<ominus> \<lambda>) = I"
  using axiom_I3 by simp

theorem symmetric_consistency: "(\<kappa> \<ominus> \<lambda>) \<oplus> (\<lambda> \<ominus> \<kappa>) = I"
  using axiom_I3 by simp

(* Extended Cardinal Arithmetic Properties *)

axiomatization where
  card_add_comm: "\<kappa> \<oplus> \<lambda> = \<lambda> \<oplus> \<kappa>" and
  card_add_assoc: "(\<kappa> \<oplus> \<lambda>) \<oplus> \<mu> = \<kappa> \<oplus> (\<lambda> \<oplus> \<mu>)" and
  card_mul_comm: "\<kappa> \<otimes> \<lambda> = \<lambda> \<otimes> \<kappa>" and
  card_mul_assoc: "(\<kappa> \<otimes> \<lambda>) \<otimes> \<mu> = \<kappa> \<otimes> (\<lambda> \<otimes> \<mu>)" and
  card_mul_add_distrib: "\<kappa> \<otimes> (\<lambda> \<oplus> \<mu>) = (\<kappa> \<otimes> \<lambda>) \<oplus> (\<kappa> \<otimes> \<mu>)"

(* Zero and successor cardinals *)
consts
  card_zero :: Cardinal ("\<zero>")
  card_succ :: "Cardinal \<Rightarrow> Cardinal"

axiomatization where
  card_zero_add: "\<zero> \<oplus> \<kappa> = \<kappa>" and
  card_zero_mul: "\<zero> \<otimes> \<kappa> = \<zero>"

(* Integration with ZFC *)
consts card :: "ZFSet \<Rightarrow> Cardinal"

axiomatization where
  card_empty: "\<exists>E. card E = \<zero>" and
  card_singleton: "\<exists>S. card S = card_succ \<zero>"

end
