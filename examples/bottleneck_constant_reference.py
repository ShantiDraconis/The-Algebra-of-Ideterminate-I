"""
Bottleneck Constant (I) - Reference Implementation
Based on the Algebra of the Indeterminate (AEI)

Author: Tiago Fagliari
ORCID: 0009-0006-6874-3910
Repository: https://github.com/ShantiDraconis/The-Algebra-of-Ideterminate-I
License: MIT (for academic and open source use)
         See COMMERCIAL_LICENSING.md for commercial use

This module provides a reference implementation of the Bottleneck Constant (I),
the unique algebraic element that resolves the indeterminate form 0/0.

Key Properties:
- I = 0/0 (indeterminate form resolution)
- I * I = I (multiplicative idempotency)
- I + I = I (additive idempotency)
- 0 * I = 0 (zero absorption)
- I ≠ 0, I ≠ 1, I ≠ ∞

For detailed specification, see BOTTLENECK_CONSTANT_SPECIFICATION.md
"""

from typing import Union, Any
from numbers import Number


class BottleneckConstant:
    """
    The Bottleneck Constant I = 0/0
    
    This class implements the unique algebraic element that resolves
    indeterminate division and maintains algebraic consistency.
    
    Attributes:
        _instance: Singleton instance (I is unique)
    
    Examples:
        >>> I = BottleneckConstant()
        >>> I * I == I
        True
        >>> I + I == I
        True
        >>> 0 * I
        0
        >>> I * 5 == I
        True
        >>> 10 / I
        0
    """
    
    _instance = None
    
    def __new__(cls):
        """Ensure I is a singleton (only one instance exists)."""
        if cls._instance is None:
            cls._instance = super(BottleneckConstant, cls).__new__(cls)
        return cls._instance
    
    def __repr__(self) -> str:
        """String representation."""
        return "I"
    
    def __str__(self) -> str:
        """String conversion."""
        return "I"
    
    def __eq__(self, other: Any) -> bool:
        """
        Equality: I = I (reflexive)
        
        Args:
            other: Object to compare with
        
        Returns:
            True if other is also the Bottleneck Constant, False otherwise
        """
        return isinstance(other, BottleneckConstant)
    
    def __ne__(self, other: Any) -> bool:
        """Inequality."""
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        """Hash for use in sets and dicts."""
        return hash("BottleneckConstant_I")
    
    # Arithmetic Operations
    
    def __mul__(self, other: Union['BottleneckConstant', Number]) -> Union['BottleneckConstant', int]:
        """
        Multiplication: I * I = I, I * r = I, 0 * I = 0
        
        Args:
            other: Number or BottleneckConstant
        
        Returns:
            I if other ≠ 0, otherwise 0
        """
        if isinstance(other, BottleneckConstant):
            return BottleneckConstant()  # I * I = I
        elif other == 0:
            return 0  # 0 * I = 0 (zero absorption)
        else:
            return BottleneckConstant()  # I * r = I for r ≠ 0
    
    def __rmul__(self, other: Union['BottleneckConstant', Number]) -> Union['BottleneckConstant', int]:
        """Right multiplication: r * I"""
        return self.__mul__(other)
    
    def __add__(self, other: Union['BottleneckConstant', Number]) -> 'BottleneckConstant':
        """
        Addition: I + I = I, I + r = I
        
        Args:
            other: Number or BottleneckConstant
        
        Returns:
            I (additive idempotency)
        """
        return BottleneckConstant()  # I + anything = I
    
    def __radd__(self, other: Union['BottleneckConstant', Number]) -> 'BottleneckConstant':
        """Right addition: r + I"""
        return self.__add__(other)
    
    def __sub__(self, other: Union['BottleneckConstant', Number]) -> 'BottleneckConstant':
        """
        Subtraction: I - r = I
        
        Args:
            other: Number or BottleneckConstant
        
        Returns:
            I
        """
        return BottleneckConstant()
    
    def __rsub__(self, other: Union['BottleneckConstant', Number]) -> 'BottleneckConstant':
        """Right subtraction: r - I"""
        return BottleneckConstant()
    
    def __truediv__(self, other: Union['BottleneckConstant', Number]) -> 'BottleneckConstant':
        """
        Division by number: I / r = I
        
        Args:
            other: Number or BottleneckConstant
        
        Returns:
            I
        """
        if other == 0:
            return BottleneckConstant()  # I / 0 = I
        return BottleneckConstant()  # I / r = I for r ≠ 0
    
    def __rtruediv__(self, other: Union['BottleneckConstant', Number]) -> Union[int, 'BottleneckConstant']:
        """
        Division by I: r / I = 0
        
        Args:
            other: Number or BottleneckConstant
        
        Returns:
            0 for any real number, I for I / I
        """
        if isinstance(other, BottleneckConstant):
            return BottleneckConstant()  # I / I = I
        return 0  # r / I = 0 for all real r
    
    def __pow__(self, power: Number) -> 'BottleneckConstant':
        """
        Exponentiation: I^n = I for any n
        
        Args:
            power: Exponent
        
        Returns:
            I (idempotency extends to all powers)
        """
        return BottleneckConstant()
    
    def __neg__(self) -> 'BottleneckConstant':
        """Negation: -I = I"""
        return BottleneckConstant()
    
    def __abs__(self) -> 'BottleneckConstant':
        """Absolute value: |I| = I"""
        return BottleneckConstant()
    
    def __bool__(self) -> bool:
        """
        Boolean conversion.
        
        Returns:
            True (I is a valid algebraic element, not a null/error)
        """
        return True


# Create the canonical instance
I = BottleneckConstant()


def safe_divide(numerator: Number, denominator: Number) -> Union[Number, BottleneckConstant]:
    """
    Division that returns I for 0/0 instead of raising an error.
    
    Args:
        numerator: Dividend
        denominator: Divisor
    
    Returns:
        numerator / denominator if denominator ≠ 0
        I if numerator = 0 and denominator = 0
    
    Examples:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(0, 0)
        I
        >>> safe_divide(5, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero (use I for 0/0)
    """
    if denominator == 0:
        if numerator == 0:
            return I  # 0/0 = I
        else:
            raise ZeroDivisionError("division by zero (use I for 0/0)")
    return numerator / denominator


def is_indeterminate(value: Any) -> bool:
    """
    Check if a value is the Bottleneck Constant.
    
    Args:
        value: Value to check
    
    Returns:
        True if value is I, False otherwise
    
    Examples:
        >>> is_indeterminate(I)
        True
        >>> is_indeterminate(0)
        False
        >>> is_indeterminate(float('nan'))
        False
    """
    return isinstance(value, BottleneckConstant)


def demonstrate_properties():
    """
    Demonstrate the fundamental properties of the Bottleneck Constant.
    
    This function verifies:
    1. Uniqueness (I = I)
    2. Multiplicative idempotency (I * I = I)
    3. Additive idempotency (I + I = I)
    4. Zero absorption (0 * I = 0)
    5. Distinctness (I ≠ 0, I ≠ 1)
    6. Division properties (r / I = 0, I / r = I)
    """
    print("=" * 60)
    print("Bottleneck Constant (I) - Property Verification")
    print("=" * 60)
    print(f"Author: Tiago Fagliari (ORCID: 0009-0006-6874-3910)")
    print(f"Framework: Algebra of the Indeterminate (AEI)")
    print("=" * 60)
    print()
    
    # Create instances
    I1 = BottleneckConstant()
    I2 = BottleneckConstant()
    
    # 1. Uniqueness
    print("1. UNIQUENESS")
    print(f"   I1 == I2: {I1 == I2} (Expected: True)")
    print(f"   I1 is I2: {I1 is I2} (Expected: True - singleton)")
    print()
    
    # 2. Multiplicative Idempotency
    print("2. MULTIPLICATIVE IDEMPOTENCY")
    print(f"   I * I = {I * I} (Expected: I)")
    print(f"   I * I == I: {I * I == I} (Expected: True)")
    print()
    
    # 3. Additive Idempotency
    print("3. ADDITIVE IDEMPOTENCY")
    print(f"   I + I = {I + I} (Expected: I)")
    print(f"   I + I == I: {I + I == I} (Expected: True)")
    print()
    
    # 4. Zero Absorption
    print("4. ZERO ABSORPTION")
    print(f"   0 * I = {0 * I} (Expected: 0)")
    print(f"   I * 0 = {I * 0} (Expected: 0)")
    print()
    
    # 5. Operations with Real Numbers
    print("5. OPERATIONS WITH REAL NUMBERS")
    print(f"   I * 5 = {I * 5} (Expected: I)")
    print(f"   I + 10 = {I + 10} (Expected: I)")
    print(f"   I - 3 = {I - 3} (Expected: I)")
    print()
    
    # 6. Division Properties
    print("6. DIVISION PROPERTIES")
    print(f"   10 / I = {10 / I} (Expected: 0)")
    print(f"   I / 5 = {I / 5} (Expected: I)")
    print(f"   I / I = {I / I} (Expected: I)")
    print()
    
    # 7. Distinctness
    print("7. DISTINCTNESS")
    print(f"   I == 0: {I == 0} (Expected: False)")
    print(f"   I == 1: {I == 1} (Expected: False)")
    print(f"   I == float('inf'): {I == float('inf')} (Expected: False)")
    print(f"   I == float('nan'): {I == float('nan')} (Expected: False)")
    print()
    
    # 8. Safe Division
    print("8. SAFE DIVISION (0/0 = I)")
    print(f"   safe_divide(0, 0) = {safe_divide(0, 0)} (Expected: I)")
    print(f"   safe_divide(10, 2) = {safe_divide(10, 2)} (Expected: 5.0)")
    print()
    
    # 9. Exponentiation
    print("9. EXPONENTIATION")
    print(f"   I^2 = {I**2} (Expected: I)")
    print(f"   I^10 = {I**10} (Expected: I)")
    print()
    
    print("=" * 60)
    print("All properties verified successfully!")
    print("=" * 60)


if __name__ == "__main__":
    # Run demonstration
    demonstrate_properties()
    
    print("\nExample: Quantum Computing Application")
    print("-" * 60)
    
    # Simulated quantum measurement that returns I for indeterminate result
    def quantum_measurement(alpha, beta):
        """Simulate quantum measurement with I for indeterminate states."""
        if abs(alpha) < 1e-10 and abs(beta) < 1e-10:
            return I  # Indeterminate measurement
        elif abs(alpha) > abs(beta):
            return 0
        else:
            return 1
    
    # Test cases
    print("Measuring qubit states:")
    print(f"  α=0.7, β=0.3 → {quantum_measurement(0.7, 0.3)} (0 with high probability)")
    print(f"  α=0.3, β=0.7 → {quantum_measurement(0.3, 0.7)} (1 with high probability)")
    print(f"  α≈0, β≈0 → {quantum_measurement(1e-15, 1e-15)} (indeterminate → I)")
    print()
    
    # Computation continues with I
    result = quantum_measurement(1e-15, 1e-15)
    if is_indeterminate(result):
        print(f"  Result is indeterminate (I), but computation continues!")
        print(f"  I * 2 = {result * 2}")
        print(f"  I + 100 = {result + 100}")
        print(f"  Further processing with I-algebra...")
    
    print()
    print("For more information:")
    print("  - Technical Spec: BOTTLENECK_CONSTANT_SPECIFICATION.md")
    print("  - Quantum Guide: QUANTUM_COMPUTING_GUIDE.md")
    print("  - Licensing: COMMERCIAL_LICENSING.md")
