
INPUT_FILE = "dictionary.txt"

with open(INPUT_FILE) as inf:
    for line in inf.read().splitlines():
        if line == (line[::-1]):
            print line
