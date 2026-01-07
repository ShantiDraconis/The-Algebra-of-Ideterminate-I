"""
Practical Examples: Using the Theory of I

This file demonstrates practical applications and computations
using the Theory of I implementation.
"""

from field_axioms import (
    ExtendedReal, ElementType, real, add, mul, sub, div,
    ZERO, ONE, I, J
)


def print_section(title):
    """Print a section header"""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def example_basic_operations():
    """Example 1: Basic operations with I"""
    print_section("Example 1: Basic Operations with I")
    
    print("\n1. Addition:")
    print(f"   I + I = {add(I, I)}")
    print(f"   I + 5 = {add(I, real(5))}")
    print(f"   5 + I = {add(real(5), I)}")
    print(f"   I + 0 = {add(I, ZERO)}")
    
    print("\n2. Multiplication:")
    print(f"   I × I = {mul(I, I)}")
    print(f"   I × 5 = {mul(I, real(5))}")
    print(f"   5 × I = {mul(real(5), I)}")
    print(f"   I × 0 = {mul(I, ZERO)}")  # Special: 0 × I = 0
    print(f"   I × 1 = {mul(I, ONE)}")
    
    print("\n3. Subtraction:")
    print(f"   I - I = {sub(I, I)}")  # Note: I - I = I (not 0!)
    print(f"   I - 5 = {sub(I, real(5))}")
    print(f"   5 - I = {sub(real(5), I)}")
    
    print("\n4. Division:")
    print(f"   I / I = {div(I, I)}")
    print(f"   I / 5 = {div(I, real(5))}")
    print(f"   5 / I = {div(real(5), I)}")
    print(f"   I / 0 = {div(I, ZERO)}")


def example_division_by_zero():
    """Example 2: Division by zero"""
    print_section("Example 2: Division by Zero")
    
    print("\nDivision of various numbers by zero:")
    test_values = [0, 1, -1, 2, -2, 0.5, 10, 100]
    
    for val in test_values:
        result = div(real(val), ZERO)
        print(f"   {val} / 0 = {result}")
    
    print("\nObservation: All divisions by zero yield I")
    print("This is the fundamental postulate: a/0 = I for all a")


def example_idempotency():
    """Example 3: Idempotency of I"""
    print_section("Example 3: Idempotency of I")
    
    print("\nI is idempotent under both addition and multiplication:")
    
    print("\nAdditive idempotency:")
    result = I
    for i in range(5):
        print(f"   Adding I {i+1} time(s): {result}")
        result = add(result, I)
    print(f"   Result: I + I + I + I + I = {result}")
    
    print("\nMultiplicative idempotency:")
    result = I
    for i in range(5):
        print(f"   Multiplying I {i+1} time(s): {result}")
        result = mul(result, I)
    print(f"   Result: I × I × I × I × I = {result}")


def example_no_inverses():
    """Example 4: I has no inverses"""
    print_section("Example 4: I Has No Inverses")
    
    print("\nSearching for additive inverse of I:")
    print("(Looking for x such that I + x = 0)")
    
    candidates = [ZERO, ONE, I, J, real(-1), real(1), real(2), real(-2)]
    found_add_inv = False
    
    for x in candidates:
        result = add(I, x)
        match = "✓ FOUND!" if result == ZERO else "✗"
        print(f"   I + {x} = {result}  {match}")
        if result == ZERO:
            found_add_inv = True
    
    print(f"\n   Conclusion: {'Found' if found_add_inv else 'No'} additive inverse exists")
    
    print("\nSearching for multiplicative inverse of I:")
    print("(Looking for x such that I × x = 1)")
    
    found_mul_inv = False
    
    for x in candidates:
        result = mul(I, x)
        match = "✓ FOUND!" if result == ONE else "✗"
        print(f"   I × {x} = {result}  {match}")
        if result == ONE:
            found_mul_inv = True
    
    print(f"\n   Conclusion: {'Found' if found_mul_inv else 'No'} multiplicative inverse exists")


def example_algebraic_properties():
    """Example 5: Testing algebraic properties"""
    print_section("Example 5: Algebraic Properties")
    
    print("\n1. Commutativity:")
    a, b = real(3), real(5)
    print(f"   {a} + {b} = {add(a, b)}")
    print(f"   {b} + {a} = {add(b, a)}")
    print(f"   Equal? {add(a, b) == add(b, a)}")
    
    print(f"\n   I + {a} = {add(I, a)}")
    print(f"   {a} + I = {add(a, I)}")
    print(f"   Equal? {add(I, a) == add(a, I)}")
    
    print("\n2. Associativity:")
    a, b, c = real(2), real(3), real(5)
    lhs = add(add(a, b), c)
    rhs = add(a, add(b, c))
    print(f"   ({a} + {b}) + {c} = {lhs}")
    print(f"   {a} + ({b} + {c}) = {rhs}")
    print(f"   Equal? {lhs == rhs}")
    
    print("\n3. Distributivity:")
    a, b, c = real(2), real(3), real(5)
    lhs = mul(a, add(b, c))
    rhs = add(mul(a, b), mul(a, c))
    print(f"   {a} × ({b} + {c}) = {lhs}")
    print(f"   ({a} × {b}) + ({a} × {c}) = {rhs}")
    print(f"   Equal? {lhs == rhs}")


def example_special_cases():
    """Example 6: Special cases and edge conditions"""
    print_section("Example 6: Special Cases")
    
    print("\n1. Zero absorption:")
    print(f"   0 × I = {mul(ZERO, I)}")
    print(f"   I × 0 = {mul(I, ZERO)}")
    print("   Note: 0 × I = 0 (not I!)")
    
    print("\n2. Identity elements:")
    print(f"   I + 0 = {add(I, ZERO)}")
    print(f"   I × 1 = {mul(I, ONE)}")
    print("   Note: Identities work normally with I")
    
    print("\n3. Self-operations:")
    print(f"   I - I = {sub(I, I)}")
    print(f"   I / I = {div(I, I)}")
    print("   Note: I - I = I and I / I = I (not 0 and 1!)")
    
    print("\n4. Mixed with J:")
    print(f"   I + J = {add(I, J)}")
    print(f"   I × J = {mul(I, J)}")
    print("   Note: I dominates in operations with J")


def example_real_world_calculation():
    """Example 7: Real-world-style calculation"""
    print_section("Example 7: Symbolic Calculation")
    
    print("\nProblem: Simplify (x + I) × (y + I) where x, y are reals")
    print("\nLet's use x = 2, y = 3")
    
    x = real(2)
    y = real(3)
    
    print(f"\n   x = {x}")
    print(f"   y = {y}")
    
    # (x + I)
    term1 = add(x, I)
    print(f"\n   x + I = {term1}")
    
    # (y + I)
    term2 = add(y, I)
    print(f"   y + I = {term2}")
    
    # (x + I) × (y + I)
    result = mul(term1, term2)
    print(f"\n   (x + I) × (y + I) = {result}")
    
    print("\n   Observation: Any expression involving I yields I")
    print("   This is due to I's absorption property")


def example_limit_interpretation():
    """Example 8: Limit interpretation"""
    print_section("Example 8: Limit Interpretation")
    
    print("\nClassical limits vs I-algebra:")
    
    print("\n1. lim(x→0+) 1/x in classical analysis:")
    print("   x = 0.1: 1/x =", 1/0.1)
    print("   x = 0.01: 1/x =", 1/0.01)
    print("   x = 0.001: 1/x =", 1/0.001)
    print("   Classical limit: +∞")
    
    print("\n2. lim(x→0-) 1/x in classical analysis:")
    print("   x = -0.1: 1/x =", 1/-0.1)
    print("   x = -0.01: 1/x =", 1/-0.01)
    print("   x = -0.001: 1/x =", 1/-0.001)
    print("   Classical limit: -∞")
    
    print("\n3. In I-algebra:")
    print(f"   1 / 0 = {div(ONE, ZERO)}")
    print("   No distinction between +∞ and -∞")
    print("   Value at 0 is I (indeterminate)")
    
    print("\n   Key insight: I is NOT infinity!")
    print("   I represents indeterminacy, not unbounded growth")


def example_field_violations():
    """Example 9: Field axiom violations"""
    print_section("Example 9: Why K_I is Not a Field")
    
    print("\nField requires:")
    print("1. Every element has an additive inverse")
    print("2. Every non-zero element has a multiplicative inverse")
    
    print("\nViolation 1: I has no additive inverse")
    print(f"   I ≠ 0? {I != ZERO} ✓")
    print(f"   I ≠ 1? {I != ONE} ✓")
    print(f"   I + ? = 0? No such element exists ✗")
    
    print("\nViolation 2: I has no multiplicative inverse")
    print(f"   I ≠ 0? {I != ZERO} ✓")
    print(f"   I × ? = 1? No such element exists ✗")
    
    print("\nConclusion: K_I is NOT a field")
    print("But it IS an algebraically consistent structure!")


def example_physical_singularities():
    """Example 10: Physical singularities"""
    print_section("Example 10: Physical Singularities")
    
    print("\nBlack Hole Singularity:")
    print("   Classical: T_μν → ∞ (undefined)")
    print(f"   With I: T_μν = {I} (indeterminate but stable)")
    
    print("\nBig Bang:")
    print("   Classical: ρ(t=0) → ∞ (singularity)")
    print(f"   With I: ρ(t=0) = {I} (no true singularity)")
    
    print("\nPlanck Scale:")
    print("   Classical: E → ∞ as ℓ → 0")
    print(f"   With I: E_Planck = {I} (fundamental limit)")
    
    print("\nInterpretation:")
    print("   I represents a state beyond our current physics")
    print("   Not infinite, but fundamentally indeterminate")
    print("   Mathematically consistent, physically speculative")


def main():
    """Run all examples"""
    print("\n" + "█" * 80)
    print("█" + " " * 78 + "█")
    print("█" + "  PRACTICAL EXAMPLES: THEORY OF I".center(78) + "█")
    print("█" + " " * 78 + "█")
    print("█" * 80)
    
    examples = [
        example_basic_operations,
        example_division_by_zero,
        example_idempotency,
        example_no_inverses,
        example_algebraic_properties,
        example_special_cases,
        example_real_world_calculation,
        example_limit_interpretation,
        example_field_violations,
        example_physical_singularities,
    ]
    
    for example in examples:
        example()
    
    print("\n" + "=" * 80)
    print(" END OF EXAMPLES")
    print("=" * 80)
    print("\nFor more information, see:")
    print("  - docs/FORMAL_VERIFICATION.md")
    print("  - docs/VERIFICATION_SUMMARY.md")
    print("  - docs/INTEGRATION_GUIDE.md")
    print()


if __name__ == "__main__":
    main()
