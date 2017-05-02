def merge_intervals(arr)

end


given = [[1, 3], [2, 6], [8, 10], [15, 18]]
given_intervals = [Interval(*i) for i in given]
expected = [[1, 6], [8, 10], [15, 18]]
p("input: #{given}")
p("result: #{merge_intervals(given)}")
p("output should be: #{expected}")