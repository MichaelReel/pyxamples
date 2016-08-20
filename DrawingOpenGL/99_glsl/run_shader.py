import pyglet
from pyglet.gl import *

import sys
sys.path.append('../tristam_macdonald')
from shader import Shader

class ShaderWindow(pyglet.window.Window):
  def __init__(self, shader_path):
    self.w = 512
    self.h = 512

    self.windowSize = (float(self.w), float(self.h))
    self.XY = (float(self.w / 2), float(self.h / 2))
    super(ShaderWindow, self).__init__(caption = 'Shader', width=self.w, height=self.h)

    self.shader = Shader(
      ' '.join(open('%s.v.glsl' % shader_path)),
      ' '.join(open('%s.f.glsl' % shader_path))
    )

  def on_mouse_motion(self, x, y, dx, dy):
    self.XY = (float(x), float(y))
    
  def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
    self.XY = (float(x), float(y))

  def on_mouse_press(self, x, y, button, modifiers):
    # Assign a byte buffer (int didn't appear to work - for rgb anyway)
    a = (GLubyte * (4 * self.w * self.h))(0)

    # Call the (rather slow) pixel read
    glReadPixels(0, 0, self.w, self.h, GL_RGBA, GL_UNSIGNED_BYTE, a)

    # For debugging purposes, create an image using the data
    image = pyglet.image.ImageData(self.w, self.h, 'RGBA', a)
    
    # Save the image to disk
    image.save("screenshot.png")

  def on_draw(self):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1., 1., 1., -1., 0., 1.)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    self.shader.bind()
    self.shader.uniformf('WindowSize', *self.windowSize)
    self.shader.uniformf('XY', *self.XY)

    glBegin(GL_QUADS)
    glVertex2i(-1, -1)
    glTexCoord2i(-2, -2)
    glVertex2f(1, -1)
    glTexCoord2i(2, -2)
    glVertex2i(1, 1)
    glTexCoord2i(2, 2)
    glVertex2i(-1, 1)
    glTexCoord2i(-2, 2)
    glEnd()

    self.shader.unbind()

window = ShaderWindow('shader')
pyglet.app.run()
