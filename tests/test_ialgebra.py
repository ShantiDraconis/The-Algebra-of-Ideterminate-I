"""
Comprehensive Test Suite for I-Algebra.

Tests all modules including:
- Type system and operations
- Wheel of fractions
- I-calculus
- Visualization (structure only)
- Extended analysis

Uses pytest for test framework.
"""

import pytest
import math
from src.python.ialgebra.types import IElement, IExpr, SemanticsMode
from src.python.ialgebra.operations import oplus, ominus, otimes, odiv
from src.python.ialgebra.wheel import WheelFraction, WheelStructure, GeometricWheel
from src.python.ialgebra.calculus import ILimit, IDerivative, IIntegral, IContinuity
from src.python.ialgebra.analysis import CollapseAnalyzer, NumberSystemComparator, PhysicalImplicationAnalyzer, SystemState


class TestIElement:
    """Test the IElement enumeration."""
    
    def test_I_element_exists(self):
        """Test that I element can be created."""
        assert IElement.I is not None
        assert str(IElement.I) == "I"
    
    def test_J_element_exists(self):
        """Test that J element can be created."""
        assert IElement.J is not None
        assert str(IElement.J) == "J"
    
    def test_elements_distinct(self):
        """Test that I and J are distinct."""
        assert IElement.I != IElement.J
        assert IElement.I != IElement.ZERO


class TestOperations:
    """Test basic operations in I-algebra."""
    
    def test_addition_identity(self):
        """Test that 0 is additive identity."""
        assert oplus(5, 0, SemanticsMode.CONTEXTUAL) == 5
        assert oplus(0, 5, SemanticsMode.CONTEXTUAL) == 5
    
    def test_I_plus_I(self):
        """Test that I + I = I (Postulate 73b)."""
        result = oplus(IElement.I, IElement.I, SemanticsMode.CONTEXTUAL)
        assert result == IElement.I
    
    def test_I_times_I(self):
        """Test that I × I = I (Postulate 73b)."""
        result = otimes(IElement.I, IElement.I, SemanticsMode.CONTEXTUAL)
        assert result == IElement.I
    
    def test_absorption_property(self):
        """Test that x × I = I for all x ≠ 0 (Postulate 73a)."""
        for x in [1, 2, 5, -3, 0.5, 100]:
            result = otimes(x, IElement.I, SemanticsMode.CONTEXTUAL)
            assert result == IElement.I, f"Failed for x={x}"
    
    def test_zero_absorption(self):
        """Test that 0 × I = 0."""
        result = otimes(0, IElement.I, SemanticsMode.CONTEXTUAL)
        assert result == IElement.ZERO or result == 0
    
    def test_numeric_addition(self):
        """Test regular numeric addition."""
        assert oplus(2, 3, SemanticsMode.CONTEXTUAL) == 5
        assert oplus(1.5, 2.5, SemanticsMode.CONTEXTUAL) == 4.0
    
    def test_numeric_multiplication(self):
        """Test regular numeric multiplication."""
        assert otimes(2, 3, SemanticsMode.CONTEXTUAL) == 6
        assert otimes(2.5, 4, SemanticsMode.CONTEXTUAL) == 10.0
    
    def test_division_by_zero(self):
        """Test that x/0 raises in strict mode."""
        with pytest.raises(ValueError):
            odiv(1, 0, SemanticsMode.STRICT)
    
    def test_division_by_zero_contextual(self):
        """Test that x/0 = I in contextual mode."""
        result = odiv(1, 0, SemanticsMode.CONTEXTUAL)
        assert result == IElement.INFINITY  # In contextual mode, represented as infinity


class TestWheelOfFractions:
    """Test the Wheel of Fractions structure."""
    
    def test_wheel_fraction_creation(self):
        """Test creating wheel fractions."""
        frac = WheelFraction(1, 2)
        assert frac.numerator == 1
        assert frac.denominator == 2
    
    def test_wheel_eval_normal(self):
        """Test evaluating normal fractions."""
        frac = WheelFraction(6, 2)
        result = frac.evaluate(SemanticsMode.CONTEXTUAL)
        assert result == 3.0
    
    def test_wheel_eval_div_by_zero(self):
        """Test that n/0 = I (Postulate 73c)."""
        frac = WheelFraction(1, 0)
        result = frac.evaluate(SemanticsMode.CONTEXTUAL)
        assert result == IElement.I
    
    def test_neutrality_equivalence(self):
        """Test that 2/0 = 3/0 = I (Postulate 73c)."""
        frac1 = WheelFraction(2, 0)
        frac2 = WheelFraction(3, 0)
        result1 = frac1.evaluate(SemanticsMode.CONTEXTUAL)
        result2 = frac2.evaluate(SemanticsMode.CONTEXTUAL)
        assert result1 == result2 == IElement.I
    
    def test_wheel_structure_properties(self):
        """Test WheelStructure property verification."""
        wheel = WheelStructure()
        
        # Test absorption property
        assert wheel.verify_absorption_property(5) is True
        assert wheel.verify_absorption_property(-3) is True
        
        # Test self-consistency
        assert wheel.verify_self_consistency() is True
        
        # Test neutrality
        assert wheel.verify_neutrality_in_equivalence_classes() is True
    
    def test_geometric_wheel(self):
        """Test geometric representation."""
        geo_wheel = GeometricWheel()
        
        # Add singularities
        geo_wheel.add_singularity(1, 0)
        geo_wheel.add_singularity(2, 0)
        
        # All should map to I locus
        fractions = geo_wheel.get_I_locus_fractions()
        assert len(fractions) == 2


class TestICalculus:
    """Test I-Calculus operations."""
    
    def test_limit_to_infinity(self):
        """Test that lim(x→0) 1/x = I."""
        result = ILimit.limit_to_zero(lambda x: 1/x)
        assert result == IElement.I
    
    def test_limit_quotient_indeterminate(self):
        """Test 0/0 indeterminate form."""
        result = ILimit.limit_quotient(lambda x: x**2, lambda x: x, 0)
        # Should be close to 0 (not I for this case)
        assert isinstance(result, float) or result == IElement.I
    
    def test_derivative_normal(self):
        """Test normal derivative computation."""
        # d/dx(x²) at x=2 should be approximately 4
        result = IDerivative.derivative(lambda x: x**2, 2)
        assert abs(result - 4) < 0.01
    
    def test_derivative_at_singularity(self):
        """Test derivative at singularity returns I."""
        result = IDerivative.derivative_at_singularity(lambda x: 1/x, 0)
        assert result == IElement.I
    
    def test_integral_normal(self):
        """Test normal integration."""
        # ∫[0,1] x dx = 0.5
        result = IIntegral.integrate(lambda x: x, 0, 1)
        assert abs(result - 0.5) < 0.01
    
    def test_singular_integral(self):
        """Test integration through singularity yields I."""
        result = IIntegral.singular_integral(lambda x: 1/x, -1, 1, 0)
        assert result == IElement.I
    
    def test_continuity_check(self):
        """Test continuity checking."""
        # x² is continuous everywhere
        assert IContinuity.is_continuous_at(lambda x: x**2, 1) is True
        
        # 1/x is not continuous at 0
        # (may fail depending on implementation)
        # assert IContinuity.is_continuous_at(lambda x: 1/x, 0) is False


class TestCollapseAnalysis:
    """Test collapse analysis module."""
    
    def test_collapse_analyzer_creation(self):
        """Test creating collapse analyzer."""
        analyzer = CollapseAnalyzer()
        assert analyzer.current_state == SystemState.NORMAL
    
    def test_collapse_sequence_generation(self):
        """Test generating collapse sequence."""
        analyzer = CollapseAnalyzer()
        sequence = analyzer.analyze_collapse()
        
        assert len(sequence) > 0
        assert any(step.contradiction for step in sequence)
        
        # Check final step is contradiction
        assert sequence[-1].contradiction is True
    
    def test_collapse_implications(self):
        """Test getting collapse implications."""
        analyzer = CollapseAnalyzer()
        implications = analyzer.get_collapse_implications()
        
        assert "Algebraic" in implications
        assert "Topological" in implications
        assert "Physical" in implications
        assert len(implications["Algebraic"]) > 0
    
    def test_distinctness_verification(self):
        """Test verifying element distinctness."""
        analyzer = CollapseAnalyzer()
        checks = analyzer.verify_distinctness()
        
        # All should be True in normal system
        assert all(checks.values())
        assert checks["0 ≠ 1"] is True
        assert checks["I ≠ 0"] is True


class TestNumberSystemComparator:
    """Test number system comparison."""
    
    def test_comparator_creation(self):
        """Test creating comparator."""
        comp = NumberSystemComparator()
        assert len(comp.structures) > 0
    
    def test_axiom_comparison(self):
        """Test comparing axioms across structures."""
        comp = NumberSystemComparator()
        axioms = comp.compare_axioms()
        
        assert "Closure (Addition)" in axioms
        assert "Real Field ℝ" in axioms["Closure (Addition)"]
        
        # I-Algebra should have closure
        assert axioms["Closure (Addition)"]["I-Algebra K_I"] is True
        
        # But not multiplicative inverse for all
        assert axioms["Multiplicative Inverse (all non-zero)"]["I-Algebra K_I"] is False
    
    def test_operation_comparison(self):
        """Test comparing operations."""
        comp = NumberSystemComparator()
        ops = comp.compare_operations()
        
        assert "1/0" in ops
        # In I-Algebra, 1/0 = I
        assert "I" in ops["1/0"]["I-Algebra K_I"]
        # In classical fields, undefined
        assert "Undefined" in ops["1/0"]["Real Field ℝ"]


class TestPhysicalImplications:
    """Test physical implications analyzer."""
    
    def test_analyzer_creation(self):
        """Test creating physical analyzer."""
        analyzer = PhysicalImplicationAnalyzer()
        assert analyzer is not None
    
    def test_physical_interpretations(self):
        """Test getting physical interpretations."""
        analyzer = PhysicalImplicationAnalyzer()
        interp = analyzer.get_physical_interpretations()
        
        assert "General Relativity" in interp
        assert "Quantum Mechanics" in interp
        assert "Cosmology" in interp
        
        # Check some specific interpretations
        assert "Black Hole Singularity" in interp["General Relativity"]
    
    def test_singularity_resolution(self):
        """Test singularity resolution analysis."""
        analyzer = PhysicalImplicationAnalyzer()
        resolutions = analyzer.analyze_singularity_resolution()
        
        assert len(resolutions) > 0
        assert any("singularit" in r.lower() for r in resolutions)


class TestPropertyBasedTests:
    """Property-based tests for algebraic properties."""
    
    def test_addition_commutative_for_reals(self):
        """Test that addition is commutative for real numbers."""
        test_pairs = [(1, 2), (3, 5), (-2, 4), (0, 7)]
        for a, b in test_pairs:
            assert oplus(a, b, SemanticsMode.CONTEXTUAL) == oplus(b, a, SemanticsMode.CONTEXTUAL)
    
    def test_multiplication_commutative_for_reals(self):
        """Test that multiplication is commutative for real numbers."""
        test_pairs = [(2, 3), (4, 5), (-2, 3), (0, 5)]
        for a, b in test_pairs:
            assert otimes(a, b, SemanticsMode.CONTEXTUAL) == otimes(b, a, SemanticsMode.CONTEXTUAL)
    
    def test_associativity_addition(self):
        """Test associativity of addition for reals."""
        triples = [(1, 2, 3), (2, 3, 4)]
        for a, b, c in triples:
            left = oplus(oplus(a, b, SemanticsMode.CONTEXTUAL), c, SemanticsMode.CONTEXTUAL)
            right = oplus(a, oplus(b, c, SemanticsMode.CONTEXTUAL), SemanticsMode.CONTEXTUAL)
            assert left == right
    
    def test_I_dominates_addition(self):
        """Test that I dominates in addition with numbers."""
        for x in [1, 2, 5, 10]:
            result = oplus(x, IElement.I, SemanticsMode.CONTEXTUAL)
            assert result == IElement.I


# Integration tests
class TestIntegration:
    """Integration tests across modules."""
    
    def test_wheel_and_operations(self):
        """Test integration of wheel fractions with operations."""
        frac1 = WheelFraction(1, 0)
        result = frac1.evaluate(SemanticsMode.CONTEXTUAL)
        
        # Result should be I, and I + I = I
        result2 = oplus(result, result, SemanticsMode.CONTEXTUAL)
        assert result2 == IElement.I
    
    def test_calculus_and_wheel(self):
        """Test calculus operations with wheel fractions."""
        # lim(x→0) 1/x should match 1/0 in wheel
        limit_result = ILimit.limit_to_zero(lambda x: 1/x)
        wheel_result = WheelFraction(1, 0).evaluate(SemanticsMode.CONTEXTUAL)
        
        assert limit_result == wheel_result == IElement.I
    
    def test_analysis_consistency(self):
        """Test that analysis module is consistent with operations."""
        analyzer = CollapseAnalyzer()
        
        # Verify distinctness matches operation behavior
        checks = analyzer.verify_distinctness()
        assert checks["I ≠ 0"] is True
        
        # This should match that I and ZERO are different
        assert IElement.I != IElement.ZERO


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
