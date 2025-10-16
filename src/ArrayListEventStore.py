from EventStore import EventStore
import Event

class ArrayListEventStore(EventStore):

    def __init__(self, size:int):
        self.events = []
        self.size = size

    def get_size(self):
        return self.size

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
    
    def insertion_sort(self):
          for i in range(1, len(self.events)):
            key = self.events[i]
            j = i - 1
            while j >= 0 and key.getTimestamp() < self.events[j].getTimestamp():
                self.events[j + 1] = self.events[j]
                j -= 1
            self.events[j + 1] = key

    def insertion_sort_by_id(self):
        for i in range(1, len(self.events)):
            key = self.events[i]
            j = i - 1
            while j >= 0 and key.getId() < self.events[j].getId():
                self.events[j + 1] = self.events[j]
                j -= 1
            self.events[j + 1] = key

    def merge_sort(self):
        if len(self.events) > 1:
            mid = len(self.events) // 2
            left_half = self.events[:mid]
            right_half = self.events[mid:]

            left_store = ArrayListEventStore(len(left_half))
            left_store.events = left_half
            left_store.merge_sort()

            right_store = ArrayListEventStore(len(right_half))
            right_store.events = right_half
            right_store.merge_sort()

            i = j = k = 0

            while i < len(left_store.events) and j < len(right_store.events):
                if left_store.events[i].getTimestamp() < right_store.events[j].getTimestamp():
                    self.events[k] = left_store.events[i]
                    i += 1
                else:
                    self.events[k] = right_store.events[j]
                    j += 1
                k += 1

            while i < len(left_store.events):
                self.events[k] = left_store.events[i]
                i += 1
                k += 1

            while j < len(right_store.events):
                self.events[k] = right_store.events[j]
                j += 1
                k += 1

    def quick_sort(self):
        def _quick_sort(events, low, high):
            if low < high:
                pi = partition(events, low, high)
                _quick_sort(events, low, pi - 1)
                _quick_sort(events, pi + 1, high)

        def partition(events, low, high):
            pivot = events[high]
            i = low - 1
            for j in range(low, high):
                if events[j].getId() <= pivot.getId():
                    i += 1
                    events[i], events[j] = events[j], events[i]
            events[i + 1], events[high] = events[high], events[i + 1]
            return i + 1

        _quick_sort(self.events, 0, len(self.events) - 1)

    def linear_search(self, event_id:int):
        for event in self.events:
            if event.getId() == event_id:
                return event
        return None
    

    def binary_search(self, event_id:int):
        self.insertion_sort_by_id()
        low = 0
        high = len(self.events) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.events[mid].getId() == event_id:
                return self.events[mid]
            elif self.events[mid].getId() < event_id:
                low = mid + 1
            else:
                high = mid - 1
        return None
    