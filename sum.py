def add(a, b):
    """
    Returns the sum of a and b.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of a and b.
    """
    try:
        return a + b
    except TypeError:
        print("Error: Both a and b must be numbers.")
        return None