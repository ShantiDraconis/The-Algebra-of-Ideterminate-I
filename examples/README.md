# Examples and Tutorials

This directory contains practical examples and tutorials for working with the I-Algebra framework.

## Available Examples

### 1. Bottleneck Constant Reference Implementation (`bottleneck_constant_reference.py`)

**NEW**: The official reference implementation of the Bottleneck Constant (I).

**Author**: Tiago Fagliari (ORCID: 0009-0006-6874-3910)  
**License**: MIT (academic/open source), See COMMERCIAL_LICENSING.md for commercial use

**Features**:
- Canonical implementation of I = 0/0
- All fundamental properties (idempotency, uniqueness, distinctness)
- Singleton pattern ensuring I is unique
- Complete arithmetic operations
- Safe division function (0/0 → I)
- Quantum computing example
- Comprehensive property verification

**Usage**:
```bash
python3 bottleneck_constant_reference.py
```

**Example Code**:
```python
from bottleneck_constant_reference import I, safe_divide, is_indeterminate

# Basic operations
print(I * I)  # I (multiplicative idempotency)
print(I + I)  # I (additive idempotency)
print(0 * I)  # 0 (zero absorption)
print(5 * I)  # I (I with non-zero)

# Safe division
result = safe_divide(0, 0)  # Returns I instead of error
print(result)  # I

# Check for indeterminacy
if is_indeterminate(result):
    print("Result is indeterminate - apply I-algebra")

# Division by I
print(10 / I)  # 0 (any number divided by I is 0)
```

**Key Properties Verified**:
- ✅ Uniqueness (singleton)
- ✅ Multiplicative idempotency: I × I = I
- ✅ Additive idempotency: I + I = I
- ✅ Zero absorption: 0 × I = 0
- ✅ Distinctness: I ≠ 0, I ≠ 1, I ≠ ∞, I ≠ NaN
- ✅ Division: r / I = 0, I / r = I
- ✅ Exponentiation: I^n = I

**Documentation**:
- Technical Spec: [BOTTLENECK_CONSTANT_SPECIFICATION.md](../BOTTLENECK_CONSTANT_SPECIFICATION.md)
- IP Notice: [INTELLECTUAL_PROPERTY.md](../INTELLECTUAL_PROPERTY.md)
- Licensing: [COMMERCIAL_LICENSING.md](../COMMERCIAL_LICENSING.md)

### 2. Python Implementation (`python_implementation.py`)

A complete computational implementation of the extended real number system in Python.

**Features**:
- Full implementation of K_I = ℝ ∪ {I, J}
- Modified algebraic operations (⊕, ⊖, ⊗, ⊘)
- Wheel of fractions structure
- Context-dependent resolution
- Physical application demonstrations

**Usage**:
```bash
python3 python_implementation.py
```

**Example Code**:
```python
from python_implementation import ExtendedReal

# Create elements
I = ExtendedReal.I()
zero = ExtendedReal.zero()
five = ExtendedReal(5)

# Operations
print(I + I)  # I
print(five / zero)  # I
print(zero * I)  # 0
print(I / I)  # I
```

## Tutorial: Getting Started with I-Algebra

### Step 1: Understanding I

The indeterminate element **I** represents 0/0:

```python
I = ExtendedReal.I()  # The indeterminate
```

**Key properties**:
- I + I = I (self-consistency)
- I × I = I (multiplicative self-consistency)
- I - I = I (subtraction indeterminacy)
- I / I = I (division indeterminacy)
- 0 × I = 0 (zero absorption)

### Step 2: Division by Zero

Unlike standard arithmetic, division by zero is well-defined:

```python
result = ExtendedReal(5) / ExtendedReal.zero()
print(result)  # I
```

This allows:
- Natural handling of singularities
- Continuous functions through undefined points
- Wheel of fractions algebra

### Step 3: The Dual Element J

J emerges from I-symmetry breaking:

```python
J = ExtendedReal.J()  # Dual indeterminate

# Mixed operations
print(I + J)  # I (I dominates)
print(J + J)  # J (self-consistent)
```

### Step 4: Physical Applications

#### Black Hole Singularity

```python
# Schwarzschild metric at r=0
r = ExtendedReal.zero()
g_00 = ExtendedReal(1) / r
print(f"Metric at singularity: {g_00}")  # I
```

#### Quantum Uncertainty

```python
# Heisenberg uncertainty principle
delta_x = ExtendedReal.I()
delta_p = ExtendedReal.I()
uncertainty = delta_x * delta_p
print(f"ΔxΔp = {uncertainty}")  # I
```

#### Dark Matter Density

```python
# NFW profile at core
rho_0 = ExtendedReal(1e9)
r_core = ExtendedReal.zero()
density = rho_0 / (r_core * r_core)
print(f"Core density: {density}")  # I
```

### Step 5: Context-Dependent Resolution

I can resolve to specific values based on context:

```python
I = ExtendedReal.I()

# Different contexts
print(I.resolve_context(0))  # 0 (zero context)
print(I.resolve_context(1))  # 1 (unity context)
print(I.resolve_context(2))  # I (indeterminate context)
```

This enables:
- Limit calculations
- Numerical methods
- Physical interpretations

## Advanced Topics

### Wheel of Fractions

The wheel structure allows unrestricted division:

```python
from python_implementation import WheelStructure

# Create wheel fractions
w1 = WheelStructure(ExtendedReal(5), ExtendedReal.zero())
print(w1.evaluate())  # I

w2 = WheelStructure(ExtendedReal.I(), ExtendedReal.I())
print(w2.evaluate())  # I
```

### Iterated Operations

Operations preserve indeterminacy:

```python
result = ExtendedReal.I()
for _ in range(100):
    result = result + ExtendedReal.I()
print(result)  # Still I
```

### Limits and Convergence

Sequences can converge to I:

```python
def limit_sequence(n):
    if n < 100:
        return ExtendedReal(1.0 / n)
    else:
        return ExtendedReal.I()

# At large n
print(limit_sequence(1000))  # I
```

## Exercises

### Exercise 1: Basic Operations

Compute the following:
1. (I + 5) × 2
2. (0 × I) + 1
3. I / (I + I)
4. (I - I) × 5

<details>
<summary>Solutions</summary>

1. I (I dominates addition, then multiplication)
2. 1 (0 × I = 0, then 0 + 1 = 1)
3. 0 (I + I = I, then I / I = I, but simplified: 0)
4. I (I - I = I, then I × 5 = I)
</details>

### Exercise 2: Physical Interpretation

Calculate the metric component at a black hole singularity:

```
g_00 = (1 - r_s/r)^(-1) at r = 0
```

<details>
<summary>Solution</summary>

```python
r_s = ExtendedReal(2)  # Schwarzschild radius
r = ExtendedReal.zero()
g_00 = ExtendedReal.one() / (ExtendedReal.one() - r_s / r)
# r_s / r = I, so 1 - I = I, then 1 / I = 0
print(g_00)  # Actually special case handling needed
```
</details>

### Exercise 3: Wheel Structure

Prove that the wheel equivalence is transitive.

### Exercise 4: Context Resolution

Design a context system for numerical PDE solving with I-valued boundary conditions.

## Common Pitfalls

### Pitfall 1: Assuming I = 0

**Wrong**: Treating I as zero
```python
if I == ExtendedReal.zero():  # False!
    # This never executes
```

**Right**: Recognizing I as distinct
```python
if I.is_real:  # False - I is not a real number
    # Handle real case
else:
    # Handle indeterminate case
```

### Pitfall 2: Cancellation Laws

**Wrong**: Assuming x = y from x + I = y + I
```python
# x + I = I and y + I = I doesn't mean x = y
```

**Right**: Recognizing I absorption
```python
# I dominates addition, so equality doesn't imply argument equality
```

### Pitfall 3: Distributivity

**Wrong**: Assuming full distributivity
```python
# I × (a + b) ≠ (I × a) + (I × b) in general
```

**Right**: Using modified distributivity
```python
# Special handling for indeterminate elements
```

## Performance Considerations

For numerical computations:

1. **Check for real values first**: Avoid indeterminate overhead
2. **Use context resolution**: Convert I to real values when possible
3. **Batch operations**: Minimize indeterminate checks

## Integration with Other Systems

### NumPy Integration

```python
import numpy as np

def extended_array(values):
    """Create array that can contain I"""
    return [ExtendedReal(v) if v != "I" else ExtendedReal.I() 
            for v in values]
```

### SymPy Integration

```python
from sympy import Symbol, limit

def symbolic_to_extended(expr, var, point):
    """Convert symbolic limit to extended real"""
    try:
        result = limit(expr, var, point)
        return ExtendedReal(float(result))
    except:
        return ExtendedReal.I()
```

## Further Reading

- [Mathematical Framework](../docs/MATHEMATICAL_FRAMEWORK.md)
- [Physical Interpretations](../docs/PHYSICAL_INTERPRETATIONS.md)
- [Lean 4 Formalization](../lean/IAlgebra.lean)
- [Coq Formalization](../coq/IAlgebra.v)

## Contributing Examples

To contribute new examples:

1. Follow the existing code style
2. Include comprehensive comments
3. Add demonstration functions
4. Document in this README
5. Submit pull request

---

**Questions?** Open an issue on the repository.
