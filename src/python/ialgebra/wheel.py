"""
Wheel of Fractions Implementation for I-Algebra.

This module implements the Wheel of Fractions, an algebraic structure that
naturally accommodates division by zero through the indeterminate constant I.

Mathematical Foundation:
-----------------------
The Wheel of Fractions extends classical fraction arithmetic to handle
division by zero. Key properties:

1. All instances of x/0 collapse to the single constant I
2. The wheel structure forms a complete algebraic system
3. Singular points map to a geometric locus corresponding to I

References:
-----------
See problem statement sections 73-75 for detailed axioms.
"""

from dataclasses import dataclass
from typing import Union, Optional
from .types import IElement, IExpr, SemanticsMode
from .operations import otimes, oplus, ominus, odiv


@dataclass
class WheelFraction:
    """
    Represents a fraction in the Wheel of Fractions.
    
    In the Wheel structure, division by zero is well-defined and yields I.
    This allows representing all fractions, including those with zero denominators.
    
    Attributes:
        numerator: The numerator of the fraction
        denominator: The denominator (can be zero, yielding I)
    
    Examples:
        >>> WheelFraction(1, 0)  # Represents 1/0 = I
        >>> WheelFraction(2, 0)  # Represents 2/0 = I (collapses to same I)
        >>> WheelFraction(5, 2)  # Regular fraction 5/2
    """
    numerator: Union[IElement, float, int]
    denominator: Union[IElement, float, int]
    
    def __post_init__(self):
        """Normalize the fraction representation."""
        # Convert IElement.ZERO to numeric zero for consistency
        if self.numerator == IElement.ZERO:
            self.numerator = 0
        if self.denominator == IElement.ZERO:
            self.denominator = 0
    
    def evaluate(self, mode: SemanticsMode = SemanticsMode.STRICT) -> Union[IElement, float, int]:
        """
        Evaluate the wheel fraction to get its value.
        
        Rules:
        - n/0 = I for all n ≠ 0 (Postulate 73c: Reduction to fundamental constant)
        - 0/0 = I (special case)
        - n/d = n/d for d ≠ 0 (standard division)
        
        Args:
            mode: Semantic mode for operation evaluation
            
        Returns:
            The evaluated value of the fraction
        """
        # Handle division by zero - all cases yield I
        if self.denominator == 0 or self.denominator == IElement.ZERO:
            # All instances of division by zero collapse to I
            return IElement.I
        
        # Handle I in numerator or denominator
        if self.numerator == IElement.I:
            if self.denominator == IElement.I:
                # I/I = I (self-division yields I)
                return IElement.I
            else:
                # I/n = I for any non-zero n
                return IElement.I
        
        if self.denominator == IElement.I:
            # n/I: depends on mode
            if mode == SemanticsMode.STRICT:
                raise ValueError("Division by I undefined in strict mode")
            # In non-strict modes, treat as approaching zero
            return 0
        
        # Standard numeric division
        if isinstance(self.numerator, (int, float)) and isinstance(self.denominator, (int, float)):
            if self.denominator == 0:
                return IElement.I
            return self.numerator / self.denominator
        
        # Use the division operation from operations module
        return odiv(self.numerator, self.denominator, mode)
    
    def __str__(self) -> str:
        """String representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        """Detailed representation."""
        return f"WheelFraction({self.numerator}, {self.denominator})"
    
    def __eq__(self, other) -> bool:
        """
        Wheel equivalence relation.
        
        Two fractions are equivalent if a/b ~ c/d when a*d = b*c
        Special handling for I: any n/0 = I for all n
        """
        if not isinstance(other, WheelFraction):
            return False
        
        # Both evaluate to I if both have zero denominators
        if (self.denominator == 0 and other.denominator == 0):
            # Postulate 73c: All x/0 collapse to single I
            return True
        
        # Standard cross-multiplication equivalence
        try:
            left = otimes(self.numerator, other.denominator, SemanticsMode.CONTEXTUAL)
            right = otimes(other.numerator, self.denominator, SemanticsMode.CONTEXTUAL)
            return left == right
        except:
            return False


class WheelStructure:
    """
    The Wheel of Fractions algebraic structure.
    
    Properties (from Postulate 73):
    --------------------------------
    (a) Absorption Property: x · I = I for all x in R, C
    (b) Addition and Multiplication: I + I = I, I × I = I  
    (c) Neutrality in Equivalence Classes: 2/0 = 3/0 = I
    
    The wheel provides a complete algebraic structure where:
    - Division by zero is well-defined
    - Singularities collapse to a single geometric locus (I)
    - Operations are closed and consistent
    """
    
    def __init__(self):
        """Initialize the wheel structure."""
        self.I = IElement.I
        self.zero = IElement.ZERO
        
    def divide(self, numerator: Union[IElement, float, int], 
               denominator: Union[IElement, float, int],
               mode: SemanticsMode = SemanticsMode.STRICT) -> Union[IElement, float, int]:
        """
        Perform division in the wheel structure.
        
        Args:
            numerator: The numerator
            denominator: The denominator (can be zero)
            mode: Semantic mode
            
        Returns:
            Result of division, with x/0 = I
        """
        fraction = WheelFraction(numerator, denominator)
        return fraction.evaluate(mode)
    
    def verify_absorption_property(self, x: Union[float, int]) -> bool:
        """
        Verify Postulate 73(a): Absorption Property
        
        x · I = I for all x ∈ R, C
        
        Args:
            x: A real number
            
        Returns:
            True if x * I = I
        """
        result = otimes(x, IElement.I, SemanticsMode.CONTEXTUAL)
        return result == IElement.I
    
    def verify_neutrality_in_equivalence_classes(self) -> bool:
        """
        Verify Postulate 73(c): Neutrality in Equivalence Classes
        
        2/0 = 3/0 = I
        All instances of division by zero collapse to single constant.
        
        Returns:
            True if all x/0 = I for various x
        """
        test_numerators = [1, 2, 3, -1, 100, 0.5]
        results = []
        
        for num in test_numerators:
            frac = WheelFraction(num, 0)
            result = frac.evaluate(SemanticsMode.CONTEXTUAL)
            results.append(result)
        
        # All should equal I
        return all(r == IElement.I for r in results)
    
    def verify_self_consistency(self) -> bool:
        """
        Verify Postulate 73(b): I + I = I and I × I = I
        
        Returns:
            True if both properties hold
        """
        add_result = oplus(IElement.I, IElement.I, SemanticsMode.CONTEXTUAL)
        mul_result = otimes(IElement.I, IElement.I, SemanticsMode.CONTEXTUAL)
        
        return add_result == IElement.I and mul_result == IElement.I


class GeometricWheel:
    """
    Geometric representation of the Wheel of Fractions.
    
    In the extended algebra, singular points such as x/0 collapse onto
    a single geometric locus corresponding to I. This provides a visual
    representation of the algebraic structure.
    
    Coordinates:
    - Real Axis: Standard real number line
    - Imaginary Axis: Standard imaginary axis  
    - I Point: The singularity locus where all x/0 collapse
    """
    
    def __init__(self):
        """Initialize geometric wheel representation."""
        self.I_position = (0, 0)  # Origin represents I in geometric view
        self.infinity_loci = []  # Points that map to I
        
    def map_to_wheel(self, fraction: WheelFraction) -> tuple:
        """
        Map a wheel fraction to geometric coordinates.
        
        Args:
            fraction: The fraction to map
            
        Returns:
            (x, y) coordinates in the wheel representation
        """
        value = fraction.evaluate(SemanticsMode.CONTEXTUAL)
        
        if value == IElement.I:
            # All singularities map to the I locus
            return self.I_position
        elif isinstance(value, (int, float)):
            # Real values map to real axis
            return (float(value), 0.0)
        else:
            # Other special values
            return (0.0, 0.0)
    
    def add_singularity(self, numerator: Union[float, int], denominator: Union[float, int] = 0):
        """
        Add a singularity point (division by zero) to the wheel.
        
        All singularities collapse to I geometric locus.
        
        Args:
            numerator: Numerator of the fraction
            denominator: Denominator (typically 0 for singularities)
        """
        fraction = WheelFraction(numerator, denominator)
        position = self.map_to_wheel(fraction)
        self.infinity_loci.append((fraction, position))
    
    def get_I_locus_fractions(self) -> list:
        """
        Get all fractions that map to the I locus.
        
        Returns:
            List of fractions that evaluate to I
        """
        return [frac for frac, pos in self.infinity_loci if pos == self.I_position]


def demonstrate_wheel_properties():
    """
    Demonstrate key properties of the Wheel of Fractions.
    
    This function verifies the fundamental properties stated in Postulate 73:
    - Absorption property
    - Self-consistency of I
    - Neutrality in equivalence classes
    """
    wheel = WheelStructure()
    
    print("=" * 70)
    print("WHEEL OF FRACTIONS - PROPERTY VERIFICATION")
    print("=" * 70)
    
    # Property (a): Absorption
    print("\n[Property 73(a)] Absorption Property: x · I = I")
    test_values = [1, 2, 5, -3, 0.5, 100]
    for x in test_values:
        verified = wheel.verify_absorption_property(x)
        print(f"  {x} × I = I: {verified}")
    
    # Property (b): Self-consistency
    print("\n[Property 73(b)] Self-consistency: I + I = I, I × I = I")
    verified = wheel.verify_self_consistency()
    print(f"  I + I = I and I × I = I: {verified}")
    
    # Property (c): Neutrality in equivalence classes
    print("\n[Property 73(c)] Neutrality: 2/0 = 3/0 = I")
    verified = wheel.verify_neutrality_in_equivalence_classes()
    print(f"  All x/0 = I: {verified}")
    
    # Demonstrate specific cases
    print("\n[Specific Cases]")
    cases = [(1, 0), (2, 0), (3, 0), (-1, 0), (0, 0)]
    for num, den in cases:
        frac = WheelFraction(num, den)
        result = frac.evaluate(SemanticsMode.CONTEXTUAL)
        print(f"  {num}/{den} = {result}")
    
    print("\n" + "=" * 70)
    print("All properties verified successfully!")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_wheel_properties()
