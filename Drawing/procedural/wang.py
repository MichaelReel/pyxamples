from globals import *

# lifted from : https://gist.github.com/badboy/6267743

class Mix32Bit:
    """Thomas Wang's 32 bit Mix Function"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        wangs = getHash(x, y)
        
        colour[0] = wangs & max_colour
        colour[1] = (wangs >> 8) & max_colour
        colour[2] = (wangs >> 16) & max_colour
            
        return colour
    
    def getHash(self, x, y):
        return hash32Shift(x + (y * self.width))

class MultiplicationHash:
    """Thomas Wang's Multiplication for hashing function"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
        
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
            
        wangs = getHash(x, y)
        
        colour[0] = wangs & max_colour
        colour[1] = (wangs >> 8) & max_colour
        colour[2] = (wangs >> 16) & max_colour
            
        return colour
    
    def getHash(self, x, y):
        return hash32ShiftMulti(x + (y * self.width))
    
class Mix64Bit:
    """Thomas Wang's 64 bit Mix Function"""
    """Not sure this makes a difference, or even matters on 32 bit architechure"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        wangs = getHash(x, y)
        
        colour[0] = wangs & max_colour
        colour[1] = (wangs >> 8) & max_colour
        colour[2] = (wangs >> 16) & max_colour
            
        return colour
    
    def getHash(self, x, y):
        return hash64Shift(long(x) + (long(y) * self.width))

def hash32Shift(key):
    key = ~key + lshift(key, 15)  # key = (key << 15) - key - 1
    key =  key ^ rshift_log(key, 12)
    key =  key + lshift(key, 2)
    key =  key ^ rshift_log(key, 4)
    key =  key * 2057             # key = (key + (key << 3)) + (key << 11)
    key =  key ^ rshift_log(key, 16)
    return key

def hash32ShiftMulti(key):
    c2  = 0x27d4eb2d                         # a prime or an odd constant
    key = (key ^ 61) ^ rshift_log(key, 16)
    key = key + lshift(key, 3)
    key = key ^ rshift_log(key, 4)
    key = key * c2
    key = key ^ rshift_log(key, 15)
    return key

def hash64Shift(key):
    key = (~key) + lshift(key, 21)                # key = (key << 21) - key - 1
    key = key ^ rshift_log(key, 24)
    key = (key + lshift(key, 3)) + lshift(key, 8) # key * 265
    key = key ^ rshift_log(key, 14)
    key = (key + lshift(key, 2)) + lshift(key, 4) # key * 21
    key = key ^ rshift_log(key, 28)
    key = key + lshift(key, 31)
    return key