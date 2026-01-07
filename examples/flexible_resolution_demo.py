"""
Demonstration of the Flexible Resolution Framework

This script showcases the key features of the flexible indeterminate system,
including:
- Extended number system K_I
- Absorption properties
- Modified operations
- Context-dependent resolution
- Non-triviality preservation
"""

from ialgebra import (
    I, ExtendedElement, 
    add, subtract, multiply, divide, power,
    create_system, ResolutionStrategy,
    omega_scaled, equals
)


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print('=' * 60)


def demo_basic_types():
    """Demonstrate the basic type system."""
    print_section("1. Basic Type System")
    
    # Field elements
    print(f"Field element: 5")
    
    # Pure indeterminate
    print(f"Indeterminate I: {I}")
    
    # Extended elements
    e1 = ExtendedElement(3, 2)  # 3 + 2I
    print(f"Extended element: {e1}")
    
    e2 = ExtendedElement(0, 1)  # Pure I
    print(f"Pure I element: {e2}")
    
    e3 = ExtendedElement(5, 0)  # Pure field element
    print(f"Pure field element: {e3}")


def demo_separation_axiom():
    """Demonstrate the separation axiom: I ≠ λ for all λ ∈ K."""
    print_section("2. Separation Axiom (I ≠ λ for all λ ∈ K)")
    
    print(f"I ≠ 0: {not equals(I, 0)}")
    print(f"I ≠ 1: {not equals(I, 1)}")
    print(f"I ≠ 5: {not equals(I, 5)}")
    print(f"I ≠ -1: {not equals(I, -1)}")
    
    print("\n✓ I is fundamentally distinct from any field element")


def demo_absorption():
    """Demonstrate absorption properties (Axiom 24)."""
    print_section("3. Absorption Properties (Axiom 24)")
    
    # Addition absorption: a + I = I
    print("Addition absorption: a + I = I")
    result1 = add(5, I)
    print(f"  5 + I = {result1}")
    print(f"  Is pure I? {result1.is_pure_indeterminate()}")
    
    result2 = add(ExtendedElement(3, 2), I)
    print(f"  (3 + 2I) + I = {result2}")
    
    # Multiplication absorption: a · I = I
    print("\nMultiplication absorption: a · I = I")
    result3 = multiply(7, I)
    print(f"  7 · I = {result3}")
    print(f"  Is pure I? {result3.is_pure_indeterminate()}")
    
    result4 = multiply(ExtendedElement(2, 3), I)
    print(f"  (2 + 3I) · I = {result4}")


def demo_idempotency():
    """Demonstrate I's idempotent properties."""
    print_section("4. Idempotent Properties of I")
    
    # I + I = I (additive idempotency)
    result1 = add(I, I)
    print(f"I + I = {result1}")
    print(f"  Is I? {result1.is_pure_indeterminate()}")
    
    # I · I = I (multiplicative idempotency)
    result2 = multiply(I, I)
    print(f"I · I = {result2}")
    print(f"  Is I? {result2.is_pure_indeterminate()}")
    
    # I^n = I for all n ≥ 1
    print("\nPowers of I:")
    for n in [1, 2, 3, 5, 10]:
        result = power(I, n)
        print(f"  I^{n} = {result} (is I? {result.is_pure_indeterminate()})")


def demo_modified_operations():
    """Demonstrate modified operations in K_I."""
    print_section("5. Modified Operations (Axiom 25)")
    
    # Standard addition
    e1 = ExtendedElement(2, 3)  # 2 + 3I
    e2 = ExtendedElement(4, 5)  # 4 + 5I
    result = add(e1, e2)
    print(f"Addition: (2 + 3I) + (4 + 5I) = {result}")
    print(f"  Real part: {result.real_part}, Indet coeff: {result.indet_coeff}")
    
    # Modified multiplication (with default Ω(I) = I)
    result2 = multiply(e1, e2)
    print(f"\nMultiplication: (2 + 3I)(4 + 5I) = {result2}")
    print(f"  Real part: {result2.real_part}, Indet coeff: {result2.indet_coeff}")
    print(f"  Formula: ac + (ad+bc)I + bd·Ω(I)")
    print(f"  where ac=8, ad+bc=22, bd·Ω(I)=15I (since Ω(I)=I)")
    
    # Multiplication with custom corrective function Ω(I) = 2I
    omega = omega_scaled(2)
    result3 = multiply(e1, e2, omega)
    print(f"\nWith Ω(I) = 2I: (2 + 3I)(4 + 5I) = {result3}")
    print(f"  bd·Ω(I) = 15·2I = 30I")


def demo_division_by_zero():
    """Demonstrate division by zero (Axiom 23)."""
    print_section("6. Division by Zero (Axiom 23)")
    
    # x/0 = I for x ≠ 0
    print("For all x ≠ 0: x/0 = I")
    
    for x in [1, 2, 5, -3, 100]:
        result = divide(x, 0)
        print(f"  {x}/0 = {result} (is I? {result.is_pure_indeterminate()})")
    
    # 0/0 is also I (indeterminate form)
    result = divide(0, 0)
    print(f"\n0/0 = {result} (indeterminate)")
    
    # Division by I is undefined
    print("\nDivision by I is undefined (Axiom I4)")
    try:
        divide(5, I)
    except ValueError as e:
        print(f"  5/I raises error: {e}")


def demo_flexible_resolution():
    """Demonstrate the flexible resolution framework."""
    print_section("7. Flexible Resolution Framework")
    
    system = create_system("R")
    
    # I remains indeterminate by default
    print("By default, I remains indeterminate (non-trivial)")
    print(f"  System is non-trivial: {system.check_non_triviality()}")
    
    # Create local resolution context
    ctx1 = system.create_context("problem1")
    print(f"\nCreated local context 'problem1'")
    print(f"  Context is unresolved: {not ctx1.is_resolved()}")
    
    # Resolve locally to a specific value
    ctx2 = ctx1.resolve(5)
    print(f"\nResolved I = 5 locally in context")
    print(f"  Is resolved: {ctx2.is_resolved()}")
    print(f"  Resolved value: {ctx2.resolved_value}")
    print(f"  Is consistent: {ctx2.check_consistency()}")
    
    # Demonstrate division by zero handling
    print("\nDivision by zero creates constraint")
    result = system.division_by_zero(10)
    print(f"  10/0 = {result}")
    

def demo_non_triviality():
    """Demonstrate non-triviality preservation (Axiom 27)."""
    print_section("8. Non-Triviality Preservation (Axiom 27)")
    
    system = create_system("R")
    
    print("Global I ≠ 0 requirement:")
    print(f"  System is non-trivial: {system.check_non_triviality()}")
    
    # Local resolution to non-zero is allowed
    ctx = system.create_context("local_test")
    ctx_resolved = ctx.resolve(7)
    print(f"\nLocal resolution to I = 7:")
    print(f"  Is consistent: {ctx_resolved.check_consistency()}")
    
    # Add division by zero constraint
    ctx.add_constraint("division_by_zero_test", {"numerator": 5})
    
    # Try to resolve to zero with division constraint
    ctx_zero = ctx.resolve(0)
    print(f"\nTrying I = 0 with division by zero constraint:")
    print(f"  Is consistent: {ctx_zero.check_consistency()}")
    print(f"  ✓ Setting I = 0 globally would cause collapse (1 = 0)")


def demo_extended_system():
    """Demonstrate the extended system K_I properties."""
    print_section("9. Extended System K_I = {a + bI | a,b ∈ K}")
    
    print("K_I extends K with an additional dimension from I")
    
    # Various elements of K_I
    elements = [
        ExtendedElement(0, 0),    # 0 (identity)
        ExtendedElement(1, 0),    # 1 (in K)
        ExtendedElement(0, 1),    # I (pure indeterminate)
        ExtendedElement(3, 2),    # 3 + 2I (general form)
        ExtendedElement(-2, 5),   # -2 + 5I
    ]
    
    print("\nExamples of elements in K_I:")
    for e in elements:
        print(f"  {e}")
        if e.is_field_element():
            print(f"    → Reduces to field element")
        elif e.is_pure_indeterminate():
            print(f"    → Pure indeterminate I")
        else:
            print(f"    → Genuine extended element (a + bI)")
    
    # Show that K_I is closed under operations
    print("\nK_I is closed under addition and multiplication:")
    e1 = ExtendedElement(2, 3)
    e2 = ExtendedElement(4, 1)
    print(f"  {e1} + {e2} = {add(e1, e2)}")
    print(f"  {e1} · {e2} = {multiply(e1, e2)}")


def demo_practical_example():
    """Show a practical example of flexible resolution."""
    print_section("10. Practical Example: Solving with Flexible Resolution")
    
    system = create_system("R")
    
    print("Consider the equation: xI = 10")
    print("where x = 2")
    print("\nWithout flexible resolution, this has no solution in K.")
    print("With flexible resolution, we can locally resolve I = 5.")
    
    # Create context for this problem
    ctx = system.create_context("equation_solver")
    ctx_solved = ctx.resolve(5)
    
    print(f"\nLocal resolution: I = {ctx_solved.resolved_value}")
    print(f"Then: 2 · I = 2 · 5 = 10 ✓")
    print(f"Context is consistent: {ctx_solved.check_consistency()}")
    
    print("\nThis demonstrates the flexibility:")
    print("  • I remains indeterminate globally")
    print("  • I can take specific values locally to satisfy equations")
    print("  • System remains non-trivial (I ≠ 0 globally)")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 60)
    print("  FLEXIBLE RESOLUTION FRAMEWORK DEMONSTRATION")
    print("  The Algebra of Indeterminate I")
    print("=" * 60)
    
    demo_basic_types()
    demo_separation_axiom()
    demo_absorption()
    demo_idempotency()
    demo_modified_operations()
    demo_division_by_zero()
    demo_flexible_resolution()
    demo_non_triviality()
    demo_extended_system()
    demo_practical_example()
    
    print("\n" + "=" * 60)
    print("  Demonstration Complete!")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("  1. I is fundamentally distinct from any field element (Separation)")
    print("  2. I absorbs all elements under addition and multiplication")
    print("  3. I is idempotent: I + I = I, I · I = I")
    print("  4. Division by zero yields I: x/0 = I")
    print("  5. I can be resolved locally while maintaining global non-triviality")
    print("  6. The system K_I extends K with a genuine new dimension")
    print()


if __name__ == "__main__":
    main()
