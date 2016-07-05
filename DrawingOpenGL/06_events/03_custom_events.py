import pyglet

# http://pyglet.readthedocs.io/en/latest/programming_guide/events.html#creating-your-own-event-dispatcher

# The steps for creating an event dispatcher are:
# 1. Subclass EventDispatcher
# 2. Call the register_event_type class method on your subclass for each event your subclass will recognise.
# 3. Call dispatch_event to create and dispatch an event as needed.

class ClankingWidget(pyglet.event.EventDispatcher):
    def clank(self):
        self.dispatch_event('on_clank')

    def click(self, clicks):
        self.dispatch_event('on_clicked', clicks)

    def on_clank(self):
        print 'Default clank handler.'

ClankingWidget.register_event_type('on_clank')
ClankingWidget.register_event_type('on_clicked')

widget = ClankingWidget()

@widget.event
def on_clank():
    print "ker-clank!"

def override_on_clicked(clicks):
    print "whrr-%s!" % ("click" * clicks)

widget.push_handlers(on_clicked=override_on_clicked)

widget.clank()
widget.click(2)
