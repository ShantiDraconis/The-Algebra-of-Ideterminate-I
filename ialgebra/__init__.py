"""
The Indeterminate Extended Algebra (IEA) Package

This package implements the Indeterminate Extended Algebra (IEA),
a non-field algebraic structure that consistently handles division by zero
and related singularities through the indeterminate element I.

Main modules:
- types: Core type definitions for IEA elements
- operations: Modified algebraic operations
- axioms: Fundamental axioms and verification

Author: IEA Implementation
Date: 2026-01-05
"""

from .types import IEAElement, ElementType, IndeterminateForm
from .operations import IEAOperations, IEAAxioms
from .axioms import IEAFundamentalAxioms, FieldAxiomFailures
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
    "IEAElement",
    "ElementType",
    "IndeterminateForm",
    # Operations
    "IEAOperations",
    "IEAAxioms",
    # Axioms
    "IEAFundamentalAxioms",
    "FieldAxiomFailures",
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
