"""
Operations Module for the Indeterminate Algebra

Implements arithmetic operations in the extended algebra K_I with flexible resolution,
including the modified operations from Axioms 23-27.
"""

from typing import Union, Callable, Optional
from .types import (
    AlgebraElement, ExtendedElement, Indeterminate, FieldElement,
    to_extended, is_indeterminate_element, I
)


def add(a: AlgebraElement, b: AlgebraElement) -> ExtendedElement:
    """
    Addition in K_I with absorption property.
    
    Implements Axiom 24: a + I = I for all a ∈ K_I (absorption)
    
    Standard case: (a + bI) + (c + dI) = (a + c) + (b + d)I (Equation 213)
    
    Args:
        a, b: Elements to add
        
    Returns:
        The sum in K_I
    """
    # Convert to extended elements
    a_ext = to_extended(a)
    b_ext = to_extended(b)
    
    # Check for absorption: if either is pure I, result is I
    if a_ext.is_pure_indeterminate() or b_ext.is_pure_indeterminate():
        return ExtendedElement(0, 1, a_ext.indeterminate or b_ext.indeterminate)
    
    # Standard addition: (a + bI) + (c + dI) = (a + c) + (b + d)I
    result_real = a_ext.real_part + b_ext.real_part
    result_indet = a_ext.indet_coeff + b_ext.indet_coeff
    
    # Preserve indeterminate context
    indet = a_ext.indeterminate if a_ext.indeterminate else b_ext.indeterminate
    
    return ExtendedElement(result_real, result_indet, indet)


def subtract(a: AlgebraElement, b: AlgebraElement) -> ExtendedElement:
    """
    Subtraction in K_I.
    
    Defined as: a - b = a + (-b)
    
    Args:
        a, b: Elements to subtract
        
    Returns:
        The difference in K_I
    """
    b_ext = to_extended(b)
    b_neg = ExtendedElement(-b_ext.real_part, -b_ext.indet_coeff, b_ext.indeterminate)
    return add(a, b_neg)


def multiply(a: AlgebraElement, b: AlgebraElement, 
             omega: Optional[Callable[[Indeterminate], AlgebraElement]] = None) -> ExtendedElement:
    """
    Multiplication in K_I with corrective term Ω(I).
    
    Implements:
    - Axiom 24: a · I = I for all a ∈ K_I (absorption)
    - Axiom 25: (a + bI)(c + dI) = ac + (ad + bc)I + bd·Ω(I) (Equation 214)
    
    The corrective function Ω(I) ensures consistency. Default: Ω(I) = I
    
    Args:
        a, b: Elements to multiply
        omega: Corrective function Ω(I). If None, uses Ω(I) = I
        
    Returns:
        The product in K_I
    """
    # Convert to extended elements
    a_ext = to_extended(a)
    b_ext = to_extended(b)
    
    # Absorption: if either is pure I, result is I
    if a_ext.is_pure_indeterminate() or b_ext.is_pure_indeterminate():
        indet = a_ext.indeterminate if a_ext.is_pure_indeterminate() else b_ext.indeterminate
        return ExtendedElement(0, 1, indet)
    
    # Get indeterminate context
    indet = a_ext.indeterminate if a_ext.indeterminate else b_ext.indeterminate
    
    # Modified multiplication: (a + bI)(c + dI) = ac + (ad + bc)I + bd·Ω(I)
    # Standard terms
    ac = a_ext.real_part * b_ext.real_part
    ad_plus_bc = a_ext.real_part * b_ext.indet_coeff + a_ext.indet_coeff * b_ext.real_part
    bd = a_ext.indet_coeff * b_ext.indet_coeff
    
    # Apply corrective term
    if omega is None:
        # Default: Ω(I) = I, so bd·Ω(I) contributes to I coefficient
        # Since I·I = I, bd·I = bd·I
        result_real = ac
        result_indet = ad_plus_bc + bd
    else:
        # Apply custom corrective function
        omega_result = to_extended(omega(indet))
        result_real = ac + bd * omega_result.real_part
        result_indet = ad_plus_bc + bd * omega_result.indet_coeff
    
    return ExtendedElement(result_real, result_indet, indet)


def divide(a: AlgebraElement, b: AlgebraElement) -> ExtendedElement:
    """
    Division in K_I with special handling for division by zero.
    
    Implements Axiom 23: x/0 = I for all x ≠ 0
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        The quotient in K_I
        
    Divisão por I, ou de I por qualquer coisa, dá I (absorção, como em Indet).
    """
    a_ext = to_extended(a)
    b_ext = to_extended(b)
    
    # Check for division by zero
    if b_ext.real_part == 0 and b_ext.indet_coeff == 0:
        # Division by zero: x/0 = I (Axiom 23)
        if a_ext.real_part == 0 and a_ext.indet_coeff == 0:
            # 0/0 is still indeterminate but needs special handling
            return ExtendedElement(0, 1)  # Return I
        else:
            # x/0 = I for x ≠ 0
            return ExtendedElement(0, 1)
    
    # Divisão por I dá I, como na biblioteca Indet (Lean): x / 𝕀 = 𝕀. Antes lançava
    # ValueError, citando um "Axiom I4" que em python/indeterminate.py é a absorção
    # (I ⊕ κ = I, I ⊗ κ = I); a absorção é o que vale aqui também.
    if b_ext.is_pure_indeterminate() or a_ext.is_pure_indeterminate():
        return ExtendedElement(0, 1)
    
    # Standard division for field elements
    if a_ext.is_field_element() and b_ext.is_field_element():
        return ExtendedElement(a_ext.real_part / b_ext.real_part, 0)
    
    # General case: would require field inverse operations
    # For now, handle simple cases
    if b_ext.indet_coeff == 0:
        # Dividing by a pure field element
        result_real = a_ext.real_part / b_ext.real_part
        result_indet = a_ext.indet_coeff / b_ext.real_part
        return ExtendedElement(result_real, result_indet, a_ext.indeterminate)
    
    # Complex division would require rationalization
    raise NotImplementedError("General division in K_I not yet implemented")


def power(a: AlgebraElement, n: int) -> ExtendedElement:
    """
    Exponentiation in K_I.
    
    Implements Axiom I5: I^n = I for all n ∈ ℕ
    
    Args:
        a: Base element
        n: Exponent (positive integer)
        
    Returns:
        The power in K_I
    """
    if n < 0:
        raise ValueError("Negative exponents require multiplicative inverse")
    
    a_ext = to_extended(a)
    
    # I^n = I for all n ≥ 1
    if a_ext.is_pure_indeterminate():
        if n == 0:
            # I^0 is ambiguous; we define it as 1 by convention
            return ExtendedElement(1, 0)
        return a_ext  # I^n = I
    
    # 0^0 = 1 by convention
    if n == 0:
        return ExtendedElement(1, 0)
    
    # For field elements, use standard exponentiation
    if a_ext.is_field_element():
        return ExtendedElement(a_ext.real_part ** n, 0)
    
    # General case: repeated multiplication
    result = ExtendedElement(1, 0)
    for _ in range(n):
        result = multiply(result, a_ext)
    
    return result


def negate(a: AlgebraElement) -> ExtendedElement:
    """
    Additive inverse in K_I.
    
    Args:
        a: Element to negate
        
    Returns:
        The additive inverse -a
    """
    a_ext = to_extended(a)
    return ExtendedElement(-a_ext.real_part, -a_ext.indet_coeff, a_ext.indeterminate)


# Convenience functions for common operations

def add_I(a: AlgebraElement) -> ExtendedElement:
    """Add I to an element (demonstrating absorption)."""
    return add(a, I)


def multiply_I(a: AlgebraElement) -> ExtendedElement:
    """Multiply an element by I (demonstrating absorption)."""
    return multiply(a, I)


def is_zero(a: AlgebraElement) -> bool:
    """Check if an element is zero."""
    a_ext = to_extended(a)
    return a_ext.real_part == 0 and a_ext.indet_coeff == 0


def equals(a: AlgebraElement, b: AlgebraElement) -> bool:
    """
    Check equality in K_I.
    
    Note: I ≠ λ for all λ ∈ K (Separation Axiom)
    """
    a_ext = to_extended(a)
    b_ext = to_extended(b)
    return a_ext == b_ext


# Corrective functions for Ω(I)

def omega_identity(i: Indeterminate) -> Indeterminate:
    """Default corrective function: Ω(I) = I"""
    return i


def omega_scaled(k: Union[int, float, complex]) -> Callable[[Indeterminate], ExtendedElement]:
    """
    Scaled corrective function: Ω(I) = k·I where k ∈ K \\ {0, 1}
    
    Args:
        k: Scaling factor from the base field
        
    Returns:
        A corrective function
    """
    if k == 0 or k == 1:
        raise ValueError("k must be in K \\ {0, 1}")
    
    def omega(i: Indeterminate) -> ExtendedElement:
        return ExtendedElement(0, k, i)
    
    return omega


def omega_nilpotent(epsilon: Union[int, float, complex]) -> Callable[[Indeterminate], ExtendedElement]:
    """
    Nilpotent corrective function: Ω(I) = I + ε where ε² = 0
    
    This is a more advanced construction for dual numbers.
    
    Args:
        epsilon: Nilpotent element (for symbolic purposes, just a marker)
        
    Returns:
        A corrective function
    """
    def omega(i: Indeterminate) -> ExtendedElement:
        # In practice, this would need a more sophisticated type system
        # For now, just return I + epsilon symbolically
        return ExtendedElement(epsilon, 1, i)
    
    return omega
