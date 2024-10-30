def sort(width, height, length, mass):
    # Check for negative dimensions or mass
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative numbers.")
    
    # Calculate volume
    vol = width * height * length
    # Find largest dimension
    max_dim = max(width, height, length)
    
    # Check if package is bulky
    is_bulky = vol >= 1_000_000 or max_dim >= 150
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Determine the correct stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"