#!/usr/bin/env python3
"""
Gallery of Line-Art examples
Generate beautiful ASCII art patterns
"""

from main import create_canvas, draw_line, display_canvas

def star_pattern():
    """Create a star pattern"""
    print("=" * 60)
    print("⭐ Star Pattern")
    print("=" * 60)
    canvas = create_canvas(30, 30)
    center_x, center_y = 15, 15
    radius = 12
    
    # Draw star points
    import math
    for i in range(5):
        angle1 = (i * 2 * math.pi / 5) - math.pi / 2
        angle2 = ((i + 2) * 2 * math.pi / 5) - math.pi / 2
        
        x1 = int(center_x + radius * math.cos(angle1))
        y1 = int(center_y + radius * math.sin(angle1))
        x2 = int(center_x + radius * math.cos(angle2))
        y2 = int(center_y + radius * math.sin(angle2))
        
        draw_line(canvas, center_x, center_y, x1, y1, '*')
        draw_line(canvas, x1, y1, x2, y2, '*')
    
    display_canvas(canvas)
    print()

def geometric_pattern():
    """Create a geometric pattern"""
    print("=" * 60)
    print("🔷 Geometric Pattern")
    print("=" * 60)
    canvas = create_canvas(40, 20)
    
    # Draw interconnected geometric shapes
    # Large X
    draw_line(canvas, 2, 2, 37, 17, '*')
    draw_line(canvas, 2, 17, 37, 2, '*')
    
    # Inner diamond
    draw_line(canvas, 20, 2, 37, 10, '*')
    draw_line(canvas, 37, 10, 20, 17, '*')
    draw_line(canvas, 20, 17, 2, 10, '*')
    draw_line(canvas, 2, 10, 20, 2, '*')
    
    # Outer frame
    draw_line(canvas, 5, 5, 34, 5, '*')
    draw_line(canvas, 34, 5, 34, 14, '*')
    draw_line(canvas, 34, 14, 5, 14, '*')
    draw_line(canvas, 5, 14, 5, 5, '*')
    
    display_canvas(canvas)
    print()

def spiral_pattern():
    """Create a spiral-like pattern"""
    print("=" * 60)
    print("🌀 Spiral Pattern")
    print("=" * 60)
    canvas = create_canvas(35, 35)
    center = 17
    
    # Create spiral with lines
    points = []
    for i in range(0, 360, 15):
        import math
        angle = math.radians(i)
        radius = i / 10
        x = int(center + radius * math.cos(angle))
        y = int(center + radius * math.sin(angle))
        points.append((x, y))
    
    # Connect points
    for i in range(len(points) - 1):
        draw_line(canvas, points[i][0], points[i][1], points[i+1][0], points[i+1][1], '*')
    
    display_canvas(canvas)
    print()

def abstract_art():
    """Create abstract line art"""
    print("=" * 60)
    print("🎨 Abstract Art")
    print("=" * 60)
    canvas = create_canvas(50, 25)
    
    # Multiple intersecting lines creating abstract pattern
    lines = [
        (5, 5, 45, 20),
        (5, 20, 45, 5),
        (10, 2, 10, 23),
        (25, 2, 25, 23),
        (40, 2, 40, 23),
        (5, 12, 45, 12),
        (15, 5, 35, 20),
        (15, 20, 35, 5),
        (2, 8, 48, 8),
        (2, 16, 48, 16),
    ]
    
    for x1, y1, x2, y2 in lines:
        draw_line(canvas, x1, y1, x2, y2, '*')
    
    display_canvas(canvas)
    print()

def mandala_pattern():
    """Create a mandala-like pattern"""
    print("=" * 60)
    print("🕉️  Mandala Pattern")
    print("=" * 60)
    canvas = create_canvas(40, 40)
    center_x, center_y = 20, 20
    
    import math
    # Draw radial lines
    for i in range(8):
        angle = i * math.pi / 4
        x = int(center_x + 18 * math.cos(angle))
        y = int(center_y + 18 * math.sin(angle))
        draw_line(canvas, center_x, center_y, x, y, '*')
    
    # Draw circles with lines
    for radius in [8, 15]:
        points = []
        for i in range(16):
            angle = i * 2 * math.pi / 16
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            points.append((x, y))
        
        # Connect adjacent points
        for i in range(len(points)):
            next_i = (i + 1) % len(points)
            draw_line(canvas, points[i][0], points[i][1], points[next_i][0], points[next_i][1], '*')
    
    display_canvas(canvas)
    print()

def wave_pattern():
    """Create wave patterns"""
    print("=" * 60)
    print("🌊 Wave Pattern")
    print("=" * 60)
    canvas = create_canvas(60, 20)
    
    import math
    # Create multiple wave lines
    for wave_offset in [0, 5, 10]:
        prev_x, prev_y = 0, 0
        for x in range(0, 60, 2):
            y = int(10 + 8 * math.sin((x + wave_offset) * math.pi / 15))
            if x > 0:
                draw_line(canvas, prev_x, prev_y, x, y, '*')
            prev_x, prev_y = x, y
    
    display_canvas(canvas)
    print()

def main():
    """Display all gallery examples"""
    print("\n" + "=" * 60)
    print("🎨 Line-Art Gallery")
    print("=" * 60 + "\n")
    
    star_pattern()
    geometric_pattern()
    spiral_pattern()
    abstract_art()
    mandala_pattern()
    wave_pattern()
    
    print("=" * 60)
    print("✨ Gallery complete! Create your own art with: python main.py")
    print("=" * 60)

if __name__ == "__main__":
    main()

