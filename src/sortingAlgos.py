class sortingAlgos():
    def insertionSortArray(myArray):
        for i in range(1, len(myArray)):
            key = myArray[i]
            j = i - 1

            while j >= 0 and key < myArray[j]:
                myArray[j+1] = myArray[j]
                j -= 1
            
            myArray[j+1] = key

        return myArray
    
    def insertionSortLL():
        #set the varible current to the first node  
        current = head
        
        #begin iterating through the linked list
        while current:
            # create your temp variables
            key = current.next
            prev = current

            #if there isnt a next node break from the loop
            if key == None:
                break
            
            # if while iterating we notice that the next one is less then the first one we have some sorting to do.
            while prev and key.data < prev.data:
                # create a temp variable to start from the first node
                sortCurrent = head

                #swap the current to the head of the list
                sortCurrent.data, prev.data = prev.data, sortCurrent.data
                
                #iterate through
                while sortCurrent:
                    # if there isnt a next break out of this loop
                    if sortCurrent.next == None:
                        break
                    
                    # where we see the current bigger then its neighbor switch them
                    if sortCurrent.data > sortCurrent.next.data:
                        sortCurrent.data, sortCurrent.next.data = sortCurrent.next.data, sortCurrent.data
                    sortCurrent = sortCurrent.next

                key.data, prev.data = prev.data, key.data
            current = current.next
    
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
