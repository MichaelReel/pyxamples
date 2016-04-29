import pygame
import random
from pygame.locals import *

# Define the screen dimensions
size = [400, 300]
tps = 10

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Line Draw Example")

done = False
clock = pygame.time.Clock()

# define the strobe colours
r = 128
g = 128
b = 128

d = 5 # diff speed
min = 0
max = 255

while not done:
    
    # This limits the while loop to a max of _tps_ times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(tps)
    
    # Set the loop to done on the close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    screen.fill((r, g, b))
    
    r += random.randint(-d, d)
    g += random.randint(-d, d)
    b += random.randint(-d, d)
    r = sorted((min, r, max))[1]
    g = sorted((min, g, max))[1]
    b = sorted((min, b, max))[1]
    
    # Finally update the screen
    pygame.display.flip()
    
# Done
pygame.quit()