import pyglet
from pyglet.window import key

# http://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html#keyboard-events

class KeyEventWindow(pyglet.window.Window):

    def on_key_press(self, symbol, modifiers):
        print '{} was pressed with modifers: {}'.format(key.symbol_string(symbol), key.modifiers_string(modifiers))

    def on_key_release(self, symbol, modifiers):
        print '{} was released with modifers: {}'.format(key.symbol_string(symbol), key.modifiers_string(modifiers))

    def on_draw(self):
        self.clear()

window = KeyEventWindow()

pyglet.app.run()