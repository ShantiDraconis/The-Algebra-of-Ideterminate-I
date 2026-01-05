# GitHub Copilot Instructions for The Algebra of Indeterminate I

## Project Overview

This project implements a computational algebra system for the indeterminate unit **I**. It combines:
- Python implementation for computational algebra
- Lean 4 for formal verification
- LaTeX for documentation
- YAML-based axiom and rule definitions

## Code Style and Conventions

### Python (ialgebra/)
- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Write comprehensive docstrings in NumPy style
- Prefer composition over inheritance
- Use dataclasses for immutable data structures
- All public APIs must have complete docstrings and type annotations

### Lean 4 (lean/)
- Follow Mathlib4 naming conventions
- Document all theorems and definitions
- Use `#check` and `#eval` for examples
- Organize proofs hierarchically

### General
- Write clear, descriptive commit messages
- Keep functions small and focused
- Add tests for all new functionality
- Update documentation when changing APIs

## Architecture

### Core Components

1. **Type System** (`ialgebra/types.py`)
   - Define expression types involving I
   - Handle symbolic representations
   - Implement type checking and validation

2. **Operations** (`ialgebra/operations.py`)
   - Arithmetic operations with I
   - Algebraic transformations
   - Symbolic manipulation

3. **Rewrite System** (`ialgebra/rewrite.py`)
   - Pattern matching on expressions
   - Rule application and normalization
   - Confluence checking

4. **Wheel of Fractions** (`ialgebra/wheel.py`)
   - Extended division handling
   - Wheel structure operations
   - Special cases for I

5. **I-Calculus** (`ialgebra/calculus.py`)
   - Differentiation rules for I
   - Integration techniques
   - Limit operations

## Data Format

### Axioms (data/axioms/*.yaml)
```yaml
axiom:
  name: "axiom_name"
  statement: "I * I = -1"
  category: "fundamental"
  dependencies: []
```

### Rules (data/rules/*.yaml)
```yaml
rule:
  name: "rule_name"
  pattern: "I^2"
  replacement: "-1"
  conditions: []
```

## Testing

- Write unit tests for all modules
- Include property-based tests where appropriate
- Test edge cases and error conditions
- Verify mathematical properties hold

## Documentation

- Keep README.md up to date
- Document design decisions
- Provide usage examples
- Explain mathematical foundations

## CI/CD

The project uses GitHub Actions for:
- Python: linting, testing, type checking
- Lean: building and verification
- LaTeX: document compilation
- Integration testing across components

## Issue Tracking

Issues are organized into phases:
- **Phase 1**: Types and printing
- **Phase 2**: Operations
- **Phase 3**: Rewrite rules
- **Wheel of Fractions**: Extended arithmetic
- **I-Calculus**: Calculus operations

## Contributing

When implementing features:
1. Start with type definitions
2. Add core operations
3. Implement rewrite rules
4. Write comprehensive tests
5. Update documentation
6. Verify in Lean if applicable

## Resources

- Mathematical foundation: [Reference to book/paper]
- Lean 4 documentation: https://lean-lang.org/
- Python packaging: https://packaging.python.org/
