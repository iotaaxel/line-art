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
    import sys
    print("=" * 50)
    print("Testing Line-Art")
    print("=" * 50)
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        test_single_line()
        tests_passed += 1
    except Exception as e:
        tests_failed += 1
        print(f"Test 1 failed: {e}")
        import traceback
        traceback.print_exc()
    
    try:
        test_multiple_lines()
        tests_passed += 1
    except Exception as e:
        tests_failed += 1
        print(f"Test 2 failed: {e}")
        import traceback
        traceback.print_exc()
    
    try:
        test_odd_coordinates()
        tests_passed += 1
    except Exception as e:
        tests_failed += 1
        print(f"Test 3 failed: {e}")
        import traceback
        traceback.print_exc()
    
    try:
        test_display()
        tests_passed += 1
    except Exception as e:
        tests_failed += 1
        print(f"Test 4 failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 50)
    if tests_failed == 0:
        print(f"All {tests_passed} tests passed! ✓")
        print("=" * 50)
        sys.exit(0)
    else:
        print(f"Tests: {tests_passed} passed, {tests_failed} failed ✗")
        print("=" * 50)
        sys.exit(1)

