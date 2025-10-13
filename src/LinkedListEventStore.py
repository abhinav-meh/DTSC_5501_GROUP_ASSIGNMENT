from EventStore import EventStore
from Event import Event
from Node import Node

class LinkedListEventStore(EventStore):

    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_event(self, event):
        new_node = Node(event)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.size += 1

    def delete_event(self, event_id):

        prev = None
        current = self.head

        while current:
            if current.event.id == event_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False
    
    def search_by_id(self, event_id):

        current = self.head
        while current:
            if current.event.id == event_id:
                return current.event
            current = current.next
        return None
    

    def list_events(self):
        events = []
        current = self.head
        while current:
            events.append(current.event)
            current = current.next
        return events

