"""
Draw a simple hexagon grid and allow placing multiple chips
"""
import sys
import pygame
import math
import operator

class Hexagon():
    """Class for drawing a hollow hexagon"""

    def __init__(self, position, radius, color, line = 2):
        self.center = position
        self.radius = radius
        self.color = color
        self.line = line

    def hex_corner(self, i):
        """Get corner"""
        angle_deg = 60.0 * i
        angle_rad = math.pi / 180 * angle_deg
        return (self.center[0] + self.radius * math.cos(angle_rad),
                self.center[1] + self.radius * math.sin(angle_rad))

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
        if not hasattr(self, 'selection_hexagon'):
            self.selection_hexagon = Hexagon(hexagon.center, hexagon.radius, hexagon.color)
        self.selection_hexagon.center = tuple(map(operator.add, self.hexagon.center, (0, -12)))

    def draw(self, surface):
        """Draw the chip on top of the hexagon"""
        if hasattr(self, 'hexagon') and self.hexagon:
            pos = tuple(map(operator.add, self.hexagon.center, self.offset))
            surface.blit(self.image, pos)

    def draw_outline(self, surface):
        """Draw the outline of the chip if it's placed"""
        if hasattr(self, 'selection_hexagon') and self.selection_hexagon:
            self.selection_hexagon.draw(surface, (200, 200, 0))

    def is_mouse_on(self, mouse_pos):
        if hasattr(self, 'hexagon') and self.hexagon:
            vector = tuple(map(operator.sub, self.hexagon.center, mouse_pos))
            magnatude = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
            return magnatude < self.hexagon.radius

class PlusChip(Chip):
    """Class for drawing a chip with a plus on it"""

    def __init__(self):
        icon = pygame.image.load("images/Plus.png").convert_alpha()
        self.image = pygame.image.load("images/BlankChip.png").convert_alpha()
        self.image.blit(icon, (0,0))
        self.offset = (-49, -55)

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
        # setup draw_gui
        self.init_gui()
        # Create chips
        self.init_chips()
        self.cursor = None

    def init_hexagons(self, screen_size, radius):
        # Find all the "centers" that will fit on the screen
        centers = self.centers_visible(screen_size, radius)
        color = (200, 200, 200)
        self.hexagons = {c: Hexagon(centers[c], radius, color) for c in centers.keys()}

    def init_chips(self):
        self.chips = []
        # put chip at 0,0
        start_chip = self.create_chip()
        start_chip.set_grid_pos(self.hexagons[(0,0)])

    def create_chip(self):
        new_chip = Chip()
        new_chip.set_grid_pos(self.add_chip.hexagon)
        self.chips.append(new_chip)
        self.selected_chip = new_chip
        return new_chip

    def init_gui(self):
        self.add_chip = (PlusChip())
        self.add_chip.set_grid_pos(Hexagon((50, 50), 50, (0,0,0)))

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

    def clicked_chip(self, mouse_pos):
        for chip in self.chips:
            if chip.is_mouse_on(mouse_pos):
                return chip

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
        # TODO: sort chips from top of screen down before drawing
        for chip in self.chips:
            chip.draw(self.screen)

    def draw_gui(self):
        self.add_chip.draw(self.screen)
        self.selected_chip.draw_outline(self.screen)

    def run(self):
        """Draw the screen with a hexagon grid"""
        move = (0,0)

        # Loop
        while not self.done:
            # Clear Events
            click = None
            selected = None

            # Events
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    # Check if we're on the gui first
                    if self.add_chip.is_mouse_on(pos):
                        selected = self.add_chip
                    # Then check if we're on an existing chip
                    if not selected:
                        selected = self.clicked_chip(pos)
                    # Otherwise check the grid pos
                    if not selected:
                        click = self.screen_to_axial(pos)
                if event.type == pygame.MOUSEMOTION:
                    move_a = self.screen_to_axial(pos)

            # Update
            if selected:
                if selected == self.add_chip:
                    self.create_chip()
                else:
                    self.selected_chip = selected
            if click and self.hexagons.has_key(click):
                self.selected_chip.set_grid_pos(self.hexagons[click])

            # Draw
            self.screen.fill((255,255,255))
            self.draw_hexagons()
            self.draw_chips()
            self.draw_gui()

            # Draw debug
            if self.hexagons.has_key(move_a):
                self.hexagons[move_a].draw(self.screen, (255, 150, 150))

            pygame.display.update()

        # Tear down
        pygame.quit()
        sys.exit()

drawer = GridDrawer((800, 600), 50)
drawer.run()