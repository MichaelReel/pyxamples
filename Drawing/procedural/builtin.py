from globals import *
import hashlib, sys

class Hashing:
    """Use builtin python to produce hash"""
    
    def __init__(self, (width, height), salt):
        self.width = width
        self.height = height
        self.salt = salt
        self.min_hash = 0.0
        self.max_hash = 0.0
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        hash_v = self.getHash(x, y)
        
        grey = int(max_colour * (0.5 + float(hash_v) / (2 * sys.maxint)))
        for i in range(len(colour)):
            colour[i] = grey
            
        return colour
    
    def getHash(self, x, y):
        """Return a hash value."""
        h = hashlib.md5()
        
        h.update(str(self.salt))
        h.update(str(x + (y * self.width)))
        
        hash_v = hash(h.digest())

        self.min_hash = min(hash_v, self.min_hash)
        self.max_hash = max(hash_v, self.max_hash)
        
        return hash_v