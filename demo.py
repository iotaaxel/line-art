#!/usr/bin/env python3
"""
Quick demo script - generates a sample art piece
"""

from main import create_canvas, draw_line, display_canvas

def demo():
    print("\n" + "=" * 60)
    print("🎨 Line-Art Demo - Abstract Composition")
    print("=" * 60 + "\n")
    
    canvas = create_canvas(50, 30)
    
    # Create an interesting abstract composition
    # Using multiple lines in one go
    lines = [
        # Outer frame
        (5, 5, 45, 5),
        (45, 5, 45, 25),
        (45, 25, 5, 25),
        (5, 25, 5, 5),
        # Diagonal cross
        (5, 5, 45, 25),
        (5, 25, 45, 5),
        # Inner shapes
        (15, 10, 35, 10),
        (35, 10, 35, 20),
        (35, 20, 15, 20),
        (15, 20, 15, 10),
        # Radial lines from center
        (25, 15, 10, 8),
        (25, 15, 40, 8),
        (25, 15, 40, 22),
        (25, 15, 10, 22),
        # Additional patterns
        (10, 12, 40, 18),
        (10, 18, 40, 12),
    ]
    
    for x1, y1, x2, y2 in lines:
        draw_line(canvas, x1, y1, x2, y2, '*')
    
    display_canvas(canvas)
    
    print("\n" + "=" * 60)
    print("✨ This art was created with Line-Art!")
    print("Run 'python main.py' to create your own!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    demo()

