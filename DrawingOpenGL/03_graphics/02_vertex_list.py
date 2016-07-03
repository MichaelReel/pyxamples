from pyglet.gl import *
from pyglet.graphics import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window()

# vertex lists can be setup in advance, sometimes avoiding immediate mode
# This will setup a magenta pixel at (10, 15)
# and a green pixel at (30, 35)
# This is similar to draw, except the primitive isn't included
vertex_list = vertex_list(2, 
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (255, 0, 255, 0, 255, 0)),
)

@window.event
def on_draw():
    # http://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#vertex-lists
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw pre-created vertices, primitive mode is given here
    vertex_list.draw(GL_POINTS)

pyglet.app.run()