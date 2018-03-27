def solve(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res


def dfs(nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target - nums[i], i, path + [nums[i]], res)


a = [1,2,3,4]
print(solve(a, 6))  # should be [[2, 2, 3], [7]]
