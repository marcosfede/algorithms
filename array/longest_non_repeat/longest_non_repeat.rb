def longest_non_repeat(string)
  start = 0
  maxlen = 0
  used_char = {}
  string.each_char.with_index do |char, i|
    symb = char.to_sym
    if used_char.key?(symb) && (start <= used_char[symb])
      start = used_char[symb] + 1
    else
      maxlen = [maxlen, i + 1 - start].max
    end
    used_char[symb] = i
  end
  maxlen
end

a = 'abcabcdefbb'
p("input: #{a}")
p("result: #{longest_non_repeat(a)}")
p('output should be 6')
