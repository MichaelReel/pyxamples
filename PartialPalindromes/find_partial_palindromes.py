"""
This will read the dictionary file and output any partial palindromes

A partial palindrome is defined as a word that would
be a palindrome if the first or last letter was removed.
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

