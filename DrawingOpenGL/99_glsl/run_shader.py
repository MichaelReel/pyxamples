import pyglet
from pyglet.gl import *

import sys
sys.path.append('../tristam_macdonald')
from shader import Shader

class ShaderWindow(pyglet.window.Window):
  def __init__(self, shader_path):
    width = 512
    height = 512

    self.windowSize = (float(width), float(height))
    super(ShaderWindow, self).__init__(caption = 'Shader', width=width, height=height)

    self.shader = Shader(
      ' '.join(open('%s.v.glsl' % shader_path)),
      ' '.join(open('%s.f.glsl' % shader_path))
    )

  def on_draw(self):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1., 1., 1., -1., 0., 1.)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    self.shader.bind()
    self.shader.uniformf('WindowSize', *self.windowSize)

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
