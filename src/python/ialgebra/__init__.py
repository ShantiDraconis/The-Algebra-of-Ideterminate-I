"""
I-Algebra: Algebra of Indeterminate I

A Python implementation of algebraic operations with indeterminate elements,
supporting multiple semantic modes and validation of algebraic invariants.

Note: This library follows Python logging best practices. By default, it uses
NullHandler and produces no output. Applications should configure logging as needed.
For interactive use, the REPL automatically configures logging to display
semantic decisions.
"""

from .types import IElement, IExpr, SemanticsMode
from .operations import oplus, ominus, otimes, odiv, _ensure_logging_configured

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
