def solve(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res


def dfs(nums, target, index, path, res):
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        next = target - nums[i]
        if next < 0:
            return
        dfs(nums, next, i, path + [nums[i]], res)


a = [2, 3, 6, 7]
print(solve(a, 7))  # should be [[2, 2, 3], [7]]
