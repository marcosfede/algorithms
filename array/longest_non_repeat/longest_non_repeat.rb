def longest_non_repeat(s)
  start, maxlen = 0, 0
  used_char = {}
  s.each_char.with_index do |char, i|
    symb = char.to_sym
    if used_char.key?(symb) and start <= used_char[symb]
      start = used_char[symb] + 1
    else
      maxlen = [maxlen, i + 1 - start].max
    end
    used_char[symb] = i
  end
  return maxlen
end

a = "abcabcdefbb"
p("input: #{a}")
p("result: #{longest_non_repeat(a)}")
p("output should be 6")