from globals import *

class Multiplactive:
    """Knuths Multiplicative Method"""
    
    def __init__(self, (width, height)):
        self.ratio = 2654435761
        self.width = width
        self.height = height
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        knuth = (y * self.width + x) * self.ratio
        
        colour[0] = knuth & max_colour
        colour[1] = (knuth >> 8) & max_colour
        colour[2] = (knuth >> 16) & max_colour
            
        return colour