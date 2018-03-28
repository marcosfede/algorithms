function solve(candidates, target)
    res = []
    sort!(candidates)
    dfs(candidates, target, 1, Int[], res)
    return res
end


function dfs(nums::Array{Int, 1}, target, index, path, res)
    if target == 0
        push!(res, path)
        return
    end
    for i = index:length(nums)
        next = target - nums[i]
        if next < 0
            return
        end
        dfs(nums, next, i, vcat(path, nums[i]), res)
    end
end

a = [2, 3, 6, 7]
print(solve(a, 7))  # should be [[2, 2, 3], [7]]
