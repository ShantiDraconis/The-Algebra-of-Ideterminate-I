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
    """A minimal AST node for algebraic expressions."""
    op: str
    a: Atom | "IExpr"
    b: Atom | "IExpr"
