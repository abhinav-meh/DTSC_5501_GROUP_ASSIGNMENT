import unittest
from Event import Event
from ArrayListEventStore import ArrayListEventStore

class TestArraylistEventStore():

    def createStore(self):
        print("Creating an ArrayListEventStore object...")
        return ArrayListEventStore(5)
    
    def test_insert_event(self):
        store = self.createStore()

        for i in range(5):
            event = Event(i, f"Event {i}", "2023-10-01", "10:00", "Location")
            store.insert_event(event)
            print(f"Inserted: {event}")
