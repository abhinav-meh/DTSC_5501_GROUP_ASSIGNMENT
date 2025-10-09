from EventStore import EventStore

class ArrayListEventStore(EventStore):

    def __init__(self, size:int):
        self.events = []
        self.size = size

    def insert_event(self, event):
        if len(self.events) < self.size:
            self.events.append(event)


    def delete_event(self, event_id):
        


