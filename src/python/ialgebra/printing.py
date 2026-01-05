from __future__ import annotations
from .types import IExpr, IConst


def pretty(x) -> str:
    if isinstance(x, IExpr):
        return f"({pretty(x.a)} {x.op} {pretty(x.b)})"
    if isinstance(x, IConst):
        return x.value
    return str(x)
