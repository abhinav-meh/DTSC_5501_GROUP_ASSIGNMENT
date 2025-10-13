from EventStore import EventStore
import Event

class ArrayListEventStore(EventStore):

    def __init__(self, size:int):
        self.events = []
        self.size = size

    def insert_event(self, event):
        if len(self.events) < self.size:
            self.events.append(event)


    def delete_event(self, event_id):
        for event in self.events:
            if event.getId() == event_id:
                self.events.remove(event)
                return True
        return False  
    
    def search_by_id(self, event_id:int):
        for event in self.events:
            if event.getId() == event_id:
                return event
        return None
    
    def list_all_events(self):
        return self.events
    
