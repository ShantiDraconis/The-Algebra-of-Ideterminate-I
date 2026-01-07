"""
Flexible Resolution Framework for the Indeterminate I

This module implements the flexible resolution mechanism where I can be
adapted to specific values when required by problem constraints, while
maintaining non-triviality of the system.
"""

from typing import Union, Optional, Dict, Any, Callable
from dataclasses import dataclass
from enum import Enum

from .types import AlgebraElement, ExtendedElement, Indeterminate, to_extended, I
from .operations import add, subtract, multiply, divide, equals


class ResolutionStrategy(Enum):
    """Strategies for resolving indeterminacy."""
    KEEP_INDETERMINATE = "keep_indeterminate"  # I remains indeterminate
    RESOLVE_TO_ZERO = "resolve_to_zero"  # I = 0 (if consistent)
    RESOLVE_TO_VALUE = "resolve_to_value"  # I = α for specific α
    ADAPTIVE = "adaptive"  # Let the system choose based on constraints


@dataclass
class ResolutionContext:
    """
    Context for flexible resolution of I.
    
    Tracks constraints and determines appropriate resolution strategy.
    """
    constraints: Dict[str, Any]
    strategy: ResolutionStrategy = ResolutionStrategy.KEEP_INDETERMINATE
    resolved_value: Optional[Union[int, float, complex]] = None
    
    def is_resolved(self) -> bool:
        """Check if I has been resolved in this context."""
        return self.resolved_value is not None
    
    def add_constraint(self, name: str, constraint: Any) -> None:
        """Add a constraint to the context."""
        self.constraints[name] = constraint
    
    def check_consistency(self) -> bool:
        """
        Check if resolving I to the current value maintains consistency.
        
        Returns:
            True if consistent (doesn't lead to 1 = 0)
        """
        if not self.is_resolved():
            return True
        
        # Check for trivialization: if I = 0 globally leads to 1 = 0
        if self.resolved_value == 0:
            # Check constraint: does I = 0 cause collapse?
            # If we have x/0 = I and I = 0, then x/0 = 0, implying x = 0 for all x
            # This would give 1 = 0, which is inconsistent
            for name, constraint in self.constraints.items():
                if name.startswith("division_by_zero"):
                    # Division by zero constraint present
                    return False  # Setting I = 0 globally would collapse the system
        
        return True
    
    def resolve(self, value: Union[int, float, complex]) -> 'ResolutionContext':
        """
        Create a new context with I resolved to a specific value.
        
        Args:
            value: The value to resolve I to
            
        Returns:
            A new ResolutionContext with resolved value
        """
        new_context = ResolutionContext(
            constraints=self.constraints.copy(),
            strategy=ResolutionStrategy.RESOLVE_TO_VALUE,
            resolved_value=value
        )
        return new_context


class FlexibleIndeterminateSystem:
    """
    Extended number system K_I with flexible resolution of I.
    
    Implements the flexible approach where I can be:
    1. An indeterminate constant (non-trivial, I ≠ 0)
    2. Specialized to a value α when required by problem constraints
    
    Key principles:
    - Non-triviality preservation (Axiom 27): I ≠ 0 unless context demands
    - Resolution criterion: I = α only locally/contextually
    - Consistency check: Never allow I = 0 globally (prevents 1 = 0)
    """
    
    def __init__(self, base_field: str = "R"):
        """
        Initialize the flexible system.
        
        Args:
            base_field: The base field K ("R" for reals, "C" for complex)
        """
        self.base_field = base_field
        self.global_context = ResolutionContext(constraints={})
        self.local_contexts: Dict[str, ResolutionContext] = {}
    
    def create_context(self, name: str) -> ResolutionContext:
        """
        Create a new local resolution context.
        
        Args:
            name: Name for the context
            
        Returns:
            A new ResolutionContext
        """
        context = ResolutionContext(constraints={})
        self.local_contexts[name] = context
        return context
    
    def solve_with_resolution(self, equation: Callable[[AlgebraElement], AlgebraElement],
                             target: AlgebraElement,
                             context_name: str = "default") -> Optional[Union[int, float, complex]]:
        """
        Solve an equation by potentially resolving I to a specific value.
        
        Example: If we have xI = 1, we can resolve I = 1/x for specific x.
        
        Args:
            equation: A function representing the equation (left side)
            target: The target value (right side)
            context_name: Name of the context for this resolution
            
        Returns:
            The resolved value of I, or None if no resolution needed
        """
        context = self.local_contexts.get(context_name) or self.create_context(context_name)
        
        # Try to solve with I as indeterminate first
        result = equation(I)
        result_ext = to_extended(result)
        target_ext = to_extended(target)
        
        # Check if equation is satisfied without resolution
        if equals(result, target):
            return None  # No resolution needed
        
        # Check if we need to resolve I
        # If result involves I and target doesn't, we may need resolution
        if result_ext.indet_coeff != 0 and target_ext.indet_coeff == 0:
            # Try to solve for I
            # result = a + bI, target = c
            # So: a + bI = c => bI = c - a => I = (c - a) / b
            if result_ext.indet_coeff != 0:
                resolved_value = (target_ext.real_part - result_ext.real_part) / result_ext.indet_coeff
                
                # Check consistency
                test_context = context.resolve(resolved_value)
                if test_context.check_consistency():
                    self.local_contexts[context_name] = test_context
                    return resolved_value
        
        return None
    
    def check_non_triviality(self, context: Optional[ResolutionContext] = None) -> bool:
        """
        Verify that the system remains non-trivial.
        
        Non-triviality means I ≠ 0 or, if I = 0 locally, it doesn't cause
        system collapse (1 = 0).
        
        Args:
            context: The context to check, or global if None
            
        Returns:
            True if non-trivial
        """
        ctx = context if context else self.global_context
        
        if not ctx.is_resolved():
            # I is indeterminate, system is non-trivial
            return True
        
        if ctx.resolved_value == 0:
            # Check if I = 0 causes collapse
            # Test: does x/0 = I = 0 lead to contradiction?
            # If x/0 = 0, then x = 0 * 0 = 0, so 1 = 0 (contradiction)
            return not ctx.check_consistency()
        
        return True
    
    def division_by_zero(self, x: AlgebraElement, 
                        context: Optional[ResolutionContext] = None) -> ExtendedElement:
        """
        Handle division by zero: x/0 = I
        
        Implements Axiom 23: For all x ∈ K \\ {0}, x/0 = I
        
        Args:
            x: The numerator
            context: Resolution context
            
        Returns:
            I or resolved value of I
        """
        x_ext = to_extended(x)
        ctx = context if context else self.global_context
        
        # Add division by zero constraint
        ctx.add_constraint(f"division_by_zero_{id(x)}", {"numerator": x_ext})
        
        # x/0 = I (Axiom 23)
        if ctx.is_resolved():
            # I has been resolved to a value
            return ExtendedElement(0, 1, Indeterminate(ctx.resolved_value))
        else:
            # I remains indeterminate
            return ExtendedElement(0, 1)
    
    def apply_absorption(self, a: AlgebraElement, operation: str = "add") -> ExtendedElement:
        """
        Apply absorption axiom (Axiom 24).
        
        - a + I = I for all a ∈ K_I
        - a · I = I for all a ∈ K_I
        
        Args:
            a: The element
            operation: "add" or "multiply"
            
        Returns:
            I (absorbed result)
        """
        if operation == "add":
            return add(a, I)
        elif operation == "multiply":
            return multiply(a, I)
        else:
            raise ValueError(f"Unknown operation: {operation}")
    
    def modified_distributivity(self, a: AlgebraElement, b: AlgebraElement, c: AlgebraElement,
                                lambda_coeff: Union[int, float, complex] = 0,
                                J: Optional[Indeterminate] = None) -> ExtendedElement:
        """
        Apply modified distributivity (Axiom 26).
        
        a(b + c) = ab + ac + λJ
        
        where J = iI is the imaginary extension of I and λ is a correction coefficient.
        
        Args:
            a, b, c: Elements for distributivity
            lambda_coeff: The correction coefficient λ
            J: The imaginary indeterminate (if None, treated as I)
            
        Returns:
            The result with correction term
        """
        # Standard distributivity
        ab = multiply(a, b)
        ac = multiply(a, c)
        standard = add(ab, ac)
        
        # Add correction term if any term involves I
        a_ext = to_extended(a)
        b_ext = to_extended(b)
        c_ext = to_extended(c)
        
        if (a_ext.indet_coeff != 0 or b_ext.indet_coeff != 0 or c_ext.indet_coeff != 0):
            # Apply correction
            if J is None:
                J = I  # Use I as J if not provided
            correction = ExtendedElement(0, lambda_coeff, J)
            return add(standard, correction)
        
        return standard


# Convenience functions

def create_system(base_field: str = "R") -> FlexibleIndeterminateSystem:
    """Create a new flexible indeterminate system."""
    return FlexibleIndeterminateSystem(base_field)


def resolve_locally(value: Union[int, float, complex], 
                    operation: Callable[[Indeterminate], Any]) -> Any:
    """
    Resolve I to a specific value for a local operation.
    
    Args:
        value: The value to resolve I to
        operation: A function that uses I
        
    Returns:
        The result of the operation with I resolved
    """
    resolved_I = Indeterminate(resolved_value=value)
    return operation(resolved_I)


def check_collapse(resolved_value: Union[int, float, complex]) -> bool:
    """
    Check if resolving I to a value causes system collapse (1 = 0).
    
    Args:
        resolved_value: The value to test
        
    Returns:
        True if collapse occurs
    """
    # If I = 0, then x/0 = I = 0 for all x ≠ 0
    # This means x = 0 * 0 = 0, so 1 = 0 (contradiction)
    if resolved_value == 0:
        return True  # Collapse!
    
    return False
