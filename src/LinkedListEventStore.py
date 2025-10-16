from EventStore import EventStore
from Event import Event
from Node import Node

class LinkedListEventStore(EventStore):

    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_event(self, event):
        new_node = Node(event)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.size += 1

    def delete_event(self, event_id):

        prev = None
        current = self.head

        while current:
            if current.event.id == event_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False
    
    def search_by_id(self, event_id):

        current = self.head
        while current:
            if current.event.id == event_id:
                return current.event
            current = current.next
        return None
    

    def list_all_events(self):
        events = []
        current = self.head
        while current:
            events.append(current.event)
            current = current.next
        return events
    

    # def bubble_sort_events(self):
    #     if self.head is None or self.head.next is None:
    #         return
        
    #     swapped = True
    #     while swapped:
    #         swapped = False
    #         current = self.head
    #         while current and current.next:
    #             if current.event.getTimestamp() > current.next.event.getTimestamp():
    #                 current.event, current.next.event = current.next.event, current.event
    #                 swapped = True
    #             current = current.next

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_head = None

        current = self.head
        while current:
            next_node = current.next
            if sorted_head is None or current.event.getTimestamp() < sorted_head.event.getTimestamp():
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_current = sorted_head
                while (sorted_current.next and 
                       sorted_current.next.event.getTimestamp() < current.event.getTimestamp()):
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node

        self.head = sorted_head


    def insertion_sort_by_id(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_head = None

        current = self.head
        while current:
            next_node = current.next
            if sorted_head is None or current.event.id < sorted_head.event.id:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_current = sorted_head
                while (sorted_current.next and 
                       sorted_current.next.event.id < current.event.id):
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node

        self.head = sorted_head

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            
            if left.event.getTimestamp() < right.event.getTimestamp():
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)
            return result

        def merge_sort_helper(head):
            if head is None or head.next is None:
                return head
            
            left, right = split(head)
            left = merge_sort_helper(left)
            right = merge_sort_helper(right)
            return merge(left, right)

        self.head = merge_sort_helper(self.head)


    def quick_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        def partition(head, end):
            pivot = end
            prev = None
            current = head
            tail = pivot

            while current != pivot:
                if current.event.getTimestamp() < pivot.event.getTimestamp():
                    if prev:
                        prev.next = current.next
                    else:
                        head = current.next
                    current.next = head
                    head = current
                    current = prev.next if prev else head
                else:
                    prev = current
                    current = current.next

            return head, pivot, tail

        def quick_sort_helper(head, end):
            if head is None or head == end:
                return head
            
            new_head, pivot, new_end = partition(head, end)

            if new_head != pivot:
                temp = new_head
                while temp.next != pivot:
                    temp = temp.next
                temp.next = None

                new_head = quick_sort_helper(new_head, temp)

                temp = self.get_tail(new_head)
                temp.next = pivot

            pivot.next = quick_sort_helper(pivot.next, new_end)

            return new_head

        self.head = quick_sort_helper(self.head, self.get_tail(self.head))


    def get_tail(self, node):
        while node and node.next:
            node = node.next
        return node
    
    def linear_search(self, event_id):
        current = self.head
        while current:
            if current.event.id == event_id:
                return current.event
            current = current.next
        return None
    
    def binary_search(self, event_id):
        self.insertion_sort_by_id()
        left, right = 0, self.size - 1
        events = self.list_all_events()

        while left <= right:
            mid = (left + right) // 2
            if events[mid].id == event_id:
                return events[mid]
            elif events[mid].id < event_id:
                left = mid + 1
            else:
                right = mid - 1
        return None



        

