"""
This will simply read the dictionary.txt file line by line,
and will print any partial palindromes it encounters.

Partial palindromes in this case are defined by having a
palindrome preceeded or succeeded by a single letter.
"""

INPUT_FILE = "dictionary.txt"

with open(INPUT_FILE) as inf:
    for line in inf.read().splitlines():
        if len(line) < 3:
            continue
        partial = line[1::]
        if partial == (partial[::-1]):
            print line
        partial = line[:-1:]
        if partial == (partial[::-1]):
            print line
