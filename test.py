#!/usr/bin/env python3
"""Test script for line-art"""

from main import create_canvas, draw_line, display_canvas, parse_coordinates

def test_single_line():
    print("Test 1: Single line")
    canvas = create_canvas(20, 20)
    line_pairs = parse_coordinates("1,1 5,5")
    assert len(line_pairs) == 1
    start, end = line_pairs[0]
    draw_line(canvas, start[0], start[1], end[0], end[1])
    print("✓ Single line parsed correctly")
    return True

def test_multiple_lines():
    print("\nTest 2: Multiple lines")
    canvas = create_canvas(20, 20)
    line_pairs = parse_coordinates("1,1 5,5 2,2 8,8 3,3 9,9")
    assert len(line_pairs) == 3
    for start, end in line_pairs:
        draw_line(canvas, start[0], start[1], end[0], end[1])
    print("✓ Multiple lines parsed correctly")
    return True

def test_odd_coordinates():
    print("\nTest 3: Odd number of coordinates (should ignore last)")
    canvas = create_canvas(20, 20)
    line_pairs = parse_coordinates("1,1 5,5 2,2 8,8 3,3")
    assert len(line_pairs) == 2  # Should ignore the last odd coordinate
    for start, end in line_pairs:
        draw_line(canvas, start[0], start[1], end[0], end[1])
    print("✓ Odd coordinates handled correctly (last ignored)")
    return True

def test_display():
    print("\nTest 4: Display canvas")
    canvas = create_canvas(20, 20)
    line_pairs = parse_coordinates("1,1 10,5 2,2 8,12 15,1 20,10")
    for start, end in line_pairs:
        draw_line(canvas, start[0], start[1], end[0], end[1])
    print("Canvas with 3 lines:")
    display_canvas(canvas)
    print("✓ Display works")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Line-Art")
    print("=" * 50)
    
    try:
        test_single_line()
        test_multiple_lines()
        test_odd_coordinates()
        test_display()
        print("\n" + "=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
    except Exception as e:
        print(f"\nTest failed: {e}")
        import traceback
        traceback.print_exc()

