from procedural import rand, gradient, knuth, jenkins, wang, builtin, perlin, perlin_ref
import sys
from time import time

width = 200
height = 200

gridSize = (width, height)

md5hash = builtin.Hashing(gridSize, "mhlem")
generators = [
        rand.RandomColour(),
        gradient.Gradient(gridSize),
        knuth.Multiplactive(gridSize),
        jenkins.Mix96(gridSize),
        wang.Mix32Bit(gridSize),
        jenkins.Mix32Bit(gridSize),
        wang.MultiplicationHash(gridSize),
        wang.Mix64Bit(gridSize),
        md5hash,
        perlin.Linear(gridSize, md5hash, 4, 0.485),
        perlin_ref.PerlinRef(gridSize),
    ]

bits = 32
    
for generator in generators:
    bits_used = [0] * bits
    start = time()
    
    for x,y in [(x,y) for x in range(width) for y in range(height)]:
        hsh = generator.getHash(x, y)
        for b in range(len(bits_used)):
            bits_used[b] += 1 if hsh & (1 << b) else 0
        # print "{{0:0{0:d}b}} : {{0:d}}".format(bits).format(hsh)
    run_time = time() - start
    
    print generator.__class__.__name__
    print bits_used
    print "spread: {}, runtime: {}".format(max(bits_used) - min(bits_used), run_time)
    sys.stdout.flush()