import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from Event_Gen import EventGen
from ArrayListEventStore import ArrayListEventStore
from LinkedListEventStore import LinkedListEventStore
from Event import Event

SIZES = [5, 500, 5000, 50000]


def populate_unsorted(store, n):
    for i in range(n, 0, -1):
        store.insert_event(Event(i, f"Event {i}", "2025-10-10", "10:00", "Room"))

class TestUnsortedArrayList(unittest.TestCase):
    def test_linear_search_unsorted(self):
        for n in SIZES:
            with self.subTest(size=n):
                s = ArrayListEventStore(size=n)
                populate_unsorted(s, n)
                self.assertIsNotNone(s.linear_search(1))
                self.assertIsNotNone(s.linear_search(n))
                self.assertIsNotNone(s.linear_search(n // 2 if n >= 2 else 1))
                self.assertIsNone(s.linear_search(n + 1))

class TestUnsortedLinkedList(unittest.TestCase):
    def test_linear_search_unsorted(self):
        for n in SIZES:
            with self.subTest(size=n):
                s = LinkedListEventStore()
                populate_unsorted(s, n)
                self.assertIsNotNone(s.linear_search(1))
                self.assertIsNotNone(s.linear_search(n))
                self.assertIsNotNone(s.linear_search(n // 2 if n >= 2 else 1))
                self.assertIsNone(s.linear_search(n + 1))


class TestSortedArrayList(unittest.TestCase):
    def test_insertion_sort_by_id_then_search(self):
        for n in SIZES:
            with self.subTest(size=n):
                s = ArrayListEventStore(size=n)
                populate_unsorted(s, n)

                s.insertion_sort_by_id()

                ids = [e.getId() for e in s.list_all_events()]
                self.assertEqual(ids, sorted(ids))

                self.assertIsNotNone(s.linear_search(1))
                self.assertIsNotNone(s.linear_search(n))
                self.assertIsNotNone(s.binary_search(n // 2 if n >= 2 else 1))
                self.assertIsNone(s.binary_search(n + 1))

class TestSortedLinkedList(unittest.TestCase):
    def test_insertion_sort_by_id_then_search(self):
        for n in SIZES:
            with self.subTest(size=n):
                s = LinkedListEventStore()
                populate_unsorted(s, n)

                s.insertion_sort_by_id()

                ids = [e.getId() for e in s.list_all_events()]
                self.assertEqual(ids, sorted(ids))
                self.assertIsNotNone(s.linear_search(1))
                self.assertIsNotNone(s.linear_search(n))
                self.assertIsNotNone(s.binary_search(n // 2 if n >= 2 else 1))
                self.assertIsNone(s.binary_search(n + 1))

if __name__ == "__main__":
    unittest.main(verbosity=2)
