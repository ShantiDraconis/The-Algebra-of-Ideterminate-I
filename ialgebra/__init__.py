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
]
