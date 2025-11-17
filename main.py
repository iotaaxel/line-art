#!/usr/bin/env python3
"""
Line-Art - Draw ASCII art lines from coordinate input
Users input coordinates (x1, y1, x2, y2) to draw lines on a canvas
Supports unlimited lines - keep entering start/end pairs until done
"""

def clip_to_bounds(x, y, width, height):
    """Clip coordinates to canvas bounds"""
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))
    return x, y

def draw_line(board, x1, y1, x2, y2, char='*'):
    """
    Draw a line from (x1, y1) to (x2, y2) using Bresenham's line algorithm
    Lines that cross boundaries are clipped (not expanded)
    """
    # Ensure coordinates are integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    # Get board dimensions
    height = len(board)
    width = len(board[0]) if height > 0 else 0
    
    # Clip coordinates to bounds (don't expand canvas)
    x1, y1 = clip_to_bounds(x1, y1, width, height)
    x2, y2 = clip_to_bounds(x2, y2, width, height)
    
    # Bresenham's line algorithm
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    x, y = x1, y1
    
    while True:
        # Plot the point (with bounds check for safety)
        if 0 <= x < width and 0 <= y < height:
            board[y][x] = char
        
        # Check if we've reached the end point
        if x == x2 and y == y2:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def create_canvas(width, height):
    """
    Create an empty canvas (no borders)
    """
    # Create empty canvas
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    return canvas


def display_canvas(canvas):
    """
    Display the canvas
    """
    for row in canvas:
        print(''.join(row))


def parse_coordinates(input_str):
    """
    Parse coordinate input. Supports formats like:
    - "x1,y1 x2,y2" - single line
    - "x1,y1 x2,y2 x3,y3 x4,y4" - multiple lines (even number of pairs)
    - "x1,y1\nx2,y2"
    - "x1,y1,x2,y2"
    If odd number of coordinate pairs, the last one is ignored (no end point)
    Returns list of line pairs: [(start1, end1), (start2, end2), ...]
    """
    # Split by spaces and newlines
    parts = input_str.replace('\n', ' ').split()
    
    # Try to parse all coordinate pairs
    coord_pairs = []
    for part in parts:
        coords = part.split(',')
        if len(coords) == 2:
            try:
                coord_pairs.append((int(coords[0]), int(coords[1])))
            except ValueError:
                raise ValueError(f"Invalid coordinate: {part}")
        else:
            # Try comma-separated format like "x1,y1,x2,y2"
            if len(coords) == 4:
                try:
                    coord_pairs.append((int(coords[0]), int(coords[1])))
                    coord_pairs.append((int(coords[2]), int(coords[3])))
                except ValueError:
                    raise ValueError(f"Invalid coordinate format: {part}")
    
    if not coord_pairs:
        raise ValueError("No valid coordinates found. Use: x1,y1 x2,y2")
    
    # If odd number of pairs, ignore the last one (no end point)
    if len(coord_pairs) % 2 != 0:
        coord_pairs = coord_pairs[:-1]
        if len(coord_pairs) == 0:
            raise ValueError("Need at least 2 coordinate pairs (start and end) for a line")
    
    # Group into line pairs: (start, end)
    line_pairs = []
    for i in range(0, len(coord_pairs), 2):
        line_pairs.append((coord_pairs[i], coord_pairs[i+1]))
    
    return line_pairs


def main():
    """
    Main function to handle user input and draw lines
    Supports unlimited lines - users can keep entering start/end pairs
    """
    print("=" * 50)
    print("Line-Art - ASCII Line Drawing Tool")
    print("=" * 50)
    print("\nEnter canvas dimensions (width height, default: 20 20):")
    
    try:
        dim_input = input().strip()
        if dim_input:
            width, height = map(int, dim_input.split())
        else:
            width, height = 20, 20
    except:
        width, height = 20, 20
    
    canvas = create_canvas(width, height)
    line_count = 0
    
    print(f"\nCanvas created: {width}x{height}")
    print("\nEnter lines (format: x1,y1 x2,y2)")
    print("You can enter multiple lines at once: x1,y1 x2,y2 x3,y3 x4,y4 ...")
    print("If odd number of coordinates, the last one is ignored")
    print("Enter 'done' when finished, 'show' to display, 'clear' to reset")
    print("Example: 1,1 5,5")
    print("Example (multiple): 1,1 5,5 2,2 8,8 3,3 9,9")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
                
            user_input_lower = user_input.lower()
            
            if user_input_lower == 'done' or user_input_lower == 'quit' or user_input_lower == 'exit':
                break
            elif user_input_lower == 'show' or user_input_lower == 'display':
                print("\nCurrent canvas:")
                display_canvas(canvas)
                print()
            elif user_input_lower == 'clear':
                canvas = create_canvas(width, height)
                line_count = 0
                print("Canvas cleared!\n")
            else:
                # Parse and draw lines (can be multiple)
                line_pairs = parse_coordinates(user_input)
                lines_drawn = 0
                for start, end in line_pairs:
                    x1, y1 = start
                    x2, y2 = end
                    draw_line(canvas, x1, y1, x2, y2)
                    line_count += 1
                    lines_drawn += 1
                    print(f"Line {line_count} drawn from ({x1},{y1}) to ({x2},{y2})")
                
                if lines_drawn > 1:
                    print(f"(Drew {lines_drawn} lines, total: {line_count})\n")
                else:
                    print(f"(Total lines: {line_count})\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}\n")
    
    # Final display
    print(f"\nFinal canvas ({line_count} lines total):")
    display_canvas(canvas)
    print()


if __name__ == "__main__":
    main()

