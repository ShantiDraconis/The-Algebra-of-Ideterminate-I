# Multi-State I Algebra: Tutorial and Examples

This notebook demonstrates the multi-state logic system for the indeterminate element **I** and extended algebraic operations.

## Setup

```python
# Import the necessary modules
from ialgebra import (
    # Multi-state types
    IndeterminateState,
    MultiStateResult,
    subtract_I_from_I,
    divide_I_by_I,
    divide_I_by_zero,
    QuantumSuperposition,
    ContextDependentResolver,
    create_equal_superposition,
    create_I_dominated_superposition,
    
    # Extended operations
    ExtendedNumber,
    ExtendedAlgebra,
    I, J, ZERO_I, I_ZERO, ZERO, ONE,
)

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
```

## Part 1: Multi-State Operations

### Example 1.1: I - I (Indeterminate Subtraction)

The operation I - I doesn't have a single determinate value. Instead, it exists in multiple possible states:

```python
result = subtract_I_from_I()
print(f"I - I can be: {result}")
print(f"Is determinate? {result.is_determinate()}")
print()

# Check which states are possible
print("Possible states:")
for state in [IndeterminateState.ZERO, IndeterminateState.I, IndeterminateState.INDETERMINATE]:
    if result.contains(state):
        print(f"  ✓ {state}")
```

**Output:**
```
I - I can be: 0 ∨ ? ∨ I
Is determinate? False

Possible states:
  ✓ 0
  ✓ I
  ✓ ?
```

### Example 1.2: I / I (Context-Dependent Division)

```python
result = divide_I_by_I()
print(f"I / I can be: {result}")
print()

# Check specific states
print(f"Can equal 1? {result.contains(IndeterminateState.ONE)}")
print(f"Can equal I? {result.contains(IndeterminateState.I)}")
print(f"Can be indeterminate? {result.contains(IndeterminateState.INDETERMINATE)}")
```

**Output:**
```
I / I can be: 1 ∨ ? ∨ I

Can equal 1? True
Can equal I? True
Can be indeterminate? True
```

### Example 1.3: I / 0 (Extended Singularity)

```python
result = divide_I_by_zero()
print(f"I / 0 can be: {result}")
print()

# This operation connects to extended infinity
print(f"Can equal I? {result.contains(IndeterminateState.I)}")
print(f"Can equal ∞? {result.contains(IndeterminateState.INFINITY)}")
```

**Output:**
```
I / 0 can be: ? ∨ I ∨ ∞

Can equal I? True
Can equal ∞? True
```

## Part 2: Context-Dependent Resolution

Multi-state results can be "collapsed" to a single value based on mathematical context:

### Example 2.1: Different Contexts, Different Results

```python
resolver = ContextDependentResolver()

# I - I in different contexts
result = subtract_I_from_I()

print("I - I resolves to:")
print(f"  Standard context: {resolver.resolve(result, 'standard')}")
print(f"  Limit context:    {resolver.resolve(result, 'limit')}")
print(f"  Infinity context: {resolver.resolve(result, 'infinity')}")
```

**Output:**
```
I - I resolves to:
  Standard context: I
  Limit context:    0
  Infinity context: I
```

### Example 2.2: Comparing All Operations Across Contexts

```python
operations = {
    "I - I": subtract_I_from_I(),
    "I / I": divide_I_by_I(),
    "I / 0": divide_I_by_zero(),
}

contexts = ["standard", "limit", "infinity"]

print("Resolution Table:")
print("-" * 60)
print(f"{'Operation':<10} | {'Standard':<10} | {'Limit':<10} | {'Infinity':<10}")
print("-" * 60)

for op_name, result in operations.items():
    resolutions = [str(resolver.resolve(result, ctx)) for ctx in contexts]
    print(f"{op_name:<10} | {resolutions[0]:<10} | {resolutions[1]:<10} | {resolutions[2]:<10}")
```

**Output:**
```
Resolution Table:
------------------------------------------------------------
Operation  | Standard   | Limit      | Infinity  
------------------------------------------------------------
I - I      | I          | 0          | I         
I / I      | I          | 1          | I         
I / 0      | I          | I          | ∞         
```

## Part 3: Quantum Superposition Analogy

The multi-state nature of I can be understood through quantum mechanics:

### Example 3.1: Equal Superposition

```python
# Create equal superposition: |I⟩ = (1/√3)|0⟩ + (1/√3)|I⟩ + (1/√3)|∞⟩
superpos = create_equal_superposition()
print(f"Equal superposition: {superpos}")
print()

# Probabilities
print("Measurement probabilities:")
print(f"  P(0) = {abs(superpos.alpha)**2:.3f}")
print(f"  P(I) = {abs(superpos.beta)**2:.3f}")
print(f"  P(∞) = {abs(superpos.gamma)**2:.3f}")
print(f"  Sum  = {abs(superpos.alpha)**2 + abs(superpos.beta)**2 + abs(superpos.gamma)**2:.3f}")
```

**Output:**
```
Equal superposition: 0.577|0⟩ + 0.577|I⟩ + 0.577|∞⟩

Measurement probabilities:
  P(0) = 0.333
  P(I) = 0.333
  P(∞) = 0.333
  Sum  = 1.000
```

### Example 3.2: I-Dominated Superposition

```python
# Create I-dominated superposition
superpos = create_I_dominated_superposition()
print(f"I-dominated superposition: {superpos}")
print()

print("Measurement probabilities:")
print(f"  P(0) = {abs(superpos.alpha)**2:.3f}")
print(f"  P(I) = {abs(superpos.beta)**2:.3f}")
print(f"  P(∞) = {abs(superpos.gamma)**2:.3f}")
```

**Output:**
```
I-dominated superposition: 0.200|0⟩ + 0.940|I⟩ + 0.270|∞⟩

Measurement probabilities:
  P(0) = 0.040
  P(I) = 0.884
  P(∞) = 0.073
```

### Example 3.3: Simulating Measurements

```python
# Simulate 1000 measurements
superpos = create_I_dominated_superposition()
measurements = [superpos.measure() for _ in range(1000)]

# Count results
counts = Counter(measurements)
print("Results from 1000 measurements:")
for state, count in counts.most_common():
    percentage = (count / 1000) * 100
    print(f"  {state}: {count} times ({percentage:.1f}%)")

# Visualize (if matplotlib is available)
try:
    states = list(counts.keys())
    values = list(counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar([str(s) for s in states], values)
    plt.xlabel('State')
    plt.ylabel('Frequency')
    plt.title('Measurement Results from I-Dominated Superposition (1000 trials)')
    plt.tight_layout()
    plt.savefig('measurements.png')
    print("\nVisualization saved as 'measurements.png'")
except Exception as e:
    print(f"\nVisualization skipped: {e}")
```

## Part 4: Extended Operations

To maintain algebraic consistency, extended operations are introduced:

### Example 4.1: Multiplicative Inverse Solution (J)

```python
# Solution 104.1: I · J = 1
result = ExtendedAlgebra.multiply(I, J)
print(f"I · J = {result}")
print(f"J · I = {ExtendedAlgebra.multiply(J, I)}")
print()

# Verify this is truly 1
print(f"Result equals ONE? {result == ONE}")
```

**Output:**
```
I · J = 1
J · I = 1

Result equals ONE? True
```

### Example 4.2: Extended Zero (0_I)

```python
# Solution 104.3: 0 · I = 0_I (not standard 0)
result = ExtendedAlgebra.multiply(ZERO, I)
print(f"0 · I = {result}")
print(f"Is standard zero? {result == ZERO}")
print(f"Is extended zero (0_I)? {result == ZERO_I}")
```

**Output:**
```
0 · I = 0_I
Is standard zero? False
Is extended zero (0_I)? True
```

### Example 4.3: Extended Additive Identity (I_0)

```python
# Solution 104.4: I + 0 = I_0 (not I)
result = ExtendedAlgebra.add(I, ZERO)
print(f"I + 0 = {result}")
print(f"Equals I? {result == I}")
print(f"Is extended identity (I_0)? {result == I_ZERO}")
```

**Output:**
```
I + 0 = I_0
Equals I? False
Is extended identity (I_0)? True
```

### Example 4.4: Exponentiation

```python
# Solution 104.6: I^n = I for all n ≥ 1
print("Powers of I:")
for n in [0, 1, 2, 3, 5, 10, 100]:
    result = ExtendedAlgebra.power(I, n)
    print(f"  I^{n:<3} = {result}")
```

**Output:**
```
Powers of I:
  I^0   = 1
  I^1   = I
  I^2   = I
  I^3   = I
  I^5   = I
  I^10  = I
  I^100 = I
```

### Example 4.5: Logarithm

```python
# Solution 104.7: log(I) = J, log(J) = I
print("Logarithmic operations:")
print(f"  log(I) = {ExtendedAlgebra.log(I)}")
print(f"  log(J) = {ExtendedAlgebra.log(J)}")
print()

# Verify inverse relationship
log_I = ExtendedAlgebra.log(I)
log_log_I = ExtendedAlgebra.log(log_I) if log_I else None
print(f"  log(log(I)) = {log_log_I}")
```

**Output:**
```
Logarithmic operations:
  log(I) = J
  log(J) = I

  log(log(I)) = I
```

### Example 4.6: Cancellation Law

```python
# Solution 104.5: Cancellation restricted to standard non-zero elements
print("Cancellation law applicability:")
print(f"  Can cancel I? {ExtendedAlgebra.can_cancel(I)}")
print(f"  Can cancel J? {ExtendedAlgebra.can_cancel(J)}")
print(f"  Can cancel 0? {ExtendedAlgebra.can_cancel(ZERO)}")
print(f"  Can cancel 5? {ExtendedAlgebra.can_cancel(ExtendedNumber(5))}")
```

**Output:**
```
Cancellation law applicability:
  Can cancel I? False
  Can cancel J? False
  Can cancel 0? False
  Can cancel 5? True
```

## Part 5: Verification

All extended operations can be verified:

```python
print("Extended Algebra Verification:\n")
results = ExtendedAlgebra.verify_all()

for name, status in results:
    symbol = "✓" if status == "PASS" else "✗"
    print(f"{symbol} {name}: {status}")
```

**Output:**
```
Extended Algebra Verification:

✓ Multiplicative Inverse: PASS
✓ Zero Multiplication Fix: PASS
✓ Additive Identity: PASS
✓ Exponentiation: PASS
✓ Logarithm: PASS
```

## Part 6: Practical Applications

### Example 6.1: Resolving Singularities in Calculations

```python
def safe_divide(a, b):
    """Division that handles singularities using I"""
    if b == 0:
        return I
    return ExtendedNumber(a / b)

# Example calculations
print("Safe division examples:")
calculations = [
    (5, 2),
    (10, 0),  # Would normally cause error
    (0, 0),   # Indeterminate
]

for a, b in calculations:
    result = safe_divide(a, b)
    print(f"  {a} / {b} = {result}")
```

### Example 6.2: Context-Dependent Function Evaluation

```python
def evaluate_limit(result, approach):
    """Evaluate a multi-state limit based on approach"""
    resolver = ContextDependentResolver()
    
    context_map = {
        "from_above": "infinity",
        "from_below": "limit",
        "oscillating": "standard"
    }
    
    context = context_map.get(approach, "standard")
    return resolver.resolve(result, context)

# Example: lim(x→0) f(x) where f has singularity
result = divide_I_by_zero()
print("Limit evaluation:")
print(f"  Approaching from above: {evaluate_limit(result, 'from_above')}")
print(f"  Approaching from below: {evaluate_limit(result, 'from_below')}")
print(f"  Oscillating approach:   {evaluate_limit(result, 'oscillating')}")
```

## Summary

The multi-state algebra of I provides:

1. **Multiple Valid States**: Operations like I - I can have multiple outcomes
2. **Context Resolution**: Mathematical context determines which state is relevant
3. **Quantum Analogy**: States exist in superposition until "measured"
4. **Extended Operations**: New elements (J, 0_I, I_0) maintain consistency
5. **Formal Verification**: Proven in Lean, Coq, and Isabelle

This framework bridges gaps in traditional mathematics by providing structured handling of singularities and indeterminate forms.

## References

- Section 106: Multi-State Analysis of I
- Section 107: Logical and Physical Interpretations
- Section 104: Proposed Solutions and Refinements
- Python Implementation: `ialgebra/multistate.py`, `ialgebra/extended_operations.py`
- Formal Verifications: `lean/MultiStateI.lean`, `coq/MultiStateI.v`, `isabelle/MultiStateI.thy`
