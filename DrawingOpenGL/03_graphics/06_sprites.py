from pyglet.gl import *
from pyglet.graphics import *
from math import cos, sin, radians

# http://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batches-and-groups-in-other-modules

image = pyglet.image.load('../image.png')

window = pyglet.window.Window()
batch = Batch()

sprites = [pyglet.sprite.Sprite(image, batch=batch) for i in range(100)]

# Spread all the sprites out in an arc, 1 degree per sprite
def update(dt):
    for theta, s in enumerate(sprites):
        s.x += cos(radians(theta))
        s.y += sin(radians(theta))

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    batch.draw()

# Schedule updates
pyglet.clock.schedule_interval(update, 0.1)

pyglet.app.run()