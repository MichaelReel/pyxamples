from procedural.builtin import Hashing
from procedural.rand import RandomColour

width = 200
height = 200
generator = Hashing((width, height), "salt")
# generator = RandomColour()
bits = 32

bits_used = [0] * bits

for x,y in [(x,y) for x in range(width) for y in range(height)]:
    hsh = generator.getHash(x, y)
    for b in range(len(bits_used)):
        bits_used[b] += 1 if hsh & (1 << b) else 0
    print "{{0:0{0:d}b}} : {{0:d}}".format(bits).format(hsh)
        
print bits_used