from procedural import rand, gradient, knuth, jenkins, wang, builtin, perlin, perlin_ref

width = 200
height = 200

gridSize = (width, height)

# generator = rand.RandomColour()
# generator = gradient.Gradient(gridSize)
# generator = knuth.Multiplactive(gridSize)
# generator = jenkins.Mix96(gridSize)
# generator = wang.Mix32Bit(gridSize)
generator = jenkins.Mix32Bit(gridSize)
# generator = wang.MultiplicationHash(gridSize)
# generator = wang.Mix64Bit(gridSize)
# md5hash = builtin.Hashing(gridSize, "salt")
# generator = md5hash
# generator = perlin.Linear(gridSize, md5hash, 4, 0.485)
# generator = perlin_ref.PerlinRef(gridSize)

bits = 32

bits_used = [0] * bits

for x,y in [(x,y) for x in range(width) for y in range(height)]:
    hsh = generator.getHash(x, y)
    for b in range(len(bits_used)):
        bits_used[b] += 1 if hsh & (1 << b) else 0
    print "{{0:0{0:d}b}} : {{0:d}}".format(bits).format(hsh)
        
print bits_used