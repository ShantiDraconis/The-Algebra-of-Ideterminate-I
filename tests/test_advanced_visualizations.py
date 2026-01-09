"""
Tests for Advanced Book Visualizations

Ensures all visualizer classes can be instantiated and generate outputs
without errors.
"""

import unittest
import tempfile
import os
import sys

# Ensure matplotlib uses non-interactive backend
import matplotlib
matplotlib.use('Agg')

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'python'))

from ialgebra.advanced_visualizations import (
    HealedSingularityVisualizer,
    PhaseTransitionVisualizer,
    StabilityHeatMapVisualizer,
    EnhancedWheelVisualizer,
    GalacticRotationCurveVisualizer,
    SchwarzschildModifiedVisualizer,
    EntropyAccelerationVisualizer,
    generate_all_book_visualizations
)


class TestVisualizerInstantiation(unittest.TestCase):
    """Test that all visualizer classes can be instantiated."""
    
    def test_healed_singularity_instantiation(self):
        """Test HealedSingularityVisualizer instantiation."""
        viz = HealedSingularityVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (12, 8))
    
    def test_phase_transition_instantiation(self):
        """Test PhaseTransitionVisualizer instantiation."""
        viz = PhaseTransitionVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (14, 10))
    
    def test_stability_heatmap_instantiation(self):
        """Test StabilityHeatMapVisualizer instantiation."""
        viz = StabilityHeatMapVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (16, 7))
    
    def test_enhanced_wheel_instantiation(self):
        """Test EnhancedWheelVisualizer instantiation."""
        viz = EnhancedWheelVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (12, 12))
    
    def test_galactic_rotation_instantiation(self):
        """Test GalacticRotationCurveVisualizer instantiation."""
        viz = GalacticRotationCurveVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (14, 8))
    
    def test_schwarzschild_instantiation(self):
        """Test SchwarzschildModifiedVisualizer instantiation."""
        viz = SchwarzschildModifiedVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (14, 10))
    
    def test_entropy_acceleration_instantiation(self):
        """Test EntropyAccelerationVisualizer instantiation."""
        viz = EntropyAccelerationVisualizer()
        self.assertIsNotNone(viz)
        self.assertEqual(viz.figsize, (14, 8))


class TestVisualizerGeneration(unittest.TestCase):
    """Test that visualizers can generate output without errors."""
    
    def setUp(self):
        """Create temporary directory for test outputs."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary directory."""
        import shutil
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_healed_singularity_generation(self):
        """Test generating healed singularity graph."""
        viz = HealedSingularityVisualizer(figsize=(8, 6))
        output_path = os.path.join(self.test_dir, 'test_singularity.png')
        
        fig, ax = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)  # Non-empty file
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
    
    def test_phase_transition_generation(self):
        """Test generating phase transition diagram."""
        viz = PhaseTransitionVisualizer(figsize=(10, 8))
        output_path = os.path.join(self.test_dir, 'test_phase.png')
        
        fig, ax = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
    
    def test_stability_heatmap_generation(self):
        """Test generating stability heat map."""
        viz = StabilityHeatMapVisualizer(figsize=(12, 6))
        output_path = os.path.join(self.test_dir, 'test_stability.png')
        
        fig, axes = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)
        self.assertIsNotNone(fig)
        self.assertEqual(len(axes), 2)  # Two subplots
    
    def test_enhanced_wheel_generation(self):
        """Test generating enhanced wheel diagram."""
        viz = EnhancedWheelVisualizer(figsize=(10, 10))
        output_path = os.path.join(self.test_dir, 'test_wheel.png')
        
        fig, ax = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
    
    def test_galactic_rotation_generation(self):
        """Test generating galactic rotation curve."""
        viz = GalacticRotationCurveVisualizer(figsize=(10, 6))
        output_path = os.path.join(self.test_dir, 'test_galactic.png')
        
        fig, ax = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
    
    def test_schwarzschild_generation(self):
        """Test generating modified Schwarzschild spacetime."""
        viz = SchwarzschildModifiedVisualizer(figsize=(10, 8))
        output_path = os.path.join(self.test_dir, 'test_schwarzschild.png')
        
        fig, ax = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
    
    def test_entropy_acceleration_generation(self):
        """Test generating entropy acceleration graph."""
        viz = EntropyAccelerationVisualizer(figsize=(10, 6))
        output_path = os.path.join(self.test_dir, 'test_entropy.png')
        
        fig, axes = viz.plot(save_path=output_path)
        
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 1000)
        self.assertIsNotNone(fig)
        self.assertEqual(len(axes), 2)  # Main and twin axes


class TestBatchGeneration(unittest.TestCase):
    """Test batch generation of all visualizations."""
    
    def setUp(self):
        """Create temporary directory for test outputs."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary directory."""
        import shutil
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_generate_all_visualizations(self):
        """Test generating all visualizations at once."""
        generate_all_book_visualizations(self.test_dir)
        
        # Check that all expected files were created
        expected_files = [
            '01_healed_singularity.png',
            '02_phase_transition_diagram.png',
            '03_stability_heatmap.png',
            '04_enhanced_wheel.png',
            '05_galactic_rotation.png',
            '06_schwarzschild_modified.png',
            '07_entropy_acceleration.png',
            'INDEX.md'
        ]
        
        for filename in expected_files:
            filepath = os.path.join(self.test_dir, filename)
            self.assertTrue(os.path.exists(filepath), 
                          f"Expected file not found: {filename}")
            
            # Check that image files are non-empty
            if filename.endswith('.png'):
                self.assertGreater(os.path.getsize(filepath), 1000,
                                 f"File too small: {filename}")


class TestColorScheme(unittest.TestCase):
    """Test that color scheme is properly defined."""
    
    def test_neon_colors_defined(self):
        """Test that NEON_COLORS dictionary exists and is complete."""
        from ialgebra.advanced_visualizations import NEON_COLORS
        
        expected_colors = [
            'cyan', 'magenta', 'lime', 'yellow', 
            'orange', 'pink', 'blue', 'white', 'red'
        ]
        
        for color in expected_colors:
            self.assertIn(color, NEON_COLORS, 
                         f"Missing color in palette: {color}")
            self.assertTrue(NEON_COLORS[color].startswith('#'),
                          f"Color not in hex format: {color}")
    
    def test_background_color_defined(self):
        """Test that BACKGROUND_COLOR is defined."""
        from ialgebra.advanced_visualizations import BACKGROUND_COLOR
        
        self.assertTrue(BACKGROUND_COLOR.startswith('#'))
        self.assertEqual(len(BACKGROUND_COLOR), 7)  # #RRGGBB format


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
