import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from Event import Event
from LinkedListEventStore import LinkedListEventStore

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.store = LinkedListEventStore()
        self.event1 = Event(1, "Event 1", "2023-10-01", "10:00", "Location 1")
        self.event2 = Event(2, "Event 2", "2023-01-01", "10:00", "Location 2")
        self.event3 = Event(3, "Event 3", "2023-09-01", "10:00", "Location 3")

    def test_insert(self):
        self.store.insert_event(self.event1)
        self.store.insert_event(self.event2)
        self.store.insert_event(self.event3)
        events = self.store.list_all_events()
        for event in events:
            time = event.getTimestamp()
            print(time)
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0].title, "Event 1")
        self.assertEqual(events[1].title, "Event 2")
        self.assertEqual(events[2].title, "Event 3")

    def test_sort_events(self):
        self.store.insert_event(self.event1)
        self.store.insert_event(self.event2)
        self.store.insert_event(self.event3)
        self.store.sort_events()  
        events = self.store.list_all_events()
        for event in events:
            time = event.getTimestamp()
            print(time)
        self.assertEqual(events[0].title, "Event 2")  
        self.assertEqual(events[1].title, "Event 3")
        self.assertEqual(events[2].title, "Event 1")

if __name__ == '__main__':
    unittest.main()