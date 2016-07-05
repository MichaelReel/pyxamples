import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/events.html#setting-event-handlers

class EventWindow(pyglet.window.Window):
    def __init__(self):
        super(EventWindow, self).__init__(resizable=True)
        self.label = pyglet.text.Label('Hello, world!')

    def on_draw(self):
        self.clear()
        self.label.draw()

    def on_resize(self, width, height):
        print "resized to ({},{})".format(width, height)

    def on_mouse_enter(self, x, y):
        print "Mouse enter @ ({},{})".format(x, y)

    def on_mouse_leave(self, x, y):
        print "Mouse leave @ ({},{})".format(x, y)

    # More events listed at:
    # https://pythonhosted.org/pyglet/api/pyglet.window.Window-class.html#section-Events

window = EventWindow()

pyglet.app.run()
