import pygame
import random
from pygame.locals import *

# Define the screen dimensions
size = [400, 300]
tps = 10

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Pixel Draw Example")

done = False

min = 0
max = 255

pos = [0, 0]
colour = [0, 0, 0]
screen.fill(colour)
    
while not done:
    
    # Set the loop to done on the close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    # Get a random color
    for i in range(len(colour)):
        colour[i] = random.randint(min, max)
    
    # Draw the next pixel
    screen.set_at(pos, colour)
    
    # increment x / y
    pos[0] += 1
    if pos[0] >= size[0]:
        pos[0] = 0
        pos[1] += 1
    
    # check we're not done
    if pos[0] >= size[0] and pos[1] >= size[1]:
        done=True
    
    # Finally update the screen
    pygame.display.flip()
    
# Done
pygame.quit()