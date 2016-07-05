import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#subclassing-window

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__()

        self.label = pyglet.text.Label('Hello, world!')
    
    # Useful for attaching handlers as soon as the window is created
    def on_draw(self):
        self.clear()
        self.label.draw()

if __name__ == '__main__':
    # Only execute if not importing as a module
    window = HelloWorldWindow()
    pyglet.app.run()