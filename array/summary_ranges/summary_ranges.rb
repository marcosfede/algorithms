def summary_ranges(nums)
  res = []
  l = nums.length
  if l == 1
    return [str(nums[0])]
  end
  i = 0
  while i < l
    start = nums[i]
    while i + 1 < l and nums[i + 1] - nums[i] == 1
      i += 1
    end
    if nums[i] != start
      res.push(start.to_s + "->" + nums[i].to_s)
    else
      res.push(start.to_s)
    end
    i += 1
  end
  return res
end

a = [0, 1, 2, 4, 5, 7]
p("input: ")
p(a)
p("output should be")
p(["0->2", "4->5", "7"])
p("output: ")
p(summary_ranges(a))
