from procedural import *

class Gradient:
    """A simple red + blue = magenta gradient class"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.dx = float(max_colour) / width
        self.dy = float(max_colour) / height
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        colour[0] = int(x * self.dx)
        colour[2] = int(y * self.dy)
            
        return colour
    
    def getHash(self, x, y):
        return x + y * self.width
    