"""
This will simply read the dictionary.txt file line by line,
and will print any partial palindromes it encounters.

Partial palindromes in this case are defined by having a
palindrome preceeded or succeeded by a single letter.
"""

INPUT_FILE = "dictionary.txt"

def is_partial_palindrome(word):
    """
    Returns true if a word is a partial palindrome
    """
    if len(word) < 3:
        return False
    return is_palindrome(word[1::]) or is_palindrome(word[:-1:])

def is_palindrome(word):
    """
    Returns true if a word is a palindrome
    """
    return word == word[::-1]

with open(INPUT_FILE) as inf:
    for line in inf.read().splitlines():
        if is_partial_palindrome(line):
            print line
