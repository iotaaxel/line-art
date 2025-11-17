# Line-Art 🎨

A beautiful ASCII art line drawing tool where users can input coordinates to create stunning line-based artwork. Draw unlimited lines, create geometric patterns, and express your creativity through simple coordinate input.

## Features

- Draw unlimited lines by entering start and end coordinates
- Clean canvas without borders
- Supports as many lines as you want - keep entering start/end pairs
- Uses Bresenham's line algorithm for smooth line drawing
- Lines that cross boundaries are clipped (canvas doesn't expand)
- Real-time canvas display

## Quick Start

```bash
# Interactive mode - draw lines by entering coordinates
python main.py

# View gallery of examples
python gallery.py

# Run examples
python example.py
```

### Input Format

Enter coordinates in one of these formats:
- `x1,y1 x2,y2` - Single line (two coordinate pairs separated by space)
- `x1,y1 x2,y2 x3,y3 x4,y4 ...` - Multiple lines (even number of coordinate pairs)
- `x1,y1,x2,y2` - All coordinates comma-separated (single line)

**Note:** If you enter an odd number of coordinate pairs, the last one will be ignored (no end point).

### Commands

- `show` or `display` - Display the current canvas
- `clear` - Clear the canvas and start fresh
- `done` or `quit` or `exit` - Exit the program

### Example

```
Enter canvas dimensions (width height, default: 20 20):
> 25 15

Enter lines (format: x1,y1 x2,y2)
> 1,1 10,5
> 2,2 8,12 15,1 20,10
> show
> done
```

## Examples

### Star Pattern
```bash
python gallery.py
```

### Interactive Drawing
```bash
python main.py
# Enter: 1,1 10,10 5,5 15,15 10,1 1,10
```

## How It Works

The program uses **Bresenham's line algorithm** to draw lines between two points. This algorithm efficiently determines which pixels should be filled to create a smooth line between the start and end coordinates. Lines that extend beyond the canvas boundaries are automatically clipped.

## Gallery

Run `python gallery.py` to see examples including:
- ⭐ Star patterns
- 🔷 Geometric shapes
- 🌀 Spiral designs
- 🎨 Abstract art
- 🕉️ Mandala patterns
- 🌊 Wave patterns

## Requirements

- Python 3.6+

## Installation

No dependencies required! Just clone and run:

```bash
git clone https://github.com/iotaaxel/line-art.git
cd line-art
python main.py
```

## Contributing

Contributions welcome! Feel free to submit issues, feature requests, or pull requests.

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

Made with ❤️ for ASCII art enthusiasts
