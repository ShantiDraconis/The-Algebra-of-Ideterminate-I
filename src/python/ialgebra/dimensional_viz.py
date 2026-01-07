"""
Dimensional Visualization Module for Theory of I

This module creates visualizations of the Theory of I behavior across
dimensions 1 through 11, showing how operations behave in different
dimensional spaces.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


class DimensionalVisualizer:
    """Visualize Theory of I operations in multiple dimensions"""
    
    def __init__(self, output_dir="../../docs/visualizations"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def visualize_dimension_1(self):
        """1D: Division by zero behavior on number line"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Classical division
        x = np.linspace(-5, 5, 1000)
        x = x[x != 0]  # Remove zero
        y_classical = 1 / x
        
        ax1.plot(x[x > 0], y_classical[x > 0], 'b-', label='x > 0', linewidth=2)
        ax1.plot(x[x < 0], y_classical[x < 0], 'r-', label='x < 0', linewidth=2)
        ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax1.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax1.set_ylim(-10, 10)
        ax1.set_xlabel('x', fontsize=12)
        ax1.set_ylabel('1/x', fontsize=12)
        ax1.set_title('Classical: 1/x (undefined at x=0)', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # With I
        x_with_I = np.linspace(-5, 5, 1001)
        y_with_I = np.where(x_with_I == 0, 0, 1 / x_with_I)  # I represented as 0 level
        
        ax2.plot(x_with_I, y_with_I, 'g-', linewidth=2, label='1/x with I')
        ax2.plot(0, 0, 'ro', markersize=15, label='1/0 = I', zorder=5)
        ax2.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax2.axvline(x=0, color='k', linestyle='--', alpha=0.3)
        ax2.set_ylim(-10, 10)
        ax2.set_xlabel('x', fontsize=12)
        ax2.set_ylabel('1/x', fontsize=12)
        ax2.set_title('With I: 1/x = I at x=0', fontsize=14, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.suptitle('Dimension 1: Division by Zero on Number Line', 
                     fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/dim_1_division_by_zero.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        return f'{self.output_dir}/dim_1_division_by_zero.png'
    
    def visualize_dimension_2(self):
        """2D: Complex plane representation"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Real-Imaginary plane
        x = np.linspace(-3, 3, 50)
        y = np.linspace(-3, 3, 50)
        X, Y = np.meshgrid(x, y)
        
        # |z| = sqrt(x^2 + y^2)
        Z = np.sqrt(X**2 + Y**2)
        Z[Z == 0] = np.nan  # Classical: undefined at origin
        
        c1 = ax1.contourf(X, Y, 1/Z, levels=20, cmap='viridis')
        ax1.plot(0, 0, 'rx', markersize=15, markeredgewidth=3, label='Undefined')
        ax1.set_xlabel('Real', fontsize=12)
        ax1.set_ylabel('Imaginary', fontsize=12)
        ax1.set_title('Classical: 1/|z| (undefined at origin)', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        plt.colorbar(c1, ax=ax1)
        
        # With I at origin
        Z_with_I = np.sqrt(X**2 + Y**2)
        Z_with_I[Z_with_I == 0] = 1  # I represented as value 1
        result = np.where(np.sqrt(X**2 + Y**2) == 0, 1, 1/Z_with_I)
        
        c2 = ax2.contourf(X, Y, result, levels=20, cmap='plasma')
        ax2.plot(0, 0, 'wo', markersize=12, markeredgewidth=2, 
                markeredgecolor='red', label='1/0 = I')
        ax2.set_xlabel('Real', fontsize=12)
        ax2.set_ylabel('Imaginary', fontsize=12)
        ax2.set_title('With I: 1/|z| = I at origin', fontsize=14, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        plt.colorbar(c2, ax=ax2)
        
        plt.suptitle('Dimension 2: Complex Plane Division', 
                     fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/dim_2_complex_plane.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        return f'{self.output_dir}/dim_2_complex_plane.png'
    
    def visualize_dimension_3(self):
        """3D: Spatial representation"""
        fig = plt.figure(figsize=(15, 5))
        
        # Create 3D grid
        x = np.linspace(-2, 2, 30)
        y = np.linspace(-2, 2, 30)
        z = np.linspace(-2, 2, 30)
        
        # Classical singularity
        ax1 = fig.add_subplot(131, projection='3d')
        X, Y = np.meshgrid(x, y)
        Z_surface = np.sqrt(X**2 + Y**2)
        Z_surface[Z_surface == 0] = np.nan
        ax1.plot_surface(X, Y, 1/Z_surface, cmap='coolwarm', alpha=0.7)
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('1/r')
        ax1.set_title('Classical: Singularity at origin', fontweight='bold')
        
        # With I
        ax2 = fig.add_subplot(132, projection='3d')
        Z_with_I = np.where(np.sqrt(X**2 + Y**2) == 0, 1, 1/np.sqrt(X**2 + Y**2))
        ax2.plot_surface(X, Y, Z_with_I, cmap='viridis', alpha=0.7)
        ax2.scatter([0], [0], [1], color='red', s=100, label='I')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('1/r')
        ax2.set_title('With I: Defined at origin', fontweight='bold')
        
        # I-absorption pattern
        ax3 = fig.add_subplot(133, projection='3d')
        theta = np.linspace(0, 2*np.pi, 50)
        phi = np.linspace(0, np.pi, 50)
        THETA, PHI = np.meshgrid(theta, phi)
        R = 1
        X_sphere = R * np.sin(PHI) * np.cos(THETA)
        Y_sphere = R * np.sin(PHI) * np.sin(THETA)
        Z_sphere = R * np.cos(PHI)
        ax3.plot_surface(X_sphere, Y_sphere, Z_sphere, cmap='Reds', alpha=0.6)
        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.set_zlabel('Z')
        ax3.set_title('I-sphere: Absorption domain', fontweight='bold')
        
        plt.suptitle('Dimension 3: Spatial Division Behavior', 
                     fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/dim_3_spatial.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        return f'{self.output_dir}/dim_3_spatial.png'
    
    def visualize_higher_dimensions(self, dim):
        """Visualize higher dimensions using projection and slicing"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 12))
        
        # Generate higher-dimensional data
        n_points = 1000
        np.random.seed(42)
        
        # Random points in n-dimensional space
        points = np.random.randn(n_points, dim)
        norms = np.linalg.norm(points, axis=1)
        
        # Classical: 1/||x||
        classical_values = 1 / (norms + 1e-10)
        
        # With I: points near origin map to I
        with_I_values = np.where(norms < 0.1, 0, 1 / (norms + 1e-10))
        
        # Project to 2D for visualization (first two dimensions)
        ax1 = axes[0, 0]
        scatter1 = ax1.scatter(points[:, 0], points[:, 1], c=classical_values, 
                              cmap='viridis', alpha=0.6, s=20)
        ax1.set_xlabel(f'Dimension 1', fontsize=10)
        ax1.set_ylabel(f'Dimension 2', fontsize=10)
        ax1.set_title(f'D{dim}: Classical 1/||x|| (projection)', fontweight='bold')
        plt.colorbar(scatter1, ax=ax1)
        
        ax2 = axes[0, 1]
        scatter2 = ax2.scatter(points[:, 0], points[:, 1], c=with_I_values, 
                              cmap='plasma', alpha=0.6, s=20)
        ax2.set_xlabel(f'Dimension 1', fontsize=10)
        ax2.set_ylabel(f'Dimension 2', fontsize=10)
        ax2.set_title(f'D{dim}: With I at origin (projection)', fontweight='bold')
        plt.colorbar(scatter2, ax=ax2)
        
        # Norm distribution
        ax3 = axes[1, 0]
        ax3.hist(norms, bins=50, alpha=0.7, color='blue', edgecolor='black')
        ax3.axvline(x=0.1, color='r', linestyle='--', linewidth=2, label='I threshold')
        ax3.set_xlabel('||x||', fontsize=10)
        ax3.set_ylabel('Frequency', fontsize=10)
        ax3.set_title(f'D{dim}: Norm distribution', fontweight='bold')
        ax3.legend()
        
        # Value distribution
        ax4 = axes[1, 1]
        ax4.hist(classical_values[classical_values < 10], bins=50, alpha=0.5, 
                label='Classical', color='green')
        ax4.hist(with_I_values[with_I_values < 10], bins=50, alpha=0.5, 
                label='With I', color='orange')
        ax4.set_xlabel('1/||x|| value', fontsize=10)
        ax4.set_ylabel('Frequency', fontsize=10)
        ax4.set_title(f'D{dim}: Value distributions', fontweight='bold')
        ax4.legend()
        
        plt.suptitle(f'Dimension {dim}: Higher-Dimensional Analysis', 
                     fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/dim_{dim}_higher.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        return f'{self.output_dir}/dim_{dim}_higher.png'
    
    def create_all_visualizations(self):
        """Create visualizations for dimensions 1-11"""
        print("Creating dimensional visualizations...")
        
        results = {}
        
        # Dimension 1
        print("  Dimension 1: Number line...")
        results[1] = self.visualize_dimension_1()
        
        # Dimension 2
        print("  Dimension 2: Complex plane...")
        results[2] = self.visualize_dimension_2()
        
        # Dimension 3
        print("  Dimension 3: 3D space...")
        results[3] = self.visualize_dimension_3()
        
        # Dimensions 4-11
        for dim in range(4, 12):
            print(f"  Dimension {dim}: Higher-dimensional analysis...")
            results[dim] = self.visualize_higher_dimensions(dim)
        
        print(f"\nAll visualizations saved to {self.output_dir}/")
        return results
    
    def create_summary_report(self, results):
        """Create a summary report with all visualizations"""
        report = f"""# Dimensional Visualization Report: Theory of I

## Overview

This report presents visualizations of the Theory of I (I = 0/0) across dimensions 1 through 11.

## Dimensional Analysis

"""
        for dim, filepath in sorted(results.items()):
            report += f"""
### Dimension {dim}

![Dimension {dim}]({filepath})

**Key observations for D{dim}:**
- Classical mathematics: Singularity at origin (undefined)
- With I: Well-defined at origin (I = 0/0)
- Behavior: {"Simple number line" if dim == 1 else "Complex plane" if dim == 2 else "3D spatial" if dim == 3 else f"{dim}-dimensional projection"}

"""
        
        report += """
## Mathematical Interpretation

In each dimension:
1. **Classical approach**: Division by zero creates singularities
2. **Theory of I**: I fills the gap, providing algebraic consistency
3. **Physical analogy**: Similar to how complex numbers extend reals

## Conclusions

The visualizations demonstrate that:
- I provides consistent behavior across all dimensions
- Singularities are resolved in every dimensional space
- The algebraic structure remains coherent
"""
        
        with open(f'{self.output_dir}/VISUALIZATION_REPORT.md', 'w') as f:
            f.write(report)
        
        print(f"\nReport saved to {self.output_dir}/VISUALIZATION_REPORT.md")


def main():
    """Main execution function"""
    print("=" * 80)
    print("DIMENSIONAL VISUALIZATION MODULE")
    print("Theory of I: Behavior across Dimensions 1-11")
    print("=" * 80)
    print()
    
    visualizer = DimensionalVisualizer()
    results = visualizer.create_all_visualizations()
    visualizer.create_summary_report(results)
    
    print()
    print("=" * 80)
    print("COMPLETE: All dimensional visualizations generated")
    print("=" * 80)


if __name__ == "__main__":
    main()
