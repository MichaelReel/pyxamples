import pyglet
from pyglet.window import key

# http://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#size-and-position

# Window size can be set on creation, and windows can be set as resizable
window = pyglet.window.Window(width=800, height=600, resizable=True)

# If resizable, min and max boundaries can be set
window.set_minimum_size(320, 200)
window.set_maximum_size(1024, 768)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        # Pressing <space> will set the screen size to 800x600
        window.set_size(800, 600)
    # Move the window using arrowkeys (coords are from top left)
    x, y = window.get_location()
    if symbol == key.UP:
        y -= 20
    if symbol == key.DOWN:
        y += 20
    if symbol == key.LEFT:
        x -= 20
    if symbol == key.RIGHT:
        x += 20
    window.set_location(x, y)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()