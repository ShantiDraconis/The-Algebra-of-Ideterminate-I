"""
Test suite for the Indeterminate Extended Algebra (IEA)

This module contains comprehensive tests for the IEA implementation,
verifying axioms, operations, and field axiom failures.

Author: IEA Implementation
Date: 2026-01-05
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ialgebra.types import IEAElement, ElementType, IndeterminateForm
from ialgebra.operations import IEAOperations, IEAAxioms
from ialgebra.axioms import IEAFundamentalAxioms, FieldAxiomFailures


class TestIEATypes(unittest.TestCase):
    """Test the IEA type system."""
    
    def test_create_real(self):
        """Test creating real number elements."""
        x = IEAElement.real(3.5)
        self.assertEqual(x.value, 3.5)
        self.assertEqual(x.element_type, ElementType.REAL)
        self.assertTrue(x.is_real())
    
    def test_create_I(self):
        """Test creating the indeterminate element I."""
        I = IEAElement.I()
        self.assertEqual(I.element_type, ElementType.INDETERMINATE)
        self.assertTrue(I.is_indeterminate())
        self.assertFalse(I.is_zero())
    
    def test_create_J(self):
        """Test creating the imaginary singularity J."""
        J = IEAElement.J()
        self.assertEqual(J.element_type, ElementType.IMAGINARY_SINGULARITY)
        self.assertTrue(J.is_imaginary_singularity())
    
    def test_I_not_equal_zero(self):
        """Test that I ≠ 0."""
        I = IEAElement.I()
        zero = IEAElement.zero()
        self.assertNotEqual(I, zero)
    
    def test_infinities(self):
        """Test creation of infinity elements."""
        pos_inf = IEAElement.pos_infinity()
        neg_inf = IEAElement.neg_infinity()
        iI = IEAElement.imaginary_infinity()
        neg_iI = IEAElement.neg_imaginary_infinity()
        
        self.assertTrue(pos_inf.is_singularity())
        self.assertTrue(neg_inf.is_singularity())
        self.assertTrue(iI.is_singularity())
        self.assertTrue(neg_iI.is_singularity())


class TestIEAOperations(unittest.TestCase):
    """Test IEA operations."""
    
    def test_real_addition(self):
        """Test addition of real numbers."""
        a = IEAElement.real(3.0)
        b = IEAElement.real(4.0)
        result = IEAOperations.add(a, b)
        self.assertTrue(result.is_real())
        self.assertEqual(result.value, 7.0)
    
    def test_absorption_addition(self):
        """Test that x + I = I."""
        x = IEAElement.real(5.0)
        I = IEAElement.I()
        result = IEAOperations.add(x, I)
        self.assertTrue(result.is_indeterminate())
    
    def test_infinity_minus_infinity(self):
        """Test that ∞ - ∞ = I."""
        pos_inf = IEAElement.pos_infinity()
        result = IEAOperations.subtract(pos_inf, pos_inf)
        self.assertTrue(result.is_indeterminate())
    
    def test_real_multiplication(self):
        """Test multiplication of real numbers."""
        a = IEAElement.real(3.0)
        b = IEAElement.real(4.0)
        result = IEAOperations.multiply(a, b)
        self.assertTrue(result.is_real())
        self.assertEqual(result.value, 12.0)
    
    def test_absorption_multiplication(self):
        """Test that x · I = I for x ≠ 0."""
        x = IEAElement.real(5.0)
        I = IEAElement.I()
        result = IEAOperations.multiply(x, I)
        self.assertTrue(result.is_indeterminate())
    
    def test_zero_times_I(self):
        """Test special case: 0 · I = 0."""
        zero = IEAElement.zero()
        I = IEAElement.I()
        result = IEAOperations.multiply(zero, I)
        self.assertTrue(result.is_zero())
    
    def test_division_by_zero(self):
        """Test that x/0 = I for x ≠ 0."""
        x = IEAElement.real(5.0)
        zero = IEAElement.zero()
        result = IEAOperations.divide(x, zero)
        self.assertTrue(result.is_indeterminate())
    
    def test_zero_divided_by_zero(self):
        """Test that 0/0 = I."""
        zero = IEAElement.zero()
        result = IEAOperations.divide(zero, zero)
        self.assertTrue(result.is_indeterminate())
    
    def test_real_division(self):
        """Test division of real numbers."""
        a = IEAElement.real(12.0)
        b = IEAElement.real(3.0)
        result = IEAOperations.divide(a, b)
        self.assertTrue(result.is_real())
        self.assertEqual(result.value, 4.0)


class TestMultiplicativeInverse(unittest.TestCase):
    """Test multiplicative inverse properties."""
    
    def test_I_has_no_inverse(self):
        """Test that I has no multiplicative inverse."""
        I = IEAElement.I()
        self.assertFalse(IEAOperations.has_multiplicative_inverse(I))
    
    def test_zero_has_no_inverse(self):
        """Test that 0 has no multiplicative inverse."""
        zero = IEAElement.zero()
        self.assertFalse(IEAOperations.has_multiplicative_inverse(zero))
    
    def test_nonzero_real_has_inverse(self):
        """Test that non-zero real numbers have inverses."""
        x = IEAElement.real(5.0)
        self.assertTrue(IEAOperations.has_multiplicative_inverse(x))
    
    def test_compute_real_inverse(self):
        """Test computing the inverse of a real number."""
        x = IEAElement.real(4.0)
        inv = IEAOperations.attempt_inverse(x)
        self.assertIsNotNone(inv)
        self.assertTrue(inv.is_real())
        self.assertAlmostEqual(inv.value, 0.25)
    
    def test_I_inverse_returns_none(self):
        """Test that attempting to compute I⁻¹ returns None."""
        I = IEAElement.I()
        inv = IEAOperations.attempt_inverse(I)
        self.assertIsNone(inv)
    
    def test_I_squared(self):
        """Test that I · I = I."""
        I = IEAElement.I()
        result = IEAOperations.multiply(I, I)
        self.assertTrue(result.is_indeterminate())


class TestModifiedDistributive(unittest.TestCase):
    """Test the modified distributive law."""
    
    def test_standard_distributive_for_reals(self):
        """Test that standard distributivity works for real numbers."""
        a = IEAElement.real(2.0)
        b = IEAElement.real(3.0)
        c = IEAElement.real(4.0)
        
        # a(b + c)
        left = IEAOperations.multiply(a, IEAOperations.add(b, c))
        
        # ab + ac
        ab = IEAOperations.multiply(a, b)
        ac = IEAOperations.multiply(a, c)
        right = IEAOperations.add(ab, ac)
        
        self.assertTrue(left.is_real())
        self.assertTrue(right.is_real())
        self.assertAlmostEqual(left.value, right.value)
    
    def test_modified_distributive_with_infinity(self):
        """Test modified distributive law with infinities."""
        a = IEAElement.real(2.0)
        pos_inf = IEAElement.pos_infinity()
        neg_inf = IEAElement.neg_infinity()
        
        # a(∞ - ∞) should give I
        inf_diff = IEAOperations.subtract(pos_inf, neg_inf)
        result = IEAOperations.multiply(a, inf_diff)
        
        self.assertTrue(result.is_indeterminate())
    
    def test_modified_distributive_function(self):
        """Test the modified_distributive helper function."""
        a = IEAElement.real(2.0)
        b = IEAElement.real(3.0)
        c = IEAElement.real(4.0)
        
        left, right = IEAOperations.modified_distributive(a, b, c, lambda_coeff=0.0)
        
        # For reals, both sides should be equal
        self.assertTrue(left.is_real())
        self.assertTrue(right.is_real())
        self.assertAlmostEqual(left.value, right.value)


class TestIEAAxiomsVerification(unittest.TestCase):
    """Test axiom verification functions."""
    
    def test_verify_extended_division(self):
        """Test extended division axiom verification."""
        self.assertTrue(IEAAxioms.verify_extended_division())
    
    def test_verify_I_not_zero(self):
        """Test I ≠ 0 axiom verification."""
        self.assertTrue(IEAAxioms.verify_I_not_zero())
    
    def test_verify_absorption_addition(self):
        """Test absorption under addition axiom verification."""
        self.assertTrue(IEAAxioms.verify_absorption_addition())
    
    def test_verify_absorption_multiplication(self):
        """Test absorption under multiplication axiom verification."""
        self.assertTrue(IEAAxioms.verify_absorption_multiplication())
    
    def test_verify_zero_times_I(self):
        """Test 0 · I = 0 axiom verification."""
        self.assertTrue(IEAAxioms.verify_zero_times_I())
    
    def test_verify_no_inverse_for_I(self):
        """Test I has no inverse axiom verification."""
        self.assertTrue(IEAAxioms.verify_no_inverse_for_I())
    
    def test_verify_infinity_minus_infinity(self):
        """Test ∞ - ∞ = I axiom verification."""
        self.assertTrue(IEAAxioms.verify_infinity_minus_infinity())
    
    def test_verify_collapse_contradiction(self):
        """Test collapse contradiction axiom verification."""
        self.assertTrue(IEAAxioms.verify_collapse_contradiction())


class TestFundamentalAxioms(unittest.TestCase):
    """Test the 5 fundamental axioms of the IEA."""
    
    def test_axiom_A1(self):
        """Test Axiom A1: Extended Division."""
        result = IEAFundamentalAxioms.verify_axiom_A1()
        self.assertTrue(result["all_passed"], 
                       f"Axiom A1 verification failed: {result}")
    
    def test_axiom_A2(self):
        """Test Axiom A2: Absorption Properties."""
        result = IEAFundamentalAxioms.verify_axiom_A2()
        self.assertTrue(result["all_passed"],
                       f"Axiom A2 verification failed: {result}")
    
    def test_axiom_A3(self):
        """Test Axiom A3: Modified Distributivity."""
        result = IEAFundamentalAxioms.verify_axiom_A3()
        self.assertTrue(result["all_passed"],
                       f"Axiom A3 verification failed: {result}")
    
    def test_axiom_A4(self):
        """Test Axiom A4: Nonexistence of Inverses for I."""
        result = IEAFundamentalAxioms.verify_axiom_A4()
        self.assertTrue(result["all_passed"],
                       f"Axiom A4 verification failed: {result}")
    
    def test_axiom_A5(self):
        """Test Axiom A5: Preservation of Non-Triviality."""
        result = IEAFundamentalAxioms.verify_axiom_A5()
        self.assertTrue(result["all_passed"],
                       f"Axiom A5 verification failed: {result}")
    
    def test_all_axioms(self):
        """Test verification of all fundamental axioms."""
        result = IEAFundamentalAxioms.verify_all_axioms()
        self.assertTrue(result["all_axioms_verified"],
                       f"Not all axioms verified: {result}")


class TestFieldAxiomFailures(unittest.TestCase):
    """Test demonstrations of field axiom failures."""
    
    def test_multiplicative_inverse_failure(self):
        """Test demonstration of multiplicative inverse failure."""
        result = FieldAxiomFailures.test_multiplicative_inverse_failure()
        self.assertIn("failure", result)
        self.assertEqual(result["conclusion"], 
                        "Field axiom FAILS: I ≠ 0 but has no inverse")
    
    def test_distributivity_failure(self):
        """Test demonstration of distributivity failure."""
        result = FieldAxiomFailures.test_distributivity_failure()
        self.assertIn("failure", result)
        self.assertIn("Distributive law requires modification", result["conclusion"])


class TestCollapseContradiction(unittest.TestCase):
    """Test the collapse contradiction: I = 0 → 1 = 0."""
    
    def test_I_not_zero_prevents_collapse(self):
        """Test that I ≠ 0 prevents the collapse."""
        I = IEAElement.I()
        zero = IEAElement.zero()
        self.assertNotEqual(I, zero)
    
    def test_if_I_were_zero_then_one_div_zero_is_zero(self):
        """
        Demonstrate the collapse logic:
        If I = 0, then 1/0 = I = 0.
        But 1/0 = I ≠ 0, so the system doesn't collapse.
        """
        one = IEAElement.one()
        zero = IEAElement.zero()
        one_div_zero = IEAOperations.divide(one, zero)
        
        # 1/0 = I
        self.assertTrue(one_div_zero.is_indeterminate())
        
        # I ≠ 0 (prevents collapse)
        self.assertNotEqual(one_div_zero, zero)
    
    def test_collapse_would_give_one_equals_zero(self):
        """
        Verify the logical chain:
        If I = 0, then 1 = 0·0 = 0 (contradiction).
        
        We test that this doesn't happen because I ≠ 0.
        """
        one = IEAElement.one()
        zero = IEAElement.zero()
        
        # These should NOT be equal
        self.assertNotEqual(one, zero)
        
        # 1/0 = I, not 0
        one_div_zero = IEAOperations.divide(one, zero)
        self.assertNotEqual(one_div_zero, zero)


def run_all_tests():
    """Run all test suites and print results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestIEATypes))
    suite.addTests(loader.loadTestsFromTestCase(TestIEAOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestMultiplicativeInverse))
    suite.addTests(loader.loadTestsFromTestCase(TestModifiedDistributive))
    suite.addTests(loader.loadTestsFromTestCase(TestIEAAxiomsVerification))
    suite.addTests(loader.loadTestsFromTestCase(TestFundamentalAxioms))
    suite.addTests(loader.loadTestsFromTestCase(TestFieldAxiomFailures))
    suite.addTests(loader.loadTestsFromTestCase(TestCollapseContradiction))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
