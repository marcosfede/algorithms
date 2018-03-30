def two_sum(nums, target)
  dic = {}
  nums.each.with_index do |num, i|
    return [dic[num], i] if dic.include? num
    dic[target - num] = i
  end
end

arr = [3, 2, 4]
target = 6
res = two_sum(arr, target)
p res
