def missing_ranges(arr, low, high):
    hashed = set(arr)
    for n in range(low, high):
        if n not in hashed:
            print(n)


inpt = [10, 12, 11, 15]
low, hi = 10, 15
print("input: ", inpt)
print("result: ")
missing_ranges(inpt, low, hi)