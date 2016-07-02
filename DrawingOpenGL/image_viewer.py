import pyglet

window = pyglet.window.Window()
image = pyglet.image.load('alex_holkner/tristam_macdonald/game_of_life_init.png')
pos = [(window.width - image.width ) //2, (window.height - image.height) //2]

@window.event
def on_draw():
    window.clear()
    image.blit(pos[0], pos[1])

pyglet.app.run()