#!/usr/bin/env python3
"""
Generate Book Visualizations

Standalone script to generate all 7 main visualizations for the book
"The Algebra of the Indeterminate I" with neon aesthetic.

Usage:
    python generate_book_visualizations.py [output_directory]

Default output directory: ./book_visualizations
"""

import sys
import os

# Add src to path to enable imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'python'))

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server/batch generation

from ialgebra.advanced_visualizations import generate_all_book_visualizations


def main():
    """Main entry point for visualization generation."""
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    else:
        output_dir = './book_visualizations'
    
    print(f"\nOutput directory: {output_dir}\n")
    
    # Generate all visualizations
    try:
        generate_all_book_visualizations(output_dir)
        print("\n✓ Success! All visualizations generated.")
        print(f"\nView the results:")
        print(f"  - Images: {output_dir}/*.png")
        print(f"  - Index: {output_dir}/INDEX.md")
        print(f"  - Documentation: {output_dir}/README.md")
        return 0
        
    except Exception as e:
        print(f"\n✗ Error generating visualizations: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
