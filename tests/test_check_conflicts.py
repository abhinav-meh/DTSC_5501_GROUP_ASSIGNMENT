import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from Event_Gen import EventGen
from ArrayListEventStore import ArrayListEventStore
from LinkedListEventStore import LinkedListEventStore

SIZES = [5, 500, 5000, 50000]

def count_timestamp_conflicts_in_store(store):
    seen = set()
    conflicted = set()
    for e in store.list_all_events():
        ts = e.getTimestamp()
        if ts in seen and ts not in conflicted:
            conflicted.add(ts)
        else:
            seen.add(ts)
    return len(conflicted)

class TestArrayListTimestampConflicts(unittest.TestCase):
    def test_conflicts_in_arraylist(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = ArrayListEventStore(size=n)
                EventGen.generate_n_random_events(n, store)
                conflicts = count_timestamp_conflicts_in_store(store)
                print(f"ArrayList ({n} events): {conflicts} timestamp conflicts found.")
                self.assertGreaterEqual(conflicts, 0)
                if n >= 500:
                    self.assertGreater(conflicts, 0)

class TestLinkedListTimestampConflicts(unittest.TestCase):
    def test_conflicts_in_linkedlist(self):
        for n in SIZES:
            with self.subTest(size=n):
                store = LinkedListEventStore()
                EventGen.generate_n_random_events(n, store)
                conflicts = count_timestamp_conflicts_in_store(store)
                print(f"LinkedList ({n} events): {conflicts} timestamp conflicts found.")
                self.assertGreaterEqual(conflicts, 0)
                if n >= 500:
                    self.assertGreater(conflicts, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
