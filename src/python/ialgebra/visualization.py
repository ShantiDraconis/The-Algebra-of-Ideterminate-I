"""
Visualization Module for I-Algebra.

This module provides comprehensive graphical representations of the
indeterminate algebra, including:

1. I-plane representation in extended algebra
2. Wheel of Fractions structure
3. Singularity collapse diagrams
4. Convergence behavior
5. I vs 0 contradiction visualization

Requirements: matplotlib, numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Wedge
from matplotlib.collections import PatchCollection
from typing import List, Tuple, Optional
import math

try:
    from .types import IElement
    from .wheel import WheelFraction, WheelStructure
except ImportError:
    # For standalone execution
    import sys
    sys.path.append('..')
    from types import IElement


class IPlaneVisualizer:
    """
    Visualize the extended I-plane.
    
    Shows the representation of I in the extended algebraic structure,
    mapping real and imaginary axes along with the I singularity locus.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (10, 10)):
        """Initialize the visualizer."""
        self.figsize = figsize
        self.fig = None
        self.ax = None
    
    def plot_extended_plane(self, show_singularities: bool = True,
                          save_path: Optional[str] = None):
        """
        Plot the extended I-plane with real/imaginary axes.
        
        Creates a visualization showing:
        - Real axis
        - Imaginary axis
        - I singularity point
        - Paths from various x/0 to I
        
        Args:
            show_singularities: Whether to show singularity paths
            save_path: Path to save figure (None for display only)
        """
        self.fig, self.ax = plt.subplots(figsize=self.figsize)
        
        # Set up coordinate system
        self.ax.set_xlim(-3, 3)
        self.ax.set_ylim(-3, 3)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        
        # Draw axes
        self.ax.axhline(y=0, color='k', linewidth=1.5, label='Real Axis')
        self.ax.axvline(x=0, color='k', linewidth=1.5, label='Imaginary Axis')
        
        # Mark special points
        # I at origin (in this geometric representation)
        circle_I = Circle((0, 0), 0.15, color='red', zorder=10, label='I')
        self.ax.add_patch(circle_I)
        self.ax.text(0.2, 0.2, 'I', fontsize=16, fontweight='bold', color='red')
        
        # Mark 1/0, -1/0 positions (conceptual)
        if show_singularities:
            # Show arrows from various x/0 converging to I
            singularities = [
                (2, 2, '1/0'),
                (-2, 2, '-1/0'),
                (2, -2, '2/0'),
                (-2, -2, '3/0')
            ]
            
            for x, y, label in singularities:
                # Point at position
                self.ax.plot(x, y, 'bo', markersize=8, alpha=0.6)
                self.ax.text(x + 0.2, y + 0.2, label, fontsize=10)
                
                # Arrow pointing to I
                arrow = FancyArrowPatch((x, y), (0.15, 0.15),
                                      arrowstyle='->', mutation_scale=20,
                                      color='blue', alpha=0.5, linewidth=2,
                                      linestyle='--')
                self.ax.add_patch(arrow)
        
        # Add title and labels
        self.ax.set_title('Representation of I in the Extended Algebra\n' +
                         'All x/0 collapse to single point I',
                         fontsize=14, fontweight='bold')
        self.ax.set_xlabel('Real Component', fontsize=12)
        self.ax.set_ylabel('Imaginary Component', fontsize=12)
        
        # Legend
        self.ax.legend(loc='upper right', fontsize=10)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved to {save_path}")
        else:
            plt.show()
        
        return self.fig, self.ax


class WheelVisualizer:
    """
    Visualize the Wheel of Fractions structure.
    
    Creates diagrams showing how the wheel naturally accommodates
    division by zero through the geometric structure.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (12, 10)):
        """Initialize wheel visualizer."""
        self.figsize = figsize
    
    def plot_wheel_structure(self, save_path: Optional[str] = None):
        """
        Plot the Wheel of Fractions structure.
        
        Shows the wheel as a circular structure with:
        - Regular fractions on the rim
        - I at the center/hub
        - Singularity spokes leading to I
        
        Args:
            save_path: Path to save figure
        """
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Draw wheel rim (circle)
        rim = Circle((0, 0), 2.0, fill=False, edgecolor='black', linewidth=3)
        ax.add_patch(rim)
        
        # Draw hub at center (I)
        hub = Circle((0, 0), 0.2, color='red', zorder=10)
        ax.add_patch(hub)
        ax.text(0, 0, 'I', ha='center', va='center', fontsize=16,
               fontweight='bold', color='white', zorder=11)
        
        # Place fractions around rim
        n_fractions = 12
        angles = np.linspace(0, 2*np.pi, n_fractions, endpoint=False)
        
        regular_fractions = [
            "1/2", "2/3", "3/4", "4/5", "5/6", "1/1",
            "6/5", "5/4", "4/3", "3/2", "2/1", "3/1"
        ]
        
        for i, (angle, frac_str) in enumerate(zip(angles, regular_fractions)):
            x = 2.0 * np.cos(angle)
            y = 2.0 * np.sin(angle)
            
            # Point on rim
            ax.plot(x, y, 'bo', markersize=10)
            
            # Label
            label_x = 2.3 * np.cos(angle)
            label_y = 2.3 * np.sin(angle)
            ax.text(label_x, label_y, frac_str, ha='center', va='center',
                   fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
        
        # Draw spokes from singularities to hub
        singular_angles = [0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3]
        singular_labels = ["1/0", "2/0", "3/0", "-1/0", "-2/0", "-3/0"]
        
        for angle, label in zip(singular_angles, singular_labels):
            # Singularity point outside rim
            sx = 2.5 * np.cos(angle)
            sy = 2.5 * np.sin(angle)
            
            # Spoke from singularity to hub
            ax.plot([sx, 0.2*np.cos(angle)], [sy, 0.2*np.sin(angle)],
                   'r--', linewidth=2, alpha=0.7)
            
            # Singularity label
            ax.text(sx, sy, label, ha='center', va='center', fontsize=11,
                   fontweight='bold', color='red',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
        
        # Add title
        ax.text(0, -2.7, 'Wheel of Fractions Structure', ha='center',
               fontsize=16, fontweight='bold')
        ax.text(0, -2.95, 'All x/0 singularities collapse to central I',
               ha='center', fontsize=12, style='italic')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved to {save_path}")
        else:
            plt.show()
        
        return fig, ax


class CollapseVisualizer:
    """
    Visualize the mathematical collapse when I = 0.
    
    Shows how assuming I = 0 leads to the contradiction 1 = 0,
    causing the entire number system to collapse.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (14, 8)):
        """Initialize collapse visualizer."""
        self.figsize = figsize
    
    def plot_collapse_diagram(self, save_path: Optional[str] = None):
        """
        Plot the collapse of the number system when I = 0.
        
        Demonstrates:
        1. Normal extended system with distinct numbers
        2. Assumption I = 0
        3. Resulting collapse where all numbers become equal
        
        Args:
            save_path: Path to save figure
        """
        fig, axes = plt.subplots(1, 2, figsize=self.figsize)
        
        # Left panel: Normal system
        ax1 = axes[0]
        ax1.set_xlim(-1, 5)
        ax1.set_ylim(-1, 5)
        ax1.set_aspect('equal')
        ax1.set_title('Extended Number System\n(Normal State)', 
                     fontsize=14, fontweight='bold')
        ax1.axis('off')
        
        # Draw distinct numbers in normal system
        numbers_normal = [
            (1, 3, '0', 'blue'),
            (2, 3, '1', 'green'),
            (3, 3, 'I', 'red'),
            (1, 2, '2', 'purple'),
            (2, 2, '3', 'orange'),
            (3, 2, 'x', 'brown')
        ]
        
        for x, y, label, color in numbers_normal:
            circle = Circle((x, y), 0.3, color=color, alpha=0.7)
            ax1.add_patch(circle)
            ax1.text(x, y, label, ha='center', va='center',
                    fontsize=14, fontweight='bold', color='white')
        
        ax1.text(2, 0.5, 'All numbers distinct\n0 ≠ 1 ≠ I ≠ 2 ≠ 3 ≠ x',
                ha='center', fontsize=11, style='italic',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))
        
        # Right panel: Collapsed system
        ax2 = axes[1]
        ax2.set_xlim(-1, 5)
        ax2.set_ylim(-1, 5)
        ax2.set_aspect('equal')
        ax2.set_title('System After I = 0 Assumption\n(Collapsed State)',
                     fontsize=14, fontweight='bold', color='red')
        ax2.axis('off')
        
        # All numbers collapse to same point
        center_x, center_y = 2, 2.5
        
        # Large circle representing singularity
        singularity = Circle((center_x, center_y), 0.8, color='black', alpha=0.3)
        ax2.add_patch(singularity)
        
        # All number labels at same location
        labels_collapsed = ['0', '1', 'I', '2', '3', 'x']
        label_offsets = [
            (-0.3, 0.3), (0.3, 0.3), (0, 0),
            (-0.3, -0.3), (0.3, -0.3), (0, -0.5)
        ]
        
        for label, (dx, dy) in zip(labels_collapsed, label_offsets):
            ax2.text(center_x + dx, center_y + dy, label,
                    ha='center', va='center', fontsize=12,
                    fontweight='bold', color='red')
        
        # Draw arrows showing collapse
        arrow_starts = [(1, 3), (2, 3), (3, 3), (1, 1.5), (3, 1.5)]
        for start in arrow_starts:
            arrow = FancyArrowPatch(start, (center_x, center_y),
                                  arrowstyle='->', mutation_scale=20,
                                  color='red', alpha=0.5, linewidth=2)
            ax2.add_patch(arrow)
        
        ax2.text(center_x, 0.5, 'All numbers collapse to 0\n1 = 0 (CONTRADICTION)',
                ha='center', fontsize=11, fontweight='bold', color='red',
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
        
        # Main title
        fig.suptitle('Mathematical Collapse when I = 0', fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved to {save_path}")
        else:
            plt.show()
        
        return fig, axes


class ConvergenceVisualizer:
    """
    Visualize convergence behavior of sequences approaching I.
    
    Shows how limits like lim(x→0) 1/x converge to I.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (12, 6)):
        """Initialize convergence visualizer."""
        self.figsize = figsize
    
    def plot_limit_convergence(self, save_path: Optional[str] = None):
        """
        Plot convergence of 1/x to I as x approaches 0.
        
        Args:
            save_path: Path to save figure
        """
        fig, axes = plt.subplots(1, 2, figsize=self.figsize)
        
        # Left: approach from positive side
        ax1 = axes[0]
        x_pos = np.logspace(-3, 0, 100)  # 0.001 to 1
        y_pos = 1 / x_pos
        
        ax1.plot(x_pos, y_pos, 'b-', linewidth=2, label='f(x) = 1/x')
        ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax1.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax1.set_xlabel('x', fontsize=12)
        ax1.set_ylabel('f(x)', fontsize=12)
        ax1.set_title('Approach from x > 0', fontsize=13, fontweight='bold')
        ax1.set_ylim(0, 1000)
        ax1.set_xlim(0, 1)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Add annotation
        ax1.annotate('Diverges to ∞ (I)', xy=(0.01, 100), xytext=(0.3, 700),
                    arrowprops=dict(arrowstyle='->', color='red', lw=2),
                    fontsize=11, fontweight='bold', color='red')
        
        # Right: approach from negative side
        ax2 = axes[1]
        x_neg = -np.logspace(-3, 0, 100)  # -1 to -0.001
        y_neg = 1 / x_neg
        
        ax2.plot(x_neg, y_neg, 'r-', linewidth=2, label='f(x) = 1/x')
        ax2.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax2.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax2.set_xlabel('x', fontsize=12)
        ax2.set_ylabel('f(x)', fontsize=12)
        ax2.set_title('Approach from x < 0', fontsize=13, fontweight='bold')
        ax2.set_ylim(-1000, 0)
        ax2.set_xlim(-1, 0)
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # Add annotation
        ax2.annotate('Diverges to -∞ (I)', xy=(-0.01, -100), xytext=(-0.7, -700),
                    arrowprops=dict(arrowstyle='->', color='red', lw=2),
                    fontsize=11, fontweight='bold', color='red')
        
        fig.suptitle('Convergence to I: lim(x→0) 1/x = I', 
                    fontsize=15, fontweight='bold')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved to {save_path}")
        else:
            plt.show()
        
        return fig, axes


class ComparisonVisualizer:
    """
    Visualize comparison between classical and I-algebra approaches.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (14, 8)):
        """Initialize comparison visualizer."""
        self.figsize = figsize
    
    def plot_comparison_table(self, save_path: Optional[str] = None):
        """
        Create a visual comparison table of algebraic properties.
        
        Args:
            save_path: Path to save figure
        """
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.axis('off')
        
        # Create table data
        properties = [
            ['Property', 'Classical Algebra', 'I-Algebra'],
            ['Division by zero', 'Undefined', 'I = x/0'],
            ['I + I', 'N/A', 'I'],
            ['I × I', 'N/A', 'I'],
            ['x × I', 'N/A', 'I (absorption)'],
            ['I - I', 'N/A', 'I (or 0 contextually)'],
            ['Multiplicative inverse', 'All x≠0', 'None for I'],
            ['Field axioms', 'Satisfied', 'Modified'],
            ['Singularities', 'Undefined', 'Computable (= I)']
        ]
        
        # Create table
        table = ax.table(cellText=properties, cellLoc='center', loc='center',
                        bbox=[0, 0, 1, 1])
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1, 2)
        
        # Style header row
        for i in range(3):
            cell = table[(0, i)]
            cell.set_facecolor('#4CAF50')
            cell.set_text_props(weight='bold', color='white')
        
        # Alternate row colors
        for i in range(1, len(properties)):
            for j in range(3):
                cell = table[(i, j)]
                if i % 2 == 0:
                    cell.set_facecolor('#f0f0f0')
                else:
                    cell.set_facecolor('#ffffff')
        
        ax.set_title('Comparison: Classical Algebra vs I-Algebra',
                    fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved to {save_path}")
        else:
            plt.show()
        
        return fig, ax


def generate_all_visualizations(output_dir: str = './visualizations'):
    """
    Generate all visualization diagrams for the I-algebra.
    
    Creates comprehensive set of diagrams including:
    - Extended I-plane
    - Wheel of fractions
    - Collapse diagram
    - Convergence plots
    - Comparison tables
    
    Args:
        output_dir: Directory to save all visualizations
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating I-Algebra Visualizations...")
    print("=" * 70)
    
    # 1. Extended I-plane
    print("\n1. Creating Extended I-Plane diagram...")
    plane_viz = IPlaneVisualizer()
    plane_viz.plot_extended_plane(save_path=f"{output_dir}/i_plane.png")
    
    # 2. Wheel structure
    print("\n2. Creating Wheel of Fractions diagram...")
    wheel_viz = WheelVisualizer()
    wheel_viz.plot_wheel_structure(save_path=f"{output_dir}/wheel_structure.png")
    
    # 3. Collapse diagram
    print("\n3. Creating Collapse diagram...")
    collapse_viz = CollapseVisualizer()
    collapse_viz.plot_collapse_diagram(save_path=f"{output_dir}/collapse_i_equals_zero.png")
    
    # 4. Convergence plots
    print("\n4. Creating Convergence plots...")
    conv_viz = ConvergenceVisualizer()
    conv_viz.plot_limit_convergence(save_path=f"{output_dir}/convergence_to_i.png")
    
    # 5. Comparison table
    print("\n5. Creating Comparison table...")
    comp_viz = ComparisonVisualizer()
    comp_viz.plot_comparison_table(save_path=f"{output_dir}/comparison_table.png")
    
    print("\n" + "=" * 70)
    print(f"All visualizations saved to: {output_dir}/")
    print("=" * 70)


if __name__ == "__main__":
    # Generate all visualizations
    generate_all_visualizations()
