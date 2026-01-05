# I-Algebra Python Implementation

A Python implementation of the Algebra of Indeterminate I, providing algebraic operations with special elements and semantic modes.

## Structure

```
src/python/
├── ialgebra/
│   ├── __init__.py          # Main package exports
│   ├── types.py             # Core types (IElement, IExpr, SemanticsMode)
│   ├── operations.py        # Algebraic operations (oplus, ominus, otimes, odiv)
│   └── validation/
│       ├── __init__.py      # Validation package exports
│       └── invariants.py    # Invariant validators
└── cli/
    ├── __init__.py          # CLI package exports
    └── repl.py              # Interactive REPL
```

## Core Components

### 1. Types (`ialgebra/types.py`)

#### IElement Enum
Defines special algebraic elements:
- `I`: The primary indeterminate element
- `J`: Secondary indeterminate
- `ZERO`: Additive identity (0)
- `INFINITY`: Unbounded element (∞)

#### SemanticsMode Enum
Controls operation semantics:
- `STRICT`: Rigid rules, fails on ambiguous operations
- `CONTEXTUAL`: Context-dependent interpretation
- `EXPERIMENTAL`: Allows exploratory operations

#### IExpr Class
Abstract Syntax Tree for algebraic expressions:
- `Atom`: Atomic values (IElement or numeric)
- `BinaryOp`: Binary operations (+, -, *, /)
- `UnaryOp`: Unary operations (negation, etc.)

### 2. Operations (`ialgebra/operations.py`)

Implements four core operations with explicit I and 0 handling:

#### `oplus(a, b, mode=STRICT)` - Addition
- Identity: `0 + x = x`
- Idempotent: `I + I = I`
- Logs semantic decisions in non-strict modes

#### `ominus(a, b, mode=STRICT)` - Subtraction
- Identity: `x - 0 = x`
- Restricted cancellation: `I - I = 0`

#### `otimes(a, b, mode=STRICT)` - Multiplication
- Identity: `1 * x = x`
- Absorption: `0 * x = 0` (dominates I)
- Idempotent: `I * I = I`

#### `odiv(a, b, mode=STRICT)` - Division
- Identity: `x / 1 = x`
- Zero: `0 / x = 0`
- Restricted cancellation: `I / I = 1`

### 3. Validation (`ialgebra/validation/invariants.py`)

#### NonTrivialityValidator
Ensures I is distinct from 0 and numeric values.

#### RestrictedCancellationValidator
Validates cancellation rules:
- `I - I = 0`
- `I / I = 1`

#### DistributivityValidator
Validates distributive properties:
- `a * (b + c) = a*b + a*c`
- Special handling for I

#### InvariantChecker
Coordinates all validators and provides unified checking interface.

### 4. REPL (`cli/repl.py`)

Interactive command-line interface for live testing.

## Usage

### Basic Operations

```python
import sys
sys.path.insert(0, 'src/python')

from ialgebra import IElement, oplus, ominus, otimes, odiv, SemanticsMode

# Basic operations
result = oplus(IElement.I, IElement.ZERO)  # I + 0 = I
result = ominus(IElement.I, IElement.I)     # I - I = 0
result = otimes(IElement.I, IElement.I)     # I * I = I
result = odiv(IElement.I, IElement.I)       # I / I = 1

# Numeric operations
result = oplus(5, 3)   # 8
result = otimes(2, 4)  # 8

# With different semantic modes
result = oplus(IElement.I, 5, SemanticsMode.CONTEXTUAL)  # I (with logging)
```

### Validation

```python
from ialgebra.validation import InvariantChecker

checker = InvariantChecker(SemanticsMode.STRICT)

# Check non-triviality
checker.non_triviality.check_not_equal_to_zero(IElement.I)

# Check cancellation
checker.cancellation.validate_subtraction_cancellation(IElement.I, IElement.I)
checker.cancellation.validate_division_cancellation(IElement.I, IElement.I)

# Check distributivity
checker.check_distributivity(2, 3, 4)
```

### Interactive REPL

```bash
python3 src/python/cli/repl.py
```

REPL Commands:
- `help` - Show help
- `mode <mode>` - Set semantic mode (strict/contextual/experimental)
- `test` - Run example tests
- `check` - Check invariants
- `quit/exit` - Exit REPL

REPL Examples:
```
I-Algebra> I + 0
  => I

I-Algebra> I * I
  => I

I-Algebra> I - I
  => 0

I-Algebra> oplus(I, 5)
  => I

I-Algebra> mode strict
Mode set to: strict

I-Algebra> test
--- Running Example Tests ---
  I + 0 => I
  I + I => I
  I - I => 0
  ...
```

## Operation Rules

### Addition (oplus)
- **Identity**: `0 + x = x + 0 = x`
- **With I**: `I + 0 = I`, `I + I = I`
- **Strict mode**: Fails on `I + number`
- **Non-strict**: `I + number = I` (I dominates)

### Subtraction (ominus)
- **Identity**: `x - 0 = x`
- **Cancellation**: `I - I = 0` (restricted cancellation rule)
- **Strict mode**: Fails on `I - number` or `number - I`

### Multiplication (otimes)
- **Identity**: `1 * x = x * 1 = x`
- **Absorption**: `0 * x = x * 0 = 0` (zero dominates everything)
- **With I**: `I * 0 = 0`, `I * I = I`, `I * number = I`

### Division (odiv)
- **Identity**: `x / 1 = x`
- **Zero**: `0 / x = 0` (x ≠ 0)
- **Cancellation**: `I / I = 1`
- **Division by zero**: Raises error in strict mode, returns ∞ in non-strict
- **Strict mode**: Fails on `number / I`
- **Non-strict**: `number / I ≈ 0`

## Semantic Modes

### STRICT Mode
- Rigid rules
- Fails on ambiguous operations (e.g., `I + number`)
- Best for formal verification

### CONTEXTUAL Mode
- Context-dependent interpretation
- Logs semantic decisions
- I dominates in mixed operations
- Suitable for exploratory work

### EXPERIMENTAL Mode
- Most permissive
- Allows experimental operations
- Heavy logging of decisions
- For research and development

## Testing

Run basic tests:
```bash
python3 -c "
import sys
sys.path.insert(0, 'src/python')
from ialgebra import IElement, oplus, ominus, otimes, odiv

print('I + 0 =', oplus(IElement.I, IElement.ZERO))
print('I - I =', ominus(IElement.I, IElement.I))
print('I * I =', otimes(IElement.I, IElement.I))
print('I / I =', odiv(IElement.I, IElement.I))
"
```

Run validation tests:
```bash
python3 -c "
import sys
sys.path.insert(0, 'src/python')
from ialgebra.validation import InvariantChecker
from ialgebra import IElement, SemanticsMode

checker = InvariantChecker(SemanticsMode.STRICT)
checker.check_distributivity(2, 3, 4)
print('All validations passed!')
"
```

## Design Principles

1. **Non-triviality**: I is distinct from 0 and all numeric values
2. **Restricted Cancellation**: `I - I = 0` and `I / I = 1` are allowed
3. **Zero Dominance**: 0 absorbs everything in multiplication, even I
4. **Idempotence**: `I + I = I` and `I * I = I` in most interpretations
5. **Semantic Logging**: All non-strict decisions are logged for transparency

## Future Extensions

Potential areas for expansion:
- Complex expression simplification
- Expression parsing from string notation
- Graphical visualization of expressions
- Additional algebraic properties (commutativity, associativity proofs)
- Integration with symbolic mathematics libraries
- Extended wheel operations for more complex transformations
