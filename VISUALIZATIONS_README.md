# Book Visualizations - Quick Reference

## Overview

This repository includes **7 publication-quality visualizations** designed for the book "The Algebra of the Indeterminate I". All visualizations use a distinctive **neon aesthetic** with deep black backgrounds.

## Generate All Visualizations

```bash
# Simple one-liner
python3 generate_book_visualizations.py

# Or specify output directory
python3 generate_book_visualizations.py ./my_output_dir
```

## The 7 Visualizations

1. **Healed Singularity** - f(x) = sin(x)/x with I at x=0
2. **Phase Transition Diagram** - I-Symmetry Breaking to J Field (Mexican Hat)
3. **Stability Heat Map** - Proof that I≠0 prevents system collapse
4. **Enhanced Wheel of Fractions** - Projective wheel geometry with I at center
5. **Galactic Rotation Curve** - AEI correction explaining dark matter observations
6. **Modified Schwarzschild Spacetime** - Black hole with finite I-core
7. **Entropy Acceleration C_EA** - Entropy-driven universe expansion

## Visual Style

- **Background**: Deep Black (#0a0a0a)
- **Primary Colors**: Neon Cyan, Magenta, Lime Green, Yellow
- **Resolution**: 300 DPI (publication quality)
- **Purpose**: Suitable for 350-page technical book

## Documentation

- **Full Guide**: [`docs/visualizations_guide.md`](docs/visualizations_guide.md)
- **Mathematical Details**: [`book_visualizations/README.md`](book_visualizations/README.md)
- **Generated Index**: [`book_visualizations/INDEX.md`](book_visualizations/INDEX.md)

## Requirements

```bash
pip install matplotlib numpy scipy
```

## Python API

```python
from src.python.ialgebra.advanced_visualizations import HealedSingularityVisualizer

viz = HealedSingularityVisualizer(figsize=(12, 8))
viz.plot(save_path='output/singularity.png')
```

## Tests

```bash
python3 -m unittest tests.test_advanced_visualizations -v
```

All 17 tests verify that visualizations can be generated successfully.

## Design Philosophy

The neon-on-black aesthetic serves as:
1. **Visual Identity** - Distinctive and memorable
2. **Conceptual Metaphor** - "Bringing light to the indeterminate"
3. **Technical Clarity** - High contrast for mathematical features
4. **Print Quality** - Excellent reproduction on paper

---

Part of the formal framework for "The Algebra of the Indeterminate I".
