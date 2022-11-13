"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
E.g.,"The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
    """
    This function checks whether a given string is a pangram.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz" # full alphabet to compare string contents
    for letter in alphabet: # for loop alphabet to evaluate string
        if letter not in s.lower(): # if statement for non pangram/ and ignores case
            return False # returns False the string is not a pangram

    return True # returns True if the string is a pangram

print(is_pangram("The quick, brown fox jumps over the lazy dog!")) # should return True

print(is_pangram("1bcdefghijklmnopqrstuvwxyz")) # should return False
