## Package Sorting Function

This function is designed for Thoughtful's robotic automation factory to dispatch packages to the correct stack based on their dimensions and mass.

### Function Signature

```python
def sort(width, height, length, mass):
```

- `width`, `height`, `length`: Dimensions of the package in centimeters (cm).
- `mass`: Mass of the package in kilograms (kg).

### Sorting Criteria

1. **Bulky Package**:
   - Volume (Width x Height x Length) ≥ 1,000,000 cm³, or
   - Any dimension ≥ 150 cm.

2. **Heavy Package**:
   - Mass ≥ 20 kg.

### Stack Assignment

- **REJECTED**: Package is both bulky and heavy.
- **SPECIAL**: Package is either bulky or heavy (but not both).
- **STANDARD**: Package is neither bulky nor heavy.

### Usage

```python
result = sort(width, height, length, mass)
print(result)  # Outputs: "STANDARD", "SPECIAL", or "REJECTED"
```

### Examples

```python
sort(30, 40, 50, 10)      # Returns "STANDARD"
sort(200, 50, 50, 10)     # Returns "SPECIAL" (Bulky due to dimension)
sort(100, 100, 100, 10)   # Returns "SPECIAL" (Bulky due to volume)
sort(50, 50, 50, 25)      # Returns "SPECIAL" (Heavy)
sort(200, 200, 200, 25)   # Returns "REJECTED" (Bulky and Heavy)
```

### Testing

Run the unit tests to verify the function's correctness:

```bash
python -m unittest test_sort.py
```

The tests cover various scenarios including standard packages, bulky packages (due to volume and dimensions), heavy packages, rejected packages, and edge cases like zero or negative values.