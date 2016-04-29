from globals import *

def alphorder(s):
    """Create tuple list with single list comprehension."""
    # Modified version of JH's solution (slower)
    f = [(a <= b, a >= b) for a,b in zip(s,s[1:])]
    return inOrder if all(g[0] for g in f) else revOrder if all(g[1] for g in f) else noOrder