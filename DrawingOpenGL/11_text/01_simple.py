import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/text.html#simple-text-rendering

class TextWindow(pyglet.window.Window):

    def __init__(self):
        super(TextWindow, self).__init__()

        # Draw "Hello World!" in the top have of the screen
        self.label1 = pyglet.text.Label('Hello, world',
                        font_name='Times New Roman',
                        font_size=36,
                        x=self.width//2, y=self.height // 4 * 3,
                        anchor_x='center', anchor_y='center')

        # Draw "Hello World!" in middle of the screen
        self.label2 = pyglet.text.HTMLLabel(
                        '<font face="Times New Roman" size="4" color="white">Hello, <i>world</i></font>',
                        x=self.width//2, y=self.height//2,
                        anchor_x='center', anchor_y='center')
        # The following HTML elements are supported:
        # B BLOCKQUOTE BR CENTER CODE DD DIR DL EM FONT H1 H2 H3 H4 H5 H6 I IMG KBD
        # LI MENU OL P PRE Q SAMP STRONG SUB SUP TT U UL VAR

    def on_draw(self):
        self.clear()
        self.label1.draw()
        self.label2.draw()

window = TextWindow()
pyglet.app.run()