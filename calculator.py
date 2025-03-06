"""
This module contains functions for basic arithmetic operations: addition, multiplication, and subtraction.

Functions:
    add(a, b): Returns the sum of a and b. (To be implemented by Ian)
    multiply(a, b): Returns the product of a and b. (To be implemented by Rashid)
    subtract(a, b): Returns the difference between a and b. (To be implemented by Gladys)
"""

def multiply(a, b):
    """
    Returns the product of a and b.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The product of a and b.
    """
    try:
        return a * b
    except TypeError:
        print("Error: Both a and b must be numbers.")
        return None
    

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