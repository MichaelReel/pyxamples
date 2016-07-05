import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#creating-a-window

# window's can be set to display later
window = pyglet.window.Window(visible=False)
# ... perform some additional initialisation
window.set_visible()

# Get platform/display/screen for further examples
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[0]
config = pyglet.gl.Config()
template = pyglet.gl.Config(alpha_size=8)

# Window context cannot be changed once created
# But context can be supplied in various ways

# Supply a template Config using the config argument
# Custom configs appear to have issues with some environments
# Win 8 64x, Python 2.7.11, pyglet 1.2.0 - 1.2.4 : Doesn't work
# Win 8 64x, Python 2.7.11, pyglet 1.1.4         : Works
# Win 7 64x, Python 2.7.11, pyglet 1.2.4         : Works
window1 = pyglet.window.Window(config=config)

# Specify a Screen using the screen argument
window2 = pyglet.window.Window(screen=screen)

# Specify a Display using the display argument
window3 = pyglet.window.Window(display=display)

# Supply a complete Config obtained from a Screen using the config argument
config4 = screen.get_best_config(template)
window4 = pyglet.window.Window(config=config4)

# Supply an already-created Context using the context argument
context5 = config4.create_context(None)
window5 = pyglet.window.Window(context=context5)


