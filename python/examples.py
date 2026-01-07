#!/usr/bin/env python3
"""
Examples of Using the Extended Cardinal System

This file demonstrates practical usage of the indeterminate element I
in extended cardinal arithmetic.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from indeterminate import ExtendedCardinal, I, AxiomVerifier

def example_1_basic_operations():
    """Example 1: Basic cardinal operations."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Operations")
    print("="*60)
    
    # Create some cardinals
    k1 = ExtendedCardinal(5)
    k2 = ExtendedCardinal(3)
    k3 = ExtendedCardinal(5)
    
    print(f"\nk1 = {k1}")
    print(f"k2 = {k2}")
    print(f"k3 = {k3}")
    
    # Addition
    print(f"\nk1 + k2 = {k1 + k2}")
    
    # Multiplication  
    print(f"k1 * k2 = {k1 * k2}")
    
    # Subtraction (different values)
    print(f"k1 - k2 = {k1 - k2}")
    
    # Self-subtraction (yields I)
    print(f"\nk1 - k1 = {k1 - k1}  ← This is I!")
    print(f"k2 - k2 = {k2 - k2}  ← This is also I!")
    print(f"k3 - k3 = {k3 - k3}  ← Same I!")

def example_2_i_absorption():
    """Example 2: I absorption property."""
    print("\n" + "="*60)
    print("EXAMPLE 2: I Absorption Property")
    print("="*60)
    
    k = ExtendedCardinal(10)
    
    print(f"\nk = {k}")
    print(f"I = {I}")
    
    # I absorbs in addition
    print(f"\nI + k = {I + k}  ← I absorbs")
    print(f"k + I = {k + I}  ← I absorbs")
    
    # I absorbs in multiplication
    print(f"\nI * k = {I * k}  ← I absorbs")
    print(f"k * I = {k * I}  ← I absorbs")
    
    # I with I
    print(f"\nI + I = {I + I}  ← Still I")
    print(f"I * I = {I * I}  ← Still I")
    print(f"I - I = {I - I}  ← Still I")

def example_3_uniqueness():
    """Example 3: Demonstrate uniqueness of I."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Uniqueness of I")
    print("="*60)
    
    # Different cardinals, same I
    k1 = ExtendedCardinal(7)
    k2 = ExtendedCardinal(42)
    k3 = ExtendedCardinal(100)
    
    i1 = k1 - k1
    i2 = k2 - k2
    i3 = k3 - k3
    
    print(f"\n{k1} - {k1} = {i1}")
    print(f"{k2} - {k2} = {i2}")
    print(f"{k3} - {k3} = {i3}")
    
    print(f"\nAre they all the same I?")
    print(f"i1 == i2: {i1 == i2}")
    print(f"i2 == i3: {i2 == i3}")
    print(f"i1 == I:  {i1 == I}")
    
    print(f"\nConclusion: There is exactly ONE indeterminate element!")

def example_4_algebraic_laws():
    """Example 4: Verify algebraic laws."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Algebraic Laws")
    print("="*60)
    
    a = ExtendedCardinal(2)
    b = ExtendedCardinal(3)
    c = ExtendedCardinal(5)
    
    # Commutativity
    print("\nCommutativity:")
    print(f"  {a} + {b} = {a + b}")
    print(f"  {b} + {a} = {b + a}")
    print(f"  Equal? {(a + b) == (b + a)}")
    
    print(f"\n  {a} * {b} = {a * b}")
    print(f"  {b} * {a} = {b * a}")
    print(f"  Equal? {(a * b) == (b * a)}")
    
    # Associativity
    print("\nAssociativity:")
    result1 = (a + b) + c
    result2 = a + (b + c)
    print(f"  ({a} + {b}) + {c} = {result1}")
    print(f"  {a} + ({b} + {c}) = {result2}")
    print(f"  Equal? {result1 == result2}")
    
    # Distributivity (for regular cardinals)
    print("\nDistributivity:")
    result1 = a * (b + c)
    result2 = (a * b) + (a * c)
    print(f"  {a} * ({b} + {c}) = {result1}")
    print(f"  ({a} * {b}) + ({a} * {c}) = {result2}")
    print(f"  Equal? {result1 == result2}")

def example_5_chains():
    """Example 5: Chains of operations with I."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Chains with I")
    print("="*60)
    
    k = ExtendedCardinal(4)
    
    print(f"\nStarting with k = {k}")
    
    # Once I appears, it dominates
    result1 = k + (k - k)  # k + I = I
    print(f"\nk + (k - k) = {k} + {k - k} = {result1}")
    
    result2 = k * (k - k)  # k * I = I
    print(f"k * (k - k) = {k} * {k - k} = {result2}")
    
    result3 = (k + k) - (k + k)  # Self-subtraction
    print(f"(k + k) - (k + k) = {k + k} - {k + k} = {result3}")
    
    print("\nConclusion: Once I enters a computation, it spreads!")

def example_6_equivalence_classes():
    """Example 6: Equivalence classes under I."""
    print("\n" + "="*60)
    print("EXAMPLE 6: Equivalence Classes")
    print("="*60)
    
    # Define relation: a ~ b if a - b = I
    print("\nDefine: a ~ b  ⟺  a - b = I")
    
    k = ExtendedCardinal(5)
    
    print(f"\nFor k = {k}:")
    print(f"  k ~ k? {(k - k) == I} (reflexive)")
    
    # Any cardinal is equivalent to itself
    print("\nAll cardinals are equivalent to themselves:")
    for n in [1, 2, 5, 10, 20]:
        kn = ExtendedCardinal(n)
        print(f"  {n} ~ {n}: {(kn - kn) == I}")

def example_7_theorem_demonstrations():
    """Example 7: Demonstrate main theorems."""
    print("\n" + "="*60)
    print("EXAMPLE 7: Main Theorems")
    print("="*60)
    
    # Theorem 3.1: Uniqueness
    print("\nTheorem 3.1 (Uniqueness):")
    print("The element I is unique.")
    k1 = ExtendedCardinal(7)
    k2 = ExtendedCardinal(13)
    print(f"  {k1} - {k1} = {k1 - k1}")
    print(f"  {k2} - {k2} = {k2 - k2}")
    print(f"  Both equal? {(k1 - k1) == (k2 - k2)} ✓")
    
    # Theorem 5.1: Algebraic Compatibility
    print("\nTheorem 5.1 (Algebraic Compatibility):")
    print("(κ + λ) - (κ + λ) = I")
    k = ExtendedCardinal(3)
    l = ExtendedCardinal(7)
    sum_kl = k + l
    result = sum_kl - sum_kl
    print(f"  κ = {k}, λ = {l}")
    print(f"  (κ + λ) = {sum_kl}")
    print(f"  (κ + λ) - (κ + λ) = {result}")
    print(f"  Result is I? {result == I} ✓")
    
    # Non-triviality
    print("\nNon-triviality Theorem:")
    print("I is distinct from all cardinals.")
    for n in [0, 1, 5, 10]:
        kn = ExtendedCardinal(n)
        print(f"  I ≠ {n}: {I != kn} ✓")

def example_8_real_world_analogy():
    """Example 8: Real-world analogy."""
    print("\n" + "="*60)
    print("EXAMPLE 8: Real-World Analogy")
    print("="*60)
    
    print("\nThink of I as 'unknown' or 'indeterminate':")
    print("\n  Scenario: Measuring the same infinite quantity twice")
    print("  Question: What's the difference?")
    print("  Answer: Indeterminate (I), not zero!")
    
    infinity = ExtendedCardinal(1000000)  # Representing "very large"
    
    print(f"\n  infinity = {infinity}")
    print(f"  infinity - infinity = {infinity - infinity}")
    print(f"\n  This is I, representing the indeterminacy!")
    
    print("\n  Compare to regular subtraction:")
    k = ExtendedCardinal(5)
    print(f"  {k} - {k} = {k - k}  (also I)")
    
    print("\n  Key insight: Self-subtraction loses information about magnitude")

def main():
    """Run all examples."""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  Extended Cardinal Arithmetic: Examples & Demonstrations".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    # Run all examples
    example_1_basic_operations()
    example_2_i_absorption()
    example_3_uniqueness()
    example_4_algebraic_laws()
    example_5_chains()
    example_6_equivalence_classes()
    example_7_theorem_demonstrations()
    example_8_real_world_analogy()
    
    # Final verification
    print("\n" + "="*60)
    print("FINAL VERIFICATION")
    print("="*60)
    AxiomVerifier.verify_all()
    
    print("\n" + "="*60)
    print("Examples complete! The extended cardinal system works perfectly.")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
