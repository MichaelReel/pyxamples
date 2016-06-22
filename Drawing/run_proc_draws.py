import pygame, sys, os, time
from procedural import rand, gradient, knuth, jenkins, wang, builtin, perlin, perlin_ref
from pygame.locals import *

# Define the screen dimensions
pixelSize = [1, 1]
gridSize = [400, 300]
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
# md5hash = builtin.Hashing(gridSize, "salt")
# generator = md5hash
# generator = perlin.Linear(gridSize, md5hash, 4, 0.485)
# generator = perlin_ref.PerlinRef(gridSize)
# generator = perlin_ref.SeededPerlinRef(gridSize, "seed")
# generator = perlin_ref.ColourPerlin(gridSize, "mlem", (11, 13, 17))
# generator = perlin_ref.PerlinBlobs(gridSize, "salt", 5, 128, 24)
# generator = perlin_ref.PerlinContours(gridSize, "seed")
generator = perlin_ref.PerlinTopography(gridSize, "seed")

pos = [0, 0]
colour = [0, 0, 0]

screen.fill(colour)

while not done:
    # Set the loop to done on the close event
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.KEYUP:
            # Parse key inputs
            if event.key == pygame.K_F1:
                # print "md5hash: {} -> {}".format(md5hash.min_hash, md5hash.max_hash)
                print "perlin:  {} -> {}".format(generator.min_hash, generator.max_hash)
                print "{}".format(sys.maxint)
            elif event.key == pygame.K_F2:
                scriptPath = os.path.dirname(os.path.realpath(__file__))
                filePath = scriptPath + "/TESTSAVE_" + time.strftime("%Y%m%d_%H%M%S") + ".png"
                print "save to {}".format(filePath)
                pygame.image.save(screen, filePath)
            
    # Only calculate cells until there aren't any more to calculate
    if pos[1] < gridSize[1]:
        # Get a random color
        colour = generator.getColour(pos)
        
        # Draw the next pixel
        try:
            screen.fill(colour, rect=(
                pos[0] * pixelSize[0], pos[1] * pixelSize[1], pixelSize[0], pixelSize[1]))
        except TypeError:
            # Report error on STDOUT and colour errored pixel magenta
            print "colour: {}, pos: {}, ERROR: {}".format(colour, pos, TypeError)
            screen.fill((255,0,255), rect=(
                pos[0] * pixelSize[0], pos[1] * pixelSize[1], pixelSize[0], pixelSize[1]))
        
        # increment x / y
        pos[0] += 1
        if pos[0] >= gridSize[0]:
            pos[0] = 0
            pos[1] += 1
    
    # Update the screen only on tick (not every update)
    if (pygame.time.get_ticks() > lastTime + frameTime):
        # Finally update the screen
        sys.stdout.flush()
        pygame.display.flip()
        lastTime += frameTime
    
# Done
pygame.quit()