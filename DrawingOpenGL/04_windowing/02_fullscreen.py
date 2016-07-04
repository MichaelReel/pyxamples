import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#fullscreen-windows

fs = False

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[0]
window = pyglet.window.Window(fullscreen=fs, screen=screen)

@window.event
def on_key_press(symbol, modifiers):
    # Any keypress will switch the fullscreen state
    global fs
    fs = not fs
    window.set_fullscreen(fs)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()