def rotate(arr, k)
    n = arr.length
    k = k % n
    return arr[n-k..-1] + arr[0...n-k]
end


a = [1, 2, 3, 4, 5, 6, 7]
p("in: ", a)
p("expected: ", [5, 6, 7, 1, 2, 3, 4])
p("out: ", rotate(a, 3))