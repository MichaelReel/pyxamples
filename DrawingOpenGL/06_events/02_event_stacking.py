import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/events.html#stacking-event-handlers

window = pyglet.window.Window()

class StackedHandler(object):
    def __init__(self, name, block=False):
        self.name = name
        self.block = block

    def on_key_press(self, symbol, modifiers):
        print "handler %s activated" %  self.name
        return self.block

# Pushed handlers are activated in reverse order
# Four is never run as the return from three is True
window.push_handlers(StackedHandler("four"))
window.push_handlers(StackedHandler("three", block=True))
window.push_handlers(StackedHandler("two"))
window.push_handlers(StackedHandler("one"))

pyglet.app.run()