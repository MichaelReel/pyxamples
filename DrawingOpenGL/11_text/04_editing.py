import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/text.html#user-editable-text

class TextWindow(pyglet.window.Window):

    def __init__(self):
        super(TextWindow, self).__init__()
        
        self.batch = pyglet.graphics.Batch()

        document = pyglet.text.document.UnformattedDocument()

        # Layout the text with display properties
        doc_attrs = dict(font_size=12, color=(255,255,255,255))
        document.set_style(start=0, end=0, attributes=doc_attrs)
        layout = pyglet.text.layout.IncrementalTextLayout(
                document=document, 
                width=self.width, 
                height=self.height, 
                multiline=True, 
                wrap_lines=True,
                batch=self.batch)
        caret = pyglet.text.caret.Caret(layout)
        self.push_handlers(caret)

    def on_draw(self):
        self.clear()
        self.batch.draw()

window = TextWindow()
pyglet.app.run()