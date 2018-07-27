def merge_intervals(arr)
  arr.sort! { |a, b| a[0] - b[0] }
  n = [arr[0]]
  arr[1..-1].each do |i|
    last = n[-1]
    if i[0] > last[1]
      n.push(i)
    else
      n[-1] = [last[0], [i[1], last[1]].max]
    end
  end
  n
end

given = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected = [[1, 6], [8, 10], [15, 18]]
p("input: #{given}")
p("result: #{merge_intervals(given)}")
p("output should be: #{expected}")
