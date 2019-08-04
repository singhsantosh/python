# Code

def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    if len(input) == 0:
        return ""

    return input[len(input) - 1] + reverse_string(input[0:len(input) - 1])


# Test Cases

print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")