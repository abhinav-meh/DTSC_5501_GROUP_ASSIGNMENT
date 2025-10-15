class Search:
    def __init__(self):
        pass

    def linear_search(self, linked_list, target_id):
        current = linked_list.head

        while current:
            if current.event["id"] == target_id:
                return current.event
            current = current.next

        return None

    def binary_search(self, sorted_events, target_id):
        low = 0
        high = len(sorted_events) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_id = sorted_events[mid]["id"]
            if mid_id == target_id:
                return sorted_events[mid]
            elif mid_id < target_id:
                low = mid + 1
            else:
                high = mid - 1

        return None