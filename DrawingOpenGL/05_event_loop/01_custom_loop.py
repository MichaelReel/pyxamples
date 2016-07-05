import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/eventloop.html#customising-the-event-loop

event_loop = pyglet.app.EventLoop()
window1 = pyglet.window.Window()

@event_loop.event
def on_enter():
    print "Entering game loop"

@event_loop.event
def on_window_close(window):
    print "Window closed"
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED

@event_loop.event
def on_exit():
    print "Exiting game loop"

# It's also possible to subclass and override exit(self), idle(self) and 
# run(self) on the event loop, but it's not generally recommended.
# https://pythonhosted.org/pyglet/api/pyglet.app.EventLoop-class.html

event_loop.run()