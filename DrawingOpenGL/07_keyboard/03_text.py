import pyglet
from pyglet.window import key

# http://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html#text-and-motion-events

class KeyEventWindow(pyglet.window.Window):
    def __init__(self):
        super(KeyEventWindow, self).__init__()
        self.label = pyglet.text.Label("")

    def on_text(self, text):
        self.label.text = text

    def on_text_motion(self, motion):
        print 'text motion: {}'.format(key.motion_string(motion))

    def on_draw(self):
        self.clear()
        self.label.draw()
        
window = KeyEventWindow()

pyglet.app.run()