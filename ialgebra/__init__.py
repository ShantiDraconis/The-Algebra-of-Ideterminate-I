"""
The Algebra of Indeterminate I

A computational algebra system for the indeterminate element I with flexible resolution.
"""

from .types import (
    ElementType,
    FieldElement,
    Indeterminate,
    ExtendedElement,
    I,
    AlgebraElement,
    to_extended,
    is_indeterminate_element
)

from .operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    negate,
    add_I,
    multiply_I,
    is_zero,
    equals,
    omega_identity,
    omega_scaled,
    omega_nilpotent
)

from .flexible_resolution import (
    ResolutionStrategy,
    ResolutionContext,
    FlexibleIndeterminateSystem,
    create_system,
    resolve_locally,
    check_collapse
)

__version__ = "0.1.0"

__all__ = [
    # Types
    "ElementType",
    "FieldElement",
    "Indeterminate",
    "ExtendedElement",
    "I",
    "AlgebraElement",
    "to_extended",
    "is_indeterminate_element",
    # Operations
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "negate",
    "add_I",
    "multiply_I",
    "is_zero",
    "equals",
    "omega_identity",
    "omega_scaled",
    "omega_nilpotent",
    # Flexible Resolution
    "ResolutionStrategy",
    "ResolutionContext",
    "FlexibleIndeterminateSystem",
    "create_system",
    "resolve_locally",
    "check_collapse",
]
