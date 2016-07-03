# http://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#using-opengl
from pyglet.gl import *

window = pyglet.window.Window(resizable=True)

# Setup the vertices (same as the previous example)
vertices = [
    0, 0,
    window.width, 0,
    window.width, window.height]

# Convert the vertices to ctypes (GLfloats)
vertices_gl = (GLfloat * len(vertices))(*vertices)

# This pre-loads the vertex information
glEnableClientState(GL_VERTEX_ARRAY)          # https://www.opengl.org/sdk/docs/man2/xhtml/glEnableClientState.xml
glVertexPointer(2, GL_FLOAT, 0, vertices_gl)  # https://www.opengl.org/sdk/docs/man2/xhtml/glVertexPointer.xml

# vertices_gl is just supplied to the GPU as a pointer
# So calulate the number of vertices we're going to draw
verts = len(vertices) // 2

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)              # https://www.opengl.org/sdk/docs/man2/xhtml/glClear.xml
    # Default Matrix Mode is GL_MODELVIEW?
    glLoadIdentity()                          # https://www.opengl.org/sdk/docs/man2/xhtml/glLoadIdentity.xml
    
    # Draw the information thats already loaded into the GPU
    glDrawArrays(GL_TRIANGLES, 0, verts)      # https://www.opengl.org/sdk/docs/man2/xhtml/glDrawArrays.xml

@window.event
def on_resize(width, height):
    # Unlike the previous example this doesn't update
    # the vertices so there is no stretching
    glViewport(0, 0, width, height)           # https://www.opengl.org/sdk/docs/man2/xhtml/glViewport.xml
    glMatrixMode(GL_PROJECTION)               # https://www.opengl.org/sdk/docs/man2/xhtml/glMatrixMode.xml
    glLoadIdentity()                          # Load the identity matrix on the projection matrix
    glOrtho(0, width, 0, height, -1, 1)       # https://www.opengl.org/sdk/docs/man2/xhtml/glOrtho.xml
    # glMatrixMode(GL_MODELVIEW)                # Return to default (MODELVIEW)

pyglet.app.run()
