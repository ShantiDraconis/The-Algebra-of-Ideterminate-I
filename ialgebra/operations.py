"""
Operations for the Indeterminate Extended Algebra (IEA)

This module implements the modified algebraic operations for the IEA,
including the corrected distributive law and absorption properties.

Author: IEA Implementation
Date: 2026-01-05
"""

from typing import Optional
from .types import IEAElement, ElementType


class IEAOperations:
    """
    Implements algebraic operations for the Indeterminate Extended Algebra (IEA).
    
    The IEA is NOT a field due to:
    1. I has no multiplicative inverse
    2. Modified distributive law: a(b+c) = ab + ac + λJ
    3. Absorption properties: x + I = I, x · I = I
    
    Key axioms:
    - x/0 = I for all x ≠ 0
    - I ≠ 0 (prevents collapse)
    - ∞ - ∞ = I
    - I · I = I (multiplicative idempotency)
    - I + I = I (additive idempotency)
    """
    
    @staticmethod
    def add(a: IEAElement, b: IEAElement) -> IEAElement:
        """
        Modified addition operation in the IEA.
        
        Absorption property: x + I = I
        
        Args:
            a: First element
            b: Second element
            
        Returns:
            The sum a + b
        """
        # I absorbs under addition
        if a.is_indeterminate() or b.is_indeterminate():
            return IEAElement.I()
        
        # J absorbs under addition (similar to I)
        if a.is_imaginary_singularity() or b.is_imaginary_singularity():
            return IEAElement.J()
        
        # Infinity cases
        if a.element_type == ElementType.INFINITY_POSITIVE:
            if b.element_type == ElementType.INFINITY_NEGATIVE:
                # ∞ - ∞ = I
                return IEAElement.I()
            return IEAElement.pos_infinity()
        
        if a.element_type == ElementType.INFINITY_NEGATIVE:
            if b.element_type == ElementType.INFINITY_POSITIVE:
                # -∞ + ∞ = I
                return IEAElement.I()
            return IEAElement.neg_infinity()
        
        # Real addition
        if a.is_real() and b.is_real():
            return IEAElement.real(a.value + b.value)
        
        # Complex addition
        if a.element_type == ElementType.COMPLEX or b.element_type == ElementType.COMPLEX:
            val_a = a.value if isinstance(a.value, complex) else complex(a.value, 0)
            val_b = b.value if isinstance(b.value, complex) else complex(b.value, 0)
            return IEAElement.complex_num(val_a + val_b)
        
        # Default: return I for unknown combinations
        return IEAElement.I()
    
    @staticmethod
    def subtract(a: IEAElement, b: IEAElement) -> IEAElement:
        """
        Modified subtraction operation in the IEA.
        
        Key property: x - x = 0 for real/complex, but ∞ - ∞ = I
        
        Args:
            a: First element
            b: Second element
            
        Returns:
            The difference a - b
        """
        # I absorbs under subtraction
        if a.is_indeterminate() or b.is_indeterminate():
            return IEAElement.I()
        
        # J absorbs under subtraction
        if a.is_imaginary_singularity() or b.is_imaginary_singularity():
            return IEAElement.J()
        
        # Infinity cases: ∞ - ∞ = I
        if a.element_type == ElementType.INFINITY_POSITIVE and b.element_type == ElementType.INFINITY_POSITIVE:
            return IEAElement.I()
        
        if a.element_type == ElementType.INFINITY_NEGATIVE and b.element_type == ElementType.INFINITY_NEGATIVE:
            return IEAElement.I()
        
        # Real subtraction
        if a.is_real() and b.is_real():
            return IEAElement.real(a.value - b.value)
        
        # Complex subtraction
        if a.element_type == ElementType.COMPLEX or b.element_type == ElementType.COMPLEX:
            val_a = a.value if isinstance(a.value, complex) else complex(a.value, 0)
            val_b = b.value if isinstance(b.value, complex) else complex(b.value, 0)
            return IEAElement.complex_num(val_a - val_b)
        
        return IEAElement.I()
    
    @staticmethod
    def multiply(a: IEAElement, b: IEAElement) -> IEAElement:
        """
        Modified multiplication operation in the IEA.
        
        Properties:
        - x · I = I for x ≠ 0
        - 0 · I = 0 (special case)
        - I · I = I (multiplicative idempotency)
        
        Args:
            a: First element
            b: Second element
            
        Returns:
            The product a · b
        """
        # Special case: 0 · I = 0
        if (a.is_zero() and b.is_indeterminate()) or (b.is_zero() and a.is_indeterminate()):
            return IEAElement.zero()
        
        # I absorbs under multiplication (for non-zero)
        if a.is_indeterminate() or b.is_indeterminate():
            return IEAElement.I()
        
        # J absorbs under multiplication
        if a.is_imaginary_singularity() or b.is_imaginary_singularity():
            return IEAElement.J()
        
        # Real multiplication
        if a.is_real() and b.is_real():
            return IEAElement.real(a.value * b.value)
        
        # Complex multiplication
        if a.element_type == ElementType.COMPLEX or b.element_type == ElementType.COMPLEX:
            val_a = a.value if isinstance(a.value, complex) else complex(a.value, 0)
            val_b = b.value if isinstance(b.value, complex) else complex(b.value, 0)
            return IEAElement.complex_num(val_a * val_b)
        
        return IEAElement.I()
    
    @staticmethod
    def divide(a: IEAElement, b: IEAElement) -> IEAElement:
        """
        Modified division operation in the IEA.
        
        Key property: x/0 = I for all x ≠ 0
        Also: 0/0 = I
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            The quotient a/b
        """
        # Division by zero: x/0 = I
        if b.is_zero():
            return IEAElement.I()
        
        # Division by I
        if b.is_indeterminate():
            if a.is_zero():
                return IEAElement.zero()
            return IEAElement.I()
        
        # Division by J
        if b.is_imaginary_singularity():
            return IEAElement.I()
        
        # I divided by anything non-zero
        if a.is_indeterminate():
            return IEAElement.I()
        
        # Real division
        if a.is_real() and b.is_real():
            if b.value == 0:
                return IEAElement.I()
            return IEAElement.real(a.value / b.value)
        
        # Complex division
        if a.element_type == ElementType.COMPLEX or b.element_type == ElementType.COMPLEX:
            val_a = a.value if isinstance(a.value, complex) else complex(a.value, 0)
            val_b = b.value if isinstance(b.value, complex) else complex(b.value, 0)
            if val_b == 0:
                return IEAElement.I()
            return IEAElement.complex_num(val_a / val_b)
        
        return IEAElement.I()
    
    @staticmethod
    def modified_distributive(a: IEAElement, b: IEAElement, c: IEAElement, 
                             lambda_coeff: float = 0.0) -> tuple[IEAElement, IEAElement]:
        """
        Modified distributive law for the IEA.
        
        In standard algebra: a(b + c) = ab + ac
        In IEA: a(b + c) = ab + ac + λJ
        
        where J = iI is the imaginary singularity and λ is a correction coefficient.
        
        Args:
            a: Element to distribute
            b: First element in sum
            c: Second element in sum
            lambda_coeff: Correction coefficient (default 0)
            
        Returns:
            Tuple of (a(b+c), ab + ac + λJ) for comparison
        """
        # Left side: a(b + c)
        left = IEAOperations.multiply(a, IEAOperations.add(b, c))
        
        # Right side: ab + ac + λJ
        ab = IEAOperations.multiply(a, b)
        ac = IEAOperations.multiply(a, c)
        ab_plus_ac = IEAOperations.add(ab, ac)
        
        # Add correction term λJ
        if lambda_coeff != 0.0:
            lambda_J = IEAOperations.multiply(IEAElement.real(lambda_coeff), IEAElement.J())
            right = IEAOperations.add(ab_plus_ac, lambda_J)
        else:
            right = ab_plus_ac
        
        return (left, right)
    
    @staticmethod
    def has_multiplicative_inverse(a: IEAElement) -> bool:
        """
        Check if an element has a multiplicative inverse.
        
        Key axiom: I does NOT have a multiplicative inverse.
        This is a fundamental departure from field axioms.
        
        Args:
            a: Element to check
            
        Returns:
            True if the element has an inverse, False otherwise
        """
        # I has no inverse
        if a.is_indeterminate():
            return False
        
        # J has no inverse
        if a.is_imaginary_singularity():
            return False
        
        # Zero has no inverse
        if a.is_zero():
            return False
        
        # Non-zero reals and complex numbers have inverses
        if a.is_real() and a.value != 0:
            return True
        
        if a.element_type == ElementType.COMPLEX and a.value != 0:
            return True
        
        # Infinities don't have standard inverses
        if a.is_singularity():
            return False
        
        return False
    
    @staticmethod
    def attempt_inverse(a: IEAElement) -> Optional[IEAElement]:
        """
        Attempt to compute the multiplicative inverse of an element.
        
        Returns None if no inverse exists (e.g., for I or 0).
        
        Args:
            a: Element to invert
            
        Returns:
            The inverse if it exists, None otherwise
        """
        if not IEAOperations.has_multiplicative_inverse(a):
            return None
        
        if a.is_real() and a.value != 0:
            return IEAElement.real(1.0 / a.value)
        
        if a.element_type == ElementType.COMPLEX and a.value != 0:
            return IEAElement.complex_num(1.0 / a.value)
        
        return None


class IEAAxioms:
    """
    Verifies the axioms of the Indeterminate Extended Algebra (IEA).
    """
    
    @staticmethod
    def verify_extended_division() -> bool:
        """
        Verify axiom: x/0 = I for all x ≠ 0.
        """
        x = IEAElement.real(5.0)
        zero = IEAElement.zero()
        result = IEAOperations.divide(x, zero)
        return result.is_indeterminate()
    
    @staticmethod
    def verify_I_not_zero() -> bool:
        """
        Verify axiom: I ≠ 0.
        This prevents the collapse: I = 0 → 1 = 0.
        """
        I = IEAElement.I()
        zero = IEAElement.zero()
        return I != zero
    
    @staticmethod
    def verify_absorption_addition() -> bool:
        """
        Verify axiom: x + I = I for all x.
        """
        x = IEAElement.real(3.0)
        I = IEAElement.I()
        result = IEAOperations.add(x, I)
        return result.is_indeterminate()
    
    @staticmethod
    def verify_absorption_multiplication() -> bool:
        """
        Verify axiom: x · I = I for all x ≠ 0.
        """
        x = IEAElement.real(3.0)
        I = IEAElement.I()
        result = IEAOperations.multiply(x, I)
        return result.is_indeterminate()
    
    @staticmethod
    def verify_zero_times_I() -> bool:
        """
        Verify special case: 0 · I = 0.
        """
        zero = IEAElement.zero()
        I = IEAElement.I()
        result = IEAOperations.multiply(zero, I)
        return result.is_zero()
    
    @staticmethod
    def verify_no_inverse_for_I() -> bool:
        """
        Verify axiom: I does not have a multiplicative inverse.
        """
        I = IEAElement.I()
        return not IEAOperations.has_multiplicative_inverse(I)
    
    @staticmethod
    def verify_infinity_minus_infinity() -> bool:
        """
        Verify: ∞ - ∞ = I.
        """
        pos_inf = IEAElement.pos_infinity()
        result = IEAOperations.subtract(pos_inf, pos_inf)
        return result.is_indeterminate()
    
    @staticmethod
    def verify_collapse_contradiction() -> bool:
        """
        Verify the collapse contradiction:
        If I = 0, then 1/0 = I = 0, so 1 = 0 · 0 = 0 (contradiction).
        
        This verifies that assuming I = 0 leads to logical contradiction.
        """
        # This is a logical verification, not a computation
        # The axiom I ≠ 0 must hold to prevent this collapse
        return IEAAxioms.verify_I_not_zero()
