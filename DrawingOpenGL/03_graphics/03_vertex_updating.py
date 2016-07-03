from pyglet.gl import *
from pyglet.graphics import *

window = pyglet.window.Window()

vertex_list = vertex_list(2, 
    ('v2i/stream', (110, 115, 130, 135)),
    ('c3B/static', (255, 0, 255, 0, 255, 0))
)

vel = [-2, -1, 1, 3]

def update(dt):
    for i, v in enumerate(vertex_list.vertices):
        # Cause vertices to "bounce"
        if ((i % 2 and v >= window.height)
            or (not i % 2 and v >= window.width)):
            vel[i] = -vel[i]
        if ((i % 2 and v <= 0)
            or (not i % 2 and v <= 0)):
            vel[i] = -vel[i]
        # update vertex positions
        vertex_list.vertices[i] = (v + vel[i])

@window.event
def on_draw():
    # This is an immediate mode example, kinda old-school
    # http://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#updating-vertex-data
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    vertex_list.draw(GL_LINES)

# Schedule updates
pyglet.clock.schedule_interval(update, 0.01)

pyglet.app.run()