(*
  ZF Set Theory with Axiom of Choice in Isabelle/HOL
  
  This theory formalizes the Zermelo-Fraenkel axioms with the Axiom of Choice
  as described in Section 7.1 of "The Algebra of the Indeterminate I".
*)

theory ZFC
  imports Main
begin

(* Basic Set Type - using Isabelle's built-in set type *)
typedecl ZFSet

(* Membership relation *)
consts mem :: "ZFSet \<Rightarrow> ZFSet \<Rightarrow> bool" (infixl "\<in>" 50)

(* Subset relation *)
definition subset :: "ZFSet \<Rightarrow> ZFSet \<Rightarrow> bool" (infixl "\<subseteq>" 50) where
  "A \<subseteq> B \<equiv> \<forall>x. x \<in> A \<longrightarrow> x \<in> B"

(* ZF Axioms *)

(* Axiom of Extensionality *)
axiomatization where
  extensionality: "\<lbrakk>\<And>x. x \<in> A \<longleftrightarrow> x \<in> B\<rbrakk> \<Longrightarrow> A = B"

(* Axiom of Empty Set *)
axiomatization where
  empty_set: "\<exists>E. \<forall>x. \<not>(x \<in> E)"

(* Axiom of Pairing *)
axiomatization where
  pairing: "\<exists>p. \<forall>x. x \<in> p \<longleftrightarrow> (x = a \<or> x = b)"

(* Axiom of Union *)
axiomatization where
  union: "\<exists>U. \<forall>x. x \<in> U \<longleftrightarrow> (\<exists>s. s \<in> F \<and> x \<in> s)"

(* Axiom of Power Set *)
axiomatization where
  power_set: "\<exists>P. \<forall>x. x \<in> P \<longleftrightarrow> (\<forall>y. y \<in> x \<longrightarrow> y \<in> S)"

(* Axiom of Infinity *)
axiomatization where
  infinity: "\<exists>I. (\<exists>e. e \<in> I \<and> (\<forall>x. \<not>(x \<in> e))) \<and>
                 (\<forall>x. x \<in> I \<longrightarrow> (\<exists>s. s \<in> I \<and> (\<forall>y. y \<in> s \<longleftrightarrow> (y \<in> x \<or> y = x))))"

(* Axiom Schema of Replacement *)
axiomatization where
  replacement: "\<lbrakk>\<And>x. \<exists>!y. F x y\<rbrakk> \<Longrightarrow> 
                \<exists>B. \<forall>y. y \<in> B \<longleftrightarrow> (\<exists>x. x \<in> A \<and> F x y)"

(* Axiom of Regularity (Foundation) *)
axiomatization where
  regularity: "\<lbrakk>\<exists>x. x \<in> S\<rbrakk> \<Longrightarrow> 
               \<exists>x. x \<in> S \<and> \<not>(\<exists>y. y \<in> x \<and> y \<in> S)"

(* Axiom Schema of Comprehension *)
axiomatization where
  comprehension: "\<exists>B. \<forall>x. x \<in> B \<longleftrightarrow> (x \<in> A \<and> P x)"

(* Axiom of Choice *)
axiomatization where
  choice: "\<lbrakk>\<And>s. s \<in> F \<Longrightarrow> \<exists>x. x \<in> s\<rbrakk> \<Longrightarrow>
           \<exists>f. \<forall>s. s \<in> F \<longrightarrow> (f s) \<in> s"

(* Basic Theorems *)

theorem subset_refl: "A \<subseteq> A"
  unfolding subset_def by auto

theorem subset_trans: "\<lbrakk>A \<subseteq> B; B \<subseteq> C\<rbrakk> \<Longrightarrow> A \<subseteq> C"
  unfolding subset_def by auto

theorem subset_antisym: "\<lbrakk>A \<subseteq> B; B \<subseteq> A\<rbrakk> \<Longrightarrow> A = B"
  unfolding subset_def
  by (rule extensionality) auto

end
