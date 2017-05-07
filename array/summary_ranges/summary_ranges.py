def summary_ranges(nums):
    res = []
    l = len(nums)
    if l == 1:
        return [str(nums[0])]
    i = 0
    while i < l:
        start = nums[i]
        while i + 1 < l and nums[i + 1] - nums[i] == 1:
            i += 1
        if nums[i] != start:
            res.append(str(start) + "->" + str(nums[i]))
        else:
            res.append(str(start))
        i += 1
    return res


a = [0, 1, 2, 4, 5, 7]
print("input: ")
print(a)
print("output should be")
print(["0->2", "4->5", "7"])
print("output: ")
print(summary_ranges(a))
