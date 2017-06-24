list_flatten(l::Vector) = mapreduce(list_flatten, vcat, l)
list_flatten(i::Int) = i

println(list_flatten([2, 1, [3, [4, 5], 6], 7, [8]]))
