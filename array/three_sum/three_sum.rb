def three_sum(nums)
    res = []
    nums.sort!
    (0...nums.length-2).each do |i|
      if i > 0 && nums[i] == nums[i+1]
        next
      end
      l = i + 1
      r = nums.length - 1
      while l < r
        s = nums[i] + nums[l] + nums[r]
        if s > 0
          r -= 1
        elsif s < 0
          l += 1
        else
          res.push([nums[i], nums[l], nums[r]])

          while (l < r && nums[l] == nums[l+1])
            l += 1
          end
          while (l < r && nums[r] == nums[r-1])
            r -= 1
          end
          l += 1
          r -= 1
        end

      end
    end
    return res
end

x = [-1 , 0, 1, 2, -1, -4]

print "input: "
p x
print "output should be: "
p [[-1, -1, 2], [-1, 0, 1]]
print "output: "
p three_sum(x)