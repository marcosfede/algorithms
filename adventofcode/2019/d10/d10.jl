using DataStructures

struct Point
  x::Int
  y::Int
end

# parse
points = [Point(x,y) for (y, line) in enumerate(readlines("./input.txt")) for (x, char) in enumerate(line) if char == '#']

function angle(p1::Point, p2::Point)::Float64
  (pi/2 - atan(p2.y-p1.y, p2.x - p1.x)) % 2pi
end

function visible(points::Vector{Point}, p::Point)::Int
  length(Set(angle(p, p2) for p2 in points if p2 != p))
end

function part1(points::Vector{Point})::Tuple{Point, Int}
  counts = [visible(points, p) for p in points]
  idx = argmax(counts)
  return points[idx], counts[idx]
end

# p1

best, best_count = part1(points)
println(best, best_count)

# p2

function part2(points::Vector{Point}, base::Point)::Int
  d = Dict{Float64, Vector{Point}}()
  
end