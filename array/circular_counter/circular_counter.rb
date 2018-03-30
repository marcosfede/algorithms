a = %w[1 2 3 4 5 6 7 8 9]

def circ_counter(arr, skip)
  index = 0
  until arr.empty?
    index = (skip + index - 1) % arr.length
    puts arr.delete_at(index)
  end
end

circ_counter(a, 3)
