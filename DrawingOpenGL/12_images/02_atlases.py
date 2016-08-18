import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/image.html#image-sequences-and-atlases

class ImageWindow(pyglet.window.Window):
    def __init__(self, imageFile, rows, cols):
        super(ImageWindow, self).__init__()

        image = pyglet.image.load(imageFile)
        self.frames_grid = pyglet.image.ImageGrid(image, rows, cols)
        self.frame_ind = 0
        self.frame_max = cols * rows

        self.sprites = map(pyglet.sprite.Sprite, self.frames_grid)

        pyglet.clock.schedule_interval(self.update, 0.1)

    def on_draw(self):
        self.clear()
        self.sprites[self.frame_ind].draw()

    def update(self, dt):
        # Animation update
        self.frame_ind = (self.frame_ind + 1) % self.frame_max

window = ImageWindow("explosion.png", 1, 8)
pyglet.app.run()