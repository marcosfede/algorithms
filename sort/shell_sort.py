"""
    Shell Sort

    O(n^1.5)

    Shell Sort is an improvement of Insertion Sort. Instead of
    comparing items next to each other this algorithm
    compares every h-th item.

    https://en.wikipedia.org/wiki/Shellsort

"""

def shell_sort(arr):
    h = 1
    while h<=len(arr)/9: #initial value of h
        h = 3*h+1
    
    while h>0:
        for i in range(h,len(arr)):
            v = arr[i]
            j = i
            while arr[j-h]>v:
                arr[j] = arr[j-h]
                j -= h
                if j<h:
                    break
            arr[j] = v 
        h = h // 3

