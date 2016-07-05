import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/events.html#implementing-the-observer-pattern

# Using custom events to implement the Observer (Publisher/Subscriber) pattern

# The subject
class ClockTimer(pyglet.event.EventDispatcher):
    def tick(self):
        self.dispatch_event('on_update')
ClockTimer.register_event_type('on_update')

# Abstract observer class
class Observer(object):
    def __init__(self, subject):
        subject.push_handlers(self)

# Concrete observer
class DigitalClock(Observer):
    def on_update(self):
        print "DigitalClock updated"

# Concrete observer
class AnalogClock(Observer):
    def on_update(self):
        print "AnalogClock updated"

timer = ClockTimer()
digital_clock = DigitalClock(timer)
analog_clock = AnalogClock(timer)

timer.tick()
timer.tick()