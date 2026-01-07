"""
Test suite for field axiom verification

Tests the computational verification of field axioms for the Theory of I.
"""

import unittest
from field_axioms import (
    ExtendedReal, ElementType, real, add, mul, sub, div,
    ZERO, ONE, I, J, FieldAxiomVerifier
)


class TestExtendedReal(unittest.TestCase):
    """Tests for ExtendedReal class"""
    
    def test_real_creation(self):
        """Test creating real elements"""
        r = real(5)
        self.assertEqual(r.type, ElementType.REAL)
        self.assertEqual(r.value, 5)
    
    def test_special_elements(self):
        """Test special elements"""
        self.assertEqual(ZERO.type, ElementType.REAL)
        self.assertEqual(ZERO.value, 0.0)
        self.assertEqual(ONE.type, ElementType.REAL)
        self.assertEqual(ONE.value, 1.0)
        self.assertEqual(I.type, ElementType.I)
        self.assertEqual(J.type, ElementType.J)
    
    def test_equality(self):
        """Test element equality"""
        self.assertEqual(real(5), real(5))
        self.assertEqual(I, I)
        self.assertNotEqual(I, J)
        self.assertNotEqual(I, ZERO)
        self.assertNotEqual(I, ONE)


class TestOperations(unittest.TestCase):
    """Tests for algebraic operations"""
    
    def test_real_addition(self):
        """Test addition of real numbers"""
        result = add(real(2), real(3))
        self.assertEqual(result, real(5))
    
    def test_real_multiplication(self):
        """Test multiplication of real numbers"""
        result = mul(real(2), real(3))
        self.assertEqual(result, real(6))
    
    def test_real_subtraction(self):
        """Test subtraction of real numbers"""
        result = sub(real(5), real(3))
        self.assertEqual(result, real(2))
    
    def test_real_division(self):
        """Test division of real numbers"""
        result = div(real(6), real(3))
        self.assertEqual(result, real(2))
    
    def test_I_addition(self):
        """Test I addition properties"""
        self.assertEqual(add(I, I), I)
        self.assertEqual(add(I, real(5)), I)
        self.assertEqual(add(real(5), I), I)
        self.assertEqual(add(I, ZERO), I)
    
    def test_I_multiplication(self):
        """Test I multiplication properties"""
        self.assertEqual(mul(I, I), I)
        self.assertEqual(mul(I, real(5)), I)
        self.assertEqual(mul(real(5), I), I)
        self.assertEqual(mul(I, ONE), I)
        # Special case: 0 × I = 0
        self.assertEqual(mul(ZERO, I), ZERO)
        self.assertEqual(mul(I, ZERO), ZERO)
    
    def test_I_subtraction(self):
        """Test I subtraction properties"""
        self.assertEqual(sub(I, I), I)
        self.assertEqual(sub(I, real(5)), I)
        self.assertEqual(sub(real(5), I), I)
    
    def test_I_division(self):
        """Test I division properties"""
        self.assertEqual(div(I, I), I)
        self.assertEqual(div(real(5), I), ZERO)
        self.assertEqual(div(I, real(5)), I)
    
    def test_division_by_zero(self):
        """Test division by zero yields I"""
        self.assertEqual(div(real(1), ZERO), I)
        self.assertEqual(div(real(5), ZERO), I)
        self.assertEqual(div(ZERO, ZERO), I)


class TestFieldAxioms(unittest.TestCase):
    """Tests for field axiom verification"""
    
    def setUp(self):
        """Set up verifier"""
        self.verifier = FieldAxiomVerifier()
    
    def test_associativity_addition(self):
        """Test associativity of addition"""
        passes, _ = self.verifier.verify_axiom_1_add_associativity()
        self.assertTrue(passes)
    
    def test_commutativity_addition(self):
        """Test commutativity of addition"""
        passes, _ = self.verifier.verify_axiom_2_add_commutativity()
        self.assertTrue(passes)
    
    def test_additive_identity(self):
        """Test additive identity"""
        passes, _ = self.verifier.verify_axiom_3_add_identity()
        self.assertTrue(passes)
    
    def test_additive_inverse(self):
        """Test additive inverse - should FAIL"""
        passes, details = self.verifier.verify_axiom_4_add_inverse()
        # Axiom should fail because I has no inverse
        self.assertFalse(passes)
        self.assertIn("AXIOM FAILS", details)
    
    def test_associativity_multiplication(self):
        """Test associativity of multiplication"""
        passes, _ = self.verifier.verify_axiom_5_mul_associativity()
        self.assertTrue(passes)
    
    def test_commutativity_multiplication(self):
        """Test commutativity of multiplication"""
        passes, _ = self.verifier.verify_axiom_6_mul_commutativity()
        self.assertTrue(passes)
    
    def test_multiplicative_identity(self):
        """Test multiplicative identity"""
        passes, _ = self.verifier.verify_axiom_7_mul_identity()
        self.assertTrue(passes)
    
    def test_multiplicative_inverse(self):
        """Test multiplicative inverse - should FAIL"""
        passes, details = self.verifier.verify_axiom_8_mul_inverse()
        # Axiom should fail because I has no inverse
        self.assertFalse(passes)
        self.assertIn("AXIOM FAILS", details)
    
    def test_distributivity(self):
        """Test distributivity"""
        passes, _ = self.verifier.verify_axiom_9_distributivity()
        self.assertTrue(passes)
    
    def test_nontriviality(self):
        """Test non-triviality"""
        passes, _ = self.verifier.verify_axiom_10_nontriviality()
        self.assertTrue(passes)
    
    def test_full_verification(self):
        """Test full verification suite"""
        results = self.verifier.verify_all()
        
        # Should have 10 axioms
        self.assertEqual(len(results), 10)
        
        # Should pass 8/10 axioms
        passed = sum(1 for r in results.values() if r["passes"])
        self.assertEqual(passed, 8)
        
        # Should fail exactly 2 axioms
        failed = sum(1 for r in results.values() if not r["passes"])
        self.assertEqual(failed, 2)
        
        # Check which axioms failed
        failed_axioms = [name for name, r in results.items() if not r["passes"]]
        self.assertIn("Additive Inverse", failed_axioms)
        self.assertIn("Multiplicative Inverse", failed_axioms)


class TestSpecialProperties(unittest.TestCase):
    """Tests for special properties of I"""
    
    def test_I_idempotency(self):
        """Test I is idempotent"""
        self.assertEqual(add(I, I), I)  # I + I = I
        self.assertEqual(mul(I, I), I)  # I × I = I
    
    def test_I_distinctness(self):
        """Test I is distinct from 0 and 1"""
        self.assertNotEqual(I, ZERO)
        self.assertNotEqual(I, ONE)
        for r in [-10, -1, 0, 0.5, 1, 2, 10]:
            self.assertNotEqual(I, real(r))
    
    def test_zero_absorption(self):
        """Test 0 × I = 0"""
        self.assertEqual(mul(ZERO, I), ZERO)
        self.assertEqual(mul(I, ZERO), ZERO)
    
    def test_I_operations_complete(self):
        """Test all operations with I are defined"""
        # Addition
        self.assertIsInstance(add(I, I), ExtendedReal)
        self.assertIsInstance(add(I, real(5)), ExtendedReal)
        
        # Multiplication
        self.assertIsInstance(mul(I, I), ExtendedReal)
        self.assertIsInstance(mul(I, real(5)), ExtendedReal)
        
        # Subtraction
        self.assertIsInstance(sub(I, I), ExtendedReal)
        self.assertIsInstance(sub(I, real(5)), ExtendedReal)
        
        # Division
        self.assertIsInstance(div(I, I), ExtendedReal)
        self.assertIsInstance(div(I, real(5)), ExtendedReal)


class TestDivisionByZero(unittest.TestCase):
    """Tests specifically for division by zero"""
    
    def test_division_by_zero_yields_I(self):
        """Test a/0 = I for all a"""
        test_values = [0, 1, -1, 2, -2, 0.5, 10, 100]
        for val in test_values:
            result = div(real(val), ZERO)
            self.assertEqual(result, I, f"Failed for {val}/0")
    
    def test_zero_divided_by_zero(self):
        """Test 0/0 = I"""
        result = div(ZERO, ZERO)
        self.assertEqual(result, I)
    
    def test_I_divided_by_zero(self):
        """Test I/0 = I"""
        result = div(I, ZERO)
        self.assertEqual(result, I)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
