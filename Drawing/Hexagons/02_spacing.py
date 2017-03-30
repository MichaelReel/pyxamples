"""
Draw a simple hexagon
"""
import sys
import pygame
import math

class Hexagon():
    """Class for drawing a hollow hexagon"""

    def __init__(self, position, radius, color, line = 1, flat = True):
        self.center = position
        self.size = radius
        self.color = color
        self.line = line
        self.rot = 0 if flat else 30

    def hex_corner(self, i):
        """Get corner"""
        angle_deg = 60.0 * i + self.rot
        angle_rad = math.pi / 180 * angle_deg
        return (self.center[0] + self.size * math.cos(angle_rad),
                self.center[1] + self.size * math.sin(angle_rad))

    def draw(self, surface):
        """Draw a hexagon"""
        points = [self.hex_corner(x) for x in range(6)]
        pygame.draw.polygon(surface, self.color, points, self.line)


class GridDrawer():
    """Class that draws a hexagon grid when run"""

    def __init__(self, screen_size, hex_size):
        # Bring up
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.done = False
        self.init_hexagons(screen_size, hex_size)
        self.font = pygame.font.Font(None, 20)

    def init_hexagons(self, screen_size, radius):
        # Find all the "centers" that will fit on the screen
        centers = self.centers_visible(screen_size, radius)
        color = (255, 0, 255)
        self.hexagons = {c: Hexagon(centers[c], radius, color) for c in centers.keys()}

    @staticmethod
    def centers_visible(screen_size, radius):
        """Return a mapping of on screen cords from their axial coords to their surface coords"""
        width = radius * 2
        height = math.sqrt(3) / 2 * width
        spacing_x = width * 3 / 4
        spacing_y = height
        orig_x = screen_size[0] / 2
        orig_y = screen_size[1] / 2

        col_limit = orig_x / width + 1
        row_limit = orig_y * 2 / int(height)

        coords = {}

        for col in range(-col_limit, col_limit + 1):
            for row in range(-row_limit, row_limit + 1):
                screen_coords = GridDrawer.axial_to_screen((col, row), (spacing_x, spacing_y), (orig_x, orig_y))
                if GridDrawer.coords_in_surface(screen_coords, screen_size):
                    coords[(col, row)] = (screen_coords)

        print coords
        return coords

    @staticmethod
    def axial_to_screen((col, row), (width, height), (orig_x, orig_y)):
        x = col * width + orig_x
        y = (row * height + orig_y) + (col * height / 2)
        return (x, y)

    @staticmethod
    def coords_in_surface((x, y), (width, height)):
        return x >= 0 and x <= width and y >= 0 and y <= height 


    def draw_hexagons(self):
        for hex in self.hexagons.keys():
            self.hexagons[hex].draw(self.screen)
            coord_str = "{}".format(hex)
            coord_text = self.font.render(coord_str, 0, (255, 127, 255))
            text_pos = (self.hexagons[hex].center[0] - self.font.size(coord_str)[0] / 2, self.hexagons[hex].center[1] - self.font.size(coord_str)[1] / 2)
            self.screen.blit(coord_text, text_pos)

    def run(self):
        """Draw the screen with a hexagon grid"""
        # Loop
        while not self.done:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
            
            # Draw
            self.draw_hexagons()
            pygame.display.update()

        # Tear down
        pygame.quit()
        sys.exit()

drawer = GridDrawer((800, 600), 50)
drawer.run()