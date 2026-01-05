"""
Types for the Indeterminate Extended Algebra (IEA)

This module defines the core types for working with the indeterminate element I
and the extended algebraic structure described in "Toward an Indeterminate 
Extended Algebra (IEA)".

Author: IEA Implementation
Date: 2026-01-05
"""

from __future__ import annotations
from enum import Enum
from typing import Union, Optional
from dataclasses import dataclass


class ElementType(Enum):
    """Types of elements in the IEA system."""
    REAL = "real"
    COMPLEX = "complex"
    INDETERMINATE = "indeterminate"  # I = 0/0
    IMAGINARY_SINGULARITY = "imaginary_singularity"  # J = iI
    INFINITY_POSITIVE = "infinity_positive"  # +∞
    INFINITY_NEGATIVE = "infinity_negative"  # -∞
    IMAGINARY_INFINITY_POSITIVE = "imaginary_infinity_positive"  # iI singularity
    IMAGINARY_INFINITY_NEGATIVE = "imaginary_infinity_negative"  # -iI singularity


@dataclass(frozen=True)
class IEAElement:
    """
    Represents an element in the Indeterminate Extended Algebra (IEA).
    
    The IEA extends the complex numbers with:
    - I: The indeterminate element (0/0)
    - J: The imaginary singularity (iI)
    - Infinities: +∞, -∞, iI, -iI
    
    Key properties:
    - I ≠ 0 (to prevent collapse)
    - I has no multiplicative inverse
    - Modified distributive law applies when I is present
    """
    value: Union[float, complex, str, None]
    element_type: ElementType
    
    def __repr__(self) -> str:
        """String representation of the element."""
        if self.element_type == ElementType.INDETERMINATE:
            return "I"
        elif self.element_type == ElementType.IMAGINARY_SINGULARITY:
            return "J"
        elif self.element_type == ElementType.INFINITY_POSITIVE:
            return "+∞"
        elif self.element_type == ElementType.INFINITY_NEGATIVE:
            return "-∞"
        elif self.element_type == ElementType.IMAGINARY_INFINITY_POSITIVE:
            return "iI"
        elif self.element_type == ElementType.IMAGINARY_INFINITY_NEGATIVE:
            return "-iI"
        elif self.element_type == ElementType.COMPLEX:
            return str(self.value)
        else:
            return str(self.value)
    
    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        if not isinstance(other, IEAElement):
            return False
        return self.value == other.value and self.element_type == other.element_type
    
    def __hash__(self) -> int:
        """Hash for use in sets and dicts."""
        return hash((self.value, self.element_type))
    
    @staticmethod
    def zero() -> IEAElement:
        """Return the zero element."""
        return IEAElement(0.0, ElementType.REAL)
    
    @staticmethod
    def one() -> IEAElement:
        """Return the one element."""
        return IEAElement(1.0, ElementType.REAL)
    
    @staticmethod
    def I() -> IEAElement:
        """
        Return the indeterminate element I.
        
        I = 0/0, the fundamental indeterminate element.
        Properties:
        - I ≠ 0
        - I has no multiplicative inverse
        - x/0 = I for all x ≠ 0
        """
        return IEAElement("I", ElementType.INDETERMINATE)
    
    @staticmethod
    def J() -> IEAElement:
        """
        Return the imaginary singularity J = iI.
        
        J is used in the modified distributive law:
        a(b + c) = ab + ac + λJ
        """
        return IEAElement("J", ElementType.IMAGINARY_SINGULARITY)
    
    @staticmethod
    def pos_infinity() -> IEAElement:
        """Return positive infinity +∞."""
        return IEAElement("+∞", ElementType.INFINITY_POSITIVE)
    
    @staticmethod
    def neg_infinity() -> IEAElement:
        """Return negative infinity -∞."""
        return IEAElement("-∞", ElementType.INFINITY_NEGATIVE)
    
    @staticmethod
    def imaginary_infinity() -> IEAElement:
        """Return imaginary infinity iI."""
        return IEAElement("iI", ElementType.IMAGINARY_INFINITY_POSITIVE)
    
    @staticmethod
    def neg_imaginary_infinity() -> IEAElement:
        """Return negative imaginary infinity -iI."""
        return IEAElement("-iI", ElementType.IMAGINARY_INFINITY_NEGATIVE)
    
    @staticmethod
    def real(value: float) -> IEAElement:
        """Create a real number element."""
        return IEAElement(value, ElementType.REAL)
    
    @staticmethod
    def complex_num(value: complex) -> IEAElement:
        """Create a complex number element."""
        return IEAElement(value, ElementType.COMPLEX)
    
    def is_indeterminate(self) -> bool:
        """Check if this element is I."""
        return self.element_type == ElementType.INDETERMINATE
    
    def is_imaginary_singularity(self) -> bool:
        """Check if this element is J."""
        return self.element_type == ElementType.IMAGINARY_SINGULARITY
    
    def is_singularity(self) -> bool:
        """Check if this element is any kind of singularity."""
        return self.element_type in [
            ElementType.INDETERMINATE,
            ElementType.IMAGINARY_SINGULARITY,
            ElementType.INFINITY_POSITIVE,
            ElementType.INFINITY_NEGATIVE,
            ElementType.IMAGINARY_INFINITY_POSITIVE,
            ElementType.IMAGINARY_INFINITY_NEGATIVE
        ]
    
    def is_real(self) -> bool:
        """Check if this element is a real number."""
        return self.element_type == ElementType.REAL
    
    def is_complex(self) -> bool:
        """Check if this element is a complex number."""
        return self.element_type == ElementType.COMPLEX
    
    def is_zero(self) -> bool:
        """Check if this element is zero."""
        return self.element_type == ElementType.REAL and self.value == 0.0


class IndeterminateForm(Enum):
    """
    Types of indeterminate forms in the IEA.
    
    All indeterminate forms map to I or related singularities.
    """
    ZERO_OVER_ZERO = "0/0"  # → I
    INFINITY_MINUS_INFINITY = "∞-∞"  # → I
    ZERO_TIMES_INFINITY = "0·∞"  # → I
    INFINITY_OVER_INFINITY = "∞/∞"  # → I
    ONE_TO_INFINITY = "1^∞"  # → I
    ZERO_TO_ZERO = "0^0"  # → I
    INFINITY_TO_ZERO = "∞^0"  # → I
