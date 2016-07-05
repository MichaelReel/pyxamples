import pyglet
from pyglet.window import mouse, key

# http://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html#changing-the-mouse-cursor

class MouseEventWindow(pyglet.window.Window):
    def __init__(self):
        super(MouseEventWindow, self).__init__()
        # It's possible to set the cursor as invisible
        #> self.set_mouse_visible(False)

        # Or use a different system status cursor
        #> cursor = self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR)
        #> self.set_mouse_cursor(cursor)

        # Or use an image for the cursor
        image = pyglet.image.load('../icons/32x32.png')
        # Set "hot" spot to the top left corner
        cursor = pyglet.window.ImageMouseCursor(image, 0, 32)
        #  TODO: This only seems to be drawn at the mouse_enter position
        self.set_mouse_cursor(cursor)

    def on_mouse_enter(self, x, y):
        print "on_mouse_enter(x={}, y={})".format(x, y)

    def on_mouse_leave(self, x, y):
        print "on_mouse_leave(x={}, y={})".format(x, y)

    def on_draw(self):
        self.clear()

window = MouseEventWindow()

pyglet.app.run()