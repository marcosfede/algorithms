def merge_intervals(arr)
    arr.sort
end


given = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected = [[1, 6], [8, 10], [15, 18]]
p("input: #{given}")
p("result: #{merge_intervals(given)}")
p("output should be: #{expected}")