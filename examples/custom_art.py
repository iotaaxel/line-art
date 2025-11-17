#!/usr/bin/env python3
"""
Custom art examples - Create your own patterns!
"""

from main import create_canvas, draw_line, display_canvas

def heart_shape():
    """Create a heart shape"""
    print("=" * 60)
    print("❤️  Heart Shape")
    print("=" * 60)
    canvas = create_canvas(30, 20)
    
    # Heart shape using lines
    import math
    center_x, center_y = 15, 10
    
    # Left curve
    points = []
    for i in range(0, 180, 5):
        angle = math.radians(i)
        x = int(center_x - 8 + 8 * math.cos(angle))
        y = int(center_y - 5 + 5 * math.sin(angle))
        points.append((x, y))
    
    # Right curve
    for i in range(0, 180, 5):
        angle = math.radians(i)
        x = int(center_x + 8 - 8 * math.cos(angle))
        y = int(center_y - 5 + 5 * math.sin(angle))
        points.append((x, y))
    
    # Connect points
    for i in range(len(points) - 1):
        draw_line(canvas, points[i][0], points[i][1], points[i+1][0], points[i+1][1], '*')
    
    # Bottom point
    draw_line(canvas, points[0][0], points[0][1], center_x, center_y + 8, '*')
    draw_line(canvas, points[-1][0], points[-1][1], center_x, center_y + 8, '*')
    
    display_canvas(canvas)
    print()

def house_shape():
    """Create a simple house"""
    print("=" * 60)
    print("🏠 House Shape")
    print("=" * 60)
    canvas = create_canvas(25, 20)
    
    # House base
    draw_line(canvas, 8, 15, 17, 15, '*')  # Bottom
    draw_line(canvas, 8, 15, 8, 10, '*')   # Left wall
    draw_line(canvas, 17, 15, 17, 10, '*') # Right wall
    draw_line(canvas, 8, 10, 17, 10, '*')  # Top
    
    # Roof
    draw_line(canvas, 8, 10, 12, 5, '*')   # Left roof
    draw_line(canvas, 17, 10, 12, 5, '*')  # Right roof
    
    # Door
    draw_line(canvas, 11, 15, 11, 12, '*') # Left door
    draw_line(canvas, 14, 15, 14, 12, '*') # Right door
    draw_line(canvas, 11, 12, 14, 12, '*') # Top door
    
    display_canvas(canvas)
    print()

def tree_shape():
    """Create a tree"""
    print("=" * 60)
    print("🌲 Tree Shape")
    print("=" * 60)
    canvas = create_canvas(20, 25)
    
    # Trunk
    draw_line(canvas, 9, 20, 9, 24, '*')
    draw_line(canvas, 10, 20, 10, 24, '*')
    
    # Branches/leaves (triangular)
    draw_line(canvas, 5, 15, 10, 8, '*')
    draw_line(canvas, 15, 15, 10, 8, '*')
    draw_line(canvas, 5, 15, 15, 15, '*')
    
    # More branches
    draw_line(canvas, 7, 12, 10, 5, '*')
    draw_line(canvas, 13, 12, 10, 5, '*')
    draw_line(canvas, 7, 12, 13, 12, '*')
    
    display_canvas(canvas)
    print()

def arrow_pattern():
    """Create arrow patterns"""
    print("=" * 60)
    print("➡️  Arrow Pattern")
    print("=" * 60)
    canvas = create_canvas(40, 15)
    
    # Multiple arrows pointing different directions
    # Right arrow
    draw_line(canvas, 5, 5, 15, 5, '*')
    draw_line(canvas, 15, 5, 12, 2, '*')
    draw_line(canvas, 15, 5, 12, 8, '*')
    
    # Left arrow
    draw_line(canvas, 25, 10, 15, 10, '*')
    draw_line(canvas, 15, 10, 18, 7, '*')
    draw_line(canvas, 15, 10, 18, 13, '*')
    
    # Up arrow
    draw_line(canvas, 20, 12, 20, 2, '*')
    draw_line(canvas, 20, 2, 17, 5, '*')
    draw_line(canvas, 20, 2, 23, 5, '*')
    
    # Down arrow
    draw_line(canvas, 30, 2, 30, 12, '*')
    draw_line(canvas, 30, 12, 27, 9, '*')
    draw_line(canvas, 30, 12, 33, 9, '*')
    
    display_canvas(canvas)
    print()

def diamond_pattern():
    """Create diamond patterns"""
    print("=" * 60)
    print("💎 Diamond Pattern")
    print("=" * 60)
    canvas = create_canvas(30, 30)
    center_x, center_y = 15, 15
    
    # Multiple nested diamonds
    sizes = [12, 8, 4]
    for size in sizes:
        draw_line(canvas, center_x, center_y - size, center_x + size, center_y, '*')
        draw_line(canvas, center_x + size, center_y, center_x, center_y + size, '*')
        draw_line(canvas, center_x, center_y + size, center_x - size, center_y, '*')
        draw_line(canvas, center_x - size, center_y, center_x, center_y - size, '*')
    
    display_canvas(canvas)
    print()

def flower_pattern():
    """Create a flower pattern"""
    print("=" * 60)
    print("🌸 Flower Pattern")
    print("=" * 60)
    canvas = create_canvas(35, 35)
    center_x, center_y = 17, 17
    
    import math
    # Petals
    for i in range(8):
        angle = i * math.pi / 4
        # Outer petal
        x1 = int(center_x + 12 * math.cos(angle))
        y1 = int(center_y + 12 * math.sin(angle))
        # Inner petal
        x2 = int(center_x + 6 * math.cos(angle))
        y2 = int(center_y + 6 * math.sin(angle))
        draw_line(canvas, center_x, center_y, x1, y1, '*')
        draw_line(canvas, x1, y1, x2, y2, '*')
    
    # Center circle
    for i in range(16):
        angle1 = i * 2 * math.pi / 16
        angle2 = (i + 1) * 2 * math.pi / 16
        x1 = int(center_x + 3 * math.cos(angle1))
        y1 = int(center_y + 3 * math.sin(angle1))
        x2 = int(center_x + 3 * math.cos(angle2))
        y2 = int(center_y + 3 * math.sin(angle2))
        draw_line(canvas, x1, y1, x2, y2, '*')
    
    display_canvas(canvas)
    print()

def main():
    """Display all custom art examples"""
    print("\n" + "=" * 60)
    print("🎨 Custom Art Examples")
    print("=" * 60 + "\n")
    
    heart_shape()
    house_shape()
    tree_shape()
    arrow_pattern()
    diamond_pattern()
    flower_pattern()
    
    print("=" * 60)
    print("✨ More custom art examples!")
    print("=" * 60)

if __name__ == "__main__":
    main()

