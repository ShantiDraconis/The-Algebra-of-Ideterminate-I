"""
Tests for the Indeterminate Algebra Type System
"""

import pytest
from ialgebra.types import (
    FieldElement, Indeterminate, ExtendedElement, I,
    to_extended, is_indeterminate_element
)


class TestFieldElement:
    """Tests for FieldElement class."""
    
    def test_creation(self):
        """Test creating field elements."""
        e1 = FieldElement(5)
        assert e1.value == 5
        
        e2 = FieldElement(3.14)
        assert e2.value == 3.14
        
        e3 = FieldElement(2 + 3j)
        assert e3.value == 2 + 3j
    
    def test_equality(self):
        """Test field element equality."""
        e1 = FieldElement(5)
        e2 = FieldElement(5)
        e3 = FieldElement(7)
        
        assert e1 == e2
        assert e1 != e3
    
    def test_repr(self):
        """Test string representation."""
        e1 = FieldElement(5)
        assert str(e1) == "5"


class TestIndeterminate:
    """Tests for Indeterminate class."""
    
    def test_unresolved(self):
        """Test unresolved indeterminate."""
        i = Indeterminate()
        assert not i.is_resolved
        assert i.resolved_value is None
        assert str(i) == "I"
    
    def test_resolved(self):
        """Test resolved indeterminate."""
        i = Indeterminate(resolved_value=5)
        assert i.is_resolved
        assert i.resolved_value == 5
        assert str(i) == "I[=5]"
    
    def test_resolve_method(self):
        """Test resolving an indeterminate."""
        i1 = Indeterminate()
        i2 = i1.resolve(10)
        
        assert not i1.is_resolved
        assert i2.is_resolved
        assert i2.resolved_value == 10
    
    def test_singleton_I(self):
        """Test the singleton I."""
        assert not I.is_resolved
        assert str(I) == "I"
    
    def test_equality(self):
        """Test indeterminate equality."""
        i1 = Indeterminate()
        i2 = Indeterminate()
        i3 = Indeterminate(5)
        i4 = Indeterminate(5)
        i5 = Indeterminate(7)
        
        assert i1 == i2
        assert i3 == i4
        assert i3 != i5
        assert i1 != i3


class TestExtendedElement:
    """Tests for ExtendedElement class."""
    
    def test_field_element(self):
        """Test extended element that's just a field element."""
        e = ExtendedElement(5, 0)
        assert e.is_field_element()
        assert not e.is_pure_indeterminate()
        assert str(e) == "5"
    
    def test_pure_indeterminate(self):
        """Test pure indeterminate element."""
        e = ExtendedElement(0, 1)
        assert not e.is_field_element()
        assert e.is_pure_indeterminate()
        assert str(e) == "I"
    
    def test_general_form(self):
        """Test general extended element."""
        e = ExtendedElement(3, 2)
        assert not e.is_field_element()
        assert not e.is_pure_indeterminate()
        assert "3" in str(e) and "2I" in str(e)
    
    def test_resolve_indeterminate(self):
        """Test resolving I in an extended element."""
        e1 = ExtendedElement(3, 2)
        e2 = e1.resolve_indeterminate(5)
        
        assert not e1.indeterminate.is_resolved
        assert e2.indeterminate.is_resolved
        assert e2.indeterminate.resolved_value == 5
    
    def test_evaluate(self):
        """Test evaluating an extended element."""
        # Unresolved: should return None
        e1 = ExtendedElement(3, 2)
        assert e1.evaluate() is None
        
        # Resolved: should return numerical value
        e2 = ExtendedElement(3, 2, Indeterminate(5))
        assert e2.evaluate() == 3 + 2 * 5  # 13
        
        # Pure field element: should return value
        e3 = ExtendedElement(7, 0)
        assert e3.evaluate() == 7
    
    def test_equality(self):
        """Test extended element equality."""
        e1 = ExtendedElement(3, 2)
        e2 = ExtendedElement(3, 2)
        e3 = ExtendedElement(3, 5)
        
        assert e1 == e2
        assert e1 != e3
    
    def test_repr_variations(self):
        """Test various string representations."""
        assert str(ExtendedElement(0, 0)) == "0"
        assert str(ExtendedElement(5, 0)) == "5"
        assert str(ExtendedElement(0, 1)) == "I"
        assert str(ExtendedElement(0, -1)) == "-I"
        assert str(ExtendedElement(3, 1)) in ["3 + I", "I + 3"]
        assert str(ExtendedElement(3, -2)) in ["3 - 2I", "3 + -2I"]


class TestUtilityFunctions:
    """Tests for utility functions."""
    
    def test_to_extended(self):
        """Test converting to ExtendedElement."""
        # From int
        e1 = to_extended(5)
        assert e1.real_part == 5
        assert e1.indet_coeff == 0
        
        # From float
        e2 = to_extended(3.14)
        assert e2.real_part == 3.14
        
        # From complex
        e3 = to_extended(2 + 3j)
        assert e3.real_part == 2 + 3j
        
        # From FieldElement
        e4 = to_extended(FieldElement(7))
        assert e4.real_part == 7
        
        # From Indeterminate
        e5 = to_extended(I)
        assert e5.real_part == 0
        assert e5.indet_coeff == 1
        
        # From ExtendedElement
        e6 = ExtendedElement(3, 2)
        e7 = to_extended(e6)
        assert e6 == e7
    
    def test_is_indeterminate_element(self):
        """Test checking if element involves I."""
        assert is_indeterminate_element(I)
        assert is_indeterminate_element(ExtendedElement(0, 1))
        assert is_indeterminate_element(ExtendedElement(3, 2))
        assert not is_indeterminate_element(5)
        assert not is_indeterminate_element(FieldElement(5))
        assert not is_indeterminate_element(ExtendedElement(5, 0))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
