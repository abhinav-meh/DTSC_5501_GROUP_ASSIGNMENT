import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from Event import Event
from ArrayListEventStore import ArrayListEventStore
from LinkedListEventStore import LinkedListEventStore

SIZES = [5, 500, 5000, 50000]


def _populate_with_unsorted_timestamps(store, n):
    """Insert events with scrambled timestamps."""
    for i in range(n, 0, -1):
        hh = (i % 24)
        store.insert_event(Event(i, f"Event {i}", "2025-10-10", f"{hh:02}:00", "Room"))


def _is_sorted_by_timestamp(events):
    timestamps = [e.getTimestamp() for e in events]
    return all(timestamps[i] <= timestamps[i + 1] for i in range(len(timestamps) - 1))


# ---------------------- ArrayList tests ----------------------

class TestArrayListInsertionSort(unittest.TestCase):
    def test_arraylist_insertion_sort_timestamp(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = ArrayListEventStore(size=n)
                _populate_with_unsorted_timestamps(store, n)
                store.insertion_sort() 
                self.assertTrue(
                    _is_sorted_by_timestamp(store.list_all_events()),
                    f"ArrayList insertion_sort failed for n={n}"
                )


class TestArrayListMergeSort(unittest.TestCase):
    def test_arraylist_merge_sort_timestamp(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = ArrayListEventStore(size=n)
                _populate_with_unsorted_timestamps(store, n)
                store.merge_sort()
                self.assertTrue(
                    _is_sorted_by_timestamp(store.list_all_events()),
                    f"ArrayList merge_sort failed for n={n}"
                )


class TestArrayListQuickSort(unittest.TestCase):
    def test_arraylist_quick_sort_timestamp(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = ArrayListEventStore(size=n)
                _populate_with_unsorted_timestamps(store, n)
                store.quick_sort() 
                self.assertTrue(
                    _is_sorted_by_timestamp(store.list_all_events()),
                    f"ArrayList quick_sort failed for n={n}"
                )


# ---------------------- LinkedList tests ----------------------

class TestLinkedListInsertionSort(unittest.TestCase):
    def test_linkedlist_insertion_sort_timestamp(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = LinkedListEventStore()
                _populate_with_unsorted_timestamps(store, n)
                store.insertion_sort() 
                self.assertTrue(
                    _is_sorted_by_timestamp(store.list_all_events()),
                    f"LinkedList insertion_sort failed for n={n}"
                )


class TestLinkedListMergeSort(unittest.TestCase):
    def test_linkedlist_merge_sort_timestamp(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = LinkedListEventStore()
                _populate_with_unsorted_timestamps(store, n)
                store.merge_sort()  
                self.assertTrue(
                    _is_sorted_by_timestamp(store.list_all_events()),
                    f"LinkedList merge_sort failed for n={n}"
                )


class TestLinkedListQuickSort(unittest.TestCase):
    def test_linkedlist_quick_sort_timestamp(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = LinkedListEventStore()
                _populate_with_unsorted_timestamps(store, n)
                store.quick_sort() 
                self.assertTrue(
                    _is_sorted_by_timestamp(store.list_all_events()),
                    f"LinkedList quick_sort failed for n={n}"
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
