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


