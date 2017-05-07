def rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[n - k:] + arr[:n - k]


a = [1, 2, 3, 4, 5, 6, 7]
print("in: ", a)
print("expected: ", [5, 6, 7, 1, 2, 3, 4])
print("out: ", rotate(a, 3))
