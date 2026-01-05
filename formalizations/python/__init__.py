"""
The Algebra of the Indeterminate I - Python Implementation

This package provides computational models for the theoretical concepts from
"The Algebra of the Indeterminate I", including cardinal arithmetic with the
indeterminate element I, ultrapowers, and nonstandard analysis.

Modules:
    cardinal_arithmetic: Cardinal numbers and the indeterminate I
    ultrapowers: Ultrapower constructions and nonstandard analysis

Example:
    >>> from cardinal_arithmetic import Cardinal, CardinalArithmetic
    >>> kappa = Cardinal(5, CardinalType.FINITE)
    >>> result = CardinalArithmetic.subtract(kappa, kappa)
    >>> print(result)  # I
"""

__version__ = "1.0.0"
__author__ = "The Algebra of the Indeterminate I Project"

# Make key classes available at package level
from cardinal_arithmetic import (
    Cardinal,
    CardinalType,
    CardinalArithmetic,
    AxiomaticVerifier
)

__all__ = [
    'Cardinal',
    'CardinalType', 
    'CardinalArithmetic',
    'AxiomaticVerifier'
]
