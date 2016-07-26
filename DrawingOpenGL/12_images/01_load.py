import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/image.html#loading-an-image

class ImageWindow(pyglet.window.Window):
    def __init__(self, imageFile):
        super(ImageWindow, self).__init__()

        stream = open(imageFile, 'rb')
        image = pyglet.image.load(imageFile, file=stream)
        self.sprite = pyglet.sprite.Sprite(image)

        # Or just: self.image = pyglet.image.load(imageFile)
        # The version above uses a stream and in the filename in load
        # is just used as a decoder (png) hint.

        # For supported file types check:
        # http://pyglet.readthedocs.io/en/latest/programming_guide/image.html#supported-image-formats

    def on_draw(self):
        self.clear()
        self.sprite.draw()


window = ImageWindow("../image.png")
pyglet.app.run()