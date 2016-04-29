from globals import * 

def alphorder(s):
    """Using order functions to find ordered words."""
    return inOrder if s == ''.join(sorted(s)) else revOrder if s == ''.join(sorted(s, reverse=True)) else noOrder