"""
I-Calculus: Differential and Integral Operations for I-Algebra.

This module implements calculus operations in the extended algebra framework,
where the indeterminate I plays a fundamental role in limit processes,
derivatives, and integrals.

Mathematical Foundation:
-----------------------
The I-Calculus extends traditional calculus to handle indeterminate forms
and singularities. Key concepts:

1. Limits: lim(x→0) 1/x = I
2. Derivatives: d/dx(f) at singularities may yield I
3. Integrals: ∫f(x)dx over singular regions involves I
4. Continuity: I emerges naturally within limit structures

References:
-----------
See Postulate 74-75 for analytical and geometric interpretations.
"""

import math
from typing import Callable, Union, Optional, Tuple
from .types import IElement, SemanticsMode
from .operations import oplus, otimes, odiv, ominus


class ILimit:
    """
    Limit operations in I-Algebra.
    
    Handles limits that approach indeterminate forms, particularly
    those involving division by zero or 0/0 forms.
    """
    
    @staticmethod
    def limit_to_zero(f: Callable[[float], float], 
                     from_direction: str = 'both',
                     epsilon: float = 1e-10) -> Union[IElement, float]:
        """
        Compute limit as x approaches 0.
        
        For functions like f(x) = 1/x, the limit as x→0 is I.
        
        Args:
            f: Function to evaluate
            from_direction: 'left', 'right', or 'both'
            epsilon: Small value for numerical approximation
            
        Returns:
            Limit value or I if indeterminate
        """
        try:
            if from_direction in ['right', 'both']:
                right_val = f(epsilon)
            if from_direction in ['left', 'both']:
                left_val = f(-epsilon)
            
            if from_direction == 'both':
                # Check if approaching infinity or indeterminate
                if abs(right_val) > 1e10 or abs(left_val) > 1e10:
                    return IElement.I
                if not math.isclose(right_val, left_val, rel_tol=1e-5):
                    # Left and right limits differ - indeterminate
                    return IElement.I
                return (right_val + left_val) / 2
            elif from_direction == 'right':
                if abs(right_val) > 1e10:
                    return IElement.I
                return right_val
            else:  # left
                if abs(left_val) > 1e10:
                    return IElement.I
                return left_val
                
        except (ZeroDivisionError, ValueError, OverflowError):
            # Function undefined at limit point
            return IElement.I
    
    @staticmethod
    def limit_quotient(numerator: Callable[[float], float],
                      denominator: Callable[[float], float],
                      point: float = 0.0,
                      epsilon: float = 1e-10) -> Union[IElement, float]:
        """
        Compute limit of quotient f(x)/g(x) as x approaches point.
        
        Handles 0/0 indeterminate forms, which yield I.
        
        Args:
            numerator: Numerator function
            denominator: Denominator function
            point: Point to approach
            epsilon: Small value for approximation
            
        Returns:
            Limit value or I if indeterminate
        """
        try:
            x = point + epsilon
            num_val = numerator(x)
            den_val = denominator(x)
            
            # Check for 0/0 form
            if abs(num_val) < epsilon and abs(den_val) < epsilon:
                # 0/0 indeterminate form yields I
                return IElement.I
            
            # Check for x/0 form
            if abs(den_val) < epsilon:
                return IElement.I
            
            # Normal limit
            return num_val / den_val
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return IElement.I
    
    @staticmethod
    def l_hopital(numerator: Callable[[float], float],
                 denominator: Callable[[float], float],
                 point: float = 0.0,
                 h: float = 1e-8) -> Union[IElement, float]:
        """
        Apply L'Hôpital's rule for indeterminate forms.
        
        For 0/0 or ∞/∞ forms, compute limit of (f'/g').
        If still indeterminate, returns I.
        
        Args:
            numerator: Numerator function
            denominator: Denominator function
            point: Point of evaluation
            h: Step size for numerical differentiation
            
        Returns:
            Limit value or I if indeterminate
        """
        try:
            # Numerical derivatives
            f_prime = (numerator(point + h) - numerator(point - h)) / (2 * h)
            g_prime = (denominator(point + h) - denominator(point - h)) / (2 * h)
            
            if abs(g_prime) < 1e-10:
                # Still indeterminate after L'Hôpital
                return IElement.I
            
            return f_prime / g_prime
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return IElement.I


class IDerivative:
    """
    Derivative operations in I-Algebra.
    
    Handles differentiation of functions that may have singularities
    or involve the indeterminate constant I.
    """
    
    @staticmethod
    def derivative(f: Callable[[float], Union[float, IElement]],
                  x: float,
                  h: float = 1e-8,
                  mode: SemanticsMode = SemanticsMode.CONTEXTUAL) -> Union[IElement, float]:
        """
        Compute derivative using finite differences.
        
        For functions with singularities, may return I.
        
        Args:
            f: Function to differentiate
            x: Point of differentiation
            h: Step size
            mode: Semantic mode
            
        Returns:
            Derivative value or I if singular
        """
        try:
            f_plus = f(x + h)
            f_minus = f(x - h)
            
            # Handle I values
            if f_plus == IElement.I or f_minus == IElement.I:
                return IElement.I
            
            # Compute derivative
            derivative = (f_plus - f_minus) / (2 * h)
            
            # Check for singular derivative
            if abs(derivative) > 1e10:
                return IElement.I
            
            return derivative
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return IElement.I
    
    @staticmethod
    def derivative_at_singularity(f: Callable[[float], float],
                                  singularity: float,
                                  approach: str = 'both') -> IElement:
        """
        Compute derivative at a singularity point.
        
        At singularities, derivatives typically yield I.
        Example: d/dx(1/x) at x=0 yields I.
        
        Args:
            f: Function with singularity
            singularity: Location of singularity
            approach: Direction of approach
            
        Returns:
            I (indeterminate derivative at singularity)
        """
        # At singularities, derivative is indeterminate
        return IElement.I
    
    @staticmethod
    def partial_derivative(f: Callable[[float, float], float],
                          x: float, y: float,
                          variable: str = 'x',
                          h: float = 1e-8) -> Union[IElement, float]:
        """
        Compute partial derivative for multivariable functions.
        
        Args:
            f: Function of two variables
            x, y: Point of evaluation
            variable: 'x' or 'y' for partial derivative
            h: Step size
            
        Returns:
            Partial derivative or I if singular
        """
        try:
            if variable == 'x':
                df = (f(x + h, y) - f(x - h, y)) / (2 * h)
            else:
                df = (f(x, y + h) - f(x, y - h)) / (2 * h)
            
            if abs(df) > 1e10:
                return IElement.I
            
            return df
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return IElement.I


class IIntegral:
    """
    Integration operations in I-Algebra.
    
    Handles integration over regions that may contain singularities
    or involve the indeterminate constant I.
    """
    
    @staticmethod
    def integrate(f: Callable[[float], float],
                 a: float, b: float,
                 n: int = 1000,
                 mode: SemanticsMode = SemanticsMode.CONTEXTUAL) -> Union[IElement, float]:
        """
        Compute definite integral using trapezoidal rule.
        
        If integration region contains singularities, may return I.
        
        Args:
            f: Function to integrate
            a: Lower bound
            b: Upper bound
            n: Number of subdivisions
            mode: Semantic mode
            
        Returns:
            Integral value or I if singular
        """
        if a >= b:
            return 0.0
        
        h = (b - a) / n
        total = 0.0
        singular = False
        
        try:
            # Trapezoidal rule
            total = (f(a) + f(b)) / 2
            
            for i in range(1, n):
                x = a + i * h
                val = f(x)
                
                # Check for singularities
                if not math.isfinite(val) or abs(val) > 1e10:
                    singular = True
                    break
                
                total += val
            
            if singular:
                # Integration over singular region yields I
                return IElement.I
            
            result = total * h
            
            # Check for infinite result
            if not math.isfinite(result) or abs(result) > 1e10:
                return IElement.I
            
            return result
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return IElement.I
    
    @staticmethod
    def improper_integral(f: Callable[[float], float],
                         a: float,
                         to_infinity: bool = True,
                         limit: float = 1000.0,
                         n: int = 1000) -> Union[IElement, float]:
        """
        Compute improper integral to infinity or from -infinity.
        
        Args:
            f: Function to integrate
            a: Starting point
            to_infinity: True for ∫[a,∞), False for ∫(-∞,a]
            limit: Practical bound for infinity
            n: Number of subdivisions
            
        Returns:
            Integral value or I if divergent
        """
        try:
            if to_infinity:
                b = a + limit
            else:
                b = a
                a = a - limit
            
            result = IIntegral.integrate(f, a, b, n)
            
            # Check convergence
            if result == IElement.I:
                return IElement.I
            
            # For improper integrals, check if result is bounded
            if abs(result) > limit:
                return IElement.I
            
            return result
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return IElement.I
    
    @staticmethod
    def singular_integral(f: Callable[[float], float],
                         a: float, b: float,
                         singularity: float,
                         epsilon: float = 1e-6) -> IElement:
        """
        Integrate over region containing a singularity.
        
        When integrating through a singularity, the result is I.
        Example: ∫[-1,1] 1/x dx contains singularity at 0, yields I.
        
        Args:
            f: Function with singularity
            a: Lower bound
            b: Upper bound
            singularity: Location of singularity in [a,b]
            epsilon: Small value to avoid singularity
            
        Returns:
            I (indeterminate integral over singularity)
        """
        # Integration through singularity yields I
        return IElement.I


class IContinuity:
    """
    Continuity and discontinuity analysis in I-Algebra.
    
    The traditional assumption that division must be continuous is
    reconsidered, as I emerges naturally within limit structures.
    """
    
    @staticmethod
    def is_continuous_at(f: Callable[[float], Union[float, IElement]],
                        point: float,
                        epsilon: float = 1e-8) -> bool:
        """
        Check if function is continuous at a point.
        
        A function is continuous if lim(x→p) f(x) = f(p).
        Functions yielding I may be "I-continuous" even if not classically continuous.
        
        Args:
            f: Function to check
            point: Point of continuity check
            epsilon: Tolerance for limit
            
        Returns:
            True if continuous, False otherwise
        """
        try:
            # Evaluate at point
            f_at_point = f(point)
            
            # Evaluate limits from both sides
            f_left = f(point - epsilon)
            f_right = f(point + epsilon)
            
            # Handle I values - consider "I-continuous"
            if f_at_point == IElement.I:
                return f_left == IElement.I and f_right == IElement.I
            
            # Classical continuity check
            if isinstance(f_at_point, (int, float)):
                if isinstance(f_left, (int, float)) and isinstance(f_right, (int, float)):
                    return (math.isclose(f_left, f_at_point, rel_tol=1e-5) and
                           math.isclose(f_right, f_at_point, rel_tol=1e-5))
            
            return False
            
        except (ZeroDivisionError, ValueError, OverflowError):
            return False
    
    @staticmethod
    def find_discontinuities(f: Callable[[float], Union[float, IElement]],
                           a: float, b: float,
                           n: int = 100) -> list:
        """
        Find discontinuities in interval [a, b].
        
        Args:
            f: Function to analyze
            a: Lower bound
            b: Upper bound
            n: Number of sample points
            
        Returns:
            List of approximate discontinuity points
        """
        discontinuities = []
        h = (b - a) / n
        
        for i in range(n):
            x = a + i * h
            if not IContinuity.is_continuous_at(f, x):
                discontinuities.append(x)
        
        return discontinuities


def demonstrate_i_calculus():
    """
    Demonstrate I-Calculus operations and properties.
    
    Shows how limits, derivatives, and integrals behave with
    singularities and the indeterminate constant I.
    """
    print("=" * 70)
    print("I-CALCULUS DEMONSTRATIONS")
    print("=" * 70)
    
    # Limit examples
    print("\n[LIMITS]")
    print("1. lim(x→0) 1/x:")
    limit_result = ILimit.limit_to_zero(lambda x: 1/x)
    print(f"   Result: {limit_result}")
    
    print("\n2. lim(x→0) x²/x (0/0 form):")
    limit_result = ILimit.limit_quotient(lambda x: x**2, lambda x: x)
    print(f"   Result: {limit_result}")
    
    print("\n3. lim(x→0) sin(x)/x (L'Hôpital):")
    limit_result = ILimit.l_hopital(lambda x: math.sin(x), lambda x: x)
    print(f"   Result: {limit_result}")
    
    # Derivative examples
    print("\n[DERIVATIVES]")
    print("1. d/dx(x²) at x=2:")
    deriv = IDerivative.derivative(lambda x: x**2, 2)
    print(f"   Result: {deriv} (expected: ~4)")
    
    print("\n2. d/dx(1/x) at x=0 (singularity):")
    deriv = IDerivative.derivative_at_singularity(lambda x: 1/x, 0)
    print(f"   Result: {deriv}")
    
    # Integration examples
    print("\n[INTEGRALS]")
    print("1. ∫[0,1] x dx:")
    integral = IIntegral.integrate(lambda x: x, 0, 1)
    print(f"   Result: {integral} (expected: ~0.5)")
    
    print("\n2. ∫[-1,1] 1/x dx (singular):")
    integral = IIntegral.singular_integral(lambda x: 1/x, -1, 1, 0)
    print(f"   Result: {integral}")
    
    # Continuity examples
    print("\n[CONTINUITY]")
    print("1. f(x) = x² is continuous at x=1:")
    continuous = IContinuity.is_continuous_at(lambda x: x**2, 1)
    print(f"   Result: {continuous}")
    
    print("\n2. f(x) = 1/x is continuous at x=0:")
    continuous = IContinuity.is_continuous_at(lambda x: 1/x, 0)
    print(f"   Result: {continuous}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_i_calculus()
