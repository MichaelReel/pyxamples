from math import floor
from procedural import *
from sys import maxint
import random

# Lifted from: http://mrl.nyu.edu/~perlin/noise/

class PerlinRef(object):

    def __init__(self, (width, height), zoom = 10.0):
        self.p = []
        self.min_hash = 0.0
        self.max_hash = 0.0
        self.dx = float(zoom) / width
        self.dy = float(zoom) / height
        permutation = self.getPermutation()
        for i in range(512):
            self.p.append(permutation[i % len(permutation)])
            
    def getPermutation(self):
        return [
            151,160,137, 91, 90, 15,131, 13,201, 95, 96, 53,194,233,  7,225,
            140, 36,103, 30, 69,142,  8, 99, 37,240, 21, 10, 23,190,  6,148,
            247,120,234, 75,  0, 26,197, 62, 94,252,219,203,117, 35, 11, 32,
             57,177, 33, 88,237,149, 56, 87,174, 20,125,136,171,168, 68,175,
             74,165, 71,134,139, 48, 27,166, 77,146,158,231, 83,111,229,122,
             60,211,133,230,220,105, 92, 41, 55, 46,245, 40,244,102,143, 54,
             65, 25, 63,161,  1,216, 80, 73,209, 76,132,187,208, 89, 18,169,
            200,196,135,130,116,188,159, 86,164,100,109,198,173,186,  3, 64,
             52,217,226,250,124,123,  5,202, 38,147,118,126,255, 82, 85,212,
            207,206, 59,227, 47, 16, 58, 17,182,189, 28, 42,223,183,170,213,
            119,248,152,  2, 44,154,163, 70,221,153,101,155,167, 43,172,  9,
            129, 22, 39,253, 19, 98,108,110, 79,113,224,232,178,185,112,104,
            218,246, 97,228,251, 34,242,193,238,210,144, 12,191,179,162,241,
             81, 51,145,235,249, 14,239,107, 49,192,214, 31,181,199,106,157,
            184, 84,204,176,115,121, 50, 45,127,  4,150,254,138,236,205, 93,
            222,114, 67, 29, 24, 72,243,141,128,195, 78, 66,215, 61,156,180,
        ]
    
    def getFloatHash(self, x, y, z = 0):
        X = int(floor(x)) & 255             # FIND UNIT CUBE THAT
        Y = int(floor(y)) & 255             # CONTAINS POINT.
        Z = int(floor(z)) & 255
        x -= floor(x)                       # FIND RELATIVE X,Y,Z
        y -= floor(y)                       # OF POINT IN CUBE.
        z -= floor(z)
        u = fade(x)                         # COMPUTE FADE CURVES
        v = fade(y)                         # FOR EACH OF X,Y,Z.
        w = fade(z) 
        A  = self.p[X  ]+Y                  # HASH COORDINATES OF
        AA = self.p[A]+Z                    # THE 8 CUBE CORNERS,
        AB = self.p[A+1]+Z
        B  = self.p[X+1]+Y
        BA = self.p[B]+Z
        BB = self.p[B+1]+Z

        return lerp(w, lerp(v, lerp(u, grad(self.p[AA  ], x  , y  , z   ),   # AND ADD
                                       grad(self.p[BA  ], x-1, y  , z   )),  # BLENDED
                               lerp(u, grad(self.p[AB  ], x  , y-1, z   ),   # RESULTS
                                       grad(self.p[BB  ], x-1, y-1, z   ))), # FROM  8
                       lerp(v, lerp(u, grad(self.p[AA+1], x  , y  , z-1 ),   # CORNERS
                                       grad(self.p[BA+1], x-1, y  , z-1 )),  # OF CUBE
                               lerp(u, grad(self.p[AB+1], x  , y-1, z-1 ),
                                       grad(self.p[BB+1], x-1, y-1, z-1 ))));
    
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
                
        hash_val = self.getFloatHash(x * self.dx, y * self.dy)
        
        self.min_hash = min(hash_val, self.min_hash)
        self.max_hash = max(hash_val, self.max_hash)
        
        grey = int(max_colour * (1 + float(hash_val)) / 2)
        for i in range(len(colour)):
            colour[i] = grey
        
        return colour
    
    def getHash(self, x, y):
        return int(maxint * float(self.getFloatHash(x * self.dx, y * self.dy)))
        
class SeededPerlinRef(PerlinRef):
    def __init__(self, (width, height), seed, zoom = 10.0):
        self.rand = random.Random(seed)
        super(SeededPerlinRef, self).__init__((width, height), zoom)
        
    def getPermutation(self):
        permutation = super(SeededPerlinRef, self).getPermutation()
        return self.rand.sample(permutation, len(permutation))
    
class ColourPerlin(object):
    def __init__(self, (width, height), seed, zoom = (10.0, 10.0, 10.0)):
        random.seed(seed)
        self.rd = SeededPerlinRef((width, height), random.random(), zoom[0])
        self.gn = SeededPerlinRef((width, height), random.random(), zoom[1])
        self.be = SeededPerlinRef((width, height), random.random(), zoom[2])
        
    def getColour(self, (x, y)):
        """Return a colour."""
        colour = [0,0,0]
                
        colour[0] = self.rd.getColour((x, y))[0]
        colour[1] = self.gn.getColour((x, y))[1]
        colour[2] = self.be.getColour((x, y))[2]
        
        return colour
        
def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(t, a, b):
    return a + t * (b - a)

def grad(hsh, x, y, z):
    h = hsh & 15;                      # CONVERT LO 4 BITS OF HASH CODE
    u = x if h<8 else y                # INTO 12 GRADIENT DIRECTIONS.
    v = y if h<4 else x if h==12 or h==14 else z
    return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)
