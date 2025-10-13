class sortingAlgos():
    def InsertionSort(myArray):
        for i in range(1, len(myArray)):
            key = myArray[i]
            j = i - 1

            while j >= 0 and key < myArray[j]:
                myArray[j+1] = myArray[j]
                j -= 1
            
                myArray[j+1] = key

        return myArray


# Python program for Quick Sort on Singly Linked List

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def printList(curr):
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Returns the last node of the list
def getTail(cur):
    while cur and cur.next:
        cur = cur.next
    return cur

# Partitions the list taking the first element as the pivot
def partition(head, tail):
  
    # Select the first node as the pivot node
    pivot = head

    # 'pre' and 'curr' are used to shift all
    # smaller nodes' data to the left side of the pivot node
    pre = head
    curr = head

    # Traverse the list until you reach the node after the tail
    while curr != tail.next:
        
        # If current node's data is less than the pivot's data
        if curr.data < pivot.data:
            
            # Swap the data between 'curr' and 'pre.next'
            curr.data, pre.next.data = pre.next.data, curr.data
            
            pre = pre.next
        
        curr = curr.next

    # Swap the pivot's data with 'pre' data
    pivot.data, pre.data = pre.data, pivot.data
    
    # Return 'pre' as the new pivot
    return pre

def quickSortHelper(head, tail):
  
    # Base case: if the list is empty or consists of a single node
    if head is None or head == tail:
        return
    
    # Call partition to find the pivot node
    pivot = partition(head, tail)

    # Recursive call for the left part of the list (before the pivot)
    quickSortHelper(head, pivot)

    # Recursive call for the right part of the list (after the pivot)
    quickSortHelper(pivot.next, tail)

# The main function for quick sort.
# This is a wrapper over quickSortHelper
def quickSort(head):
  
    # Find the tail of the list
    tail = getTail(head)
    
    # Call the helper function to sort the list
    quickSortHelper(head, tail)
    return head

if __name__ == "__main__":
  
    # Creating a linked list: 30 -> 3 -> 4 -> 20 -> 5
    head = Node(30)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(20)
    head.next.next.next.next = Node(5)

    head = quickSort(head)
    printList(head)