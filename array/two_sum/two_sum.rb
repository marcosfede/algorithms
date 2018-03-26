def two_sum(nums, target)
  dic = Hash.new
  nums.each.with_index do |num, i|
    if dic.include? num
      return [dic[num], i]
    else
      dic[target - num] = i
    end
  end
end

arr = [3, 2, 4]
target = 6
res = two_sum(arr, target)
p res