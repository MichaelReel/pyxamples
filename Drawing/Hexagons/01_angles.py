"""
Draw a simple hexagon
"""
import sys
import pygame
import math

class HexDrawer():
    """Class that draws a hexagon when run"""

    def hex_corner(self, i):
        """Get corner"""
        angle_deg = 60 * i  
        angle_rad = math.pi / 180 * angle_deg
        return (self.center[0] + self.size * math.cos(angle_rad),
                self.center[1] + self.size * math.sin(angle_rad))

    def draw_hex(self):
        """Draw a hexagon"""
        points = [self.hex_corner(x) for x in range(6)]
        pygame.draw.polygon(self.screen, (255, 0, 255), points)

    def __init__(self, screen_size, hex_size):
        # Bring up
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.done = False
        self.size = hex_size
        self.center = (screen_size[0] / 2, screen_size[1] / 2)

    def run(self):
        """Draw the screen with a hexagon"""
        # Loop
        while not self.done:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
            
            # Draw
            self.draw_hex()
            pygame.display.update()

        # Tear down
        pygame.quit()
        sys.exit()

drawer = HexDrawer((400, 300), 50)
drawer.run()