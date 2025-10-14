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
    
    def mergeSort(myArray):
        if len(myArray) > 1:
            mid = len(myArray)//2
            L = myArray[:mid]
            R = myArray[mid:]
            sortingAlgos().mergeSort(L)
            sortingAlgos().mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    myArray[k] = L[i]
                    i += 1
                else:
                    myArray[k] = R[j]
                    j += 1
                k += 1

        while i < len(L):
            myArray[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            myArray[k] = R[j]
            j += 1
            k += 1

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quickSort(array, low, pi - 1)
            quickSort(array, pi + 1, high)


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