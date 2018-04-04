"""
Insertion Sort
Given a list, create two sub lists: sorted list and unsorted list.
Take an element from the unsorted list adjacent to sorted list and slide it into
place in the sorted list. Increment the size of the sorted list and decrement
size of the unsorted list. Continue until sorted list is the size of the list.

https://en.wikipedia.org/wiki/Insertion_sort
Complexity: O(n^2)
eg
<- Position of iterator i
[36, 14, 20, 19] Initial list

[36<-, 14, 20, 19]
Set pos := 0
pos == 0
    break while loop

[36, 14<-, 20, 19]
Set pos := 1
[14, 36<-, 20, 19] 14 < 36, slide 14 down sorted list
Set pos := 0
pos == 0
    break while loop

[14, 36, 20<-, 19]
Set pos := 2
[14, 20, 36<-, 19] 20 < 36, slide 20 down sorted list
Set pos := 1
[14, 20, 36<-, 19]
20 > 14
    break while loop

[14, 20, 36, 19<-]
Set pos:= 3
[14, 20, 19, 36<-] 19 < 36, slide 19 down sorted list
Set pos := 2
[14, 19, 20, 36<-] 19 < 20, slide 19 down sort list
Set pos := 1
[14, 19, 20, 36<-]
19 > 14
    break while loop
i == length of the list
    break for loop

[14, 19, 20, 36] Sorted list
"""

def insertion_sort(arr):
    for i, cursor in enumerate(arr):
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos -= 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr
