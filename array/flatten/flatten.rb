def list_flatten(list)
  list.reduce([]) do |pv, cv|
    if !cv.is_a?(Array)
      pv + [cv]
    else
      pv + list_flatten(cv)
    end
  end
end

p list_flatten([2, 1, [3, [4, 5], 6], 7, [8]])

p 'output should be [2, 1, 3, 4, 5, 6, 7, 8]'
