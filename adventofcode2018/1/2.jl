file = open("1.in")
lines = readlines(file)
lines = parse.(Float64,lines)

function solve(lines::Vector{Float64})
  set = Set{Float64}(0)
  sum = 0
  while true
    for freq in lines
      sum += freq
      if in(sum, set)
        return sum
      end
      push!(set, sum)
    end
  end
end

println(solve(lines))
