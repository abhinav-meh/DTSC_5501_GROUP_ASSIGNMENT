from abc import ABC, abstractmethod

class EventStore(ABC):
    
    @abstractmethod
    def insert_event(self, event):
        pass

    @abstractmethod
    def delete_event(self, event_id:int):
        pass

    @abstractmethod
    def search_by_id(self, event_id:int):
        pass

    @abstractmethod
    def list_all_events(self):
        pass

    @abstractmethod
    def insertion_sort(self):
        pass

    @abstractmethod
    def insertion_sort_by_id(self):
        pass
    
    @abstractmethod
    def merge_sort(self):
        pass
    
    @abstractmethod
    def quick_sort(self):
        pass
    
    @abstractmethod
    def linear_search(self):
        pass


    @abstractmethod
    def binary_search(self):
        pass