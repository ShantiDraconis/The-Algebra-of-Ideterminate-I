from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Union


class SemanticsMode(str, Enum):
    STRICT = "strict"
    CONTEXTUAL = "contextual"
    EXPERIMENTAL = "experimental"


class IConst(str, Enum):
    I = "I"  # 0/0
    J = "J"  # optional dual element


Atom = Union[int, float, IConst]


@dataclass(frozen=True)
class IExpr:
    """A minimal AST node for algebraic expressions.
    
    Represents a binary operation in the indeterminate algebra as an immutable
    expression tree node. Each node contains an operator and two operands which
    can themselves be expressions, constants, or numeric values.
    
    Attributes:
        op: The operator symbol (e.g., '⊕', '⊖', '⊗', '⊘')
        a: Left operand (can be Atom or nested IExpr)
        b: Right operand (can be Atom or nested IExpr)
    """

    op: str
    a: Atom | IExpr
    b: Atom | IExpr
