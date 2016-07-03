import pyglet

window = pyglet.window.Window()
context = window.context
config = context.config

print config.double_buffer
#> 1

print config.stereo
#> 0

print config.sample_buffers
#> 0

platform = pyglet.window.get_platform()
display = platform.get_default_display()
print display
# on windows:
#> <pyglet.canvas.win32.Win32Display object at 0xnnnnnnnnnnnnnnnn>

# on X11 it's possible to get a named display:
# display = platform.get_display('remote:1.0')
# display = platform.get_display(':1.0')

# Displays screen details
for screen in display.get_screens():
    print screen
    # on windows with 1080 monitor:
    #> Win32Screen(x=0, y=0, width=1920, height=1080)
    # on linux (X11):
    #> XlibScreen(screen=0, x=0, y=0, width=1920, height=1080, xinerama=1)

    print screen.get_best_config()
    # on windows:
    #> Win32CanvasConfigARB([...map of properties...])

    # http://pyglet.readthedocs.io/en/latest/programming_guide/context.html#opengl-configuration-options

# Get windows (of the current app? OpenGL?) attached to the display
print display.get_windows()

# Creating a window from a config
# The gl.config function returns the default config template with given changes
config2 = pyglet.gl.Config(alpha_size=8)
window2 = pyglet.window.Window(config=config)

# Creating a context from the best config and a template:
# platform = pyglet.window.get_platform()    # performed above
# display = platform.get_default_display()   # performed above
screen = display.get_default_screen()

template3 = pyglet.gl.Config(alpha_size=8)
config3 = screen.get_best_config(template3)
context3 = config3.create_context(None)
window3 = pyglet.window.Window(context=context3)

# get_best_config can throw NoSuchConfigException, so use try/except to roll back configs:
# template4 = pyglet.gl.Config(sample_buffers=1, samples=4)
# try:
#     config4 = screen.get_best_config(template4)
# except pyglet.window.NoSuchConfigException:
#     template4 = pyglet.gl.Config()
#     config4 = screen.get_best_config(template4)
# window4 = pyglet.window.Window(config=config4)

# It's possible to get a set of valid configs that match certain criteria
# screen = display.get_default_screen()      # performed above
for config5 in screen.get_matching_configs(pyglet.gl.Config()):
    if (
            config5.aux_buffers and 
            config5.accum_red_size and 
            config5.double_buffer and
            config5.alpha_size and
            config5.stencil_size
        ):
        print config5

# It's possible to set attributes on a context's object_space to track a context's state
# Avoid naming attributes pyglet* though as this might interfer with internal modules

context6 = pyglet.gl.get_current_context()
object_space = context6.object_space
object_space.my_game_objects_loaded = True