def dfs(nums, target, index, path, res)
  if target == 0
    res.push(path)
    return
  end
  (index...nums.length).each do |i|
    nxt = target - nums[i]
    if nxt < 0
      return
    end
    dfs(nums, nxt, i, path + [nums[i]], res)
  end
end

def solve(candidates, target)
  res = []
  candidates.sort!
  dfs(candidates, target, 0, [], res)
  res
end


a = [2, 3, 6, 7]
p solve(a, 7) # should be [[2, 2, 3], [7]]