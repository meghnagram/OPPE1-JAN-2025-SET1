def deinterleave(s: str) -> str:
    """
    Deinterleave even and odd indices in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The deinterleaved string.
    """
    
    return s[::2] + s[1::2]

# #Another Method:
# def deinterleave(s: str) -> str:
#     e=s[0::2]
#     o=s[1::2]
#     return e+o

# Deinterleave Even and Odd Indices in String
# Write a function deinterleave that takes a string s as input and returns a new string where the characters at even indices are placed before the characters at odd indices.

# Examples

# "abcdef" -> "acebdf"
# "12345" -> "13524"
