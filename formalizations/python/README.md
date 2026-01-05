# Python Implementation of I-Algebra

Computational implementation of the I-Algebra framework with full support for extended operations, calculus, and physical applications.

## Files

- `ialgebra.py` - Core library with ExtendedReal class and operations
- `advanced_applications.py` - Physics, AI, and advanced numerical methods
- `test_ialgebra.py` - Comprehensive test suite

## Installation

```bash
pip install numpy matplotlib
```

## Quick Start

```python
from ialgebra import ExtendedReal, iexp, ICalculus

# Create extended real numbers
I = ExtendedReal.I()
J = ExtendedReal.J()
x = ExtendedReal(3.14)

# Use extended operations
result1 = x - x  # Returns I (indeterminate)
result2 = x + I   # Returns I (absorption)
result3 = x * ExtendedReal(2.0)  # Returns ExtendedReal(6.28)

# I-exponential
exp_result = iexp(x)

# I-derivatives
def f(x):
    return ExtendedReal(x.value ** 2) if x.is_real() else I

derivative = ICalculus.ideriv(f, ExtendedReal(3.0))
print(f"d(x²)/dx at x=3: {derivative}")  # ~6.0
```

## Core Features

### ExtendedReal Class
```python
class ExtendedReal:
    """Extended real number: R ∪ {I, J}"""
    - I = 0/0 (indeterminate)
    - J = 1/I (reciprocal indeterminate)
    - Automatic type handling
    - Operator overloading (+, -, *, /)
```

### Extended Operations

**Addition (⊕):**
```python
a + b  # Returns I if a+b=0, else a+b
```

**Subtraction (⊖):**
```python
a - a  # Always returns I
```

**Multiplication (⊗):**
```python
a * b  # Returns I if a*b=0, else a*b
```

**Division (⊘):**
```python
a / b  # Returns I if b=0, else a/b
```

### I-Calculus

```python
from ialgebra import ICalculus

# Numerical derivative
def f(x):
    return ExtendedReal(x.value ** 3)

deriv = ICalculus.ideriv(f, ExtendedReal(2.0))

# Numerical integration
integral = ICalculus.iintegral(f, ExtendedReal(0.0), ExtendedReal(1.0))
```

## Advanced Applications

### Quantum Gravity

```python
from advanced_applications import QuantumGravity

qg = QuantumGravity()

# Modified Schwarzschild radius with J-correction
M_sun = 1.989e30  # kg
rs = qg.schwarzschild_radius_i_corrected(M_sun)

# Singularity resolution
resolved = qg.singularity_resolution(r=0.0, r_s=2950.0)
```

### Dark Sector Model

```python
from advanced_applications import DarkSectorModel

dark = DarkSectorModel()

# Dark matter as J-condensate
dm_density = dark.j_condensate_density(r=1.0)

# Dark energy as J-field
de = dark.dark_energy_field(a=1.0)
```

### Computational Intelligence

```python
from advanced_applications import ComputationalIntelligence

ci = ComputationalIntelligence()

# Structured uncertainty
uncertain = ci.structured_uncertainty(x=5.0, confidence=0.3)

# I-neural activation
activation = ci.i_neural_activation(x=0.5)

# Consciousness model
consciousness = ci.consciousness_model(
    quantum_state=0.5+0.5j,
    classical_state=0.8
)
```

## Running Tests

```bash
# Run basic demonstrations
python3 ialgebra.py

# Run advanced applications
python3 advanced_applications.py

# Run full test suite
python3 test_ialgebra.py
```

### Test Coverage

The test suite includes:
- ExtendedReal construction and equality
- All extended operations
- Theorem 14.1 verification
- I-exponential function
- I-calculus (derivatives, integrals)
- Cardinal arithmetic
- Physical applications
- Operator overloading

## API Reference

### ExtendedReal

```python
ExtendedReal(value: float)          # Create real number
ExtendedReal.I()                    # Create indeterminate
ExtendedReal.J()                    # Create reciprocal indeterminate

# Methods
.is_real() -> bool
.is_I() -> bool
.is_J() -> bool
```

### Functions

```python
eadd(a, b) -> ExtendedReal         # Extended addition
esub(a, b) -> ExtendedReal         # Extended subtraction
emul(a, b) -> ExtendedReal         # Extended multiplication
ediv(a, b) -> ExtendedReal         # Extended division
iexp(x) -> ExtendedReal            # I-exponential

verify_indeterminate_invariance(x) -> bool  # Verify Theorem 14.1
```

### ICalculus

```python
ICalculus.ideriv(f, x, epsilon=1e-7) -> ExtendedReal
ICalculus.iintegral(f, a, b, n=1000) -> ExtendedReal
```

### IPhysics

```python
IPhysics.i_field_lagrangian(R, g, Lambda) -> ExtendedReal
IPhysics.modified_tov_pressure(r, rho, P, M, R_total) -> ExtendedReal
```

## Performance Considerations

- All operations use numpy for numerical stability
- Epsilon tolerance for zero comparisons: 1e-9 (via numpy.isclose)
- Numerical derivatives use forward difference with configurable epsilon
- Integration uses trapezoidal rule with configurable steps

## Examples

See the main test output:
```bash
python3 ialgebra.py
```

Output includes:
1. Basic construction
2. Self-subtraction verification
3. Indeterminate invariance theorem
4. Extended operations
5. I-exponential
6. I-derivatives
7. Physical applications

## Known Limitations

- Numerical approximations for calculus operations
- No symbolic computation (purely numerical)
- Physics applications use simplified models
- J-field corrections are conceptual

## Future Enhancements

- Symbolic computation integration (SymPy)
- GPU acceleration for large-scale computations
- Visualization tools for I-plane topology
- Machine learning integration
- Quantum computing simulator with I-algebra

---

*Author: Shalom Havah Tzedek (AS Shanti Draconis)*
*Date: January 5, 2026*
