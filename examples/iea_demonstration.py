"""
Demonstration of the Indeterminate Extended Algebra (IEA)

This script demonstrates the key features and axioms of the IEA,
showing how it handles division by zero and related singularities.

Author: IEA Implementation  
Date: 2026-01-05
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ialgebra import IEAElement, IEAOperations, IEAFundamentalAxioms, FieldAxiomFailures
import json


def print_header(title: str):
    """Print a formatted header."""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def demonstrate_basic_elements():
    """Demonstrate creation and properties of IEA elements."""
    print_header("1. Basic IEA Elements")
    
    # Create elements
    zero = IEAElement.zero()
    one = IEAElement.one()
    I = IEAElement.I()
    J = IEAElement.J()
    pos_inf = IEAElement.pos_infinity()
    neg_inf = IEAElement.neg_infinity()
    
    print("Basic elements:")
    print(f"  Zero (0):            {zero}")
    print(f"  One (1):             {one}")
    print(f"  Indeterminate (I):   {I}")
    print(f"  Imaginary Sing. (J): {J}")
    print(f"  Positive Infinity:   {pos_inf}")
    print(f"  Negative Infinity:   {neg_inf}")
    
    print("\nKey property:")
    print(f"  I ≠ 0: {I != zero} (prevents collapse)")


def demonstrate_division_by_zero():
    """Demonstrate division by zero in the IEA."""
    print_header("2. Division by Zero")
    
    zero = IEAElement.zero()
    
    test_values = [1.0, 2.0, 5.0, -3.0, 100.0]
    
    print("In the IEA, x/0 = I for all x ≠ 0:")
    for val in test_values:
        x = IEAElement.real(val)
        result = IEAOperations.divide(x, zero)
        print(f"  {val}/0 = {result}")
    
    print("\nSpecial case:")
    result = IEAOperations.divide(zero, zero)
    print(f"  0/0 = {result}")


def demonstrate_absorption():
    """Demonstrate absorption properties."""
    print_header("3. Absorption Properties")
    
    I = IEAElement.I()
    test_values = [0.0, 1.0, 5.0, -3.0]
    
    print("Addition absorption (x + I = I):")
    for val in test_values:
        x = IEAElement.real(val)
        result = IEAOperations.add(x, I)
        print(f"  {val} + I = {result}")
    
    print("\nMultiplication absorption (x · I = I for x ≠ 0):")
    for val in [1.0, 5.0, -3.0]:
        x = IEAElement.real(val)
        result = IEAOperations.multiply(x, I)
        print(f"  {val} · I = {result}")
    
    print("\nSpecial case (0 · I = 0):")
    zero = IEAElement.zero()
    result = IEAOperations.multiply(zero, I)
    print(f"  0 · I = {result}")


def demonstrate_infinity_operations():
    """Demonstrate operations involving infinities."""
    print_header("4. Infinity Operations")
    
    pos_inf = IEAElement.pos_infinity()
    neg_inf = IEAElement.neg_infinity()
    
    print("Key property: ∞ - ∞ = I")
    result = IEAOperations.subtract(pos_inf, pos_inf)
    print(f"  +∞ - (+∞) = {result}")
    
    result = IEAOperations.subtract(neg_inf, neg_inf)
    print(f"  -∞ - (-∞) = {result}")
    
    print("\nMixed operations:")
    result = IEAOperations.add(pos_inf, neg_inf)
    print(f"  +∞ + (-∞) = {result}")


def demonstrate_no_inverse():
    """Demonstrate that I has no multiplicative inverse."""
    print_header("5. Failure of Multiplicative Inverse")
    
    I = IEAElement.I()
    zero = IEAElement.zero()
    
    print("In a field, every non-zero element has an inverse.")
    print("In the IEA, I ≠ 0 but has no inverse:")
    
    print(f"\n  I ≠ 0: {I != zero}")
    print(f"  I has inverse: {IEAOperations.has_multiplicative_inverse(I)}")
    print(f"  Attempt to compute I⁻¹: {IEAOperations.attempt_inverse(I)}")
    
    print("\nWhy? Because I · I = I (not 1):")
    I_squared = IEAOperations.multiply(I, I)
    print(f"  I · I = {I_squared}")


def demonstrate_modified_distributive():
    """Demonstrate the modified distributive law."""
    print_header("6. Modified Distributive Law")
    
    print("Standard algebra: a(b + c) = ab + ac")
    print("IEA: a(b + c) = ab + ac + λJ (correction term needed)")
    
    # Case 1: Standard distributivity for reals
    a = IEAElement.real(2.0)
    b = IEAElement.real(3.0)
    c = IEAElement.real(4.0)
    
    left = IEAOperations.multiply(a, IEAOperations.add(b, c))
    right = IEAOperations.add(
        IEAOperations.multiply(a, b),
        IEAOperations.multiply(a, c)
    )
    
    print("\nFor real numbers (λ = 0):")
    print(f"  2(3 + 4) = {left}")
    print(f"  2·3 + 2·4 = {right}")
    print(f"  Equal: {left.value == right.value if left.is_real() and right.is_real() else False}")
    
    # Case 2: Failure with infinities
    pos_inf = IEAElement.pos_infinity()
    neg_inf = IEAElement.neg_infinity()
    
    print("\nFor infinities (requires correction):")
    print(f"  a(∞ - ∞) = a·I = I")
    left = IEAOperations.multiply(a, IEAOperations.subtract(pos_inf, neg_inf))
    print(f"  Result: {left}")


def demonstrate_collapse_prevention():
    """Demonstrate how I ≠ 0 prevents system collapse."""
    print_header("7. Prevention of System Collapse")
    
    print("The Collapse Contradiction:")
    print("  If I = 0, then:")
    print("    1. x/0 = I = 0 for all x")
    print("    2. Specifically, 1/0 = 0")
    print("    3. Multiplying both sides by 0: 1 = 0")
    print("    4. CONTRADICTION!")
    
    I = IEAElement.I()
    zero = IEAElement.zero()
    one = IEAElement.one()
    
    print("\nIn the IEA:")
    print(f"  I ≠ 0: {I != zero}")
    one_div_zero = IEAOperations.divide(one, zero)
    print(f"  1/0 = I: {one_div_zero}")
    print(f"  1/0 ≠ 0: {one_div_zero != zero}")
    print("\n  Therefore, the system does NOT collapse!")


def verify_all_axioms():
    """Verify all fundamental axioms."""
    print_header("8. Verification of Fundamental Axioms")
    
    results = IEAFundamentalAxioms.verify_all_axioms()
    
    print(f"Title: {results['title']}\n")
    
    for axiom_result in results['axioms']:
        axiom_id = axiom_result['axiom']
        name = axiom_result['name']
        passed = axiom_result['all_passed']
        
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"Axiom {axiom_id}: {name} ... {status}")
        
        if not passed:
            print("  Failed tests:")
            for test in axiom_result['tests']:
                if not test['passed']:
                    print(f"    - {test['description']}")
    
    print(f"\nOverall: {'✓ All axioms verified' if results['all_axioms_verified'] else '✗ Some axioms failed'}")


def demonstrate_field_axiom_failures():
    """Demonstrate where classical field axioms fail."""
    print_header("9. Field Axiom Failures")
    
    results = FieldAxiomFailures.test_all_failures()
    
    print(f"{results['title']}\n")
    
    for failure in results['failures']:
        print(f"Failure: {failure['failure']}")
        print(f"Field Axiom: {failure['field_axiom']}")
        print(f"Conclusion: {failure['conclusion']}")
        print()


def main():
    """Run all demonstrations."""
    print("\n" + "█"*80)
    print("█" + " "*78 + "█")
    print("█" + "  Demonstration of the Indeterminate Extended Algebra (IEA)".center(78) + "█")
    print("█" + " "*78 + "█")
    print("█"*80)
    
    demonstrate_basic_elements()
    demonstrate_division_by_zero()
    demonstrate_absorption()
    demonstrate_infinity_operations()
    demonstrate_no_inverse()
    demonstrate_modified_distributive()
    demonstrate_collapse_prevention()
    verify_all_axioms()
    demonstrate_field_axiom_failures()
    
    print("\n" + "="*80)
    print("  Demonstration Complete")
    print("="*80 + "\n")
    
    print("Summary:")
    print("  The IEA is NOT a field, but a consistent algebraic structure that:")
    print("    • Handles division by zero: x/0 = I")
    print("    • Prevents collapse: I ≠ 0")
    print("    • Has no inverse for I")
    print("    • Uses modified distributivity: a(b+c) = ab + ac + λJ")
    print("    • Provides a framework for singularities and indeterminate forms")
    print()


if __name__ == "__main__":
    main()
