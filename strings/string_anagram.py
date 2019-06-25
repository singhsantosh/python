# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other
        An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    if len(str1) != len(str2):
        clean_str1 = str1.replace(" ", "").lower()
        clean_str2 = str2.replace(" ", "").lower()

        if sorted(clean_str1) == sorted(clean_str2):
            return True

    return False


# Test Cases


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
