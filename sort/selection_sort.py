"""
Selection Sort
Given a list, iterate through the list and place the smallest element to the
start of the list. Two sub arrays form in the list: sorted list, and unsorted list.
Each iteration takes the smallest element in the unsorted list and places it in
the sorted list.
https://en.wikipedia.org/wiki/Selection_sort

Complexity: O(n^2)
eg
_ is the sorted sub array from 0th element to the element affixed with _, iterator i
<- position of iterator j in unsorted sub array

[15, 21, 2, 26] Initial list

Set minimum := 0
[15_, 21<-, 2, 26]
[15_, 21, 2<-, 26] 2 > 15, Set minimum := 2
[15_, 21, 2, 26]
[15_, 21, 2, 26<-]
Swap element 0 and 2 in the list
[2_, 21, 15, 26]
Increase sorted sub list
[2, 21_, 15, 26]

Set minimum := 1
[2, 21_, 15<-, 17, 26] 15 > 21, Set minimum := 2
[2, 21_, 15, 26]
[2, 21_, 15, 26<-]
Swap element 1 and element 2 in the list
[2, 15_, 21, 26]
Increase sorted sub list
[2, 15, 21_, 26]

Set minimum := 2
[2, 15, 21_, 26<-]
Swap element 2 and element 2 in the list
Increase sorted sub list
[2, 15, 21, 26_]

Set minimum := 3
Swap element 3 and element 3 in the list

[2, 15, 21, 26] List is sorted
"""
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j
        # Using a pythonic swap
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
