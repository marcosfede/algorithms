depths = readlines("input.txt") .|> x -> parse(Int64, x)

num_decrements(x)::Int = sum(x[1:end-1] .< x[2:end])

# p1
decrements = num_decrements(depths)
@show decrements

# p2
three_sums = depths[1:end-2] .+ depths[2:end-1] .+ depths[3:end]
@show num_decrements(three_sums)
