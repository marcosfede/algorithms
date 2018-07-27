def plus_one(digits)
  n = digits.length
  (0...n).reverse_each do |i|
    if digits[i] < 9
      digits[i] += 1
      return digits
    end
    digits[i] = 0
  end
  new_num = Array.new(n + 1) { 0 }
  new_num[0] = 1
  new_num
end

a = [8, 8, 9]
p('input', a)
p('output', plus_one(a))

b = [9, 9, 9, 9]
p('input', b)
p('output', plus_one(b))
