# Examples

This directory contains example art generated with Line-Art.

## Running Examples

```bash
# Run the gallery
python gallery.py

# Run basic examples
python example.py

# Run tests
python test.py
```

## Creating Your Own Art

Use the interactive mode:
```bash
python main.py
```

Or programmatically:
```python
from main import create_canvas, draw_line, display_canvas

canvas = create_canvas(30, 30)
draw_line(canvas, 5, 5, 25, 25, '*')
draw_line(canvas, 5, 25, 25, 5, '*')
display_canvas(canvas)
```

