#!/usr/bin/env python3
"""
Example script demonstrating Line-Art usage programmatically
"""

from main import create_canvas, draw_line, display_canvas

def example():
    # Create a canvas (no borders)
    canvas = create_canvas(25, 15)
    
    # Draw some example lines
    print("Example 1: Simple diagonal line")
    draw_line(canvas, 1, 1, 10, 5)
    display_canvas(canvas)
    print("\n" + "="*50 + "\n")
    
    # Create a new canvas for more examples
    canvas = create_canvas(25, 15)
    
    print("Example 2: Multiple lines (unlimited lines supported)")
    draw_line(canvas, 2, 2, 8, 12, '*')
    draw_line(canvas, 15, 1, 20, 10, '*')
    draw_line(canvas, 1, 10, 12, 2, '*')
    draw_line(canvas, 10, 1, 18, 8, '*')
    draw_line(canvas, 5, 5, 20, 3, '*')
    display_canvas(canvas)
    print("\n" + "="*50 + "\n")
    
    # Create a canvas matching the image pattern
    canvas = create_canvas(20, 15)
    
    print("Example 3: Pattern similar to the image")
    # Top-left diagonal
    draw_line(canvas, 1, 1, 4, 4, '*')
    # Middle-left horizontal
    draw_line(canvas, 1, 7, 6, 7, '*')
    # Bottom-left diagonal (upward)
    draw_line(canvas, 1, 13, 6, 8, '*')
    # Right-side vertical
    draw_line(canvas, 18, 1, 18, 14, '*')
    display_canvas(canvas)

if __name__ == "__main__":
    example()

