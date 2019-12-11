struct Point
  x::Int
  y::Int
end

points = Set{Point}()
for (y, line) in enumerate(readlines("./input.txt"))
    for (x, char) in enumerate(line)
        if char == '#'
            push!(points, Point(x,y))
        end
    end
end

function intermediate_points(p1::Point, p2::Point)::Vector{Point}
    if p1.x == p2.x
        bottom = min(p1.y, p2.y)
        top = max(p1.y, p2.y)
        return [Point(p1.x, y) for y in bottom+1:top-1]
    end
    num = (p2.y - p1.y)
    denom = (p2.x - p1.x)
    g = gcd(num, denom)

    return [Point(p1.x + convert(Int, denom * step / g), p1.y + convert(Int, num * step / g)) for step in 1:g - 1]

end

# println(intermediate_points(Point(2,2), Point(10,10)))
# println(intermediate_points(Point(2,2), Point(2,10)))
# println(intermediate_points(Point(5,5), Point(5,3)))
# println(intermediate_points(Point(2,2), Point(10,2)))
# println(intermediate_points(Point(0, 0), Point(9, 6)))

counts = Dict{Point,Int}()
for p1 in points
    for p2 in points
        if p1 == p2
            continue
        end
        # if p1.x == 5 && p1.y == 5
        #   println(p1, p2)
        #   ps = intermediate_points(p1,p2)
        #   println("intermediate points", ps)
        #   println("previous counter", get(counts, p1, 0))
        #   for p in ps
        #     if p in points
        #       println("there was already a point at ", p)
        #     end
        #   end
        #   println()
        # end

        if !any(p in points for p in intermediate_points(p1, p2))
            counts[p1] = get(counts, p1, 0) + 1
            # counts[p2] = get(counts, p2, 0) + 1
        end
    end
end

for (p, count) in counts
  if !(p in points)
    print("ERROR ", p)
  end
end

(n, pos) = findmax(counts)
println(pos, n)

# m = fill(".",31,31)
# for (p, count) in counts
#   m[CartesianIndex(p.y, p.x)] = string(count)
# end

# for row in eachrow(m)
#   println(join(row, ""))
# end