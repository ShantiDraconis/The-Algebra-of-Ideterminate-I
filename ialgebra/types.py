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
Type System for the Indeterminate Algebra

This module defines the core types for expressions involving the indeterminate I,
including the flexible resolution framework where I can take context-dependent values.
"""

from typing import Union, Optional, Any
from dataclasses import dataclass
from enum import Enum


class ElementType(Enum):
    """Types of elements in the extended algebra K_I."""
    FIELD_ELEMENT = "field"  # Elements from base field K
    INDETERMINATE = "indeterminate"  # The indeterminate I
    EXTENDED = "extended"  # Elements of form a + bI


@dataclass(frozen=True)
class FieldElement:
    """
    An element from the base field K (typically ℝ or ℂ).
    
    Attributes:
        value: The numerical value (can be int, float, complex)
    """
    value: Union[int, float, complex]
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, FieldElement):
            return self.value == other.value
        return False
    
    def __hash__(self) -> int:
        return hash(self.value)


class Indeterminate:
    """
    The indeterminate element I with flexible resolution capability.
    
    In the flexible framework, I can be:
    1. An indeterminate constant (default, I ≠ 0)
    2. Specialized to a specific value α when required by problem context
    
    Properties:
        - I + I = I (additive idempotency)
        - I · I = I (multiplicative idempotency)
        - I ≠ 0, I ≠ 1 (separation axiom)
        - x/0 = I for all x ≠ 0 (division by zero)
    """
    
    def __init__(self, resolved_value: Optional[Union[int, float, complex]] = None):
        """
        Initialize the indeterminate I.
        
        Args:
            resolved_value: If provided, I is specialized to this value in context.
                          If None, I remains indeterminate.
        """
        self._resolved_value = resolved_value
        self._is_resolved = resolved_value is not None
    
    @property
    def is_resolved(self) -> bool:
        """Check if I has been specialized to a specific value."""
        return self._is_resolved
    
    @property
    def resolved_value(self) -> Optional[Union[int, float, complex]]:
        """Get the specialized value of I, if any."""
        return self._resolved_value
    
    def resolve(self, value: Union[int, float, complex]) -> 'Indeterminate':
        """
        Create a new Indeterminate specialized to a specific value.
        
        Args:
            value: The value to specialize I to
            
        Returns:
            A new Indeterminate instance with resolved value
        """
        return Indeterminate(resolved_value=value)
    
    def __repr__(self) -> str:
        if self._is_resolved:
            return f"I[={self._resolved_value}]"
        return "I"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Indeterminate):
            if self._is_resolved and other._is_resolved:
                return self._resolved_value == other._resolved_value
            return not self._is_resolved and not other._is_resolved
        return False
    
    def __hash__(self) -> int:
        if self._is_resolved:
            return hash(("I_resolved", self._resolved_value))
        return hash("I")


# Singleton instance for the unresolved indeterminate
I = Indeterminate()


@dataclass
class ExtendedElement:
    """
    An element of the extended algebra K_I = {a + bI | a, b ∈ K}.
    
    Represents expressions of the form a + bI where:
    - a is the "real" part (from base field K)
    - b is the "indeterminate" coefficient
    - I is the indeterminate element
    
    Attributes:
        real_part: Coefficient a from the base field K
        indet_coeff: Coefficient b of I from the base field K
        indeterminate: The indeterminate element (can be resolved or not)
    """
    real_part: Union[int, float, complex]
    indet_coeff: Union[int, float, complex]
    indeterminate: Indeterminate = I
    
    def __post_init__(self):
        """Validate the extended element."""
        if self.indet_coeff == 0:
            # If coefficient of I is zero, this reduces to a field element
            object.__setattr__(self, 'indeterminate', None)
    
    def is_field_element(self) -> bool:
        """Check if this element reduces to a pure field element (b = 0)."""
        return self.indet_coeff == 0
    
    def is_pure_indeterminate(self) -> bool:
        """Check if this is pure I (a = 0, b ≠ 0)."""
        return self.real_part == 0 and self.indet_coeff != 0
    
    def resolve_indeterminate(self, value: Union[int, float, complex]) -> 'ExtendedElement':
        """
        Resolve I to a specific value in this expression.
        
        Args:
            value: The value to substitute for I
            
        Returns:
            A new ExtendedElement with I resolved
        """
        if self.indeterminate is None:
            return self
        resolved_I = self.indeterminate.resolve(value)
        return ExtendedElement(self.real_part, self.indet_coeff, resolved_I)
    
    def evaluate(self) -> Optional[Union[int, float, complex]]:
        """
        Evaluate the expression if I is resolved.
        
        Returns:
            The numerical value if I is resolved, None otherwise
        """
        if self.indeterminate is None:
            return self.real_part
        if self.indeterminate.is_resolved:
            return self.real_part + self.indet_coeff * self.indeterminate.resolved_value
        return None
    
    def __repr__(self) -> str:
        if self.is_field_element():
            return str(self.real_part)
        if self.is_pure_indeterminate():
            if self.indet_coeff == 1:
                return str(self.indeterminate)
            elif self.indet_coeff == -1:
                return f"-{self.indeterminate}"
            return f"{self.indet_coeff}{self.indeterminate}"
        
        # General case: a + bI
        parts = []
        if self.real_part != 0:
            parts.append(str(self.real_part))
        if self.indet_coeff != 0:
            if self.indet_coeff == 1:
                parts.append(str(self.indeterminate))
            elif self.indet_coeff == -1:
                parts.append(f"-{self.indeterminate}")
            else:
                parts.append(f"{self.indet_coeff}{self.indeterminate}")
        
        if not parts:
            return "0"
        return " + ".join(parts).replace("+ -", "- ")
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ExtendedElement):
            return False
        return (self.real_part == other.real_part and 
                self.indet_coeff == other.indet_coeff and
                self.indeterminate == other.indeterminate)
    
    def __hash__(self) -> int:
        return hash((self.real_part, self.indet_coeff, self.indeterminate))


# Type alias for any element in the system
AlgebraElement = Union[FieldElement, Indeterminate, ExtendedElement, int, float, complex]


def to_extended(value: AlgebraElement) -> ExtendedElement:
    """
    Convert any algebra element to an ExtendedElement.
    
    Args:
        value: An element from K, I, or K_I
        
    Returns:
        An ExtendedElement representation
    """
    if isinstance(value, ExtendedElement):
        return value
    elif isinstance(value, Indeterminate):
        return ExtendedElement(0, 1, value)
    elif isinstance(value, FieldElement):
        return ExtendedElement(value.value, 0)
    elif isinstance(value, (int, float, complex)):
        return ExtendedElement(value, 0)
    else:
        raise TypeError(f"Cannot convert {type(value)} to ExtendedElement")


def is_indeterminate_element(value: AlgebraElement) -> bool:
    """
    Check if a value represents the indeterminate I.
    
    Args:
        value: An algebra element
        
    Returns:
        True if the value is or contains I
    """
    if isinstance(value, Indeterminate):
        return True
    if isinstance(value, ExtendedElement):
        return not value.is_field_element()
    return False
