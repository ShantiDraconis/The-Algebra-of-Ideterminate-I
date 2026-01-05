"""
Test Suite for I-Algebra Implementation
Comprehensive unit tests for the Python I-Algebra framework
"""

import unittest
import numpy as np
from ialgebra import (
    ExtendedReal, eadd, esub, emul, ediv,
    verify_indeterminate_invariance, iexp,
    ICalculus, IPhysics, CardinalArithmetic
)


class TestExtendedReal(unittest.TestCase):
    """Test ExtendedReal class"""
    
    def setUp(self):
        self.I = ExtendedReal.I()
        self.J = ExtendedReal.J()
        self.x = ExtendedReal(3.14)
        self.y = ExtendedReal(2.71)
    
    def test_construction(self):
        """Test basic construction"""
        self.assertTrue(self.I.is_I())
        self.assertTrue(self.J.is_J())
        self.assertTrue(self.x.is_real())
        self.assertAlmostEqual(self.x.value, 3.14)
    
    def test_equality(self):
        """Test equality comparison"""
        x1 = ExtendedReal(5.0)
        x2 = ExtendedReal(5.0)
        self.assertEqual(x1, x2)
        
        I1 = ExtendedReal.I()
        I2 = ExtendedReal.I()
        self.assertEqual(I1, I2)


class TestExtendedOperations(unittest.TestCase):
    """Test extended operations"""
    
    def setUp(self):
        self.I = ExtendedReal.I()
        self.J = ExtendedReal.J()
    
    def test_self_subtraction(self):
        """Test κ ⊖ κ = I"""
        x = ExtendedReal(42.0)
        result = esub(x, x)
        self.assertTrue(result.is_I())
        
        result2 = esub(self.I, self.I)
        self.assertTrue(result2.is_I())
    
    def test_addition_zero(self):
        """Test addition yielding zero gives I"""
        a = ExtendedReal(5.0)
        b = ExtendedReal(-5.0)
        result = eadd(a, b)
        self.assertTrue(result.is_I())
    
    def test_multiplication_zero(self):
        """Test multiplication yielding zero gives I"""
        a = ExtendedReal(5.0)
        b = ExtendedReal(0.0)
        result = emul(a, b)
        self.assertTrue(result.is_I())
    
    def test_division_by_zero(self):
        """Test division by zero gives I"""
        a = ExtendedReal(5.0)
        b = ExtendedReal(0.0)
        result = ediv(a, b)
        self.assertTrue(result.is_I())
    
    def test_normal_operations(self):
        """Test normal arithmetic"""
        a = ExtendedReal(3.0)
        b = ExtendedReal(4.0)
        
        sum_result = eadd(a, b)
        self.assertTrue(sum_result.is_real())
        self.assertAlmostEqual(sum_result.value, 7.0)
        
        diff_result = esub(ExtendedReal(10.0), b)
        self.assertTrue(diff_result.is_real())
        self.assertAlmostEqual(diff_result.value, 6.0)
        
        prod_result = emul(a, b)
        self.assertTrue(prod_result.is_real())
        self.assertAlmostEqual(prod_result.value, 12.0)
        
        quot_result = ediv(ExtendedReal(12.0), a)
        self.assertTrue(quot_result.is_real())
        self.assertAlmostEqual(quot_result.value, 4.0)


class TestIndeterminateInvariance(unittest.TestCase):
    """Test Theorem 14.1: Indeterminate Invariance"""
    
    def test_invariance_real(self):
        """Test invariance with real numbers"""
        x = ExtendedReal(7.5)
        self.assertTrue(verify_indeterminate_invariance(x))
    
    def test_invariance_I(self):
        """Test invariance with I"""
        I = ExtendedReal.I()
        self.assertTrue(verify_indeterminate_invariance(I))
    
    def test_invariance_J(self):
        """Test invariance with J"""
        J = ExtendedReal.J()
        self.assertTrue(verify_indeterminate_invariance(J))
    
    def test_i_absorbing_add(self):
        """Test I ⊕ x = I"""
        I = ExtendedReal.I()
        x = ExtendedReal(10.0)
        result = eadd(I, x)
        self.assertTrue(result.is_I())
        
        result2 = eadd(x, I)
        self.assertTrue(result2.is_I())
    
    def test_i_absorbing_mul(self):
        """Test I ⊗ x = x ⊗ I = I"""
        I = ExtendedReal.I()
        x = ExtendedReal(10.0)
        result = emul(I, x)
        self.assertTrue(result.is_I())
        
        result2 = emul(x, I)
        self.assertTrue(result2.is_I())


class TestIExponential(unittest.TestCase):
    """Test I-exponential function"""
    
    def test_iexp_real(self):
        """Test exponential with real argument"""
        x = ExtendedReal(1.0)
        result = iexp(x)
        self.assertTrue(result.is_real())
        self.assertAlmostEqual(result.value, np.e, places=5)
    
    def test_iexp_zero(self):
        """Test exponential at zero"""
        x = ExtendedReal(0.0)
        result = iexp(x)
        self.assertTrue(result.is_real())
        self.assertAlmostEqual(result.value, 1.0, places=5)
    
    def test_iexp_I(self):
        """Test exponential with I"""
        I = ExtendedReal.I()
        result = iexp(I)
        self.assertTrue(result.is_I())
    
    def test_iexp_J(self):
        """Test exponential with J"""
        J = ExtendedReal.J()
        result = iexp(J)
        self.assertTrue(result.is_J())


class TestICalculus(unittest.TestCase):
    """Test I-calculus operations"""
    
    def test_ideriv_polynomial(self):
        """Test derivative of polynomial"""
        def f(x):
            if x.is_real():
                return ExtendedReal(x.value ** 2)
            return ExtendedReal.I()
        
        x = ExtendedReal(3.0)
        deriv = ICalculus.ideriv(f, x, epsilon=1e-6)
        
        # d(x²)/dx = 2x, at x=3 should be 6
        self.assertTrue(deriv.is_real())
        self.assertAlmostEqual(deriv.value, 6.0, places=3)
    
    def test_ideriv_constant(self):
        """Test derivative of constant"""
        def f(x):
            return ExtendedReal(5.0)
        
        x = ExtendedReal(2.0)
        deriv = ICalculus.ideriv(f, x)
        
        # Derivative of constant should be ~0
        self.assertTrue(deriv.is_real())
        self.assertAlmostEqual(deriv.value, 0.0, places=3)
    
    def test_iintegral_constant(self):
        """Test integration of constant"""
        def f(x):
            return ExtendedReal(2.0)
        
        a = ExtendedReal(0.0)
        b = ExtendedReal(5.0)
        result = ICalculus.iintegral(f, a, b, n=1000)
        
        # Integral of 2 from 0 to 5 should be 10
        self.assertTrue(result.is_real())
        self.assertAlmostEqual(result.value, 10.0, places=2)


class TestCardinalArithmetic(unittest.TestCase):
    """Test cardinal arithmetic"""
    
    def test_axiom_i1(self):
        """Test Axiom I1: κ ⊖ κ = I"""
        kappa = "arbitrary_cardinal"
        result = CardinalArithmetic.cardinal_subtraction(kappa)
        self.assertTrue(result.is_I())


class TestPhysics(unittest.TestCase):
    """Test physical applications"""
    
    def test_tov_equation(self):
        """Test modified TOV equation"""
        r = 1000.0  # meters
        rho = 1e17  # kg/m³
        P = 1e32    # Pa
        M = 2e30    # kg
        R_total = 10000.0
        
        result = IPhysics.modified_tov_pressure(r, rho, P, M, R_total)
        # Just test it returns an ExtendedReal
        self.assertIsInstance(result, ExtendedReal)


class TestOperatorOverloading(unittest.TestCase):
    """Test operator overloading"""
    
    def test_add_operator(self):
        """Test + operator"""
        a = ExtendedReal(3.0)
        b = ExtendedReal(4.0)
        result = a + b
        self.assertTrue(result.is_real())
        self.assertAlmostEqual(result.value, 7.0)
    
    def test_sub_operator(self):
        """Test - operator"""
        a = ExtendedReal(5.0)
        result = a - a
        self.assertTrue(result.is_I())
    
    def test_mul_operator(self):
        """Test * operator"""
        a = ExtendedReal(3.0)
        b = ExtendedReal(4.0)
        result = a * b
        self.assertTrue(result.is_real())
        self.assertAlmostEqual(result.value, 12.0)
    
    def test_div_operator(self):
        """Test / operator"""
        a = ExtendedReal(12.0)
        b = ExtendedReal(4.0)
        result = a / b
        self.assertTrue(result.is_real())
        self.assertAlmostEqual(result.value, 3.0)
    
    def test_div_by_zero(self):
        """Test division by zero with operator"""
        a = ExtendedReal(5.0)
        b = ExtendedReal(0.0)
        result = a / b
        self.assertTrue(result.is_I())


def run_all_tests():
    """Run all test suites"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestExtendedReal))
    suite.addTests(loader.loadTestsFromTestCase(TestExtendedOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestIndeterminateInvariance))
    suite.addTests(loader.loadTestsFromTestCase(TestIExponential))
    suite.addTests(loader.loadTestsFromTestCase(TestICalculus))
    suite.addTests(loader.loadTestsFromTestCase(TestCardinalArithmetic))
    suite.addTests(loader.loadTestsFromTestCase(TestPhysics))
    suite.addTests(loader.loadTestsFromTestCase(TestOperatorOverloading))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    result = run_all_tests()
    
    # Print summary
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    # Exit with appropriate code
    exit(0 if result.wasSuccessful() else 1)
