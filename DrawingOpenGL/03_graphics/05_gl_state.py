from pyglet.gl import *
from pyglet.graphics import *

# http://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#setting-the-opengl-state

texture1 = pyglet.image.load('../image.png').get_texture()

window = pyglet.window.Window()
batch = Batch()

class TextureEnableGroup(pyglet.graphics.Group):
    def set_state(self):
        glEnable(GL_TEXTURE_2D)

    def unset_state(self):
        glDisable(GL_TEXTURE_2D)

texture_enable_group = TextureEnableGroup()

class TextureBindGroup(pyglet.graphics.Group):
    def __init__(self, texture):
        super(TextureBindGroup, self).__init__(parent=texture_enable_group)
        assert texture.target == GL_TEXTURE_2D
        self.texture = texture

    def set_state(self):
        glBindTexture(GL_TEXTURE_2D, self.texture.id)

    # No unset_state method required.

    def __eq__(self, other):
        return (self.__class__ is other.__class__ and
                self.texture.id == other.texture.id and
                self.texture.target == other.texture.target and
                self.parent == other.parent)

    def __hash__(self):
        return hash((self.texture.id, self.texture.target))

batch.add(4, GL_QUADS, TextureBindGroup(texture1), 
    ('v2f', (0, 0, 0, window.height, window.width, window.height, window.width, 0)), 
    ('t3f', texture1.tex_coords), # Use the 3d tex coords supplied by the image load
    )

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    batch.draw()

pyglet.app.run()





