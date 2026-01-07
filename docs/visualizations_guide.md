# Advanced Visualizations Module Documentation

## Overview

The `advanced_visualizations.py` module provides publication-quality scientific visualizations for "The Algebra of the Indeterminate I" book. All visualizations use a distinctive neon aesthetic with deep black backgrounds, suitable for both print and digital media.

## Quick Start

### Generate All Visualizations

```bash
# From repository root
python3 generate_book_visualizations.py

# Or specify output directory
python3 generate_book_visualizations.py /path/to/output
```

### Use Individual Visualizers

```python
import matplotlib
matplotlib.use('Agg')  # For non-interactive/batch generation

from src.python.ialgebra.advanced_visualizations import (
    HealedSingularityVisualizer,
    PhaseTransitionVisualizer,
    # ... other visualizers
)

# Create and save individual visualization
viz = HealedSingularityVisualizer(figsize=(12, 8))
viz.plot(save_path='output/singularity.png')
```

## Visualizer Classes

### 1. HealedSingularityVisualizer

Demonstrates resolution of classical singularities in K_I algebra.

**Mathematical Content**:
- Function: f(x) = sin(x)/x
- Classical behavior: limit at x=0 is 1 (removable discontinuity)
- AEI behavior: f(0) = I (exact value)

**Usage**:
```python
viz = HealedSingularityVisualizer(figsize=(12, 8))
viz.plot(save_path='healed_singularity.png')
```

**Customization**: Modify figsize parameter to adjust dimensions.

---

### 2. PhaseTransitionVisualizer

3D Mexican Hat potential showing I-symmetry breaking to J field.

**Mathematical Content**:
- Potential: V(φ) = λ(φ² - v²)² with central I spike
- Pure I state at center (unbroken symmetry)
- Vacuum states on rim (broken symmetry → J field)

**Usage**:
```python
viz = PhaseTransitionVisualizer(figsize=(14, 10))
viz.plot(save_path='phase_transition.png')
```

**Physical Interpretation**: 
- Central peak: high-energy I state
- Valley: lower-energy vacuum with spontaneous J field
- Paths down: symmetry breaking mechanism

---

### 3. StabilityHeatMapVisualizer

Side-by-side comparison proving I≠0 is necessary for consistency.

**Mathematical Content**:
- Left panel: System with I≠0 (all operations bounded)
- Right panel: System with I=0 (operations diverge, 1=0 contradiction)

**Usage**:
```python
viz = StabilityHeatMapVisualizer(figsize=(16, 7))
viz.plot(save_path='stability_heatmap.png')
```

**Proof Concept**: Heat map visualizes stability metric across operation parameter space.

---

### 4. EnhancedWheelVisualizer

Projective wheel geometry with I at center.

**Mathematical Content**:
- Wheel structure: circular rim with fractions
- Poles: 0 (south), ∞ (north)
- Center: I (indeterminate element)
- Singularities: x/0 paths converge to I

**Usage**:
```python
viz = EnhancedWheelVisualizer(figsize=(12, 12))
viz.plot(save_path='wheel_of_fractions.png')
```

**Topology**: S¹ with identified singularity points and central I hub.

---

### 5. GalacticRotationCurveVisualizer

Astrophysics application: galaxy rotation without dark matter.

**Mathematical Content**:
- Newtonian prediction: v ~ 1/√r (fails)
- Observations: flat rotation curve
- AEI correction: v²_AEI = v²_Newton + Λ⊗J⊗⁴ term

**Usage**:
```python
viz = GalacticRotationCurveVisualizer(figsize=(14, 8))
viz.plot(save_path='galactic_rotation.png')
```

**Physical Significance**: Explains dark matter observations via J field, no exotic particles needed.

---

### 6. SchwarzschildModifiedVisualizer

Black hole singularity resolution via I-regularization.

**Mathematical Content**:
- Classical: infinite density at r=0
- Modified: finite curvature with I-core
- Event horizon: still present (at r_s)

**Usage**:
```python
viz = SchwarzschildModifiedVisualizer(figsize=(14, 10))
viz.plot(save_path='schwarzschild.png')
```

**Physical Implications**:
- No information paradox
- Quantum gravity finite at Planck scale
- Black hole interior remains meaningful

---

### 7. EntropyAccelerationVisualizer

Cosmic entropy driving universe expansion.

**Mathematical Content**:
- Entropy: S(t) ~ t^α
- Acceleration: C_EA = dS/dt
- Expansion: H(t) includes entropy term

**Usage**:
```python
viz = EntropyAccelerationVisualizer(figsize=(14, 8))
viz.plot(save_path='entropy_acceleration.png')
```

**Physical Mechanism**: Vacuum indetermination production accelerates expansion (alternative to dark energy).

---

## Color Scheme Reference

The neon palette is consistent across all visualizations:

```python
NEON_COLORS = {
    'cyan': '#00FFFF',      # Primary structures, axes, main curves
    'magenta': '#FF00FF',   # I element, indeterminate states
    'lime': '#00FF00',      # Stable states, successful predictions
    'yellow': '#FFFF00',    # Corrections, highlights, AEI theory
    'orange': '#FF8800',    # Infinity, divergences
    'pink': '#FF0088',      # Secondary indeterminate features
    'blue': '#0088FF',      # Supporting structures
    'white': '#FFFFFF',     # Text, labels, classical predictions
    'red': '#FF0000'        # Errors, contradictions, classical failures
}

BACKGROUND_COLOR = '#0a0a0a'  # Deep black
```

## Style Guidelines

### For Consistent Modifications

If you need to modify or extend the visualizations:

1. **Always use `setup_neon_style(ax, title, xlabel, ylabel)` helper**
   - Sets background, labels, ticks, spines, grid
   - Maintains consistent appearance

2. **Add glow effects for emphasis**:
   ```python
   # Plot main line
   ax.plot(x, y, color=NEON_COLORS['cyan'], linewidth=3)
   
   # Add glow layers
   for alpha, lw in zip([0.3, 0.2, 0.1], [5, 7, 9]):
       ax.plot(x, y, color=NEON_COLORS['cyan'], 
               linewidth=lw, alpha=alpha)
   ```

3. **Use high zorder for important elements**:
   ```python
   ax.plot(x, y, zorder=10)  # Appears on top
   ```

4. **Annotate with bounding boxes**:
   ```python
   ax.text(x, y, 'Label', 
           bbox=dict(boxstyle='round', 
                    facecolor=BACKGROUND_COLOR,
                    edgecolor=NEON_COLORS['cyan'],
                    linewidth=2, alpha=0.9))
   ```

## Technical Specifications

### Image Quality
- **DPI**: 300 (publication standard)
- **Format**: PNG with high compression
- **Color Space**: RGB
- **Background**: Opaque black (#0a0a0a)

### Dependencies
```bash
pip install matplotlib numpy scipy
```

Minimum versions:
- matplotlib >= 3.4.0
- numpy >= 1.21.0
- scipy >= 1.7.0 (optional, for some calculations)

### Performance

Generation times (approximate, on standard hardware):
- Graph 1-4: ~1-2 seconds each
- Graph 5: ~2 seconds (scatter plot)
- Graph 6: ~4-6 seconds (3D surface)
- Graph 2: ~5-7 seconds (3D surface with contours)

Total generation time: ~20-30 seconds for all 7 graphs.

## Integration with Book

### Recommended Layout Strategies

#### Full-Page Figures
For maximum impact, use full page (or double-page spread):
- Image: 70% of page
- Caption: 30% of page with mathematical details

#### Half-Page Figures
For denser technical sections:
- Two graphs per page
- Shorter captions
- Cross-references to appendix for full derivations

#### Opening Composite
Create overview figure with all 7 as thumbnails:
```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(20, 12))
gs = GridSpec(3, 3, figure=fig)

# Create each subplot and render mini versions
# ... implementation details
```

### Caption Templates

Each graph should be accompanied by:

1. **Title**: Descriptive name
2. **Mathematical Summary**: 2-3 sentences on what's shown
3. **Key Equations**: 2-5 main formulas
4. **Physical Interpretation**: Real-world meaning
5. **References**: Link to formal proofs (Lean/Coq/etc.)

Example template (LaTeX):
```latex
\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{01_healed_singularity.png}
\caption{
    \textbf{The "Healed" Singularity.}
    The function $f(x) = \sin(x)/x$ in the extended $K_I$ algebra.
    
    \textbf{Mathematics:} In classical analysis, 
    $\lim_{x \to 0} f(x) = 1$ but $f(0)$ is undefined...
    
    \textbf{Key Result:} $f(0) = I$ in $K_I$ algebra, where...
    
    \textbf{Physical Interpretation:} This demonstrates how...
    
    \textbf{Formal Verification:} See Lean proof in...
}
\label{fig:healed-singularity}
\end{figure}
```

## Troubleshooting

### Common Issues

**Problem**: Matplotlib not found
```bash
pip install matplotlib numpy scipy
```

**Problem**: Figures appear blank
```python
# Use non-interactive backend
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

**Problem**: 3D plots look distorted
```python
# Adjust viewing angle
ax.view_init(elev=20, azim=45)
```

**Problem**: Text overlaps
```python
# Adjust bbox parameters or use tight_layout
plt.tight_layout()
```

### Customization Examples

**Change figure size**:
```python
viz = HealedSingularityVisualizer(figsize=(16, 10))
```

**Modify colors** (in advanced_visualizations.py):
```python
NEON_COLORS['cyan'] = '#00CCFF'  # Slightly darker cyan
```

**Add custom annotations**:
```python
viz = HealedSingularityVisualizer()
fig, ax = viz.plot()
ax.annotate('Custom note', xy=(x, y), ...)
plt.savefig('custom.png', dpi=300)
```

## Contributing

When adding new visualizations:

1. Follow the class structure pattern
2. Include comprehensive docstrings
3. Use the neon color palette
4. Add helper method to `generate_all_book_visualizations()`
5. Update this documentation
6. Test at multiple resolutions

## License

Part of "The Algebra of the Indeterminate I" project.
See main LICENSE file.

## References

- Main book: "The Algebra of the Indeterminate I"
- Formal proofs: `formalizations/` directory
- Theory documentation: `docs/theory/`
- LaTeX sources: `latex/sections/`

---

Generated visualizations provide more than illustrations—they are computational verifications of the theoretical framework, suitable for both pedagogical and research purposes.
