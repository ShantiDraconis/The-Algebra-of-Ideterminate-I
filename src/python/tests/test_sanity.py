from ialgebra.types import IConst
from ialgebra.operations import oplus
from ialgebra.printing import pretty


def test_sanity():
    expr = oplus(IConst.I, 0)
    assert "⊕" in pretty(expr)
