import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#appearance

icon1 = pyglet.image.load('../icons/64x64.png')
icon2 = pyglet.image.load('../icons/32x32.png')

# Window in default style with custom title and custom icon
window = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption="Main Window")
window.set_icon(icon1, icon2)
#> window.minimize()

# Dialog in dialog window style (default icon) and custom title
dialog = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_DIALOG, caption="Dialog Window")
# Although dialog windows don't have the minimize button, they may still be minimized using task bar/manager
# dialogs can also be minimized via code
#> dialog.minimize()

# Tool window (no icon) with custom title, may not appear on task bar/manager
tool = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_TOOL, caption="Tool Window")
# tool style windows can only be minimized via code 
#> tool.minimize()


pyglet.app.run()