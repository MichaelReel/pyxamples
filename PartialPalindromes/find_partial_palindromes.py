
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

