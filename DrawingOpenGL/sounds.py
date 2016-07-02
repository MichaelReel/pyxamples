import pyglet

music = pyglet.resource.media('music.mp3')
music.play()

sound = pyglet.resource.media('shot.wav', streaming=False)
sound.play()

pyglet.app.run()