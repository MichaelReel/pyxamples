from pyglet.gl import *
from pyglet.graphics import *

window = pyglet.window.Window()

# Batches can be used to group draws into a single draw
# http://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batched-rendering
batch = Batch()

vertex_list = batch.add(2, pyglet.gl.GL_POINTS, None,
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (255, 0, 255, 0, 255, 0))
)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    batch.draw()

pyglet.app.run()