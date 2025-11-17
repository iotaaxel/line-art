# Art Examples

This directory contains example art outputs generated with Line-Art.

## Output Files

- `gallery_output.txt` - Output from `gallery.py` (6 patterns: star, geometric, spiral, abstract, mandala, wave)
- `demo_output.txt` - Output from `demo.py` (abstract composition)
- `example_output.txt` - Output from `example.py` (basic examples)
- `custom_art_output.txt` - Output from `custom_art.py` (heart, house, tree, arrow, diamond, flower)

## Viewing the Art

You can view these files directly:
```bash
cat examples/gallery_output.txt
cat examples/demo_output.txt
cat examples/example_output.txt
cat examples/custom_art_output.txt
```

## Regenerating Art

To regenerate the art outputs:
```bash
python gallery.py > examples/gallery_output.txt
python demo.py > examples/demo_output.txt
python example.py > examples/example_output.txt
python examples/custom_art.py > examples/custom_art_output.txt
```

## Creating Your Own

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

## Art Patterns Included

### Gallery (`gallery.py`)
- ⭐ Star patterns
- 🔷 Geometric shapes
- 🌀 Spiral designs
- 🎨 Abstract art
- 🕉️ Mandala patterns
- 🌊 Wave patterns

### Custom Art (`custom_art.py`)
- ❤️ Heart shape
- 🏠 House shape
- 🌲 Tree shape
- ➡️ Arrow patterns
- 💎 Diamond patterns
- 🌸 Flower patterns
