def sort(width, height, length, mass):
    # Calculate volume 
    volume = width * height * length
    # Detect the largest dimension
    max_dimension = max(width, height, length)
    
    # Check if package is bulky
    is_bulky = volume >= 1_000_000 or max_dimension >= 150
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Determine correct stack based on criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"