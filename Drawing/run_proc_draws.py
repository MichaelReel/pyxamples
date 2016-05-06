import pygame
from procedural import rand, gradient, knuth, jenkins
from pygame.locals import *

# Define the screen dimensions
size = [400, 300]
tps = 10

lastTime = pygame.time.get_ticks()
frameTime = 1000 / 30           # milliseconds per frame
pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Pixel Draw Example")

done = False

#generator = rand.RandomColour()
#generator = gradient.Gradient(size)
#generator = knuth.Multiplactive(size)
generator = jenkins.Mix96(size)

pos = [0, 0]
colour = [0, 0, 0]
screen.fill(colour)
    
while not done:
    
    # Set the loop to done on the close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    # Get a random color
    colour = generator.getColour(pos)
    
    # Draw the next pixel
    screen.set_at(pos, colour)
    
    # increment x / y
    pos[0] += 1
    if pos[0] >= size[0]:
        pos[0] = 0
        pos[1] += 1
    
    # Update the screen only on tick (not every update)
    if (pygame.time.get_ticks() > lastTime + frameTime):
        # Finally update the screen
        pygame.display.flip()
        lastTime += frameTime
    
# Done
pygame.quit()