def rotate(arr, steps)
  n = arr.length
  steps = steps % n
  arr[n - steps..-1] + arr[0...n - steps]
end

a = [1, 2, 3, 4, 5, 6, 7]
p('in: ', a)
p('expected: ', [5, 6, 7, 1, 2, 3, 4])
p('out: ', rotate(a, 3))
