from __future__ import annotations
from typing import Union
from .types import IExpr, IConst


def pretty(x: Union[IExpr, IConst, int, float]) -> str:
    """Convert an expression or value to a human-readable string representation.
    
    Recursively formats algebraic expressions with proper operator symbols and
    parentheses. Handles indeterminate constants (I, J), numeric values, and
    nested expression trees.
    
    Args:
        x: The value to format. Can be an IExpr node, IConst constant, or numeric value.
        
    Returns:
        A string representation with operators and values properly formatted
        
    Examples:
        >>> pretty(IConst.I)
        'I'
        >>> pretty(oplus(IConst.I, 0))
        '(I ⊕ 0)'
    """
    if isinstance(x, IExpr):
        return f"({pretty(x.a)} {x.op} {pretty(x.b)})"
    if isinstance(x, IConst):
        return x.value
    return str(x)
