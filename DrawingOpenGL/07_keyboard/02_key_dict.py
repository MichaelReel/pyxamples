import pyglet
from pyglet.window import key

# http://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html#remembering-key-state

class KeyEventWindow(pyglet.window.Window):
    def __init__(self):
        super(KeyEventWindow, self).__init__()
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.label = pyglet.text.Label("")

    def on_draw(self):
        self.clear()
        self.label.text = "{}".format(self.keys)
        self.label.draw()

window = KeyEventWindow()

pyglet.app.run()