### Function Overview

```python
def sort(width, height, length, mass):
```

- **width**, **height**, **length**: Dimensions of the package in centimeters (cm).
- **mass**: Weight of the package in kilograms (kg).

### How It Works

The function checks if a package is considered **bulky** or **heavy**:

1. **Bulky Package**:
   - The volume (width × height × length) is **1,000,000 cm³ or more**, or
   - Any single dimension is **150 cm or more**.

2. **Heavy Package**:
   - The mass is **20 kg or more**.

Based on these criteria, packages are sorted into three stacks:

- **STANDARD**: Not bulky and not heavy.
- **SPECIAL**: Bulky or heavy (but not both).
- **REJECTED**: Both bulky and heavy.

### How to Use

Simply call the function with the package's dimensions and mass:

```python
result = sort(width, height, length, mass)
print(result)  # Outputs: "STANDARD", "SPECIAL", or "REJECTED"
```

### Examples

Here are some examples to illustrate how the function works:

```python
# Standard package
print(sort(30, 40, 50, 10))      # Outputs: "STANDARD"

# Bulky due to large dimension
print(sort(200, 50, 50, 10))     # Outputs: "SPECIAL"

# Bulky due to large volume
print(sort(100, 100, 100, 10))   # Outputs: "SPECIAL"

# Heavy package
print(sort(50, 50, 50, 25))      # Outputs: "SPECIAL"

# Rejected package (both bulky and heavy)
print(sort(200, 200, 200, 25))   # Outputs: "REJECTED"
```

### Running the Tests

I've included some unit tests to make sure everything is working correctly. To run the tests, use:

```bash
python -m unittest test_sort.py
```

The tests cover a variety of scenarios:

- Standard packages
- Bulky packages (due to volume or dimensions)
- Heavy packages
- Rejected packages (both bulky and heavy)
- Edge cases like zero or negative values