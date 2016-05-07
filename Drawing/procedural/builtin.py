from globals import *
import hashlib, sys

class Hashing:
    """Use builtin python to produce hash"""
    
    def __init__(self, (width, height), salt):
        self.width = width
        self.height = height
        self.salt = salt
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        hash_v = self.getHash(x, y)
        
        grey = int(max * (0.5 + float(hash_v) / (2 * sys.maxint)))
        for i in range(len(colour)):
            colour[i] = grey
            
        return colour
    
    def getHash(self, x, y):
        """Return a hash value."""
        h = hashlib.md5()
        
        h.update(str(self.salt))
        h.update(str(x + (y * self.width)))
        
        return hash(h.digest())