import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/text.html#the-document-layout-model

content = []
formatting = []

formatting.append(dict(font_size=10, color=(255,255,255,255)))
content.append('''\
This is the way the world ends
''')
formatting.append(dict(font_size=12, color=(255,0,255,255)))
content.append('''\
This is the way the world ends
''')
formatting.append(dict(font_size=14, color=(255,255,0,255)))
content.append('''\
This is the way the world ends
''')
formatting.append(dict(font_size=16, color=(0,255,255,255)))
content.append('''\
Not with a bang but a whimper.
''')

class TextWindow(pyglet.window.Window):

    def __init__(self):
        super(TextWindow, self).__init__()

        document = pyglet.text.document.FormattedDocument()

        # Insert all the contents above with the appropriate formatting
        for i in range(len(content)):
            document.insert_text(len(document.text), content[i], attributes=formatting[i])
        
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