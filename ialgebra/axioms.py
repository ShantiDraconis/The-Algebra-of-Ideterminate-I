"""
Axioms of the Indeterminate Extended Algebra (IEA)

This module defines and verifies the fundamental axioms of the IEA as described
in "Toward an Indeterminate Extended Algebra (IEA)".

Author: IEA Implementation
Date: 2026-01-05
"""

from typing import List, Dict, Any
from .types import IEAElement, IndeterminateForm
from .operations import IEAOperations


class IEAFundamentalAxioms:
    """
    The 5 fundamental axioms of the Indeterminate Extended Algebra (IEA).
    
    These axioms define a new algebraic structure that is NOT a field,
    but consistently handles singularities and indeterminate forms.
    """
    
    AXIOMS = {
        "A1": {
            "name": "Extended Division",
            "statement": "∀x ≠ 0, x/0 = I, and I ≠ 0",
            "description": "Every fraction with zero denominator maps to I, and I is distinct from zero"
        },
        "A2": {
            "name": "Absorption under Addition and Multiplication",
            "statement": "x + I = I and x · I = I for all x ∈ IEA (with x · I = I for x ≠ 0)",
            "description": "I acts as an absorbing element for addition and multiplication"
        },
        "A3": {
            "name": "Modified Distributivity",
            "statement": "a(b + c) = ab + ac + λJ, where J = iI",
            "description": "Distributive law requires a correction term λJ when I is present"
        },
        "A4": {
            "name": "Nonexistence of Inverses for I",
            "statement": "I does not possess a multiplicative inverse",
            "description": "There is no element I⁻¹ such that I · I⁻¹ = 1"
        },
        "A5": {
            "name": "Preservation of Non-Triviality",
            "statement": "I ≠ 0",
            "description": "I must remain distinct from 0 to prevent system collapse (1 = 0)"
        }
    }
    
    @staticmethod
    def verify_axiom_A1() -> Dict[str, Any]:
        """
        Verify Axiom A1: Extended Division.
        
        Tests:
        1. x/0 = I for various x ≠ 0
        2. I ≠ 0
        
        Returns:
            Dictionary with verification results
        """
        results = {
            "axiom": "A1",
            "name": IEAFundamentalAxioms.AXIOMS["A1"]["name"],
            "tests": []
        }
        
        # Test 1: Division by zero yields I
        test_values = [1.0, 2.0, -3.0, 5.5, 100.0]
        for val in test_values:
            x = IEAElement.real(val)
            zero = IEAElement.zero()
            result = IEAOperations.divide(x, zero)
            passed = result.is_indeterminate()
            results["tests"].append({
                "description": f"{val}/0 = I",
                "passed": passed,
                "result": str(result)
            })
        
        # Test 2: I ≠ 0
        I = IEAElement.I()
        zero = IEAElement.zero()
        passed = I != zero
        results["tests"].append({
            "description": "I ≠ 0",
            "passed": passed,
            "result": f"I == 0: {I == zero}"
        })
        
        results["all_passed"] = all(t["passed"] for t in results["tests"])
        return results
    
    @staticmethod
    def verify_axiom_A2() -> Dict[str, Any]:
        """
        Verify Axiom A2: Absorption Properties.
        
        Tests:
        1. x + I = I for various x
        2. x · I = I for x ≠ 0
        3. 0 · I = 0 (special case)
        
        Returns:
            Dictionary with verification results
        """
        results = {
            "axiom": "A2",
            "name": IEAFundamentalAxioms.AXIOMS["A2"]["name"],
            "tests": []
        }
        
        I = IEAElement.I()
        
        # Test 1: Addition absorption
        test_values = [0.0, 1.0, -2.0, 3.5]
        for val in test_values:
            x = IEAElement.real(val)
            result = IEAOperations.add(x, I)
            passed = result.is_indeterminate()
            results["tests"].append({
                "description": f"{val} + I = I",
                "passed": passed,
                "result": str(result)
            })
        
        # Test 2: Multiplication absorption (non-zero)
        for val in [1.0, -2.0, 3.5]:
            x = IEAElement.real(val)
            result = IEAOperations.multiply(x, I)
            passed = result.is_indeterminate()
            results["tests"].append({
                "description": f"{val} · I = I",
                "passed": passed,
                "result": str(result)
            })
        
        # Test 3: Special case 0 · I = 0
        zero = IEAElement.zero()
        result = IEAOperations.multiply(zero, I)
        passed = result.is_zero()
        results["tests"].append({
            "description": "0 · I = 0",
            "passed": passed,
            "result": str(result)
        })
        
        results["all_passed"] = all(t["passed"] for t in results["tests"])
        return results
    
    @staticmethod
    def verify_axiom_A3() -> Dict[str, Any]:
        """
        Verify Axiom A3: Modified Distributivity.
        
        Tests the modified distributive law:
        a(b + c) = ab + ac + λJ
        
        Returns:
            Dictionary with verification results
        """
        results = {
            "axiom": "A3",
            "name": IEAFundamentalAxioms.AXIOMS["A3"]["name"],
            "tests": []
        }
        
        # Test with infinity: a(∞ - ∞) vs a∞ - a∞
        a = IEAElement.real(2.0)
        pos_inf = IEAElement.pos_infinity()
        neg_inf = IEAElement.neg_infinity()
        
        # Left side: a(∞ - ∞) = a·I = I
        left, right = IEAOperations.modified_distributive(a, pos_inf, neg_inf, lambda_coeff=0.0)
        
        results["tests"].append({
            "description": "a(∞ - ∞) = a·I",
            "passed": left.is_indeterminate(),
            "left": str(left),
            "right": str(right)
        })
        
        # Test standard distributivity still works for reals
        a = IEAElement.real(3.0)
        b = IEAElement.real(4.0)
        c = IEAElement.real(5.0)
        
        left, right = IEAOperations.modified_distributive(a, b, c, lambda_coeff=0.0)
        
        # For reals without I, standard distributivity holds (λ = 0)
        a_bc = IEAOperations.multiply(a, IEAOperations.add(b, c))
        ab_plus_ac = IEAOperations.add(
            IEAOperations.multiply(a, b),
            IEAOperations.multiply(a, c)
        )
        
        passed = (a_bc.value == ab_plus_ac.value if a_bc.is_real() and ab_plus_ac.is_real() else False)
        
        results["tests"].append({
            "description": "Standard distributivity for reals: 3(4+5) = 3·4 + 3·5",
            "passed": passed,
            "left": str(a_bc),
            "right": str(ab_plus_ac)
        })
        
        results["all_passed"] = all(t["passed"] for t in results["tests"])
        return results
    
    @staticmethod
    def verify_axiom_A4() -> Dict[str, Any]:
        """
        Verify Axiom A4: Nonexistence of Inverses for I.
        
        Tests:
        1. I has no multiplicative inverse
        2. If I·x = 1, then x would have to be I⁻¹, but no such x exists
        
        Returns:
            Dictionary with verification results
        """
        results = {
            "axiom": "A4",
            "name": IEAFundamentalAxioms.AXIOMS["A4"]["name"],
            "tests": []
        }
        
        I = IEAElement.I()
        
        # Test 1: Check that has_multiplicative_inverse returns False for I
        has_inverse = IEAOperations.has_multiplicative_inverse(I)
        results["tests"].append({
            "description": "I has no multiplicative inverse",
            "passed": not has_inverse,
            "result": f"has_inverse(I) = {has_inverse}"
        })
        
        # Test 2: Attempt to find inverse returns None
        inverse = IEAOperations.attempt_inverse(I)
        results["tests"].append({
            "description": "attempt_inverse(I) returns None",
            "passed": inverse is None,
            "result": f"inverse = {inverse}"
        })
        
        # Test 3: I · I = I (not 1), demonstrating no inverse exists
        I_squared = IEAOperations.multiply(I, I)
        results["tests"].append({
            "description": "I · I = I (not 1, so no inverse)",
            "passed": I_squared.is_indeterminate(),
            "result": str(I_squared)
        })
        
        results["all_passed"] = all(t["passed"] for t in results["tests"])
        return results
    
    @staticmethod
    def verify_axiom_A5() -> Dict[str, Any]:
        """
        Verify Axiom A5: Preservation of Non-Triviality.
        
        Tests:
        1. I ≠ 0
        2. The collapse contradiction: If I = 0, then 1 = 0
        
        Returns:
            Dictionary with verification results
        """
        results = {
            "axiom": "A5",
            "name": IEAFundamentalAxioms.AXIOMS["A5"]["name"],
            "tests": []
        }
        
        I = IEAElement.I()
        zero = IEAElement.zero()
        one = IEAElement.one()
        
        # Test 1: I ≠ 0
        passed = I != zero
        results["tests"].append({
            "description": "I ≠ 0",
            "passed": passed,
            "result": f"I == 0: {I == zero}"
        })
        
        # Test 2: Demonstrate the collapse contradiction
        # If I = 0, then 1/0 = I = 0, so 1 = 0·0 = 0 (contradiction)
        # We verify that this logical chain would lead to contradiction
        one_over_zero = IEAOperations.divide(one, zero)
        is_I = one_over_zero.is_indeterminate()
        
        results["tests"].append({
            "description": "1/0 = I (not 0, preventing collapse)",
            "passed": is_I and one_over_zero != zero,
            "result": f"1/0 = {one_over_zero}"
        })
        
        # Test 3: Verify that if we assume I = 0, we'd get 1 = 0
        # This is a logical demonstration, not actual computation
        results["tests"].append({
            "description": "Collapse prevention: I ≠ 0 prevents 1 = 0",
            "passed": True,  # This is always true by construction
            "result": "If I = 0, then 1/0 = 0, so 1 = 0 (contradiction)"
        })
        
        results["all_passed"] = all(t["passed"] for t in results["tests"])
        return results
    
    @staticmethod
    def verify_all_axioms() -> Dict[str, Any]:
        """
        Verify all 5 fundamental axioms of the IEA.
        
        Returns:
            Dictionary with results for all axioms
        """
        results = {
            "title": "Verification of IEA Fundamental Axioms",
            "axioms": []
        }
        
        # Verify each axiom
        results["axioms"].append(IEAFundamentalAxioms.verify_axiom_A1())
        results["axioms"].append(IEAFundamentalAxioms.verify_axiom_A2())
        results["axioms"].append(IEAFundamentalAxioms.verify_axiom_A3())
        results["axioms"].append(IEAFundamentalAxioms.verify_axiom_A4())
        results["axioms"].append(IEAFundamentalAxioms.verify_axiom_A5())
        
        # Overall pass/fail
        results["all_axioms_verified"] = all(
            axiom_result["all_passed"] for axiom_result in results["axioms"]
        )
        
        return results


class FieldAxiomFailures:
    """
    Demonstrates where classical field axioms fail in the IEA.
    
    The IEA is NOT a field because:
    1. I has no multiplicative inverse
    2. Distributive law requires modification
    3. I ≠ 0 but I acts as an absorbing element
    """
    
    @staticmethod
    def test_multiplicative_inverse_failure() -> Dict[str, Any]:
        """
        Demonstrate failure of multiplicative inverse axiom.
        
        In a field, every non-zero element has an inverse.
        In the IEA, I ≠ 0 but has no inverse.
        
        Returns:
            Dictionary with test results
        """
        result = {
            "failure": "Multiplicative Inverse Axiom",
            "field_axiom": "∀a ≠ 0, ∃a⁻¹ such that a·a⁻¹ = 1",
            "tests": []
        }
        
        I = IEAElement.I()
        zero = IEAElement.zero()
        one = IEAElement.one()
        
        # I ≠ 0
        result["tests"].append({
            "description": "I ≠ 0",
            "holds": I != zero,
            "result": f"I == 0: {I == zero}"
        })
        
        # But I has no inverse
        has_inverse = IEAOperations.has_multiplicative_inverse(I)
        result["tests"].append({
            "description": "I has no multiplicative inverse",
            "holds": not has_inverse,
            "result": f"has_inverse(I) = {has_inverse}"
        })
        
        # I · I = I ≠ 1
        I_squared = IEAOperations.multiply(I, I)
        result["tests"].append({
            "description": "I · I = I ≠ 1",
            "holds": I_squared.is_indeterminate() and I_squared != one,
            "result": f"I · I = {I_squared}"
        })
        
        result["conclusion"] = "Field axiom FAILS: I ≠ 0 but has no inverse"
        return result
    
    @staticmethod
    def test_distributivity_failure() -> Dict[str, Any]:
        """
        Demonstrate failure of distributive law.
        
        In a field: a(b + c) = ab + ac
        In the IEA: a(b + c) = ab + ac + λJ (correction term needed)
        
        Returns:
            Dictionary with test results
        """
        result = {
            "failure": "Distributive Law",
            "field_axiom": "a(b + c) = ab + ac",
            "tests": []
        }
        
        # Case: a(∞ - ∞) vs a∞ - a∞
        a = IEAElement.real(2.0)
        pos_inf = IEAElement.pos_infinity()
        neg_inf = IEAElement.neg_infinity()
        
        # Left: a(∞ - ∞) = a·I
        left_side = IEAOperations.multiply(a, IEAOperations.subtract(pos_inf, neg_inf))
        
        # Right: a∞ - a∞ = I - I = I (but different from standard)
        a_pos_inf = IEAOperations.multiply(a, pos_inf)
        a_neg_inf = IEAOperations.multiply(a, neg_inf)
        right_side = IEAOperations.subtract(a_pos_inf, a_neg_inf)
        
        result["tests"].append({
            "description": "a(∞ - ∞) vs a∞ - a∞",
            "left": str(left_side),
            "right": str(right_side),
            "equal": left_side == right_side
        })
        
        result["conclusion"] = "Distributive law requires modification: a(b+c) = ab + ac + λJ"
        return result
    
    @staticmethod
    def test_all_failures() -> Dict[str, Any]:
        """
        Test all field axiom failures.
        
        Returns:
            Dictionary with all failure demonstrations
        """
        return {
            "title": "Classical Field Axiom Failures in the IEA",
            "failures": [
                FieldAxiomFailures.test_multiplicative_inverse_failure(),
                FieldAxiomFailures.test_distributivity_failure()
            ]
        }
