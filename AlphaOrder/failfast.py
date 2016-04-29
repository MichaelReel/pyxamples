from globals import *

def alphorder(s):
    """Checking each character against the next and failing quickly."""
    ord = True;
    rev = True;
    if s == "":
        # Maintain parity with alphorder1 function on blank lines
        return inOrder
    last = s[0]
    for c in s[1:]:
        if c > last and rev:
            rev = False
        if c < last and ord:
            ord = False
        if not (ord or rev):
            break
        last = c
    return inOrder if ord else revOrder if rev else noOrder