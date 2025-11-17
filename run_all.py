#!/usr/bin/env python3
"""
Run all tests and generate art showcase
"""

import sys
import subprocess

def run_script(script_name, description):
    """Run a Python script and display results"""
    print("\n" + "=" * 70)
    print(f"📋 {description}")
    print("=" * 70)
    try:
        import os
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running {script_name}: {e}")
        return False

def main():
    print("\n" + "🎨" * 35)
    print(" " * 20 + "LINE-ART SHOWCASE")
    print("🎨" * 35)
    
    # Run tests
    print("\n🔬 Running Tests...")
    run_script("test.py", "Test Suite")
    
    # Run demo
    print("\n🎯 Running Demo...")
    run_script("demo.py", "Quick Demo")
    
    # Run gallery
    print("\n🖼️  Running Gallery...")
    run_script("gallery.py", "Art Gallery")
    
    print("\n" + "=" * 70)
    print("✨ All done! Line-Art is working beautifully!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()

