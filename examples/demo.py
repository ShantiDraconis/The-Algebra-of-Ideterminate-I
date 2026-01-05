#!/usr/bin/env python3
"""
Example usage of I-Algebra modules.

This script demonstrates the core functionality of the I-Algebra implementation.
"""

import sys
import os

# Add parent directory to path for imports
# This allows the script to work from any location
script_dir = os.path.dirname(os.path.abspath(__file__))
src_python_dir = os.path.join(os.path.dirname(script_dir), 'src', 'python')
sys.path.insert(0, src_python_dir)

from ialgebra import IElement, IExpr, SemanticsMode, oplus, ominus, otimes, odiv
from ialgebra.validation import InvariantChecker

print("=" * 70)
print("  I-Algebra Python Implementation - Example Usage")
print("=" * 70)

print("\n1. BASIC ELEMENTS")
print("-" * 70)
print(f"I (Indeterminate):    {IElement.I}")
print(f"J (Secondary):        {IElement.J}")
print(f"Zero:                 {IElement.ZERO}")
print(f"Infinity:             {IElement.INFINITY}")

print("\n2. BASIC OPERATIONS")
print("-" * 70)
operations = [
    ("I + 0", lambda: oplus(IElement.I, IElement.ZERO)),
    ("I + I", lambda: oplus(IElement.I, IElement.I)),
    ("I - I", lambda: ominus(IElement.I, IElement.I)),
    ("I * 0", lambda: otimes(IElement.I, IElement.ZERO)),
    ("I * I", lambda: otimes(IElement.I, IElement.I)),
    ("I / I", lambda: odiv(IElement.I, IElement.I)),
    ("5 + 3", lambda: oplus(5, 3)),
    ("5 - 2", lambda: ominus(5, 2)),
    ("4 * 6", lambda: otimes(4, 6)),
    ("8 / 2", lambda: odiv(8, 2)),
]

for desc, func in operations:
    try:
        result = func()
        print(f"{desc:20} => {result}")
    except Exception as e:
        print(f"{desc:20} => Error: {e}")

print("\n3. SEMANTIC MODES")
print("-" * 70)

# Contextual mode (default, logs decisions)
print("Contextual mode (I + 5):")
result = oplus(IElement.I, 5, SemanticsMode.CONTEXTUAL)
print(f"  Result: {result}")

# Strict mode (more rigid)
print("\nStrict mode (numeric operations):")
result = oplus(3, 7, SemanticsMode.STRICT)
print(f"  3 + 7 = {result}")

print("\n4. EXPRESSION AST")
print("-" * 70)
# Create an expression: (I + 0)
expr1 = IExpr.atom(IElement.I)
expr2 = IExpr.atom(IElement.ZERO)
expr_sum = IExpr.binary('+', expr1, expr2)
print(f"Expression AST: {expr_sum}")
print(f"Is atomic: {expr_sum.is_atom()}")
print(f"Is binary op: {expr_sum.is_binary_op()}")

print("\n5. INVARIANT VALIDATION")
print("-" * 70)
checker = InvariantChecker(SemanticsMode.STRICT)

# Test non-triviality
checker.non_triviality.check_not_equal_to_zero(IElement.I)
print("✓ Non-triviality: I ≠ 0")

# Test cancellation rules
checker.cancellation.validate_subtraction_cancellation(IElement.I, IElement.I)
print("✓ Restricted cancellation: I - I = 0")

checker.cancellation.validate_division_cancellation(IElement.I, IElement.I)
print("✓ Restricted cancellation: I / I = 1")

# Test distributivity
checker.check_distributivity(2, 3, 4)
print("✓ Distributivity: 2 * (3 + 4) = 2*3 + 2*4")

print("\n6. OPERATION RULES SUMMARY")
print("-" * 70)
print("Addition (oplus):")
print("  • 0 + x = x (identity)")
print("  • I + I = I (idempotent)")
print("")
print("Subtraction (ominus):")
print("  • x - 0 = x (right identity)")
print("  • I - I = 0 (restricted cancellation)")
print("")
print("Multiplication (otimes):")
print("  • 0 * x = 0 (zero absorption dominates)")
print("  • 1 * x = x (multiplicative identity)")
print("  • I * I = I (idempotent)")
print("")
print("Division (odiv):")
print("  • x / 1 = x (right identity)")
print("  • I / I = 1 (restricted cancellation)")
print("  • x / 0 = error (strict) or ∞ (non-strict)")

print("\n" + "=" * 70)
print("  All demonstrations completed successfully!")
print("=" * 70)
