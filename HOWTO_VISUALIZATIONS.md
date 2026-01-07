# How to Use the Book Visualizations

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install matplotlib numpy scipy
```

### Step 2: Generate All Visualizations
```bash
python3 generate_book_visualizations.py
```

### Step 3: View Results
```bash
# Images saved to:
ls -lh book_visualizations/*.png

# View documentation:
cat book_visualizations/README.md
```

That's it! You now have 7 publication-quality visualizations ready for the book.

---

## What You Get

After running the generation script, you'll have:

```
book_visualizations/
├── 01_healed_singularity.png         (274 KB) - sin(x)/x with I at x=0
├── 02_phase_transition_diagram.png   (1.4 MB) - Mexican Hat potential
├── 03_stability_heatmap.png          (918 KB) - I≠0 vs I=0 comparison
├── 04_enhanced_wheel.png             (681 KB) - Projective wheel geometry
├── 05_galactic_rotation.png          (430 KB) - Galaxy rotation with AEI
├── 06_schwarzschild_modified.png     (2.0 MB) - Black hole with I-core
├── 07_entropy_acceleration.png       (463 KB) - Cosmic entropy graph
├── INDEX.md                                   - Auto-generated index
└── README.md                                  - Full documentation
```

All images are **300 DPI** and ready for print publication.

---

## Using in Your Book

### LaTeX Integration

```latex
% In your LaTeX document:
\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{book_visualizations/01_healed_singularity.png}
\caption{
    \textbf{The "Healed" Singularity.}
    The function $f(x) = \sin(x)/x$ in the extended $K_I$ algebra.
    In classical analysis, this function has a removable discontinuity at $x=0$,
    but in the $K_I$ framework, it takes the exact value $I$.
}
\label{fig:healed-singularity}
\end{figure}
```

### Markdown/Jupyter

```markdown
![Healed Singularity](book_visualizations/01_healed_singularity.png)

**Figure 1**: The "Healed" Singularity - demonstrating how I resolves 
classical discontinuities in the extended number system K_I.
```

### Word/LibreOffice

1. Insert → Image → Select PNG file
2. Right-click → Format Picture → Size → Set to desired dimensions
3. Add caption below image

---

## Customization

### Generate to Different Directory

```bash
python3 generate_book_visualizations.py /path/to/my/output
```

### Generate Individual Visualization

```python
import matplotlib
matplotlib.use('Agg')

from src.python.ialgebra.advanced_visualizations import HealedSingularityVisualizer

viz = HealedSingularityVisualizer(figsize=(12, 8))
viz.plot(save_path='my_custom_output.png')
```

### Change Figure Size

```python
# Larger figure (e.g., for poster)
viz = HealedSingularityVisualizer(figsize=(20, 14))

# Smaller figure (e.g., for thumbnail)
viz = HealedSingularityVisualizer(figsize=(6, 4))
```

---

## The 7 Visualizations Explained

### 1. Healed Singularity
**What it shows**: The function f(x) = sin(x)/x with the indeterminate value I at x=0

**Why it matters**: Demonstrates how the K_I algebra resolves classical singularities by providing exact values where traditional mathematics has discontinuities.

**Key insight**: The point at x=0 is not "undefined" or a "limit" - it has the exact value I.

---

### 2. Phase Transition Diagram
**What it shows**: 3D Mexican Hat potential showing I-symmetry breaking to J field

**Why it matters**: Explains the physical mechanism by which the indeterminate I generates observable matter-energy through symmetry breaking.

**Key insight**: The pure I state (top of hat) is unstable and "falls" to create the J field (valley), similar to Higgs mechanism in particle physics.

---

### 3. Stability Heat Map
**What it shows**: Side-by-side comparison of system stability with I≠0 vs I=0

**Why it matters**: Provides visual proof that assuming I=0 leads to mathematical collapse (the 1=0 contradiction).

**Key insight**: The green stable regions (I≠0) vs red chaos (I=0) show that I must be non-zero for consistency.

---

### 4. Enhanced Wheel of Fractions
**What it shows**: Circular wheel structure with I at center, 0 at south, ∞ at north

**Why it matters**: Geometric representation of how all indeterminate forms (x/0) converge to the central I element.

**Key insight**: The wheel topology naturally accommodates division by zero, unlike the classical number line.

---

### 5. Galactic Rotation Curve
**What it shows**: Galaxy rotation velocities with Newtonian, observed, and AEI predictions

**Why it matters**: The AEI theory (with Λ⊗J⊗⁴ term) perfectly explains dark matter observations without requiring exotic particles.

**Key insight**: What we call "dark matter" is actually a manifestation of the J field from I-symmetry breaking.

---

### 6. Modified Schwarzschild Spacetime
**What it shows**: Black hole spacetime curvature that remains finite at the center

**Why it matters**: Resolves the classical black hole singularity problem - no infinite density, no information paradox.

**Key insight**: The I-core has finite curvature, making black hole physics well-defined at all radii.

---

### 7. Entropy Acceleration
**What it shows**: Cosmic entropy production driving universe expansion acceleration

**Why it matters**: Provides alternative explanation for "dark energy" as entropy-driven expansion rather than mysterious vacuum energy.

**Key insight**: The universe accelerates because vacuum fluctuations produce indeterminate states, increasing entropy.

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'matplotlib'"
**Solution**: Install dependencies with `pip install matplotlib numpy scipy`

### Problem: "Permission denied" when running script
**Solution**: Make script executable with `chmod +x generate_book_visualizations.py`

### Problem: Images appear blank or corrupted
**Solution**: Ensure matplotlib uses non-interactive backend:
```python
import matplotlib
matplotlib.use('Agg')
```

### Problem: Want higher/lower resolution
**Solution**: Modify DPI in the visualizer code (default is 300):
```python
viz.plot(save_path='output.png')  # Uses default 300 DPI
# To change DPI, modify the savefig call in advanced_visualizations.py
```

---

## Testing

Verify everything works correctly:

```bash
# Run all tests
python3 -m unittest tests.test_advanced_visualizations -v

# Should see:
# Ran 17 tests in ~11s
# OK
```

---

## Documentation

Full documentation available:

1. **Quick Reference**: `VISUALIZATIONS_README.md`
2. **Technical Guide**: `docs/visualizations_guide.md`
3. **Mathematical Details**: `book_visualizations/README.md`
4. **Implementation Summary**: `VISUALIZATION_IMPLEMENTATION.md`

---

## Support

For issues or questions:
- Check documentation files first
- Review test suite for usage examples
- See `src/python/ialgebra/advanced_visualizations.py` for implementation details

---

## License

Part of "The Algebra of the Indeterminate I" project.
See main LICENSE file for terms.

---

**"Mais cálculos do que o livro"** — More calculations than the book.

Enjoy your publication-quality visualizations! 🎨📊✨
