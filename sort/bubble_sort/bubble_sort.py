"""
Bubble Sort
An iterators goes through the list and sorts by swapping adjacent pairs of
elements to the corrent order.
https://en.wikipedia.org/wiki/Bubble_sort

Worst-case performance: O(N^2)
eg
<- is the location of the iterator i
[3, 2, 5, 4] Initial list

Set swapped := false
First iteration
[2, 3<-, 5, 4] Swap 3 > 2
Set swapped := true
[2, 3, 5<-, 4] No swap 5 > 3
[2, 3, 5, 4<-] Swap 5 > 4
[2, 3, 4, 5]
iterator i > n
    then break out of inner for-loop
swapped == true
    then stay in while-loop

Set swapped := false
Second iteration
[2, 3<-, 4, 5] No swap 3 > 2
[2, 3, 4<-, 5] No swap 4 > 3
[2, 3, 4, 5<-] No swap 5 > 4
[2, 3, 4, 5]
iterator i > n
    then break out of inner for-loop
swapped != true
    then break out of while-loop and list is sorted

"""


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True


array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
print(array)
bubble_sort(array)
print(array)
