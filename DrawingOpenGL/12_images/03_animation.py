import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/image.html#animations

class ImageWindow(pyglet.window.Window):
    def __init__(self, imageFile, rows, cols):
        super(ImageWindow, self).__init__()

        animation = pyglet.image.load_animation(imageFile)
        bin = pyglet.image.atlas.TextureBin()
        animation.add_to_texture_bin(bin)
        self.sprite = pyglet.sprite.Sprite(animation)

    def on_draw(self):
        self.clear()
        self.sprite.draw()

window = ImageWindow("strobe.gif", 1, 8)
pyglet.app.run()