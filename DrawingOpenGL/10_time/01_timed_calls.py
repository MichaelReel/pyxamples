import pyglet, math

# http://pyglet.readthedocs.io/en/latest/programming_guide/time.html#calling-functions-periodically

class FPSWindow(pyglet.window.Window):
    def __init__(self):
        super(FPSWindow, self).__init__()
        self.label = pyglet.text.Label('0 FPS')

        pyglet.clock.schedule_interval(self.update, 0.01)
        # OR use schedule(function) to set the rate as fast as possible
        # Also, schedule_once(function, seconds) can be used for one off calls

        # Instead of update below, pyglet has a built-in fps widget:
        self.fps_display = pyglet.clock.ClockDisplay()
        
        # Animation setup
        image        = pyglet.image.load('../icons/32x32.png')
        self.batch   = pyglet.graphics.Batch()
        self.sprites = [pyglet.sprite.Sprite(image, batch=self.batch) for i in range(90)]
    
    def on_draw(self):
        self.clear()
        # Draw sprites
        self.batch.draw()
        # This draws the 'manual' fps counter "xxx.x FPS"
        self.label.draw()
        # The draws the larger, translucent counter
        self.fps_display.draw()

    # pyglet.app.run() doesn't return until the windows have been closed
    # so periodic functions need to be scheduled using schedule_interval
    def update(self, dt):
        # Animation update
        for theta, s in enumerate(self.sprites):
            s.x += math.cos(math.radians(theta))
            s.y += math.sin(math.radians(theta))
        # 'manual' FPS counter update
        self.label.text = "{:05.1f} FPS".format(pyglet.clock.get_fps())

window = FPSWindow()
pyglet.app.run()



