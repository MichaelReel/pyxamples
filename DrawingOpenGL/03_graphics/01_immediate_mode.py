from pyglet.gl import *
from pyglet.graphics import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window()

@window.event
def on_draw():
    # This is an immediate mode example, kinda old-school
    # http://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#drawing-primitives
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw 2 2d points at (10,15) and (30, 35) from the bottom left
    draw(2, GL_POINTS, ('v2i', (10, 15, 30, 35)))

    # Draw 2 3d points at (110, 115, 0) and (130, 135, 0)
    draw(2, GL_POINTS, ('v3f', (110.0, 115.0, 0.0, 130.0, 135.0, 0.0)))

    # Draw 2 indexed 2d points at (210, 215) and (230, 235)
    draw_indexed(2, GL_POINTS, [0, 1], ('v2i', (210, 215, 230, 235)) )

    # Use indexed drawing to draw 2 triangles (1 50x50 square):
    # (200, 100), (250, 100), (250, 150) and
    # (200, 100), (250, 150), (200, 150)
    draw_indexed(4, GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (200, 100,
                250, 100,
                250, 150,
                200, 150))
    )

    # draw can also apply colour to points
    # This will draw a magenta pixel at (310, 315)
    # and a green pixel at (330, 335)
    draw(2, GL_POINTS,
    ('v2i', (310, 315, 330, 335)),
    ('c3B', (255, 0, 255, 0, 255, 0))
)

pyglet.app.run()