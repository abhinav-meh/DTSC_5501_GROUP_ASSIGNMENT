import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from Event import Event

class TestEventFunctions(unittest.TestCase): 

    def createEvent(self):
        print("Creating an Event object...")
        return Event(1, "Meeting", "2023-10-01", "10:00", "Conference Room")

    def test_getId(self):
        event = self.createEvent()
        print(f"Testing getId: Expected 1, Got {event.getId()}")
        self.assertEqual(event.getId(), 1)

    def test_getTitle(self):
        event = self.createEvent()
        print(f"Testing getTitle: Expected 'Meeting', Got '{event.getTitle()}'")
        self.assertEqual(event.getTitle(), "Meeting")

    def test_getDate(self):
        event = self.createEvent()
        print(f"Testing getDate: Expected '2023-10-01', Got '{event.getDate()}'")
        self.assertEqual(event.getDate(), "2023-10-01")

    def test_getTime(self):
        event = self.createEvent()
        print(f"Testing getTime: Expected '10:00', Got '{event.getTime()}'")
        self.assertEqual(event.getTime(), "10:00")

    def test_getTimestamp(self):
        event = self.createEvent()
        print(f"Testing getTimestamp: Expected 202310011000, Got {event.getTimestamp()}")
        self.assertEqual(event.getTimestamp(), 202310011000)

    def test_getLocation(self):
        event = self.createEvent()
        print(f"Testing getLocation: Expected 'Conference Room', Got '{event.getLocation()}'")
        self.assertEqual(event.getLocation(), "Conference Room")

    def test_setDate(self):
        event = self.createEvent()
        event.setDate("2023-12-25")
        print(f"Testing setDate: Expected '2023-12-25', Got '{event.getDate()}'")
        self.assertEqual(event.getDate(), "2023-12-25")
    
    def test_setTime(self):
        event = self.createEvent()
        event.setTime("15:00")
        print(f"Testing setTime: Expected '15:00', Got '{event.getTime()}'")
        self.assertEqual(event.getTime(), "15:00")

    def test_setLocation(self):
        event = self.createEvent()
        event.setLocation("Main Hall")
        print(f"Testing setLocation: Expected 'Main Hall', Got '{event.getLocation()}'")
        self.assertEqual(event.getLocation(), "Main Hall")
    
    def test_str(self):
        event = self.createEvent()
        expected_str = "Event(ID: 1, Title: Meeting, Date: 2023-10-01, Time: 10:00, Location: Conference Room)"
        print(f"Testing __str__: Expected '{expected_str}', Got '{str(event)}'")
        self.assertEqual(str(event), expected_str)

if __name__ == '__main__':
    unittest.main()