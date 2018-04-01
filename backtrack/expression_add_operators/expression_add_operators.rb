def product(arr, repeat)
  arrs = (1..repeat - 1).map { arr }
  arr.product(*arrs)
end

def solve(num, target)
  n = num.length
  Enumerator.new do |enum|
    product(['', '+', '*', '-'], n - 1).each do |comb|
      solution = []
      # interleave numbers with operators
      (0...n - 1).each do |i|
        solution << num[i]
        solution << comb[i]
      end
      solution << num[n - 1]
      solution = solution.join('')
      enum.yield solution if eval(solution) == target
    end
  end
end

# "123", 6 -> ["1+2+3", "1*2*3"]
p solve('123', 6).to_a

# "232", 8 -> ["2*3+2", "2+3*2"]
p solve('232', 8).to_a

# "123045", 3 -> ['1+2+3*0*4*5', '1+2-3*0*4*5', '1*2+3*0-4+5', '1*2-3*0-4+5', '1-2+3+0-4+5', '1-2+3-0-4+5']
p solve('123045', 3).to_a

p solve('105', 5).to_a
