from __future__ import annotations
from .types import Atom, IExpr, SemanticsMode


def oplus(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT) -> IExpr:
    """Addition operation in the indeterminate algebra.
    
    The ⊕ operator represents addition extended to handle the indeterminate
    constant I = 0/0. This operation creates an expression tree node.
    
    Args:
        a: Left operand (numeric value or indeterminate constant)
        b: Right operand (numeric value or indeterminate constant)
        mode: Semantics mode for evaluation (reserved for future implementation)
        
    Returns:
        An IExpr node representing the addition operation
    """
    return IExpr("⊕", a, b)


def ominus(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT) -> IExpr:
    """Subtraction operation in the indeterminate algebra.
    
    The ⊖ operator represents subtraction extended to handle the indeterminate
    constant I = 0/0. This operation creates an expression tree node.
    
    Args:
        a: Left operand (numeric value or indeterminate constant)
        b: Right operand (numeric value or indeterminate constant)
        mode: Semantics mode for evaluation (reserved for future implementation)
        
    Returns:
        An IExpr node representing the subtraction operation
    """
    return IExpr("⊖", a, b)


def otimes(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT) -> IExpr:
    """Multiplication operation in the indeterminate algebra.
    
    The ⊗ operator represents multiplication extended to handle the indeterminate
    constant I = 0/0. This operation creates an expression tree node.
    
    Args:
        a: Left operand (numeric value or indeterminate constant)
        b: Right operand (numeric value or indeterminate constant)
        mode: Semantics mode for evaluation (reserved for future implementation)
        
    Returns:
        An IExpr node representing the multiplication operation
    """
    return IExpr("⊗", a, b)


def odiv(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT) -> IExpr:
    """Division operation in the indeterminate algebra.
    
    The ⊘ operator represents division extended to handle the indeterminate
    constant I = 0/0. This operation creates an expression tree node.
    
    Args:
        a: Left operand (numeric value or indeterminate constant)
        b: Right operand (numeric value or indeterminate constant)
        mode: Semantics mode for evaluation (reserved for future implementation)
        
    Returns:
        An IExpr node representing the division operation
    """
    return IExpr("⊘", a, b)
