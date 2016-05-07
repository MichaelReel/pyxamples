from globals import *

# lifted from : https://gist.github.com/badboy/6267743

class Mix96:
    """Robert Jenkins' 96 Mix Function"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
        
        jenkins = mix(x, y, 0)
        
        colour[0] = jenkins & max
        colour[1] = (jenkins >> 8) & max
        colour[2] = (jenkins >> 16) & max
            
        return colour
    
class Mix32Bit:
    """Robert Jenkins' 32 Bit Integer hash function"""
    
    def __init__(self, (width, height)):
        self.width = width
        self.height = height
        
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
            
        jenkins = mix32Bit(x + (y * self.width))
        
        colour[0] = jenkins & max
        colour[1] = (jenkins >> 8) & max
        colour[2] = (jenkins >> 16) & max
            
        return colour
    
def mix(a, b, c):
    a=a-b;  a=a-c;  a=a^rshift_log(c, 13)
    b=b-c;  b=b-a;  b=b^lshift(a, 8)
    c=c-a;  c=c-b;  c=c^rshift_log(b, 13)
    a=a-b;  a=a-c;  a=a^rshift_log(c, 12)
    b=b-c;  b=b-a;  b=b^lshift(a, 16)
    c=c-a;  c=c-b;  c=c^rshift_log(b, 5)
    a=a-b;  a=a-c;  a=a^rshift_log(c, 3)
    b=b-c;  b=b-a;  b=b^lshift(a, 10)
    c=c-a;  c=c-b;  c=c^rshift_log(b, 15)
    return c

def mix32Bit(a):
    a = (a+0x7ed55d16) + lshift(a, 12)
    a = (a^0xc761c23c) ^ rshift_ari(a, 19)
    a = (a+0x165667b1) + lshift(a, 5)
    a = (a+0xd3a2646c) ^ lshift(a, 9)
    a = (a+0xfd7046c5) + lshift(a, 3)
    a = (a^0xb55a4f09) ^ rshift_ari(a, 16)
    return a
