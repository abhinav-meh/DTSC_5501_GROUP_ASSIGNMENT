import Event

class Node():
    def __init__(self, event:Event.Event):
        self.event = event
        self.next = None