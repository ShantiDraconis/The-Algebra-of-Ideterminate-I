"""
Test suite for I-Algebra implementation
Verifies all 15 postulates and extended properties
"""

import sys
from python_implementation import ExtendedReal, WheelStructure, IndeterminateType


class TestRunner:
    """Simple test runner for I-Algebra tests"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests = []
    
    def assert_equal(self, actual, expected, test_name):
        """Assert two values are equal"""
        if actual == expected:
            self.passed += 1
            self.tests.append((test_name, True, None))
            print(f"✓ {test_name}")
        else:
            self.failed += 1
            msg = f"Expected {expected}, got {actual}"
            self.tests.append((test_name, False, msg))
            print(f"✗ {test_name}: {msg}")
    
    def assert_true(self, condition, test_name):
        """Assert condition is true"""
        self.assert_equal(condition, True, test_name)
    
    def assert_false(self, condition, test_name):
        """Assert condition is false"""
        self.assert_equal(condition, False, test_name)
    
    def report(self):
        """Print test summary"""
        total = self.passed + self.failed
        print("\n" + "=" * 60)
        print(f"TEST SUMMARY: {self.passed}/{total} passed")
        if self.failed > 0:
            print(f"FAILED: {self.failed} tests failed")
            sys.exit(1)
        else:
            print("SUCCESS: All tests passed!")
            sys.exit(0)


def test_postulates(runner):
    """Test all 15 fundamental postulates"""
    print("\n" + "=" * 60)
    print("TESTING FUNDAMENTAL POSTULATES")
    print("=" * 60 + "\n")
    
    I = ExtendedReal.I()
    J = ExtendedReal.J()
    zero = ExtendedReal.zero()
    one = ExtendedReal.one()
    
    # Postulate 1: Existence
    runner.assert_true(I is not None, "Postulate 1: I exists")
    
    # Postulate 2: Distinctness
    runner.assert_true(I != zero, "Postulate 2: I ≠ 0")
    runner.assert_true(I != one, "Postulate 2: I ≠ 1")
    runner.assert_true(I != ExtendedReal(5), "Postulate 2: I ≠ 5")
    
    # Postulate 3: Self-consistency
    runner.assert_equal(I + I, I, "Postulate 3: I + I = I")
    runner.assert_equal(I * I, I, "Postulate 3: I × I = I")
    
    # Postulate 4: Zero absorption
    runner.assert_equal(zero * I, zero, "Postulate 4: 0 × I = 0")
    runner.assert_equal(I * zero, zero, "Postulate 4: I × 0 = 0")
    
    # Postulate 5: Division by zero
    runner.assert_equal(ExtendedReal(5) / zero, I, "Postulate 5: 5/0 = I")
    runner.assert_equal(ExtendedReal(-3) / zero, I, "Postulate 5: -3/0 = I")
    
    # Postulate 6: I self-division
    runner.assert_equal(I / I, I, "Postulate 6: I/I = I")
    
    # Postulate 7: Subtraction indeterminacy
    runner.assert_equal(I - I, I, "Postulate 7: I - I = I")
    
    # Postulate 8: Dual existence
    runner.assert_true(J is not None, "Postulate 8: J exists")
    runner.assert_true(J != I, "Postulate 8: J ≠ I")
    
    # Postulate 9: Closure (tested implicitly by operations working)
    result1 = ExtendedReal(3) + ExtendedReal(4)
    result2 = ExtendedReal(3) * ExtendedReal(4)
    runner.assert_true(result1 is not None, "Postulate 9: Addition closure")
    runner.assert_true(result2 is not None, "Postulate 9: Multiplication closure")
    
    # Postulate 10: Real preservation
    runner.assert_equal(ExtendedReal(3) + ExtendedReal(4), ExtendedReal(7), 
                       "Postulate 10: Real addition preserved")
    runner.assert_equal(ExtendedReal(3) * ExtendedReal(4), ExtendedReal(12),
                       "Postulate 10: Real multiplication preserved")
    
    # Postulate 11: Real associativity
    a, b, c = ExtendedReal(2), ExtendedReal(3), ExtendedReal(4)
    runner.assert_equal((a + b) + c, a + (b + c), "Postulate 11: Real associativity")
    
    # Postulate 12: Real commutativity
    runner.assert_equal(ExtendedReal(3) + ExtendedReal(5), ExtendedReal(5) + ExtendedReal(3),
                       "Postulate 12: Real addition commutativity")
    runner.assert_equal(ExtendedReal(3) * ExtendedReal(5), ExtendedReal(5) * ExtendedReal(3),
                       "Postulate 12: Real multiplication commutativity")
    
    # Postulate 13: Additive identity
    runner.assert_equal(ExtendedReal(5) + zero, ExtendedReal(5),
                       "Postulate 13: Additive identity")
    
    # Postulate 14: Multiplicative identity
    runner.assert_equal(ExtendedReal(5) * one, ExtendedReal(5),
                       "Postulate 14: Multiplicative identity")
    
    # Postulate 15: Non-triviality
    runner.assert_true(I != zero, "Postulate 15: I ≠ 0")
    runner.assert_true(I != one, "Postulate 15: I ≠ 1")


def test_wheel_structure(runner):
    """Test wheel of fractions"""
    print("\n" + "=" * 60)
    print("TESTING WHEEL STRUCTURE")
    print("=" * 60 + "\n")
    
    zero = ExtendedReal.zero()
    I = ExtendedReal.I()
    
    # Basic wheel operations
    w1 = WheelStructure(ExtendedReal(5), zero)
    runner.assert_equal(w1.evaluate(), I, "Wheel: 5/0 = I")
    
    w2 = WheelStructure(zero, zero)
    runner.assert_equal(w2.evaluate(), I, "Wheel: 0/0 = I")
    
    w3 = WheelStructure(I, I)
    runner.assert_equal(w3.evaluate(), I, "Wheel: I/I = I")
    
    w4 = WheelStructure(ExtendedReal(10), ExtendedReal(2))
    runner.assert_equal(w4.evaluate(), ExtendedReal(5), "Wheel: 10/2 = 5")


def test_extended_operations(runner):
    """Test extended algebraic operations"""
    print("\n" + "=" * 60)
    print("TESTING EXTENDED OPERATIONS")
    print("=" * 60 + "\n")
    
    I = ExtendedReal.I()
    J = ExtendedReal.J()
    
    # Mixed I and J operations
    runner.assert_equal(I + J, I, "Mixed: I + J = I")
    runner.assert_equal(J + I, I, "Mixed: J + I = I")
    runner.assert_equal(I * J, I, "Mixed: I × J = I")
    runner.assert_equal(J * I, I, "Mixed: J × I = I")
    
    # J self-consistency
    runner.assert_equal(J + J, J, "J consistency: J + J = J")
    runner.assert_equal(J * J, J, "J consistency: J × J = J")
    
    # Iterated I operations
    result = I
    for _ in range(10):
        result = result + I
    runner.assert_equal(result, I, "Iterated: I + ... + I = I")
    
    result = I
    for _ in range(10):
        result = result * I
    runner.assert_equal(result, I, "Iterated: I × ... × I = I")


def test_context_resolution(runner):
    """Test context-dependent resolution"""
    print("\n" + "=" * 60)
    print("TESTING CONTEXT RESOLUTION")
    print("=" * 60 + "\n")
    
    I = ExtendedReal.I()
    zero = ExtendedReal.zero()
    one = ExtendedReal.one()
    
    # Context resolution
    runner.assert_equal(I.resolve_context(0), zero, "Context 0: I → 0")
    runner.assert_equal(I.resolve_context(1), one, "Context 1: I → 1")
    runner.assert_equal(I.resolve_context(2), I, "Context 2: I → I")
    runner.assert_equal(I.resolve_context(99), I, "Context 99: I → I")
    
    # Real values unchanged
    runner.assert_equal(ExtendedReal(5).resolve_context(0), ExtendedReal(5),
                       "Context: Real values unchanged")


def test_physical_applications(runner):
    """Test physical interpretation examples"""
    print("\n" + "=" * 60)
    print("TESTING PHYSICAL APPLICATIONS")
    print("=" * 60 + "\n")
    
    I = ExtendedReal.I()
    zero = ExtendedReal.zero()
    
    # Black hole singularity
    g_00 = ExtendedReal(1) / zero
    runner.assert_equal(g_00, I, "Physics: Schwarzschild singularity → I")
    
    # Dark matter density at core
    rho = ExtendedReal(1e9) / (zero * zero)
    runner.assert_equal(rho, I, "Physics: Dark matter core density → I")
    
    # Quantum uncertainty
    uncertainty = I * I
    runner.assert_equal(uncertainty, I, "Physics: ΔxΔp = I")


def test_edge_cases(runner):
    """Test edge cases and boundary conditions"""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES")
    print("=" * 60 + "\n")
    
    I = ExtendedReal.I()
    J = ExtendedReal.J()
    zero = ExtendedReal.zero()
    one = ExtendedReal.one()
    
    # Very small numbers
    tiny = ExtendedReal(1e-100)
    runner.assert_equal(tiny / zero, I, "Edge: tiny/0 = I")
    runner.assert_equal(zero * tiny, zero, "Edge: 0 × tiny = 0")
    
    # Very large numbers
    huge = ExtendedReal(1e100)
    runner.assert_equal(huge / zero, I, "Edge: huge/0 = I")
    runner.assert_equal(zero * huge, zero, "Edge: 0 × huge = 0")
    
    # Negative numbers
    neg = ExtendedReal(-5)
    runner.assert_equal(neg / zero, I, "Edge: -5/0 = I")
    runner.assert_equal(zero * I, zero, "Edge: 0 × I = 0")
    
    # Chain operations
    result = ((I + ExtendedReal(5)) * ExtendedReal(2)) - I
    runner.assert_equal(result, I, "Edge: Complex chain with I")


def test_properties(runner):
    """Test algebraic properties"""
    print("\n" + "=" * 60)
    print("TESTING ALGEBRAIC PROPERTIES")
    print("=" * 60 + "\n")
    
    I = ExtendedReal.I()
    zero = ExtendedReal.zero()
    one = ExtendedReal.one()
    
    # I is absorbing for addition (except with zero in special cases)
    runner.assert_equal(ExtendedReal(5) + I, I, "Property: 5 + I = I")
    runner.assert_equal(I + ExtendedReal(5), I, "Property: I + 5 = I")
    
    # I is absorbing for multiplication (except zero)
    runner.assert_equal(ExtendedReal(5) * I, I, "Property: 5 × I = I")
    runner.assert_equal(I * ExtendedReal(5), I, "Property: I × 5 = I")
    
    # Zero special case
    runner.assert_equal(zero * I, zero, "Property: 0 × I = 0 (special)")
    
    # Division properties
    runner.assert_equal(I / ExtendedReal(5), I, "Property: I / 5 = I")
    runner.assert_equal(ExtendedReal(5) / I, zero, "Property: 5 / I = 0")


def main():
    """Run all tests"""
    print("=" * 60)
    print("I-ALGEBRA TEST SUITE")
    print("=" * 60)
    
    runner = TestRunner()
    
    # Run test suites
    test_postulates(runner)
    test_wheel_structure(runner)
    test_extended_operations(runner)
    test_context_resolution(runner)
    test_physical_applications(runner)
    test_edge_cases(runner)
    test_properties(runner)
    
    # Final report
    runner.report()


if __name__ == "__main__":
    main()
