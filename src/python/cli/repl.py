#!/usr/bin/env python3
"""
REPL (Read-Eval-Print Loop) for I-Algebra.

Interactive command-line interface for testing I-Algebra operations live.
Users can input expressions, test operations, and explore the algebra interactively.
"""

import sys
import logging
import os
from typing import Dict, Any

# Add parent directory to path for imports
# This allows the script to work from any location
# Script is in src/python/cli/, we need to add src/python/ to path
script_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.dirname(script_dir)
sys.path.insert(0, python_dir)

from ialgebra.types import IElement, IExpr, SemanticsMode
from ialgebra.operations import oplus, ominus, otimes, odiv
from ialgebra.validation.invariants import InvariantChecker, ValidationError


class IAlgebraREPL:
    """
    Interactive REPL for I-Algebra operations.
    """
    
    def __init__(self):
        self.mode = SemanticsMode.CONTEXTUAL
        self.variables: Dict[str, Any] = {}
        self.history = []
        self.checker = InvariantChecker(self.mode)
        
        # Set up logging only if not already configured
        if not logging.getLogger().hasHandlers():
            logging.basicConfig(
                level=logging.INFO,
                format='%(levelname)s: %(message)s'
            )
    
    def print_welcome(self):
        """Print welcome message"""
        print("=" * 60)
        print("  I-Algebra REPL - Algebra of Indeterminate I")
        print("=" * 60)
        print("\nAvailable elements: I, J, 0 (Zero), ∞ (Infinity)")
        print("Operations: oplus (+), ominus (-), otimes (*), odiv (/)")
        print(f"Current mode: {self.mode.value}")
        print("\nCommands:")
        print("  help        - Show this help")
        print("  mode <mode> - Set semantic mode (strict/contextual/experimental)")
        print("  test        - Run example tests")
        print("  check       - Check invariants")
        print("  quit/exit   - Exit REPL")
        print("\nExamples:")
        print("  I + 0")
        print("  I * I")
        print("  I - I")
        print("  oplus(I, 5)")
        print("=" * 60)
    
    def parse_element(self, s: str) -> Any:
        """Parse a string into an IElement or number"""
        s = s.strip()
        
        # IElement mapping
        element_map = {
            'I': IElement.I,
            'J': IElement.J,
            '0': IElement.ZERO,
            'Zero': IElement.ZERO,
            '∞': IElement.INFINITY,
            'Infinity': IElement.INFINITY,
        }
        
        if s in element_map:
            return element_map[s]
        
        # Try to parse as number
        try:
            if '.' in s:
                return float(s)
            return int(s)
        except ValueError:
            pass
        
        # Check if it's a variable
        if s in self.variables:
            return self.variables[s]
        
        raise ValueError(f"Unknown element or variable: {s}")
    
    def parse_operation(self, line: str) -> Any:
        """Parse and evaluate an operation"""
        line = line.strip()
        
        # Handle assignment
        if '=' in line and not any(op in line.split('=')[0] for op in ['!', '<', '>', '=']):
            var_name, expr = line.split('=', 1)
            var_name = var_name.strip()
            result = self.parse_operation(expr.strip())
            self.variables[var_name] = result
            return f"{var_name} = {result}"
        
        # Handle function-style operations
        if line.startswith('oplus('):
            args = line[6:-1].split(',')
            a, b = self.parse_element(args[0]), self.parse_element(args[1])
            return oplus(a, b, self.mode)
        
        if line.startswith('ominus('):
            args = line[7:-1].split(',')
            a, b = self.parse_element(args[0]), self.parse_element(args[1])
            return ominus(a, b, self.mode)
        
        if line.startswith('otimes('):
            args = line[7:-1].split(',')
            a, b = self.parse_element(args[0]), self.parse_element(args[1])
            return otimes(a, b, self.mode)
        
        if line.startswith('odiv('):
            args = line[5:-1].split(',')
            a, b = self.parse_element(args[0]), self.parse_element(args[1])
            return odiv(a, b, self.mode)
        
        # Handle infix operations (simple parser)
        for op, func in [(' + ', oplus), (' - ', ominus), (' * ', otimes), (' / ', odiv)]:
            if op in line:
                parts = line.split(op, 1)
                if len(parts) == 2:
                    a = self.parse_element(parts[0])
                    b = self.parse_element(parts[1])
                    return func(a, b, self.mode)
        
        # Single element
        return self.parse_element(line)
    
    def handle_command(self, line: str) -> bool:
        """
        Handle a command line. Returns False if should exit.
        """
        line = line.strip()
        
        if not line:
            return True
        
        # Commands
        if line in ['quit', 'exit', 'q']:
            return False
        
        if line == 'help':
            self.print_welcome()
            return True
        
        if line.startswith('mode '):
            mode_str = line[5:].strip()
            try:
                if mode_str == 'strict':
                    self.mode = SemanticsMode.STRICT
                elif mode_str == 'contextual':
                    self.mode = SemanticsMode.CONTEXTUAL
                elif mode_str == 'experimental':
                    self.mode = SemanticsMode.EXPERIMENTAL
                else:
                    print(f"Unknown mode: {mode_str}")
                    return True
                
                self.checker = InvariantChecker(self.mode)
                print(f"Mode set to: {self.mode.value}")
            except Exception as e:
                print(f"Error setting mode: {e}")
            return True
        
        if line == 'test':
            self.run_tests()
            return True
        
        if line == 'check':
            self.run_invariant_checks()
            return True
        
        # Try to evaluate as expression
        try:
            result = self.parse_operation(line)
            print(f"  => {result}")
            self.history.append((line, result))
        except Exception as e:
            print(f"Error: {e}")
        
        return True
    
    def run_tests(self):
        """Run example tests"""
        print("\n--- Running Example Tests ---")
        
        test_cases = [
            ("I + 0", lambda: oplus(IElement.I, IElement.ZERO, self.mode)),
            ("I + I", lambda: oplus(IElement.I, IElement.I, self.mode)),
            ("I - I", lambda: ominus(IElement.I, IElement.I, self.mode)),
            ("I * 0", lambda: otimes(IElement.I, IElement.ZERO, self.mode)),
            ("I * I", lambda: otimes(IElement.I, IElement.I, self.mode)),
            ("I / I", lambda: odiv(IElement.I, IElement.I, self.mode)),
            ("5 + 3", lambda: oplus(5, 3, self.mode)),
            ("5 * 3", lambda: otimes(5, 3, self.mode)),
        ]
        
        for desc, test_func in test_cases:
            try:
                result = test_func()
                print(f"  {desc} => {result}")
            except Exception as e:
                print(f"  {desc} => Error: {e}")
        
        print("--- Tests Complete ---\n")
    
    def run_invariant_checks(self):
        """Run invariant validation checks"""
        print("\n--- Running Invariant Checks ---")
        
        try:
            # Non-triviality
            print("Checking non-triviality...")
            self.checker.non_triviality.check_not_equal_to_zero(IElement.I)
            print("  ✓ I ≠ 0")
            
            # Cancellation
            print("Checking restricted cancellation...")
            self.checker.cancellation.validate_subtraction_cancellation(IElement.I, IElement.I)
            print("  ✓ I - I = 0")
            self.checker.cancellation.validate_division_cancellation(IElement.I, IElement.I)
            print("  ✓ I / I = 1")
            
            # Distributivity (numeric test)
            print("Checking distributivity with numbers...")
            self.checker.check_distributivity(2, 3, 4)
            print("  ✓ 2 * (3 + 4) = 2*3 + 2*4")
            
            print("--- All Invariants Satisfied ---\n")
        except ValidationError as e:
            print(f"  ✗ Validation Error: {e}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    def run(self):
        """Run the REPL"""
        self.print_welcome()
        
        while True:
            try:
                line = input("\nI-Algebra> ")
                if not self.handle_command(line):
                    print("Goodbye!")
                    break
            except KeyboardInterrupt:
                print("\nUse 'quit' or 'exit' to leave the REPL")
            except EOFError:
                print("\nGoodbye!")
                break


def main():
    """Main entry point"""
    repl = IAlgebraREPL()
    repl.run()


if __name__ == "__main__":
    main()
