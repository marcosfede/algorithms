function solve(candidates, target) {
    const res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
}

function dfs(nums, target, index, path, res) {
    if (target === 0) {
        res.push(path)
        return
    }
    for (let i = index; i < nums.length; i++) {
        let next = target - nums[i]
        if (next < 0) {
            return  // backtracking
        }
        dfs(nums, next, i, path.concat(nums[i]), res)
    }
}

const a = [2, 3, 6, 7]
console.log(solve(a, 7)) // should be  [[2, 2, 3]], [7]]
