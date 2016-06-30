import pyglet
from pyglet.gl import *
from pyglet.window import key

try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4,
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config, vsync=False) # "vsync=False" to check the framerate
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)

image = pyglet.image.load('alex_holkner/tristam_macdonald/game_of_life_init.png')

label = pyglet.text.Label('Hello, World!!',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height//2,
                      anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    image.get_texture().blit((window.width - image.width ) //2, (window.height - image.height) //2)
    label.draw()

pyglet.app.run()