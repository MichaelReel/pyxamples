import pyglet
from pyglet.window import mouse, key

# http://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html#mouse-events

class MouseEventWindow(pyglet.window.Window):
    def __init__(self):
        super(MouseEventWindow, self).__init__()

    def on_mouse_motion(self, x, y, dx, dy):
        print "motion(x={}, y={}, dx={}, dy={})".format(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        print "on_mouse_press(x={}, y={}, button={}, modifiers={})".format(
                x, y, mouse.buttons_string(button), key.modifiers_string(modifiers))

    def on_mouse_release(self, x, y, button, modifiers):
        print "on_mouse_release(x={}, y={}, button={}, modifiers={})".format(
                x, y, mouse.buttons_string(button), key.modifiers_string(modifiers))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print "on_mouse_release(x={}, y={}, dx={}, dy={}, button={}, modifiers={})".format(
                x, y, dx, dy, mouse.buttons_string(buttons), key.modifiers_string(modifiers))

    def on_mouse_enter(self, x, y):
        print "on_mouse_enter(x={}, y={})".format(x, y)

    def on_mouse_leave(self, x, y):
        print "on_mouse_leave(x={}, y={})".format(x, y)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        print "on_mouse_scroll(x={}, y={}, scroll_x={}, scroll_y={})".format(
                x, y, scroll_x, scroll_y)

    def on_draw(self):
        self.clear()

window = MouseEventWindow()

pyglet.app.run()