"""
Quicksort
Given an array, it takes a divide-and-conquer strategy
by dividing the given aray into two smaller subarrays.
The following script takes a recursive approach and defines
quicksort function and a partition function.

Steps:
1. Pick a pivot, an element from the array.
   The following script takes the last element as pivot.
2. Partition the elements in the given array by reordering
   them in a way that elements with value less than the pivot
   are moved to the left of the pivot and elements with value
   greater than the pivot are moved to the right of the pivot.
3. Reapply the above steps recursively to the sublists formed
   by dividing the list at the pivot.

https://en.wikipedia.org/wiki/Quicksort

eg

[3, 7, 6, 5] Initial array

in quick_sort(arr = [3, 7, 6, 5], first = 0, last = 3):
  pos = partition(arr = [3, 7, 6, 5], first = 0, last = 3):
    in partition:
      wall = 0, last = 3
      1st loop (pos = 0):
        3 < 5
        wall = 1
        [3, 7, 6, 5]
      2nd loop (pos = 1):
        7 > 5
        wall = 1
        [3, 5, 6, 7]
      return wall(= 1)

  in quick_sort(arr = [3, 5, 6, 7], first = 0, pos - 1 = 0)
    'if first < pos - 1' is not true, thus no execution.

  in quick_sort(arr = [3, 5, 6, 7], pos + 1 = 2, last = 3)
    pos = partition(arr = [3, 5, 6, 7], first = 2, last = 3)
      in partition:
        wall = 2, last = 3
        1st for loop (pos = 2):
          6 < 7
          wall = 3
        [3, 5, 6, 7]
        return wall(= 3)

    in quick_sort(arr = [3, 5, 6, 7], first = 2, pos - 1 = 2)
      'if first < pos - 1' is not true, thus no execution.

    in quick_sort(arr = [3, 5, 6, 7], pos + 1 = 4, last = 3)
      'if pos + 1 < last' is not true, thus no execution.

arr is sorted. [3, 5, 6, 7]
"""

def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        print(arr[first:pos - 1], arr[pos + 1:last])
        # Start our two recursive calls
        quick_sort(arr, first, pos - 1)
        quick_sort(arr, pos + 1, last)


def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    print(wall)
    return wall


array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100, 4, 423, 2, 564, 9, 0, 10, 43, 64]
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
