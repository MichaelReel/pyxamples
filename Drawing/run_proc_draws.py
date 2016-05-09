import pygame, sys
from procedural import rand, gradient, knuth, jenkins, wang, builtin, perlin
from pygame.locals import *

# Define the screen dimensions
pixelSize = [4, 4]
gridSize = [100, 75]
displaySize = [gridSize[0] * pixelSize[0], gridSize[1] * pixelSize[1]]

print "disp: {}, grid: {}".format(displaySize, gridSize)

tps = 10

lastTime = pygame.time.get_ticks()
frameTime = 1000 / 30           # milliseconds per frame
pygame.init()

screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Pygame Pixel Draw Example")

done = False

# generator = rand.RandomColour()
# generator = gradient.Gradient(gridSize)
# generator = knuth.Multiplactive(gridSize)
# generator = jenkins.Mix96(gridSize)
# generator = wang.Mix32Bit(gridSize)
# generator = jenkins.Mix32Bit(gridSize)
# generator = wang.MultiplicationHash(gridSize)
# generator = wang.Mix64Bit(gridSize)
md5hash = builtin.Hashing(gridSize, "salt")
# generator = md5hash
generator = perlin.Linear(gridSize, md5hash, 2, 0.485)

pos = [0, 0]
colour = [0, 0, 0]
screen.fill(colour)
    
while not done:
    
    # Set the loop to done on the close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "md5hash: {} -> {}".format(md5hash.min_hash, md5hash.max_hash)
            print "perlin:  {} -> {}".format(generator.min_hash, generator.max_hash)
            print "{}".format(sys.maxint)
            done=True
    
    # Only calculate cells until there aren't any more to calculate
    if pos[1] < gridSize[1]:
        # Get a random color
        colour = generator.getColour(pos)
        
        # Draw the next pixel
        screen.fill(colour, rect=(
            pos[0] * pixelSize[0], pos[1] * pixelSize[1], pixelSize[0], pixelSize[1]))
        
        # increment x / y
        pos[0] += 1
        if pos[0] >= gridSize[0]:
            pos[0] = 0
            pos[1] += 1
    
    # Update the screen only on tick (not every update)
    if (pygame.time.get_ticks() > lastTime + frameTime):
        # Finally update the screen
        pygame.display.flip()
        lastTime += frameTime
    
# Done
pygame.quit()