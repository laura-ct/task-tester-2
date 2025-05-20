def reverse_string(input_string):
    """
    Reverse a given string manually without using slice notation or reverse().

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is None.
    """
    # Check for None input
    if input_string is None:
        raise ValueError("Input string cannot be None")
    
    # Check for non-string input
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, not {type(input_string).__name__}")
    
    # Manually reverse the string using a list-based approach
    reversed_chars = []
    for char in input_string:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)