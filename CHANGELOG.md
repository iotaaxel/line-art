# Changelog

## [1.0.0] - 2024-11-16

### Added
- Support for multiple line pairs in a single input
- Automatic handling of odd number of coordinates (last one ignored)
- Boundary clipping (canvas doesn't expand when lines cross boundaries)
- Clean canvas without borders
- Unlimited line support - keep entering start/end pairs

### Features
- Bresenham's line algorithm for smooth line drawing
- Multiple input formats: `x1,y1 x2,y2` or `x1,y1 x2,y2 x3,y3 x4,y4 ...`
- Interactive commands: `show`, `clear`, `done`

