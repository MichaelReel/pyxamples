from globals import *
import hashlib

class Hashing:
    """Use builtin python to produce hash"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        h = hashlib.md5()
        h.update(str(x + (y * self.width)))
        
        hash_v = hash(h.digest())
        
        colour[0] = hash_v & max
        colour[1] = (hash_v >> 8) & max
        colour[2] = (hash_v >> 16) & max
            
        return colour