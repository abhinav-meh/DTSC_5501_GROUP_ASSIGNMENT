import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

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

        print(f"Store size after insertions: {len(store.events)}")
        assert len(store.events) == 5

    def test_insert_event_overflow(self):
        store = self.createStore()

        for i in range(6):
            event = Event(i, f"Event {i}", "2023-10-01", "10:00", "Location")
            store.insert_event(event)
            print(f"Attempted to insert: {event}")

        print(f"Store size after attempting overflow insertions: {len(store.events)}")
        assert len(store.events) == 5

    def test_delete_event(self):
        store = self.createStore()

        for i in range(3):
            event = Event(i, f"Event {i}", "2023-10-01", "10:00", "Location")
            store.insert_event(event)

        print(f"Store size before deletion: {len(store.events)}")
        assert len(store.events) == 3

        result = store.delete_event(1)
        print(f"Deleted event with ID 1: {result}")
        assert result == True
        assert len(store.events) == 2

        result = store.delete_event(5)
        print(f"Attempted to delete non-existent event with ID 5: {result}")
        assert result == False
        assert len(store.events) == 2

    def test_search_by_id(self):
        store = self.createStore()

        for i in range(3):
            event = Event(i, f"Event {i}", "2023-10-01", "10:00", "Location")
            store.insert_event(event)

        event = store.search_by_id(1)
        print(f"Searched for event with ID 1: Found {event}")
        assert event is not None
        assert event.getId() == 1

        event = store.search_by_id(5)
        print(f"Searched for non-existent event with ID 5: Found {event}")
        assert event is None

    def test_list_all_events(self):
        store = self.createStore()

        for i in range(3):
            event = Event(i, f"Event {i}", "2023-10-01", "10:00", "Location")
            store.insert_event(event)

        events = store.list_all_events()
        print(f"Listed all events: {events}")
        assert len(events) == 3
        for i, event in enumerate(events):
            assert event.getId() == i

    if __name__ == '__main__':
        unittest.main()
