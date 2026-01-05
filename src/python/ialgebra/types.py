"""
Types and data structures for I-Algebra.

This module defines the core types for working with the Algebra of Indeterminate I,
including element types, expression AST, and semantic modes.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Union, List, Optional


class IElement(Enum):
    """
    Enumeration of special elements in I-Algebra.
    
    - I: The indeterminate element (primary focus of the algebra)
    - J: Secondary indeterminate (if needed for extended operations)
    - ZERO: Additive identity
    - INFINITY: Unbounded element
    """
    I = "I"
    J = "J"
    ZERO = "0"
    INFINITY = "∞"
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"IElement.{self.name}"


class SemanticsMode(Enum):
    """
    Semantic interpretation modes for I-Algebra operations.
    
    - STRICT: Rigid rules, fails on ambiguous operations
    - CONTEXTUAL: Context-dependent interpretation of operations
    - EXPERIMENTAL: Allows experimental/exploratory operations
    """
    STRICT = "strict"
    CONTEXTUAL = "contextual"
    EXPERIMENTAL = "experimental"
    
    def __str__(self):
        return self.value


@dataclass
class IExpr:
    """
    Abstract Syntax Tree (AST) for algebraic expressions in I-Algebra.
    
    Represents expressions that can be:
    - Atomic elements (IElement or numeric values)
    - Binary operations (addition, subtraction, multiplication, division)
    - Unary operations (negation, etc.)
    """
    
    @dataclass
    class Atom:
        """Atomic value: IElement or numeric"""
        value: Union[IElement, float, int]
        
        def __str__(self):
            return str(self.value)
    
    @dataclass
    class BinaryOp:
        """Binary operation: left op right"""
        op: str  # '+', '-', '*', '/'
        left: 'IExpr'
        right: 'IExpr'
        
        def __str__(self):
            return f"({self.left} {self.op} {self.right})"
    
    @dataclass
    class UnaryOp:
        """Unary operation: op expr"""
        op: str  # '-', etc.
        expr: 'IExpr'
        
        def __str__(self):
            return f"({self.op}{self.expr})"
    
    expr: Union[Atom, BinaryOp, UnaryOp]
    
    def __str__(self):
        return str(self.expr)
    
    def __repr__(self):
        return f"IExpr({repr(self.expr)})"
    
    @staticmethod
    def atom(value: Union[IElement, float, int]) -> 'IExpr':
        """Create an atomic expression"""
        return IExpr(IExpr.Atom(value))
    
    @staticmethod
    def binary(op: str, left: 'IExpr', right: 'IExpr') -> 'IExpr':
        """Create a binary operation expression"""
        return IExpr(IExpr.BinaryOp(op, left, right))
    
    @staticmethod
    def unary(op: str, expr: 'IExpr') -> 'IExpr':
        """Create a unary operation expression"""
        return IExpr(IExpr.UnaryOp(op, expr))
    
    def is_atom(self) -> bool:
        """Check if expression is atomic"""
        return isinstance(self.expr, IExpr.Atom)
    
    def is_binary_op(self) -> bool:
        """Check if expression is a binary operation"""
        return isinstance(self.expr, IExpr.BinaryOp)
    
    def is_unary_op(self) -> bool:
        """Check if expression is a unary operation"""
        return isinstance(self.expr, IExpr.UnaryOp)
    
    def get_atom_value(self) -> Optional[Union[IElement, float, int]]:
        """Get the value if expression is atomic, None otherwise"""
        if self.is_atom():
            return self.expr.value
        return None
