from globals import *
import math, sys

# Lifted from: http://freespace.virgin.net/hugo.elias/models/m_perlin.htm

class Linear:
    """A simple perlin generator."""
    
    def __init__(self, (width, height), hashgen, octives, persist):
        """todo"""
        self.width = width
        self.height = height
        self.hashgen = hashgen
        self.octives = octives
        self.persist = persist
        self.min_hash = 0.0
        self.max_hash = 0.0
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        # hash_val = self.smoothNoise(x, y)
        hash_val = self.perlinNoise(x, y)
        
        self.min_hash = min(hash_val, self.min_hash)
        self.max_hash = max(hash_val, self.max_hash)
        
        grey = int(max_colour * (0.5 + float(hash_val) / (2 * sys.maxint)))
        for i in range(len(colour)):
            colour[i] = grey
        
        return colour
    
    def smoothNoise(self, x, y):
        """Return the smoothed noise."""
        
        f = self.hashgen.getHash
        corners = ( f(x-1, y-1)+f(x+1, y-1)+f(x-1, y+1)+f(x+1, y+1) ) / float(16)
        sides   = ( f(x-1, y  )+f(x+1, y  )+f(x,   y-1)+f(x,   y+1) ) /  float(8)
        center  =   f(x,   y  ) / float(4)
        
        return corners + sides + center
    
    def perlinNoise(self, x, y):
        """Return the perlin noise."""
        
        total = 0
        p = self.persist
        n = self.octives - 1
        
        for i in range(0, n):
            frequency = math.pow(2, i)
            amplitude = math.pow(p, i)
            
            total = total + self.smoothNoise(float(x) * frequency, float(y) * frequency) * amplitude
            
        return total
    
    def getHash(self, x, y):
        return int(self.perlinNoise(x, y))
        