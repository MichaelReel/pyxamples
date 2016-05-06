from globals import *

# lifted from : https://gist.github.com/badboy/6267743

class Mix96:
    """Robert Jenkin's 96 Mix Function"""
    
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

def rshift(val, n):
    """Logical right shift"""
    return (val % 0x100000000) >> n

def lshift(val, n):
    return val << n

def mix(a, b, c):
    a=a-b;  a=a-c;  a=a^rshift(c, 13);
    b=b-c;  b=b-a;  b=b^lshift(a, 8);
    c=c-a;  c=c-b;  c=c^rshift(b, 13);
    a=a-b;  a=a-c;  a=a^rshift(c, 12);
    b=b-c;  b=b-a;  b=b^lshift(a, 16);
    c=c-a;  c=c-b;  c=c^rshift(b, 5);
    a=a-b;  a=a-c;  a=a^rshift(c, 3);
    b=b-c;  b=b-a;  b=b^lshift(a, 10);
    c=c-a;  c=c-b;  c=c^rshift(b, 15);
    return c;