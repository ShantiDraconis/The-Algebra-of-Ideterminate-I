"""
Unit tests for multi-state I algebra and extended operations.

Tests cover:
- Multi-state operations (I - I, I / I, I / 0)
- Context-dependent resolution
- Quantum superposition analogy
- Extended operations (J, 0_I, I_0)
- Consistency properties
"""

import pytest
from ialgebra.multistate import (
    IndeterminateState,
    MultiStateResult,
    ExtendedIndeterminate,
    subtract_I_from_I,
    divide_I_by_I,
    divide_I_by_zero,
    QuantumSuperposition,
    ContextDependentResolver,
    create_equal_superposition,
    create_I_dominated_superposition,
)

from ialgebra.extended_operations import (
    ExtendedElement,
    ExtendedNumber,
    ExtendedAlgebra,
    I, J, ZERO_I, I_ZERO, ZERO, ONE,
    multiply_with_inverse_solution,
    add_extended,
    power_extended,
    log_extended,
)


class TestMultiStateOperations:
    """Test multi-state operations"""
    
    def test_subtract_I_from_I_states(self):
        """Test that I - I has correct possible states"""
        result = subtract_I_from_I()
        assert result.contains(IndeterminateState.ZERO)
        assert result.contains(IndeterminateState.I)
        assert result.contains(IndeterminateState.INDETERMINATE)
        assert not result.is_determinate()
    
    def test_divide_I_by_I_states(self):
        """Test that I / I has correct possible states"""
        result = divide_I_by_I()
        assert result.contains(IndeterminateState.ONE)
        assert result.contains(IndeterminateState.I)
        assert result.contains(IndeterminateState.INDETERMINATE)
        assert not result.is_determinate()
    
    def test_divide_I_by_zero_states(self):
        """Test that I / 0 has correct possible states"""
        result = divide_I_by_zero()
        assert result.contains(IndeterminateState.I)
        assert result.contains(IndeterminateState.INFINITY)
        assert result.contains(IndeterminateState.INDETERMINATE)
        assert not result.is_determinate()
    
    def test_multistate_result_string(self):
        """Test string representation of multi-state results"""
        result = subtract_I_from_I()
        result_str = str(result)
        # Should contain all three states in some order
        assert '0' in result_str or 'I' in result_str or '?' in result_str


class TestContextResolution:
    """Test context-dependent resolution"""
    
    def test_I_minus_I_limit_context(self):
        """Test I - I resolves to 0 in limit context"""
        resolver = ContextDependentResolver()
        result = subtract_I_from_I()
        resolved = resolver.resolve(result, "limit")
        assert resolved == IndeterminateState.ZERO
    
    def test_I_minus_I_standard_context(self):
        """Test I - I resolves to I in standard context"""
        resolver = ContextDependentResolver()
        result = subtract_I_from_I()
        resolved = resolver.resolve(result, "standard")
        assert resolved == IndeterminateState.I
    
    def test_I_div_I_standard_context(self):
        """Test I / I resolves to I in standard context"""
        resolver = ContextDependentResolver()
        result = divide_I_by_I()
        resolved = resolver.resolve(result, "standard")
        assert resolved == IndeterminateState.I
    
    def test_I_div_zero_infinity_context(self):
        """Test I / 0 resolves to ∞ in infinity context"""
        resolver = ContextDependentResolver()
        result = divide_I_by_zero()
        resolved = resolver.resolve(result, "infinity")
        assert resolved == IndeterminateState.INFINITY
    
    def test_resolution_history(self):
        """Test that resolver tracks resolution history"""
        resolver = ContextDependentResolver()
        result = subtract_I_from_I()
        
        resolver.resolve(result, "limit")
        resolver.resolve(result, "standard")
        
        history = resolver.get_history()
        assert len(history) == 2
        assert history[0]['context'] == "limit"
        assert history[1]['context'] == "standard"


class TestQuantumSuperposition:
    """Test quantum superposition analogy"""
    
    def test_equal_superposition_normalization(self):
        """Test equal superposition is normalized"""
        superpos = create_equal_superposition()
        total = abs(superpos.alpha)**2 + abs(superpos.beta)**2 + abs(superpos.gamma)**2
        assert abs(total - 1.0) < 0.01  # Allow small numerical error
    
    def test_I_dominated_normalization(self):
        """Test I-dominated superposition is normalized"""
        superpos = create_I_dominated_superposition()
        total = abs(superpos.alpha)**2 + abs(superpos.beta)**2 + abs(superpos.gamma)**2
        assert abs(total - 1.0) < 0.01
    
    def test_superposition_measurement(self):
        """Test measurement returns valid state"""
        superpos = create_equal_superposition()
        state = superpos.measure()
        assert state in [IndeterminateState.ZERO, IndeterminateState.I, IndeterminateState.INFINITY]
    
    def test_invalid_superposition(self):
        """Test that invalid superposition raises error"""
        with pytest.raises(ValueError):
            # Coefficients don't sum to 1
            QuantumSuperposition(alpha=0.5, beta=0.5, gamma=0.5)
    
    def test_superposition_string_representation(self):
        """Test string representation of superposition"""
        superpos = create_equal_superposition()
        result_str = str(superpos)
        assert '|0⟩' in result_str
        assert '|I⟩' in result_str
        assert '|∞⟩' in result_str


class TestExtendedOperations:
    """Test extended algebraic operations"""
    
    def test_I_mul_J_equals_one(self):
        """Test Solution 104.1: I · J = 1"""
        result = multiply_with_inverse_solution(I, J)
        assert result.value == 1
    
    def test_J_mul_I_equals_one(self):
        """Test commutativity: J · I = 1"""
        result = multiply_with_inverse_solution(J, I)
        assert result.value == 1
    
    def test_I_mul_I_equals_I(self):
        """Test idempotency: I · I = I"""
        result = multiply_with_inverse_solution(I, I)
        assert result.is_I()
    
    def test_zero_mul_I_equals_zeroI(self):
        """Test Solution 104.3: 0 · I = 0_I"""
        result = multiply_with_inverse_solution(ZERO, I)
        assert result.value == ExtendedElement.ZERO_I
    
    def test_I_add_zero_equals_Izero(self):
        """Test Solution 104.4: I + 0 = I_0"""
        result = add_extended(I, ZERO)
        assert result.value == ExtendedElement.I_ZERO
    
    def test_I_add_I_equals_I(self):
        """Test additive idempotency: I + I = I"""
        result = add_extended(I, I)
        assert result.is_I()
    
    def test_I_power_positive(self):
        """Test Solution 104.6: I^n = I for n > 0"""
        for n in [1, 2, 3, 5, 10]:
            result = power_extended(I, n)
            assert result.is_I(), f"I^{n} should equal I"
    
    def test_I_power_zero(self):
        """Test I^0 = 1"""
        result = power_extended(I, 0)
        assert result.value == 1
    
    def test_log_I_equals_J(self):
        """Test Solution 104.7: log(I) = J"""
        result = log_extended(I)
        assert result is not None
        assert result.is_J()
    
    def test_log_J_equals_I(self):
        """Test inverse: log(J) = I"""
        result = log_extended(J)
        assert result is not None
        assert result.is_I()
    
    def test_standard_real_arithmetic(self):
        """Test that standard real arithmetic is preserved"""
        a = ExtendedNumber(3)
        b = ExtendedNumber(4)
        
        sum_result = add_extended(a, b)
        assert sum_result.value == 7
        
        prod_result = multiply_with_inverse_solution(a, b)
        assert prod_result.value == 12


class TestExtendedAlgebra:
    """Test ExtendedAlgebra verification system"""
    
    def test_verify_inverse_solution(self):
        """Test verification of multiplicative inverse solution"""
        assert ExtendedAlgebra.verify_inverse_solution()
    
    def test_verify_zero_fix(self):
        """Test verification of zero multiplication fix"""
        assert ExtendedAlgebra.verify_zero_fix()
    
    def test_verify_additive_adjustment(self):
        """Test verification of additive identity adjustment"""
        assert ExtendedAlgebra.verify_additive_adjustment()
    
    def test_verify_exponentiation(self):
        """Test verification of exponentiation"""
        assert ExtendedAlgebra.verify_exponentiation()
    
    def test_verify_logarithm(self):
        """Test verification of logarithm"""
        assert ExtendedAlgebra.verify_logarithm()
    
    def test_verify_all(self):
        """Test that all verifications pass"""
        results = ExtendedAlgebra.verify_all()
        assert all(status == "PASS" for _, status in results)
    
    def test_can_cancel_I(self):
        """Test that I cannot be cancelled"""
        assert not ExtendedAlgebra.can_cancel(I)
    
    def test_can_cancel_nonzero_real(self):
        """Test that non-zero reals can be cancelled"""
        assert ExtendedAlgebra.can_cancel(ExtendedNumber(5))
    
    def test_cannot_cancel_zero(self):
        """Test that zero cannot be cancelled"""
        assert not ExtendedAlgebra.can_cancel(ZERO)


class TestConsistency:
    """Test overall system consistency"""
    
    def test_I_not_equal_zero(self):
        """Test I ≠ 0"""
        assert I != ZERO
    
    def test_I_not_equal_one(self):
        """Test I ≠ 1"""
        assert I != ONE
    
    def test_J_not_equal_I(self):
        """Test J ≠ I"""
        assert J != I
    
    def test_zeroI_not_equal_zero(self):
        """Test 0_I ≠ 0"""
        assert ZERO_I != ZERO
    
    def test_Izero_not_equal_I(self):
        """Test I_0 ≠ I"""
        assert I_ZERO != I
    
    def test_multistate_consistency(self):
        """Test that all multi-state operations are consistent"""
        operations = [
            subtract_I_from_I(),
            divide_I_by_I(),
            divide_I_by_zero(),
        ]
        
        for op in operations:
            # All operations should be non-determinate
            assert not op.is_determinate()
            
            # All should have at least one state
            assert len(op.states) > 0
            
            # Should resolve in all contexts
            resolver = ContextDependentResolver()
            for context in ["standard", "limit", "infinity"]:
                resolved = resolver.resolve(op, context)
                assert resolved in list(IndeterminateState)


class TestPropertyBased:
    """Property-based tests for algebraic properties"""
    
    def test_real_addition_commutative(self):
        """Test commutativity of real addition"""
        for a, b in [(2, 3), (5, 7), (1, 9)]:
            x = ExtendedNumber(a)
            y = ExtendedNumber(b)
            assert add_extended(x, y).value == add_extended(y, x).value
    
    def test_real_multiplication_commutative(self):
        """Test commutativity of real multiplication"""
        for a, b in [(2, 3), (5, 7), (1, 9)]:
            x = ExtendedNumber(a)
            y = ExtendedNumber(b)
            assert multiply_with_inverse_solution(x, y).value == \
                   multiply_with_inverse_solution(y, x).value
    
    def test_I_operations_idempotent(self):
        """Test that I is idempotent under key operations"""
        assert multiply_with_inverse_solution(I, I).is_I()
        assert add_extended(I, I).is_I()
    
    def test_power_chain(self):
        """Test I^(a+b) = I^a for positive a, b"""
        # Since I^n = I for all n > 0
        assert power_extended(I, 5).is_I()
        assert power_extended(I, 10).is_I()
        # Both should equal I


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
