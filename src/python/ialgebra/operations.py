from __future__ import annotations
from .types import Atom, IConst, IExpr, SemanticsMode

def oplus(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT):
    return IExpr("⊕", a, b)

def ominus(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT):
    return IExpr("⊖", a, b)

def otimes(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT):
    return IExpr("⊗", a, b)

def odiv(a: Atom, b: Atom, mode: SemanticsMode = SemanticsMode.STRICT):
    return IExpr("⊘", a, b)
