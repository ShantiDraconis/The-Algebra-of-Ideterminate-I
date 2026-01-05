"""
I-Algebra: Algebra of Indeterminate I

A Python implementation of algebraic operations with indeterminate elements,
supporting multiple semantic modes and validation of algebraic invariants.
"""

from .types import IElement, IExpr, SemanticsMode
from .operations import oplus, ominus, otimes, odiv

__version__ = "0.1.0"
__all__ = [
    "IElement",
    "IExpr",
    "SemanticsMode",
    "oplus",
    "ominus",
    "otimes",
    "odiv",
]
