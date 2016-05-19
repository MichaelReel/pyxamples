import random, sys
from globals import *

class RandomColour:
    """A simple class that ignore input and returns a random colour"""

    def getColour(self, (x, y)):
        """Return a random colour, we don't care about position."""
        colour = [0,0,0]
        
        # Get a random color
        for i in range(len(colour)):
            colour[i] = random.randint(min_colour, max_colour)
            
        return colour
    
    def getHash(self, x, y):
        """Return a random value, we don't care about position."""
        return random.randint(-sys.maxint-1, sys.maxint)