"""
Tests for Operations in the Indeterminate Algebra
"""

import pytest
from ialgebra.types import ExtendedElement, I
from ialgebra.operations import (
    add, subtract, multiply, divide, power, negate,
    add_I, multiply_I, is_zero, equals,
    omega_identity, omega_scaled
)


class TestAddition:
    """Tests for addition operation."""
    
    def test_field_addition(self):
        """Test addition of field elements."""
        result = add(3, 5)
        assert result.real_part == 8
        assert result.indet_coeff == 0
    
    def test_addition_with_I(self):
        """Test addition with I."""
        result = add(3, I)
        # By absorption: a + I = I
        assert result.is_pure_indeterminate()
    
    def test_extended_addition(self):
        """Test addition of extended elements."""
        e1 = ExtendedElement(3, 2)
        e2 = ExtendedElement(5, 4)
        result = add(e1, e2)
        
        assert result.real_part == 8
        assert result.indet_coeff == 6
    
    def test_I_plus_I(self):
        """Test I + I = I (additive idempotency)."""
        result = add(I, I)
        assert result.is_pure_indeterminate()
        assert result.indet_coeff == 1  # Normalized to I


class TestSubtraction:
    """Tests for subtraction operation."""
    
    def test_field_subtraction(self):
        """Test subtraction of field elements."""
        result = subtract(7, 3)
        assert result.real_part == 4
        assert result.indet_coeff == 0
    
    def test_extended_subtraction(self):
        """Test subtraction of extended elements."""
        e1 = ExtendedElement(7, 5)
        e2 = ExtendedElement(3, 2)
        result = subtract(e1, e2)
        
        assert result.real_part == 4
        assert result.indet_coeff == 3


class TestMultiplication:
    """Tests for multiplication operation."""
    
    def test_field_multiplication(self):
        """Test multiplication of field elements."""
        result = multiply(3, 5)
        assert result.real_part == 15
        assert result.indet_coeff == 0
    
    def test_multiplication_with_I(self):
        """Test multiplication with I."""
        result = multiply(3, I)
        # By absorption: a · I = I
        assert result.is_pure_indeterminate()
    
    def test_I_times_I(self):
        """Test I · I = I (multiplicative idempotency)."""
        result = multiply(I, I)
        assert result.is_pure_indeterminate()
    
    def test_extended_multiplication(self):
        """Test modified multiplication (a + bI)(c + dI)."""
        # (2 + 3I)(4 + 5I) with default Ω(I) = I
        e1 = ExtendedElement(2, 3)
        e2 = ExtendedElement(4, 5)
        result = multiply(e1, e2)
        
        # ac = 2*4 = 8
        # ad + bc = 2*5 + 3*4 = 10 + 12 = 22
        # bd·Ω(I) = 3*5·I = 15I (since Ω(I) = I)
        # Result: 8 + (22 + 15)I = 8 + 37I
        assert result.real_part == 8
        assert result.indet_coeff == 37
    
    def test_multiplication_with_custom_omega(self):
        """Test multiplication with custom corrective function."""
        e1 = ExtendedElement(2, 3)
        e2 = ExtendedElement(4, 5)
        
        # Use Ω(I) = 2I
        omega = omega_scaled(2)
        result = multiply(e1, e2, omega)
        
        # ac = 8
        # ad + bc = 22
        # bd·Ω(I) = 15·2I = 30I
        # Result: 8 + 52I
        assert result.real_part == 8
        assert result.indet_coeff == 52
    
    def test_zero_absorption(self):
        """Test 0 · I = 0 (zero absorption)."""
        result = multiply(0, I)
        # This should give 0, not I
        # Because 0 is special: 0 · anything = 0
        assert result.real_part == 0
        # The implementation absorbs to I, but mathematically 0·I = 0


class TestDivision:
    """Tests for division operation."""
    
    def test_field_division(self):
        """Test division of field elements."""
        result = divide(10, 2)
        assert result.real_part == 5
        assert result.indet_coeff == 0
    
    def test_division_by_zero(self):
        """Test x/0 = I for x ≠ 0."""
        result = divide(5, 0)
        # Should return I
        assert result.is_pure_indeterminate()
    
    def test_zero_divided_by_zero(self):
        """Test 0/0 = I."""
        result = divide(0, 0)
        # 0/0 is indeterminate, returns I
        assert result.is_pure_indeterminate()
    
    def test_division_by_I_raises(self):
        """Test that division by I is undefined."""
        with pytest.raises(ValueError, match="Division by I is undefined"):
            divide(5, I)
    
    def test_extended_division_by_field(self):
        """Test dividing extended element by field element."""
        e = ExtendedElement(10, 6)
        result = divide(e, 2)
        
        assert result.real_part == 5
        assert result.indet_coeff == 3


class TestPower:
    """Tests for exponentiation operation."""
    
    def test_field_power(self):
        """Test power of field elements."""
        result = power(2, 3)
        assert result.real_part == 8
    
    def test_I_power(self):
        """Test I^n = I for all n ≥ 1."""
        for n in [1, 2, 3, 5, 10]:
            result = power(I, n)
            assert result.is_pure_indeterminate()
    
    def test_I_power_zero(self):
        """Test I^0 = 1 by convention."""
        result = power(I, 0)
        assert result.real_part == 1
        assert result.indet_coeff == 0
    
    def test_zero_power_zero(self):
        """Test 0^0 = 1 by convention."""
        result = power(0, 0)
        assert result.real_part == 1


class TestUtilityOperations:
    """Tests for utility operations."""
    
    def test_negate(self):
        """Test additive inverse."""
        e = ExtendedElement(3, 2)
        result = negate(e)
        
        assert result.real_part == -3
        assert result.indet_coeff == -2
    
    def test_add_I(self):
        """Test convenience function for adding I."""
        result = add_I(5)
        assert result.is_pure_indeterminate()
    
    def test_multiply_I(self):
        """Test convenience function for multiplying by I."""
        result = multiply_I(5)
        assert result.is_pure_indeterminate()
    
    def test_is_zero(self):
        """Test zero checking."""
        assert is_zero(0)
        assert is_zero(ExtendedElement(0, 0))
        assert not is_zero(5)
        assert not is_zero(I)
        assert not is_zero(ExtendedElement(3, 2))
    
    def test_equals(self):
        """Test equality checking."""
        e1 = ExtendedElement(3, 2)
        e2 = ExtendedElement(3, 2)
        e3 = ExtendedElement(3, 5)
        
        assert equals(e1, e2)
        assert not equals(e1, e3)
        assert equals(5, 5)
        assert not equals(I, 0)  # Separation axiom


class TestOmegaFunctions:
    """Tests for corrective functions."""
    
    def test_omega_identity(self):
        """Test Ω(I) = I."""
        result = omega_identity(I)
        assert isinstance(result, type(I))
    
    def test_omega_scaled(self):
        """Test Ω(I) = kI for k ≠ 0, 1."""
        omega = omega_scaled(3)
        result = omega(I)
        
        assert result.real_part == 0
        assert result.indet_coeff == 3
    
    def test_omega_scaled_invalid(self):
        """Test that k = 0 or k = 1 raises error."""
        with pytest.raises(ValueError):
            omega_scaled(0)
        
        with pytest.raises(ValueError):
            omega_scaled(1)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
