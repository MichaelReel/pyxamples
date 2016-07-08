import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/text.html#the-document-layout-model

goodbye = '''\
Goodbye cruel world
I'm leaving you today
Goodbye
Goodbye
Goodbye
Goodbye all you people
There's nothing you can say
To make me change
My mind
Goodbye.
'''

class TextWindow(pyglet.window.Window):

    def __init__(self):
        super(TextWindow, self).__init__()
        
        # Decode the string to a UnformattedDocument
        document = pyglet.text.decode_text(goodbye)

        # It's possible to create documents from HTML too:
        #> document = pyglet.text.decode_html('Hello, <b>world</b>')

        # Layout the text with display properties
        doc_attrs = dict(font_size=12, color=(255,255,255,255))
        document.set_style(start=0, end=0, attributes=doc_attrs)
        self.layout = pyglet.text.layout.TextLayout(
                document=document, 
                width=self.width, 
                height=self.height, 
                multiline=True, 
                wrap_lines=True)

    def on_draw(self):
        self.clear()
        self.layout.draw()

window = TextWindow()
pyglet.app.run()