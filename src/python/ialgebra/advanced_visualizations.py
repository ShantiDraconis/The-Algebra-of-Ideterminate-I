"""
Advanced Visualizations for "The Algebra of the Indeterminate I" Book

This module generates the 7 main visualizations required for the book with
neon color scheme (cyan, magenta, lime green on dark background).

Visualizations:
1. "Healed" Singularity: f(x) = sin(x)/x with I at x=0
2. Phase Transition Diagram: I-Symmetry vs J Field (Mexican Hat)
3. Algebraic Stability Heat Map: I≠0 vs I=0
4. Wheel of Fractions (Enhanced Projective Wheel Geometry)
5. Galactic Rotation Curve with AEI correction
6. Modified Schwarzschild Spacetime with I
7. Entropy C_EA (Entropy Acceleration) Graph

Visual Style:
- Deep Black background (#000000 or #0a0a0a)
- Neon Cyan (#00FFFF)
- Neon Magenta (#FF00FF)
- Lime Green (#00FF00)
- Neon Yellow (#FFFF00)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Wedge, Rectangle
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
from typing import Optional, Tuple, List
import matplotlib.gridspec as gridspec

# Neon color palette
NEON_COLORS = {
    'cyan': '#00FFFF',
    'magenta': '#FF00FF',
    'lime': '#00FF00',
    'yellow': '#FFFF00',
    'orange': '#FF8800',
    'pink': '#FF0088',
    'blue': '#0088FF',
    'white': '#FFFFFF',
    'red': '#FF0000'
}

BACKGROUND_COLOR = '#0a0a0a'  # Deep black with slight gray


def setup_neon_style(ax, title: str = "", xlabel: str = "", ylabel: str = ""):
    """Configure axes with neon style."""
    ax.set_facecolor(BACKGROUND_COLOR)
    if title:
        ax.set_title(title, color=NEON_COLORS['cyan'], fontsize=16, 
                     fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, color=NEON_COLORS['white'], fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, color=NEON_COLORS['white'], fontsize=12)
    
    ax.tick_params(colors=NEON_COLORS['white'], which='both')
    ax.spines['bottom'].set_color(NEON_COLORS['white'])
    ax.spines['top'].set_color(NEON_COLORS['white'])
    ax.spines['left'].set_color(NEON_COLORS['white'])
    ax.spines['right'].set_color(NEON_COLORS['white'])
    ax.grid(True, alpha=0.2, color=NEON_COLORS['cyan'], linestyle='--')


class HealedSingularityVisualizer:
    """
    Graph 1: The "Healed" Singularity f(x) = sin(x)/x in K_I
    
    Shows that at x=0, instead of a removable discontinuity (limit exists),
    the graph shows the exact value I. The Y-axis has a special marking for I.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (12, 8)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate the healed singularity visualization."""
        fig, ax = plt.subplots(figsize=self.figsize, facecolor=BACKGROUND_COLOR)
        
        # Calculate sin(x)/x
        x_neg = np.linspace(-4*np.pi, -0.01, 500)
        x_pos = np.linspace(0.01, 4*np.pi, 500)
        
        y_neg = np.sin(x_neg) / x_neg
        y_pos = np.sin(x_pos) / x_pos
        
        # Plot the function
        ax.plot(x_neg, y_neg, color=NEON_COLORS['cyan'], linewidth=2.5, 
                label=r'$f(x) = \frac{\sin(x)}{x}$', zorder=5)
        ax.plot(x_pos, y_pos, color=NEON_COLORS['cyan'], linewidth=2.5, zorder=5)
        
        # Special I value at x=0
        I_value = 1.0  # The limit value
        
        # Draw a glowing point at x=0
        ax.plot(0, I_value, 'o', color=NEON_COLORS['magenta'], 
                markersize=20, markeredgewidth=3, 
                markeredgecolor=NEON_COLORS['yellow'], zorder=10,
                label='I (Indeterminate Value)')
        
        # Add glow effect around the I point
        for alpha, size in zip([0.3, 0.2, 0.1], [35, 50, 65]):
            ax.plot(0, I_value, 'o', color=NEON_COLORS['magenta'], 
                    markersize=size, alpha=alpha, zorder=9)
        
        # Special marking for I on Y-axis
        ax.axhline(y=I_value, color=NEON_COLORS['lime'], linestyle='--', 
                   alpha=0.5, linewidth=1.5, label='y = I = 1')
        ax.text(-0.5, I_value + 0.05, 'I', color=NEON_COLORS['magenta'], 
                fontsize=20, fontweight='bold', ha='right')
        
        # Vertical line through singularity
        ax.axvline(x=0, color=NEON_COLORS['yellow'], linestyle=':', 
                   alpha=0.3, linewidth=1.5)
        
        # Add dimensional transition region (visual metaphor)
        rect = Rectangle((-0.5, 0.85), 1.0, 0.3, 
                        facecolor=NEON_COLORS['magenta'], 
                        alpha=0.15, edgecolor=NEON_COLORS['magenta'],
                        linewidth=2, linestyle='--', zorder=1)
        ax.add_patch(rect)
        ax.text(0, 0.7, 'Indetermination\nPlane', 
                color=NEON_COLORS['magenta'], fontsize=10,
                ha='center', style='italic', alpha=0.8)
        
        setup_neon_style(ax, 
                        title=r'The "Healed" Singularity: $f(x) = \frac{\sin(x)}{x}$ in $K_I$',
                        xlabel='x', ylabel='f(x)')
        
        ax.set_xlim(-4*np.pi, 4*np.pi)
        ax.set_ylim(-0.5, 1.3)
        ax.legend(loc='upper right', facecolor=BACKGROUND_COLOR, 
                 edgecolor=NEON_COLORS['cyan'], fontsize=11,
                 labelcolor=NEON_COLORS['white'])
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR, 
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, ax


class PhaseTransitionVisualizer:
    """
    Graph 2: Phase Transition Diagram - I-Symmetry vs J Field
    
    Modified "Mexican Hat" potential. Top of the hat is pure I state.
    Fall to edges represents symmetry breaking that generates mass and J field.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (14, 10)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate phase transition diagram with Mexican Hat potential."""
        fig = plt.figure(figsize=self.figsize, facecolor=BACKGROUND_COLOR)
        ax = fig.add_subplot(111, projection='3d', facecolor=BACKGROUND_COLOR)
        
        # Create Mexican Hat potential: V(φ) = λ(φ² - v²)²
        phi = np.linspace(-2, 2, 200)
        theta = np.linspace(0, 2*np.pi, 200)
        PHI, THETA = np.meshgrid(phi, theta)
        
        # Radial coordinate
        R = np.abs(PHI)
        
        # Modified potential with I at center
        v_squared = 0.5  # Vacuum expectation value
        lambda_coupling = 1.0
        
        V = lambda_coupling * (R**2 - v_squared)**2
        
        # Add central spike for I state
        mask_center = R < 0.3
        V[mask_center] = V[mask_center] + 2.5 * np.exp(-R[mask_center]**2 / 0.05)
        
        # Convert to Cartesian
        X = R * np.cos(THETA)
        Y = R * np.sin(THETA)
        
        # Plot surface with neon colors
        surf = ax.plot_surface(X, Y, V, cmap='twilight', 
                               alpha=0.8, linewidth=0, 
                               antialiased=True, edgecolors=NEON_COLORS['cyan'])
        
        # Add contour lines on bottom
        ax.contour(X, Y, V, levels=15, colors=NEON_COLORS['cyan'], 
                   alpha=0.4, linewidths=1.5, offset=0)
        
        # Mark special points
        # Central I state
        ax.scatter([0], [0], [2.5], color=NEON_COLORS['magenta'], 
                  s=300, marker='o', edgecolors=NEON_COLORS['yellow'],
                  linewidths=3, label='Pure I State', zorder=10)
        
        # Vacuum states (broken symmetry)
        vacuum_angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
        for angle in vacuum_angles:
            x_vac = v_squared**0.5 * np.cos(angle)
            y_vac = v_squared**0.5 * np.sin(angle)
            ax.scatter([x_vac], [y_vac], [0], color=NEON_COLORS['lime'], 
                      s=100, marker='o', alpha=0.8)
        
        # Add J field arrows
        for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
            x_start = 0.15 * np.cos(angle)
            y_start = 0.15 * np.sin(angle)
            x_end = 0.7 * np.cos(angle)
            y_end = 0.7 * np.sin(angle)
            
            ax.plot([x_start, x_end], [y_start, y_end], [2.0, 0.5],
                   color=NEON_COLORS['yellow'], linewidth=3, 
                   alpha=0.7, linestyle='--')
        
        # Styling
        ax.set_facecolor(BACKGROUND_COLOR)
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor(NEON_COLORS['white'])
        ax.yaxis.pane.set_edgecolor(NEON_COLORS['white'])
        ax.zaxis.pane.set_edgecolor(NEON_COLORS['white'])
        ax.xaxis.line.set_color(NEON_COLORS['white'])
        ax.yaxis.line.set_color(NEON_COLORS['white'])
        ax.zaxis.line.set_color(NEON_COLORS['white'])
        ax.tick_params(colors=NEON_COLORS['white'])
        
        ax.set_xlabel('Information Density φ₁', color=NEON_COLORS['white'], 
                     fontsize=11, labelpad=10)
        ax.set_ylabel('Information Density φ₂', color=NEON_COLORS['white'], 
                     fontsize=11, labelpad=10)
        ax.set_zlabel('Vacuum Energy V(φ)', color=NEON_COLORS['white'], 
                     fontsize=11, labelpad=10)
        
        ax.set_title('Phase Transition: I-Symmetry Breaking → J Field\n' +
                    'Modified Mexican Hat Potential',
                    color=NEON_COLORS['cyan'], fontsize=16, 
                    fontweight='bold', pad=20)
        
        # Add text annotations
        ax.text2D(0.15, 0.85, 'Pure I State\n(Unbroken Symmetry)', 
                 transform=ax.transAxes, color=NEON_COLORS['magenta'],
                 fontsize=11, fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR, 
                          edgecolor=NEON_COLORS['magenta'], alpha=0.8))
        
        ax.text2D(0.15, 0.72, 'J Field Vacuum\n(Broken Symmetry)', 
                 transform=ax.transAxes, color=NEON_COLORS['lime'],
                 fontsize=11, fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR, 
                          edgecolor=NEON_COLORS['lime'], alpha=0.8))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR,
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, ax


class StabilityHeatMapVisualizer:
    """
    Graph 3: Algebraic Stability Heat Map (I vs 0)
    
    Comparative heat map proving why I=0 collapses the system.
    Side A (I≠0): Green stable map showing operations maintain consistency
    Side B (I=0): Red map showing infinity/error, demonstrating "Trivialization"
    """
    
    def __init__(self, figsize: Tuple[int, int] = (16, 7)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate stability comparison heat map."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=self.figsize, 
                                       facecolor=BACKGROUND_COLOR)
        
        # Create grid for operations
        n = 50
        x = np.linspace(-10, 10, n)
        y = np.linspace(-10, 10, n)
        X, Y = np.meshgrid(x, y)
        
        # Side A: System with I ≠ 0 (Stable)
        # Simulate stability metric - operations remain bounded
        Z_stable = np.zeros_like(X)
        for i in range(n):
            for j in range(n):
                # Division operation stability
                if abs(Y[i,j]) < 0.1:  # Near zero denominator
                    Z_stable[i,j] = 1.0  # Maps to I, stable
                else:
                    Z_stable[i,j] = np.tanh(X[i,j] / (Y[i,j] + 0.01))
        
        Z_stable = np.abs(Z_stable)  # Stability measure
        
        im1 = ax1.imshow(Z_stable, cmap='viridis', origin='lower',
                        extent=[-10, 10, -10, 10], vmin=0, vmax=2,
                        interpolation='bilinear')
        
        setup_neon_style(ax1, 
                        title='System with I ≠ 0\n(STABLE)',
                        xlabel='Operation Parameter a', 
                        ylabel='Operation Parameter b')
        
        # Add colorbar
        cbar1 = plt.colorbar(im1, ax=ax1)
        cbar1.set_label('Consistency Level', color=NEON_COLORS['white'], 
                       fontsize=10)
        cbar1.ax.yaxis.set_tick_params(color=NEON_COLORS['white'])
        plt.setp(plt.getp(cbar1.ax.axes, 'yticklabels'), 
                color=NEON_COLORS['white'])
        
        # Add text annotation
        ax1.text(0, 8, 'All operations\nremain bounded', 
                ha='center', va='center', fontsize=12,
                color=NEON_COLORS['lime'], fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                         edgecolor=NEON_COLORS['lime'], linewidth=2))
        
        # Side B: System with I = 0 (Collapsed)
        # Simulate collapse - operations diverge
        Z_collapsed = np.zeros_like(X)
        for i in range(n):
            for j in range(n):
                if abs(Y[i,j]) < 0.1:  # Division by zero
                    Z_collapsed[i,j] = 100.0  # Diverges to infinity
                else:
                    result = X[i,j] / (Y[i,j])
                    Z_collapsed[i,j] = min(abs(result), 100)
        
        # Enhance instability near singularities
        Z_collapsed = np.log1p(Z_collapsed)
        
        im2 = ax2.imshow(Z_collapsed, cmap='hot', origin='lower',
                        extent=[-10, 10, -10, 10], vmin=0, vmax=5,
                        interpolation='bilinear')
        
        setup_neon_style(ax2, 
                        title='System with I = 0\n(COLLAPSED)',
                        xlabel='Operation Parameter a', 
                        ylabel='Operation Parameter b')
        
        # Add colorbar
        cbar2 = plt.colorbar(im2, ax=ax2)
        cbar2.set_label('Error/Infinity Level', color=NEON_COLORS['white'], 
                       fontsize=10)
        cbar2.ax.yaxis.set_tick_params(color=NEON_COLORS['white'])
        plt.setp(plt.getp(cbar2.ax.axes, 'yticklabels'), 
                color=NEON_COLORS['white'])
        
        # Add text annotation
        ax2.text(0, 8, 'UNDEFINED\nEVERYWHERE', 
                ha='center', va='center', fontsize=14,
                color=NEON_COLORS['red'], fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                         edgecolor=NEON_COLORS['red'], linewidth=3))
        
        # Main title
        fig.suptitle('Algebraic Stability: I ≠ 0 vs I = 0\n' + 
                    'Proof of Non-Trivialization',
                    color=NEON_COLORS['cyan'], fontsize=18, 
                    fontweight='bold', y=0.98)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR,
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, (ax1, ax2)


class EnhancedWheelVisualizer:
    """
    Graph 4: Enhanced Wheel of Fractions (Projective Wheel Geometry)
    
    Circular representation where:
    - 0 at "south" pole
    - ∞ at "north" pole  
    - I at the center (axis)
    All paths leading to indeterminate converge to wheel center.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (12, 12)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate enhanced wheel of fractions visualization."""
        fig, ax = plt.subplots(figsize=self.figsize, facecolor=BACKGROUND_COLOR)
        ax.set_xlim(-2.8, 2.8)
        ax.set_ylim(-2.8, 2.8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor(BACKGROUND_COLOR)
        
        # Draw main wheel rim
        rim = Circle((0, 0), 2.0, fill=False, edgecolor=NEON_COLORS['cyan'], 
                    linewidth=4)
        ax.add_patch(rim)
        
        # Draw inner glow
        for alpha, r in zip([0.3, 0.2, 0.1], [2.05, 2.1, 2.15]):
            glow = Circle((0, 0), r, fill=False, edgecolor=NEON_COLORS['cyan'],
                         linewidth=2, alpha=alpha)
            ax.add_patch(glow)
        
        # Center hub - I element with glow effect
        hub = Circle((0, 0), 0.25, color=NEON_COLORS['magenta'], 
                    edgecolor=NEON_COLORS['yellow'], linewidth=3, zorder=10)
        ax.add_patch(hub)
        
        # Add glow around I
        for alpha, r in zip([0.4, 0.3, 0.2, 0.1], [0.35, 0.45, 0.55, 0.65]):
            glow = Circle((0, 0), r, color=NEON_COLORS['magenta'], 
                         alpha=alpha, zorder=9)
            ax.add_patch(glow)
        
        ax.text(0, 0, 'I', ha='center', va='center', fontsize=24,
               color='white', fontweight='bold', zorder=11)
        
        # Mark poles
        # South pole: 0
        ax.plot(0, -2.0, 'o', color=NEON_COLORS['lime'], markersize=15,
               markeredgecolor=NEON_COLORS['yellow'], markeredgewidth=2)
        ax.text(0, -2.4, '0', ha='center', va='center', fontsize=18,
               color=NEON_COLORS['lime'], fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                        edgecolor=NEON_COLORS['lime'], linewidth=2))
        
        # North pole: ∞
        ax.plot(0, 2.0, 'o', color=NEON_COLORS['orange'], markersize=15,
               markeredgecolor=NEON_COLORS['yellow'], markeredgewidth=2)
        ax.text(0, 2.4, '∞', ha='center', va='center', fontsize=18,
               color=NEON_COLORS['orange'], fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                        edgecolor=NEON_COLORS['orange'], linewidth=2))
        
        # Draw radial spokes from rim to center
        n_spokes = 16
        angles = np.linspace(0, 2*np.pi, n_spokes, endpoint=False)
        
        for angle in angles:
            x_outer = 2.0 * np.cos(angle)
            y_outer = 2.0 * np.sin(angle)
            x_inner = 0.25 * np.cos(angle)
            y_inner = 0.25 * np.sin(angle)
            
            ax.plot([x_outer, x_inner], [y_outer, y_inner],
                   color=NEON_COLORS['cyan'], linewidth=1, 
                   alpha=0.3, linestyle='-')
        
        # Place fractions around the rim
        fractions = [
            (0, '1'), (np.pi/6, '1/2'), (np.pi/3, '1/3'),
            (np.pi/2, '1/∞'), (2*np.pi/3, '-1/3'), (5*np.pi/6, '-1/2'),
            (np.pi, '-1'), (7*np.pi/6, '-2'), (4*np.pi/3, '-3'),
            (3*np.pi/2, '-1/∞'), (5*np.pi/3, '3'), (11*np.pi/6, '2')
        ]
        
        for angle, frac in fractions:
            x = 2.0 * np.cos(angle)
            y = 2.0 * np.sin(angle)
            
            # Point on rim
            ax.plot(x, y, 'o', color=NEON_COLORS['yellow'], 
                   markersize=8, zorder=5)
            
            # Label
            label_x = 2.35 * np.cos(angle)
            label_y = 2.35 * np.sin(angle)
            ax.text(label_x, label_y, frac, ha='center', va='center',
                   fontsize=10, color=NEON_COLORS['white'],
                   bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                            edgecolor=NEON_COLORS['yellow'], linewidth=1,
                            alpha=0.8))
        
        # Draw special paths for singularities converging to I
        singular_angles = [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]
        singular_labels = ['1/0', '-1/0', '2/0', '-2/0']
        
        for angle, label in zip(singular_angles, singular_labels):
            # Singularity point outside wheel
            sx = 2.6 * np.cos(angle)
            sy = 2.6 * np.sin(angle)
            
            # Curved path to center
            t = np.linspace(0, 1, 50)
            x_path = sx * (1 - t)**2 + 2.0 * np.cos(angle) * 2 * t * (1 - t)
            y_path = sy * (1 - t)**2 + 2.0 * np.sin(angle) * 2 * t * (1 - t)
            
            ax.plot(x_path, y_path, color=NEON_COLORS['magenta'], 
                   linewidth=2.5, alpha=0.7, linestyle='--')
            
            # Arrow at end
            ax.annotate('', xy=(0.25*np.cos(angle), 0.25*np.sin(angle)),
                       xytext=(x_path[-10], y_path[-10]),
                       arrowprops=dict(arrowstyle='->', 
                                     color=NEON_COLORS['magenta'],
                                     lw=2.5, alpha=0.7))
            
            # Label
            ax.text(sx, sy, label, ha='center', va='center',
                   fontsize=12, color=NEON_COLORS['magenta'],
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                            edgecolor=NEON_COLORS['magenta'], 
                            linewidth=2, alpha=0.9))
        
        # Title
        ax.text(0, -3.2, 'Wheel of Fractions (Projective Geometry)', 
               ha='center', fontsize=18, color=NEON_COLORS['cyan'],
               fontweight='bold')
        ax.text(0, -3.5, 'All indeterminate forms converge to central I',
               ha='center', fontsize=12, color=NEON_COLORS['white'],
               style='italic')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR,
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, ax


class GalacticRotationCurveVisualizer:
    """
    Graph 5: Galactic Rotation Curve with AEI Correction
    
    Shows three curves:
    - Dotted: Newtonian prediction (fails)
    - Solid: Observed data (what we see)
    - Gold: AEI theory with Λ ⊗ J⊗⁴ correction (perfect fit)
    """
    
    def __init__(self, figsize: Tuple[int, int] = (14, 8)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate galactic rotation curve with AEI correction."""
        fig, ax = plt.subplots(figsize=self.figsize, facecolor=BACKGROUND_COLOR)
        
        # Radial distance (kpc)
        r = np.linspace(0.5, 30, 200)
        
        # Newtonian prediction: v ~ 1/sqrt(r) after visible matter
        M_bulge = 10  # Normalized mass
        r_bulge = 2.0
        v_newtonian = np.sqrt(M_bulge / (r + r_bulge))
        v_newtonian = v_newtonian / v_newtonian[10] * 220  # Normalize
        
        # Observed curve (flat rotation)
        v_observed = 220 * np.ones_like(r)
        v_observed[:5] = 220 * np.sqrt(r[:5] / r[5])  # Rising in center
        
        # Add realistic scatter to observations
        np.random.seed(42)
        scatter = np.random.normal(0, 10, len(r))
        v_observed_scatter = v_observed + scatter
        
        # AEI correction with J field
        # v²_AEI = v²_Newton + Λ⊗J⊗⁴ correction
        Lambda = 0.7  # Dark energy component
        J_field = 1.2  # J field coupling
        
        correction = Lambda * (J_field**4) * r / (1 + (r/10)**2)
        v_aei = np.sqrt(v_newtonian**2 + correction * 5000)
        
        # Plot curves
        ax.plot(r, v_newtonian, color=NEON_COLORS['white'], 
               linewidth=2.5, linestyle=':', label='Newtonian Gravity',
               alpha=0.7)
        
        ax.scatter(r[::5], v_observed_scatter[::5], 
                  color=NEON_COLORS['cyan'], s=50, alpha=0.6,
                  marker='o', edgecolors=NEON_COLORS['white'],
                  linewidths=0.5, label='Observed Data', zorder=5)
        
        ax.plot(r, v_aei, color=NEON_COLORS['yellow'], 
               linewidth=4, label=r'AEI Theory: $\Lambda \otimes J^{\otimes 4}$',
               zorder=10)
        
        # Add glow to AEI curve
        for alpha, lw in zip([0.3, 0.2, 0.1], [6, 8, 10]):
            ax.plot(r, v_aei, color=NEON_COLORS['yellow'], 
                   linewidth=lw, alpha=alpha, zorder=9)
        
        setup_neon_style(ax,
                        title='Galactic Rotation Curve: AEI vs Classical Prediction',
                        xlabel='Radius (kpc)', 
                        ylabel='Rotation Velocity (km/s)')
        
        ax.legend(loc='lower right', fontsize=12, facecolor=BACKGROUND_COLOR,
                 edgecolor=NEON_COLORS['cyan'], labelcolor=NEON_COLORS['white'])
        
        # Add annotations
        ax.annotate('Classical prediction fails\nat large radius',
                   xy=(20, v_newtonian[-40]), xytext=(15, 100),
                   arrowprops=dict(arrowstyle='->', 
                                 color=NEON_COLORS['white'],
                                 lw=2, alpha=0.7),
                   fontsize=11, color=NEON_COLORS['white'],
                   bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                            edgecolor=NEON_COLORS['white'], alpha=0.8))
        
        ax.annotate('AEI perfect fit\n(no dark matter needed)',
                   xy=(25, v_aei[-20]), xytext=(22, 270),
                   arrowprops=dict(arrowstyle='->', 
                                 color=NEON_COLORS['yellow'],
                                 lw=3, alpha=0.9),
                   fontsize=12, color=NEON_COLORS['yellow'],
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                            edgecolor=NEON_COLORS['yellow'], 
                            linewidth=2, alpha=0.9))
        
        ax.set_ylim(0, 300)
        ax.set_xlim(0, 30)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR,
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, ax


class SchwarzschildModifiedVisualizer:
    """
    Graph 6: Modified Schwarzschild Spacetime with I
    
    Penrose diagram or spacetime curvature mesh.
    Classical: Mesh "tears" at singularity
    AEI: Mesh converges to dense neon core where curvature is finite (value I)
    """
    
    def __init__(self, figsize: Tuple[int, int] = (14, 10)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate modified Schwarzschild spacetime visualization."""
        fig = plt.figure(figsize=self.figsize, facecolor=BACKGROUND_COLOR)
        
        # Create 3D spacetime mesh
        ax = fig.add_subplot(111, projection='3d', facecolor=BACKGROUND_COLOR)
        
        # Create radial and angular grid
        r = np.linspace(0.1, 5, 80)
        theta = np.linspace(0, 2*np.pi, 80)
        R, THETA = np.meshgrid(r, theta)
        
        # Convert to Cartesian
        X = R * np.cos(THETA)
        Y = R * np.sin(THETA)
        
        # Classical Schwarzschild: diverges at r=0
        r_s = 1.0  # Schwarzschild radius
        
        # Modified metric with I regularization
        # Z represents spacetime curvature
        Z = np.zeros_like(R)
        for i in range(len(theta)):
            for j in range(len(r)):
                r_val = R[i, j]
                if r_val < r_s * 1.5:
                    # Inside/near horizon: smooth convergence to I
                    Z[i, j] = -2.0 * np.exp(-(r_val - 0.1)**2 / 0.5)
                else:
                    # Outside: normal curvature
                    Z[i, j] = -r_s / r_val
        
        # Plot surface
        surf = ax.plot_surface(X, Y, Z, cmap='twilight', 
                              alpha=0.7, linewidth=0.5,
                              edgecolor=NEON_COLORS['cyan'],
                              antialiased=True)
        
        # Add central I core (finite curvature)
        theta_core = np.linspace(0, 2*np.pi, 30)
        z_core = np.linspace(-2.0, -1.5, 10)
        THETA_core, Z_core = np.meshgrid(theta_core, z_core)
        
        r_core = 0.15
        X_core = r_core * np.cos(THETA_core)
        Y_core = r_core * np.sin(THETA_core)
        
        ax.plot_surface(X_core, Y_core, Z_core, 
                       color=NEON_COLORS['magenta'], 
                       alpha=0.9, edgecolor=NEON_COLORS['yellow'],
                       linewidth=2)
        
        # Add glow around core
        for alpha, r_g in zip([0.3, 0.2, 0.1], [0.25, 0.35, 0.45]):
            X_glow = r_g * np.cos(THETA_core)
            Y_glow = r_g * np.sin(THETA_core)
            ax.plot_surface(X_glow, Y_glow, Z_core, 
                           color=NEON_COLORS['magenta'], 
                           alpha=alpha, linewidth=0)
        
        # Mark event horizon
        theta_horizon = np.linspace(0, 2*np.pi, 100)
        x_horizon = r_s * np.cos(theta_horizon)
        y_horizon = r_s * np.sin(theta_horizon)
        z_horizon = -r_s / r_s * np.ones_like(theta_horizon)
        
        ax.plot(x_horizon, y_horizon, z_horizon, 
               color=NEON_COLORS['yellow'], linewidth=3, 
               linestyle='--', label='Event Horizon')
        
        # Styling
        ax.set_facecolor(BACKGROUND_COLOR)
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor(NEON_COLORS['white'])
        ax.yaxis.pane.set_edgecolor(NEON_COLORS['white'])
        ax.zaxis.pane.set_edgecolor(NEON_COLORS['white'])
        ax.xaxis.line.set_color(NEON_COLORS['white'])
        ax.yaxis.line.set_color(NEON_COLORS['white'])
        ax.zaxis.line.set_color(NEON_COLORS['white'])
        ax.tick_params(colors=NEON_COLORS['white'])
        
        ax.set_xlabel('X (Schwarzschild)', color=NEON_COLORS['white'], 
                     fontsize=11, labelpad=10)
        ax.set_ylabel('Y (Schwarzschild)', color=NEON_COLORS['white'], 
                     fontsize=11, labelpad=10)
        ax.set_zlabel('Curvature', color=NEON_COLORS['white'], 
                     fontsize=11, labelpad=10)
        
        ax.set_title('Modified Schwarzschild Spacetime with I\n' +
                    'Finite Curvature at Singularity',
                    color=NEON_COLORS['cyan'], fontsize=16, 
                    fontweight='bold', pad=20)
        
        # Add text annotations
        ax.text2D(0.15, 0.85, 'I-Core\n(Finite Curvature)', 
                 transform=ax.transAxes, color=NEON_COLORS['magenta'],
                 fontsize=12, fontweight='bold',
                 bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                          edgecolor=NEON_COLORS['magenta'], 
                          linewidth=2, alpha=0.9))
        
        ax.text2D(0.15, 0.72, 'No Singularity\nNo Infinite Density', 
                 transform=ax.transAxes, color=NEON_COLORS['lime'],
                 fontsize=11, style='italic',
                 bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                          edgecolor=NEON_COLORS['lime'], alpha=0.8))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR,
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, ax


class EntropyAccelerationVisualizer:
    """
    Graph 7: Entropy C_EA (Entropy Acceleration)
    
    Logarithmic plot showing relationship between entropy increase
    and universe expansion acceleration. Acceleration curve follows
    "indetermination production" in quantum vacuum.
    """
    
    def __init__(self, figsize: Tuple[int, int] = (14, 8)):
        self.figsize = figsize
    
    def plot(self, save_path: Optional[str] = None):
        """Generate entropy acceleration graph."""
        fig, ax = plt.subplots(figsize=self.figsize, facecolor=BACKGROUND_COLOR)
        
        # Time evolution (Gyr)
        t = np.linspace(0.1, 14, 200)  # Big Bang to present
        
        # Entropy production (increasing)
        # S ~ t^α with acceleration
        alpha = 1.2
        S = t**alpha
        
        # Cosmic Entropy Acceleration (CEA)
        # C_EA = dS/dt = acceleration factor
        C_EA = alpha * t**(alpha - 1)
        
        # Hubble parameter evolution (correlated with entropy)
        # H(t) ~ 1/t + C_EA correction
        H_classical = 70 / t  # Classical deceleration
        H_aei = H_classical + C_EA * 2  # AEI with entropy acceleration
        
        # Create twin axes
        ax2 = ax.twinx()
        
        # Plot entropy
        line1 = ax.plot(t, S, color=NEON_COLORS['cyan'], 
                       linewidth=3, label='Entropy S(t)')
        
        # Add glow
        for alpha_val, lw in zip([0.3, 0.2, 0.1], [5, 7, 9]):
            ax.plot(t, S, color=NEON_COLORS['cyan'], 
                   linewidth=lw, alpha=alpha_val)
        
        # Plot acceleration on second axis
        line2 = ax2.plot(t, C_EA, color=NEON_COLORS['magenta'], 
                        linewidth=3, linestyle='--',
                        label=r'Acceleration $C_{EA}$')
        
        # Add glow
        for alpha_val, lw in zip([0.3, 0.2, 0.1], [5, 7, 9]):
            ax2.plot(t, C_EA, color=NEON_COLORS['magenta'], 
                    linewidth=lw, alpha=alpha_val)
        
        # Plot Hubble expansion
        line3 = ax2.plot(t, H_aei / 10, color=NEON_COLORS['yellow'], 
                        linewidth=2.5, label='Expansion Rate H(t)')
        
        # Styling for primary axis
        ax.set_facecolor(BACKGROUND_COLOR)
        ax.set_xlabel('Cosmic Time (Gyr)', color=NEON_COLORS['white'], 
                     fontsize=13)
        ax.set_ylabel('Entropy S (arbitrary units)', 
                     color=NEON_COLORS['cyan'], fontsize=13)
        ax.tick_params(axis='y', colors=NEON_COLORS['cyan'])
        ax.tick_params(axis='x', colors=NEON_COLORS['white'])
        
        # Styling for secondary axis
        ax2.set_ylabel(r'Acceleration $C_{EA}$ and H(t)/10', 
                      color=NEON_COLORS['magenta'], fontsize=13)
        ax2.tick_params(axis='y', colors=NEON_COLORS['magenta'])
        
        # Spines
        for spine in ax.spines.values():
            spine.set_color(NEON_COLORS['white'])
        for spine in ax2.spines.values():
            spine.set_color(NEON_COLORS['white'])
        
        # Grid
        ax.grid(True, alpha=0.2, color=NEON_COLORS['cyan'], linestyle='--')
        
        # Title
        ax.set_title('Cosmic Entropy Acceleration $C_{EA}$\n' +
                    'Entropy-Driven Expansion of the Universe',
                    color=NEON_COLORS['cyan'], fontsize=16, 
                    fontweight='bold', pad=20)
        
        # Combined legend
        lines = line1 + line2 + line3
        labels = [l.get_label() for l in lines]
        ax.legend(lines, labels, loc='upper left', fontsize=11,
                 facecolor=BACKGROUND_COLOR, edgecolor=NEON_COLORS['cyan'],
                 labelcolor=NEON_COLORS['white'])
        
        # Add annotations
        ax.annotate('Present Day\n(t ≈ 13.8 Gyr)',
                   xy=(13.8, S[-10]), xytext=(10, S[-50]),
                   arrowprops=dict(arrowstyle='->', 
                                 color=NEON_COLORS['lime'],
                                 lw=2),
                   fontsize=11, color=NEON_COLORS['lime'],
                   bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                            edgecolor=NEON_COLORS['lime'], alpha=0.8))
        
        ax2.annotate('Acceleration increases\nwith entropy production',
                    xy=(7, C_EA[100]), xytext=(4, C_EA[50] + 2),
                    arrowprops=dict(arrowstyle='->', 
                                  color=NEON_COLORS['magenta'],
                                  lw=2),
                    fontsize=11, color=NEON_COLORS['magenta'],
                    bbox=dict(boxstyle='round', facecolor=BACKGROUND_COLOR,
                             edgecolor=NEON_COLORS['magenta'], alpha=0.8))
        
        # Logarithmic scale for better visibility
        ax.set_yscale('log')
        ax2.set_yscale('log')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, facecolor=BACKGROUND_COLOR,
                       bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        else:
            plt.show()
        
        return fig, (ax, ax2)


def generate_all_book_visualizations(output_dir: str = './book_visualizations'):
    """
    Generate all 7 main visualizations for the book with neon style.
    
    Creates publication-quality figures suitable for a 350-page book with
    neon color scheme (cyan, magenta, lime green on deep black background).
    
    Args:
        output_dir: Directory to save all visualizations
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 80)
    print("Generating Advanced Book Visualizations".center(80))
    print("The Algebra of the Indeterminate I".center(80))
    print("=" * 80)
    print()
    
    visualizations = [
        ("1. Healed Singularity (sin(x)/x)", 
         HealedSingularityVisualizer, 
         "01_healed_singularity.png"),
        ("2. Phase Transition (Mexican Hat)", 
         PhaseTransitionVisualizer, 
         "02_phase_transition_diagram.png"),
        ("3. Stability Heat Map", 
         StabilityHeatMapVisualizer, 
         "03_stability_heatmap.png"),
        ("4. Enhanced Wheel of Fractions", 
         EnhancedWheelVisualizer, 
         "04_enhanced_wheel.png"),
        ("5. Galactic Rotation Curve", 
         GalacticRotationCurveVisualizer, 
         "05_galactic_rotation.png"),
        ("6. Modified Schwarzschild Spacetime", 
         SchwarzschildModifiedVisualizer, 
         "06_schwarzschild_modified.png"),
        ("7. Entropy Acceleration C_EA", 
         EntropyAccelerationVisualizer, 
         "07_entropy_acceleration.png"),
    ]
    
    for name, visualizer_class, filename in visualizations:
        print(f"\n{name}")
        print("-" * 80)
        viz = visualizer_class()
        viz.plot(save_path=f"{output_dir}/{filename}")
    
    print()
    print("=" * 80)
    print(f"All visualizations saved to: {output_dir}/".center(80))
    print("Ready for book publication!".center(80))
    print("=" * 80)
    
    # Generate index file
    index_path = f"{output_dir}/INDEX.md"
    with open(index_path, 'w') as f:
        f.write("# Book Visualizations Index\n\n")
        f.write("## The Algebra of the Indeterminate I\n\n")
        f.write("### Visual Style\n")
        f.write("- **Background**: Deep Black (#0a0a0a)\n")
        f.write("- **Primary Colors**: Neon Cyan, Magenta, Lime Green\n")
        f.write("- **Resolution**: 300 DPI (publication quality)\n\n")
        f.write("### Generated Figures\n\n")
        for i, (name, _, filename) in enumerate(visualizations, 1):
            f.write(f"{i}. **{name}**\n")
            f.write(f"   - File: `{filename}`\n")
            f.write(f"   - ![{name}]({filename})\n\n")
    
    print(f"\n✓ Index file created: {index_path}")


if __name__ == "__main__":
    import sys
    
    # Default output directory
    output_dir = './book_visualizations'
    
    # Allow command line argument for output directory
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    
    print("\nAdvanced Visualization Generator")
    print("The Algebra of the Indeterminate I")
    print()
    
    generate_all_book_visualizations(output_dir)
