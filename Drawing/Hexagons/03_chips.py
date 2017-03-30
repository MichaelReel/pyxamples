"""
Draw a simple hexagon grid and allow placing a chip
"""
import sys
import pygame
import math
import operator

class Hexagon():
    """Class for drawing a hollow hexagon"""

    def __init__(self, position, radius, color, line = 2):
        self.center = position
        self.size = radius
        self.color = color
        self.line = line

    def hex_corner(self, i):
        """Get corner"""
        angle_deg = 60.0 * i
        angle_rad = math.pi / 180 * angle_deg
        return (self.center[0] + self.size * math.cos(angle_rad),
                self.center[1] + self.size * math.sin(angle_rad))

    def draw(self, surface, color = None):
        """Draw a hexagon"""
        if not color:
            color = self.color
        points = [self.hex_corner(x) for x in range(6)]
        pygame.draw.polygon(surface, color, points, self.line)

class Chip():
    """Class for drawing a chip on the board"""

    def __init__(self):
        icon = pygame.image.load("images/Bee.png").convert_alpha()
        self.image = pygame.image.load("images/BlankChip.png").convert_alpha()
        self.image.blit(icon, (0,0))
        self.offset = (-49, -55)

    def set_grid_pos(self, hexagon):
        self.hexagon = hexagon

    def draw(self, surface):
        """Draw the chip on top of the hexagon"""
        if (self.hexagon):
            pos = tuple(map(operator.add, self.hexagon.center, self.offset))
            surface.blit(self.image, pos)

class GridDrawer():
    """Class that draws a hexagon grid when run"""

    def __init__(self, screen_size, hex_size):
        # Bring up
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.done = False
        # create grid
        self.init_hexagons(screen_size, hex_size)
        self.font = pygame.font.Font(None, 20)
        # put chip at 0,0
        self.chip = Chip()
        self.chip.set_grid_pos(self.hexagons[(0,0)])
        # setup cursor
        self.cursor = None

    def init_hexagons(self, screen_size, radius):
        # Find all the "centers" that will fit on the screen
        centers = self.centers_visible(screen_size, radius)
        color = (200, 200, 200)
        self.hexagons = {c: Hexagon(centers[c], radius, color) for c in centers.keys()}

    def centers_visible(self, screen_size, radius):
        """Return a mapping of on screen cords from their axial coords to their surface coords"""
        width = radius * 2
        height = math.sqrt(3) / 2 * width

        self.size = radius
        self.spacing_x = width * 3 / 4
        self.spacing_y = height
        self.orig_x = screen_size[0] / 2
        self.orig_y = screen_size[1] / 2

        col_limit = self.orig_x / width + 1
        row_limit = self.orig_y * 2 / int(height)

        coords = {}

        for col in range(-col_limit, col_limit + 1):
            for row in range(-row_limit, row_limit + 1):
                screen_coords = self.axial_to_screen((col, row))
                # screen_coords = self.hex_to_pixel((col, row))
                if GridDrawer.coords_in_surface(screen_coords, screen_size):
                    coords[(col, row)] = (screen_coords)

        # print coords
        return coords

    def axial_to_screen(self, (col, row)):
        """Return the center of the axial position as a screen position"""
        x = col * self.spacing_x + self.orig_x
        y = (row * self.spacing_y + self.orig_y) + (col * self.spacing_y / 2)
        return (x, y)

    def screen_to_axial(self, (x, y)):
        """Find the nearest axial center for the given screen position""" 
        col_f = (x - (self.orig_x - self.spacing_x / 2)) / self.spacing_x
        row = round ( (y - (col_f * self.spacing_y / 2) - self.orig_y) / self.spacing_y )
        col = round (col_f)
        return (int(col), int(row))

    @staticmethod
    def coords_in_surface((x, y), (width, height)):
        return x >= 0 and x <= width and y >= 0 and y <= height 

    def draw_hexagons(self):
        for hex in self.hexagons.keys():
            self.hexagons[hex].draw(self.screen)
            coord_str = "{}".format(hex)
            coord_text = self.font.render(coord_str, 0, (220, 220, 220))
            font_mid = map(operator.div, self.font.size(coord_str), (2, 2))
            text_pos = tuple(map(operator.sub, self.hexagons[hex].center, font_mid))
            self.screen.blit(coord_text, text_pos)

    def draw_chips(self):
        self.chip.draw(self.screen)

    def run(self):
        """Draw the screen with a hexagon grid"""
        move = (0,0)

        # Loop
        while not self.done:
            # Clear Events
            click = None

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    click = self.screen_to_axial(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEMOTION:
                    move_a = self.screen_to_axial(pygame.mouse.get_pos())

            # Update
            if click and self.hexagons.has_key(click):
                self.chip.set_grid_pos(self.hexagons[click])
            
            # Draw
            self.screen.fill((255,255,255))
            self.draw_hexagons()
            self.draw_chips()

            # Draw debug
            if self.hexagons.has_key(move_a):
                self.hexagons[move_a].draw(self.screen, (255, 150, 150))

            pygame.display.update()

        # Tear down
        pygame.quit()
        sys.exit()

drawer = GridDrawer((800, 600), 50)
drawer.run()