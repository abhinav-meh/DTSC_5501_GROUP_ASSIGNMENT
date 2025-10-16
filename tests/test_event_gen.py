import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from Event_Gen import EventGen
from ArrayListEventStore import ArrayListEventStore
from LinkedListEventStore import LinkedListEventStore

class TestEventStorePopulation(unittest.TestCase):

    def test_arraylist_population(self):
        for n in [5, 500, 5000, 50000]:
            with self.subTest(n=n):
                store = ArrayListEventStore(size=n)
                EventGen.generate_n_random_events(n, store)
                events = store.list_all_events()
                self.assertEqual(len(events), n, f"ArrayList should have {n} events")

    def test_linkedlist_population(self):
        for n in [5, 500, 5000, 50000]:
            with self.subTest(n=n):
                store = LinkedListEventStore()
                EventGen.generate_n_random_events(n, store)
                events = store.list_all_events()
                self.assertEqual(len(events), n, f"LinkedList should have {n} events")

if __name__ == "__main__":
    unittest.main(verbosity=2)