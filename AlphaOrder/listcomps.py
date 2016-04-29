from globals import *

def alphorder(s):
    """Using 2 list comprehensions."""
    # Modified version of JH's solution
    f = [a <= b for a,b in zip(s,s[1:])]
    g = [a >= b for a,b in zip(s,s[1:])]
    return inOrder if all(f) else revOrder if all(g) else noOrder