from ialgebra.types import IConst
from ialgebra.operations import oplus
from ialgebra.printing import pretty


def test_sanity():
    """Test basic operation creation and pretty printing.
    
    Verifies that the oplus operation can be created with the indeterminate
    constant I and a numeric value, and that the pretty printer correctly
    includes the ⊕ operator symbol in the output.
    """
    expr = oplus(IConst.I, 0)
    assert "⊕" in pretty(expr)
