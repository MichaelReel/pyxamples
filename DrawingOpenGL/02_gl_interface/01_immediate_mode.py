from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window(resizable=True)

@window.event
def on_draw():
    # This is an immediate mode example, kinda old-school
    # http://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#using-opengl
    
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()

@window.event
def on_resize(width, height):
    # Stretch the viewport to match the window
    # The stretching only occurs due to the immediate mode 
    # using the window properties to set the triangle dimensions
    # http://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#resizing-the-window
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(0, width, 0, height, -1, 1)
    # Defining a non-orthographic perspective:
    # gluPerspective(65, width / float(height), .1, 1000)

    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

pyglet.app.run()