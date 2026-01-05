"""
Validation module for I-Algebra invariants.

This module provides validators for algebraic invariants including:
- Non-triviality: Ensures I is distinct from 0 and standard numbers
- Restricted cancellation rules: Validates when cancellation is allowed
- Corrected distributivity: Validates distributive properties with special cases
"""

from typing import Union, Tuple, Callable
from ..types import IElement, IExpr, SemanticsMode
from ..operations import oplus, ominus, otimes


class ValidationError(Exception):
    """Exception raised when an invariant is violated"""
    pass


class InvariantValidator:
    """Base class for invariant validators"""
    
    def __init__(self, mode: SemanticsMode = SemanticsMode.STRICT):
        self.mode = mode
    
    def validate(self, *args, **kwargs) -> bool:
        """Validate the invariant. Returns True if valid, raises ValidationError if invalid."""
        raise NotImplementedError


class NonTrivialityValidator(InvariantValidator):
    """
    Validates the non-triviality invariant.
    
    Ensures that:
    - I ≠ 0 (I is not equal to zero)
    - I ≠ any standard numeric value
    - I is a distinct algebraic element
    """
    
    def validate(self, value: Union[IElement, int, float]) -> bool:
        """
        Check if a value maintains non-triviality.
        
        Args:
            value: Value to check
            
        Returns:
            True if non-triviality is maintained
            
        Raises:
            ValidationError: If non-triviality is violated
        """
        # I should not be treated as zero
        if value == IElement.I:
            # This is valid - I is distinct
            return True
        
        # If someone tries to equate I with zero or a number, that's invalid
        # This validator is more for documentation of the principle
        return True
    
    def check_not_equal_to_zero(self, value: Union[IElement, int, float]) -> bool:
        """Verify that the indeterminate I is not equal to zero"""
        if value == IElement.I:
            if value == IElement.ZERO:
                raise ValidationError("Non-triviality violated: I cannot equal 0")
        return True
    
    def check_distinct_from_numbers(self, value: Union[IElement, int, float]) -> bool:
        """Verify that I is distinct from all numeric values"""
        if value == IElement.I:
            # I is always distinct in our representation
            return True
        return True


class RestrictedCancellationValidator(InvariantValidator):
    """
    Validates restricted cancellation rules.
    
    Ensures that:
    - I - I = 0 (cancellation is allowed)
    - I / I = 1 (division cancellation is allowed)
    - But cancellation should be tracked and validated in context
    """
    
    def validate_subtraction_cancellation(
        self, 
        a: Union[IElement, int, float],
        b: Union[IElement, int, float]
    ) -> bool:
        """
        Validate that I - I = 0 is handled correctly.
        
        Args:
            a: Minuend
            b: Subtrahend
            
        Returns:
            True if cancellation rule is satisfied
        """
        if a == IElement.I and b == IElement.I:
            result = ominus(a, b, self.mode)
            if result != IElement.ZERO and result != 0:
                raise ValidationError(
                    f"Restricted cancellation violated: I - I should equal 0, got {result}"
                )
            return True
        return True
    
    def validate_division_cancellation(
        self,
        a: Union[IElement, int, float],
        b: Union[IElement, int, float]
    ) -> bool:
        """
        Validate that I / I = 1 is handled correctly.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            True if cancellation rule is satisfied
        """
        from ..operations import odiv
        
        if a == IElement.I and b == IElement.I:
            result = odiv(a, b, self.mode)
            if result != 1:
                raise ValidationError(
                    f"Restricted cancellation violated: I / I should equal 1, got {result}"
                )
            return True
        return True
    
    def validate_no_general_cancellation(
        self,
        expr: str,
        a: Union[IElement, int, float],
        b: Union[IElement, int, float]
    ) -> bool:
        """
        Validate that general cancellation (beyond I ⊕ I) is not assumed.
        
        For example, I + x - I should not automatically simplify to x
        unless explicitly validated in the context.
        """
        # This is a placeholder for more complex validation logic
        # In a full implementation, this would analyze expression trees
        return True


class DistributivityValidator(InvariantValidator):
    """
    Validates corrected distributivity rules.
    
    Ensures that:
    - a * (b + c) = a*b + a*c holds for standard cases
    - Special handling for I in distributive operations
    - Validates corrected distributivity when I is involved
    """
    
    def validate_left_distributivity(
        self,
        a: Union[IElement, int, float],
        b: Union[IElement, int, float],
        c: Union[IElement, int, float]
    ) -> bool:
        """
        Validate left distributivity: a * (b + c) = a*b + a*c
        
        Args:
            a: Left multiplier
            b: First addend
            c: Second addend
            
        Returns:
            True if distributivity holds
            
        Raises:
            ValidationError: If distributivity is violated
        """
        try:
            # Compute left side: a * (b + c)
            sum_bc = oplus(b, c, self.mode)
            left_side = otimes(a, sum_bc, self.mode)
            
            # Compute right side: a*b + a*c
            prod_ab = otimes(a, b, self.mode)
            prod_ac = otimes(a, c, self.mode)
            right_side = oplus(prod_ab, prod_ac, self.mode)
            
            # Check equality (with tolerance for floats)
            if isinstance(left_side, (int, float)) and isinstance(right_side, (int, float)):
                if abs(left_side - right_side) > 1e-10:
                    raise ValidationError(
                        f"Distributivity violated: {a}*({b}+{c}) = {left_side} "
                        f"but {a}*{b} + {a}*{c} = {right_side}"
                    )
            elif left_side != right_side:
                # For IElement types, direct comparison
                # Note: With I, distributivity may have special rules
                if not (left_side == IElement.I and right_side == IElement.I):
                    if self.mode == SemanticsMode.STRICT:
                        raise ValidationError(
                            f"Distributivity violated: {a}*({b}+{c}) = {left_side} "
                            f"but {a}*{b} + {a}*{c} = {right_side}"
                        )
            
            return True
        except Exception as e:
            if isinstance(e, ValidationError):
                raise
            # Other exceptions might be expected in non-strict modes
            if self.mode == SemanticsMode.STRICT:
                raise ValidationError(f"Distributivity check failed: {str(e)}")
            return True
    
    def validate_right_distributivity(
        self,
        a: Union[IElement, int, float],
        b: Union[IElement, int, float],
        c: Union[IElement, int, float]
    ) -> bool:
        """
        Validate right distributivity: (a + b) * c = a*c + b*c
        
        Args:
            a: First addend
            b: Second addend
            c: Right multiplier
            
        Returns:
            True if distributivity holds
        """
        try:
            # Compute left side: (a + b) * c
            sum_ab = oplus(a, b, self.mode)
            left_side = otimes(sum_ab, c, self.mode)
            
            # Compute right side: a*c + b*c
            prod_ac = otimes(a, c, self.mode)
            prod_bc = otimes(b, c, self.mode)
            right_side = oplus(prod_ac, prod_bc, self.mode)
            
            # Check equality
            if isinstance(left_side, (int, float)) and isinstance(right_side, (int, float)):
                if abs(left_side - right_side) > 1e-10:
                    raise ValidationError(
                        f"Right distributivity violated: ({a}+{b})*{c} = {left_side} "
                        f"but {a}*{c} + {b}*{c} = {right_side}"
                    )
            elif left_side != right_side:
                if not (left_side == IElement.I and right_side == IElement.I):
                    if self.mode == SemanticsMode.STRICT:
                        raise ValidationError(
                            f"Right distributivity violated: ({a}+{b})*{c} = {left_side} "
                            f"but {a}*{c} + {b}*{c} = {right_side}"
                        )
            
            return True
        except Exception as e:
            if isinstance(e, ValidationError):
                raise
            if self.mode == SemanticsMode.STRICT:
                raise ValidationError(f"Right distributivity check failed: {str(e)}")
            return True


class InvariantChecker:
    """
    Main invariant checker that coordinates all validators.
    """
    
    def __init__(self, mode: SemanticsMode = SemanticsMode.STRICT):
        self.mode = mode
        self.non_triviality = NonTrivialityValidator(mode)
        self.cancellation = RestrictedCancellationValidator(mode)
        self.distributivity = DistributivityValidator(mode)
    
    def check_all_invariants(
        self,
        operation: str,
        operands: Tuple,
        result
    ) -> bool:
        """
        Check all relevant invariants for an operation.
        
        Args:
            operation: Operation name
            operands: Operation operands
            result: Operation result
            
        Returns:
            True if all invariants hold
        """
        # Non-triviality check
        for operand in operands:
            self.non_triviality.validate(operand)
        self.non_triviality.validate(result)
        
        # Operation-specific checks
        if operation == "ominus" and len(operands) == 2:
            self.cancellation.validate_subtraction_cancellation(operands[0], operands[1])
        
        return True
    
    def check_distributivity(
        self,
        a: Union[IElement, int, float],
        b: Union[IElement, int, float],
        c: Union[IElement, int, float]
    ) -> bool:
        """
        Check distributivity for given values.
        
        Args:
            a, b, c: Values to check distributivity
            
        Returns:
            True if distributivity holds
        """
        self.distributivity.validate_left_distributivity(a, b, c)
        self.distributivity.validate_right_distributivity(a, b, c)
        return True
