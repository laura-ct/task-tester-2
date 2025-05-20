def reverse_string(input_string):
    """
    Reverse the given string using a manual character-by-character approach.
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if len(input_string) <= 1:
        return input_string
    
    # Convert string to list for manipulation
    chars = list(input_string)
    
    # Manual reversal using two-pointer technique
    left = 0
    right = len(chars) - 1
    
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)