import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/text.html#loading-system-fonts

# Load System fonts
times = pyglet.font.load('Times New Roman', 16)
times_bold = pyglet.font.load('Times New Roman', 16, bold=True)
times_italic = pyglet.font.load('Times New Roman', 16, italic=True)
times_bold_italic = pyglet.font.load('Times New Roman', 16, bold=True, italic=True)
sans_serif = pyglet.font.load(('Verdana', 'Helvetica', 'Arial'), 16)

# Checking font availability
# Will return "True""
print pyglet.font.have_font('Times New Roman')

# Will return "False""
print pyglet.font.have_font('missing-font-name')

# Pick the default sans-serif font
sans_serif_default = pyglet.font.load(None, 16)

# Load custom fonts
pyglet.font.add_file("WarenhausTypenhebelStandard.ttf")
warenhaus_typenhebel = pyglet.font.load("Warenhaus Typenhebel", 16)

# This will return "false", but the font is still usable (below)
print pyglet.font.have_font('Warenhaus Typenhebel')

# DEMO: Use some fonts to draw some characters
window = pyglet.window.Window()

times_string = pyglet.font.Text(times, "Times New Roman 16pt", 0, window.height - 32)
times_string_bold = pyglet.font.Text(times_bold, "Times New Roman Bold 16pt", 0, window.height - 64)
times_string_italic = pyglet.font.Text(times_italic, "Times New Roman Italic 16pt", 0, window.height - 96)
times_string_bold_italic = pyglet.font.Text(times_bold_italic, "Times New Roman Bold Italic 16pt", 0, window.height - 128)
sans_serif_string = pyglet.font.Text(sans_serif, "Sans Serif", 0, window.height - 160)
sans_serif_default_string =  pyglet.font.Text(sans_serif_default, "Sans Serif Default", 0, window.height - 192)
warenhaus_typenhebel_string = pyglet.font.Text(warenhaus_typenhebel, "Warenhaus Typenhebel", 0, window.height - 224)

@window.event
def on_draw():
    window.clear()
    times_string.draw()
    times_string_bold.draw()
    times_string_italic.draw()
    times_string_bold_italic.draw()
    sans_serif_string.draw()
    sans_serif_default_string.draw()
    warenhaus_typenhebel_string.draw()

pyglet.app.run()