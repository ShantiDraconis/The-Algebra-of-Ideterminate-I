"""
The Algebra of Indeterminate I - Python Implementation

This package provides computational tools for working with the indeterminate
element I and extended algebraic structures.
"""

from .multistate import (
    IndeterminateState,
    MultiStateResult,
    ExtendedIndeterminate,
    subtract_I_from_I,
    divide_I_by_I,
    divide_I_by_zero,
    QuantumSuperposition,
    ContextDependentResolver,
)

from .extended_operations import (
    ExtendedElement,
    ExtendedNumber,
    ExtendedAlgebra,
    I, J, ZERO_I, I_ZERO, ZERO, ONE,
    multiply_with_inverse_solution,
    add_extended,
    power_extended,
    log_extended,
)

__all__ = [
    # Multi-state types
    'IndeterminateState',
    'MultiStateResult',
    'ExtendedIndeterminate',
    'subtract_I_from_I',
    'divide_I_by_I',
    'divide_I_by_zero',
    'QuantumSuperposition',
    'ContextDependentResolver',
    
    # Extended operations
    'ExtendedElement',
    'ExtendedNumber',
    'ExtendedAlgebra',
    'I', 'J', 'ZERO_I', 'I_ZERO', 'ZERO', 'ONE',
    'multiply_with_inverse_solution',
    'add_extended',
    'power_extended',
    'log_extended',
]

__version__ = '0.1.0'
