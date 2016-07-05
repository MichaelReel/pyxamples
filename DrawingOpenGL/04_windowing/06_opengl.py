import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#windows-and-opengl-contexts

class SingleBufferWindow(pyglet.window.Window):
    def __init__(self):
        # Turn off double_buffering

        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        screen = display.get_screens()[0]
        template = pyglet.gl.Config(double_buffer=True)
        config = screen.get_best_config(template)

        # Custom configs appear to have issues with some environments
        # Win 8 64x, Python 2.7.11, pyglet 1.2.0 - 1.2.4:  Doesn't work
        # Win 8 64x, Python 2.7.11, pyglet 1.1.4  :  Works

        super(SingleBufferWindow, self).__init__(
            config=config,
            caption="Single Buffer Window",
            )

        self.label = pyglet.text.Label('Hello, world!')

        # Schedule updates
        pyglet.clock.schedule_interval(self.update, 0.1)
    
    # Useful for attaching handlers as soon as the window is created
    def on_draw(self):
        self.clear()
        self.label.draw()

    def update(self, dt):
        self.label.text = 'Hello, world! %s' % dt

class VsyncOffWindow(pyglet.window.Window):
    def __init__(self):

        # Disable Vertical Sync
        super(VsyncOffWindow, self).__init__(
            vsync=False,
            caption="Vsync Off Window",
            )

        self.label = pyglet.text.Label('Hello, world!')

        # Schedule updates
        pyglet.clock.schedule_interval(self.update, 0.1)
    
    # Useful for attaching handlers as soon as the window is created
    def on_draw(self):
        self.clear()
        self.label.draw()

    def update(self, dt):
        self.label.text = 'Hello, world! %s' % dt


class NormalWindow(pyglet.window.Window):
    def __init__(self):

        # Disable Vertical Sync
        super(NormalWindow, self).__init__(
            caption="Double Buffer Vsync Window",
            )

        self.label = pyglet.text.Label('Hello, world!')

        # Schedule updates
        pyglet.clock.schedule_interval(self.update, 0.1)
    
    # Useful for attaching handlers as soon as the window is created
    def on_draw(self):
        self.clear()
        self.label.draw()

    def update(self, dt):
        self.label.text = 'Hello, world! %s' % dt

window1 = SingleBufferWindow()
window2 = VsyncOffWindow()
window3 = NormalWindow()

pyglet.app.run()