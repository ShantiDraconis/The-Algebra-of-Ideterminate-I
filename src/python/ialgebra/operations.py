"""
Operations for I-Algebra.

This module implements the core algebraic operations (oplus, ominus, otimes, odiv)
with explicit handling for the indeterminate I and zero, along with semantic logging.
"""

import logging
from typing import Union, Tuple
from .types import IElement, IExpr, SemanticsMode

# Configure logging for semantic decisions
# Using NullHandler by default follows Python logging best practices
# Applications using this library should configure logging as needed
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def _ensure_logging_configured():
    """
    Ensure logging is configured for interactive use.
    
    This function is called by the REPL to set up logging for users
    who want to see semantic decisions. Library users should configure
    logging themselves in their applications.
    """
    root_logger = logging.getLogger()
    if not root_logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
        root_logger.setLevel(logging.INFO)


class SemanticLogger:
    """Logger for semantic decisions in non-strict modes"""
    
    @staticmethod
    def log_decision(operation: str, operands: Tuple, result, mode: SemanticsMode, reason: str):
        """Log a semantic decision made during an operation"""
        if mode != SemanticsMode.STRICT:
            logger.info(
                f"Semantic decision [{mode}]: {operation}{operands} = {result} | Reason: {reason}"
            )


def _normalize_operand(value: Union[IElement, IExpr, int, float]) -> Union[IElement, float, int]:
    """Normalize an operand to a simple value"""
    if isinstance(value, IExpr):
        atom_val = value.get_atom_value()
        if atom_val is not None:
            return atom_val
        raise ValueError(f"Cannot operate on complex expression: {value}")
    return value


def oplus(a: Union[IElement, IExpr, int, float], 
          b: Union[IElement, IExpr, int, float],
          mode: SemanticsMode = SemanticsMode.STRICT) -> Union[IElement, float, int]:
    """
    Addition operation in I-Algebra.
    
    Rules:
    - 0 + x = x + 0 = x (identity)
    - I + 0 = 0 + I = I
    - I + I: depends on semantic mode
      - STRICT: I (assuming I is idempotent in some interpretations)
      - CONTEXTUAL: may return 2*I or I depending on context
      - EXPERIMENTAL: returns I
    - I + number: returns expression or I depending on mode
    - number + number: standard addition
    
    Args:
        a: First operand
        b: Second operand
        mode: Semantic interpretation mode
    
    Returns:
        Result of addition
    """
    a = _normalize_operand(a)
    b = _normalize_operand(b)
    
    # Zero identity
    if a == IElement.ZERO or (isinstance(a, (int, float)) and a == 0):
        return b
    if b == IElement.ZERO or (isinstance(b, (int, float)) and b == 0):
        return a
    
    # Infinity handling
    if a == IElement.INFINITY or b == IElement.INFINITY:
        SemanticLogger.log_decision("oplus", (a, b), IElement.INFINITY, mode, 
                                    "Infinity absorbs finite values in addition")
        return IElement.INFINITY
    
    # I + I
    if a == IElement.I and b == IElement.I:
        result = IElement.I
        reason = ("I + I = I (idempotent in strict mode)" if mode == SemanticsMode.STRICT
                  else "I + I = I (simplified representation)")
        SemanticLogger.log_decision("oplus", (a, b), result, mode, reason)
        return result
    
    # I + number or number + I
    if a == IElement.I or b == IElement.I:
        if mode == SemanticsMode.STRICT:
            raise ValueError(f"Cannot add I and numeric value in strict mode: {a} + {b}")
        SemanticLogger.log_decision("oplus", (a, b), IElement.I, mode,
                                  "I dominates in addition with numbers (non-strict)")
        return IElement.I
    
    # J handling (similar to I)
    if a == IElement.J or b == IElement.J:
        if mode == SemanticsMode.STRICT:
            raise ValueError(f"Cannot add J and other values in strict mode: {a} + {b}")
        SemanticLogger.log_decision("oplus", (a, b), IElement.J, mode,
                                  "J dominates in addition (non-strict)")
        return IElement.J
    
    # Numeric addition
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    
    raise ValueError(f"Unsupported operands for oplus: {a}, {b}")


def ominus(a: Union[IElement, IExpr, int, float],
           b: Union[IElement, IExpr, int, float],
           mode: SemanticsMode = SemanticsMode.STRICT) -> Union[IElement, float, int]:
    """
    Subtraction operation in I-Algebra.
    
    Rules:
    - x - 0 = x (right identity)
    - 0 - x = -x
    - I - I: depends on semantic mode
      - STRICT: 0 (restricted cancellation)
      - CONTEXTUAL/EXPERIMENTAL: 0
    - I - 0 = I
    - I - number: depends on mode
    
    Args:
        a: First operand (minuend)
        b: Second operand (subtrahend)
        mode: Semantic interpretation mode
    
    Returns:
        Result of subtraction
    """
    a = _normalize_operand(a)
    b = _normalize_operand(b)
    
    # x - 0 = x
    if b == IElement.ZERO or (isinstance(b, (int, float)) and b == 0):
        return a
    
    # 0 - x = -x (for numbers)
    if a == IElement.ZERO or (isinstance(a, (int, float)) and a == 0):
        if isinstance(b, (int, float)):
            return -b
        elif b == IElement.I:
            if mode == SemanticsMode.STRICT:
                raise ValueError("Cannot negate I in strict mode")
            SemanticLogger.log_decision("ominus", (a, b), IElement.I, mode,
                                      "0 - I treated as -I ≈ I (non-strict)")
            return IElement.I
    
    # I - I = 0 (restricted cancellation)
    if a == IElement.I and b == IElement.I:
        SemanticLogger.log_decision("ominus", (a, b), IElement.ZERO, mode,
                                  "I - I = 0 (restricted cancellation rule)")
        return IElement.ZERO
    
    # I - number or number - I
    if a == IElement.I or b == IElement.I:
        if mode == SemanticsMode.STRICT:
            raise ValueError(f"Cannot subtract I and numeric value in strict mode: {a} - {b}")
        SemanticLogger.log_decision("ominus", (a, b), IElement.I, mode,
                                  "I dominates in subtraction (non-strict)")
        return IElement.I
    
    # Numeric subtraction
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    
    raise ValueError(f"Unsupported operands for ominus: {a}, {b}")


def otimes(a: Union[IElement, IExpr, int, float],
           b: Union[IElement, IExpr, int, float],
           mode: SemanticsMode = SemanticsMode.STRICT) -> Union[IElement, float, int]:
    """
    Multiplication operation in I-Algebra.
    
    Rules:
    - 0 * x = x * 0 = 0 (absorbing element)
    - 1 * x = x * 1 = x (identity)
    - I * 0 = 0 * I = 0 (I doesn't override zero absorption)
    - I * I: depends on semantic mode
    - I * number: returns I or scaled I depending on mode
    
    Args:
        a: First operand
        b: Second operand
        mode: Semantic interpretation mode
    
    Returns:
        Result of multiplication
    """
    a = _normalize_operand(a)
    b = _normalize_operand(b)
    
    # Zero absorption (dominant over I)
    if a == IElement.ZERO or (isinstance(a, (int, float)) and a == 0):
        SemanticLogger.log_decision("otimes", (a, b), IElement.ZERO, mode,
                                  "Zero absorption in multiplication")
        return IElement.ZERO
    if b == IElement.ZERO or (isinstance(b, (int, float)) and b == 0):
        SemanticLogger.log_decision("otimes", (a, b), IElement.ZERO, mode,
                                  "Zero absorption in multiplication")
        return IElement.ZERO
    
    # One identity
    if isinstance(a, (int, float)) and a == 1:
        return b
    if isinstance(b, (int, float)) and b == 1:
        return a
    
    # Infinity handling
    if a == IElement.INFINITY or b == IElement.INFINITY:
        SemanticLogger.log_decision("otimes", (a, b), IElement.INFINITY, mode,
                                  "Infinity in multiplication")
        return IElement.INFINITY
    
    # I * I
    if a == IElement.I and b == IElement.I:
        result = IElement.I
        reason = ("I * I = I (idempotent in strict mode)" if mode == SemanticsMode.STRICT
                  else "I * I = I (simplified)")
        SemanticLogger.log_decision("otimes", (a, b), result, mode, reason)
        return result
    
    # I * number or number * I
    if a == IElement.I or b == IElement.I:
        result = IElement.I
        reason = ("I * number = I (scalar multiplication absorbed)" if mode == SemanticsMode.STRICT
                  else "I * number = I (non-strict scalar absorption)")
        SemanticLogger.log_decision("otimes", (a, b), result, mode, reason)
        return result
    
    # Numeric multiplication
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    
    raise ValueError(f"Unsupported operands for otimes: {a}, {b}")


def odiv(a: Union[IElement, IExpr, int, float],
         b: Union[IElement, IExpr, int, float],
         mode: SemanticsMode = SemanticsMode.STRICT) -> Union[IElement, float, int]:
    """
    Division operation in I-Algebra.
    
    Rules:
    - x / 1 = x
    - 0 / x = 0 (x ≠ 0)
    - x / 0 = undefined (raises exception or returns infinity)
    - I / I: depends on semantic mode
      - STRICT: undefined or 1 (restricted cancellation)
      - CONTEXTUAL: 1
    - I / number: returns I
    - number / I: depends on mode (may be 0 or undefined)
    
    Args:
        a: Numerator
        b: Denominator
        mode: Semantic interpretation mode
    
    Returns:
        Result of division
    """
    a = _normalize_operand(a)
    b = _normalize_operand(b)
    
    # Division by zero
    if b == IElement.ZERO or (isinstance(b, (int, float)) and b == 0):
        if mode == SemanticsMode.STRICT:
            raise ValueError("Division by zero")
        SemanticLogger.log_decision("odiv", (a, b), IElement.INFINITY, mode,
                                  "Division by zero yields infinity (non-strict)")
        return IElement.INFINITY
    
    # 0 / x = 0
    if a == IElement.ZERO or (isinstance(a, (int, float)) and a == 0):
        return IElement.ZERO
    
    # x / 1 = x
    if isinstance(b, (int, float)) and b == 1:
        return a
    
    # I / I
    if a == IElement.I and b == IElement.I:
        result = 1
        reason = ("I / I = 1 (restricted cancellation)" if mode == SemanticsMode.STRICT
                  else "I / I = 1 (cancellation)")
        SemanticLogger.log_decision("odiv", (a, b), result, mode, reason)
        return result
    
    # I / number
    if a == IElement.I and isinstance(b, (int, float)):
        SemanticLogger.log_decision("odiv", (a, b), IElement.I, mode,
                                  "I / number = I (scalar division absorbed)")
        return IElement.I
    
    # number / I
    if isinstance(a, (int, float)) and b == IElement.I:
        if mode == SemanticsMode.STRICT:
            raise ValueError("Cannot divide number by I in strict mode")
        SemanticLogger.log_decision("odiv", (a, b), IElement.ZERO, mode,
                                  "number / I ≈ 0 (non-strict)")
        return IElement.ZERO
    
    # Numeric division
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a / b
    
    raise ValueError(f"Unsupported operands for odiv: {a}, {b}")
