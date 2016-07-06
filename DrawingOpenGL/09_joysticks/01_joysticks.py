import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/input.html#using-joysticks

joysticks = pyglet.input.get_joysticks()

for joystick in joysticks:
    print "Joystick found: %s" % joystick
    joystick.open()

if not joysticks:
    print "No joysticks found"

