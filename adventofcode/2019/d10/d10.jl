using DataStructures

struct Point
    x::Int
    y::Int
end

# parse
points = [Point(x, y) for (y, line) in enumerate(readlines("./input.txt")) for (x, char) in enumerate(line) if char == '#']

function angle(p1::Point, p2::Point)::Float64
    (atan(p2.x - p1.x, p1.y - p2.y) + 2pi) % 2pi
end

@assert angle(Point(1, 1), Point(1, 0)) == 0
@assert angle(Point(1, 1), Point(0, 0)) == 7pi / 4
@assert angle(Point(1, 1), Point(2, 0)) == pi / 4
@assert angle(Point(1, 1), Point(0, 1)) == 3pi / 2
@assert angle(Point(1, 1), Point(1, 3)) == 1.0 * pi
@assert angle(Point(1, 1), Point(2, 1)) == pi / 2

function visible(points::Vector{Point}, p::Point)::Int
    length(Set(angle(p, p2) for p2 in points if p2 != p))
end

function part1(points::Vector{Point})::Tuple{Point,Int}
    counts = [visible(points, p) for p in points]
    idx = argmax(counts)
    return points[idx], counts[idx]
end

# p1

best, best_count = part1(points)
println(best, best_count)


# p2

function distance(p1::Point, p2::Point)::Int
    (p2.y - p1.y)^2 + (p2.x - p1.x)^2
end

struct Target
    point::Point
    angle::Float64
    distance::Int
end

function part2(points::Vector{Point}, base::Point)::Int
    targets = [Target(p, angle(base, p), distance(base, p)) for p in points if p != base]
    destroyed = 0
    queue = Queue{Target}()
    for p in sort(targets, by = p->(p.angle, p.distance))
        enqueue!(queue, p)
    end

    seen = Set{Float64}()
    while true
        p = dequeue!(queue)
        if (p.angle in seen)
            enqueue!(queue, p)
        else
            destroyed += 1
            if destroyed == 200
                return (p.point.x - 1) * 100 + p.point.y - 1
            end
            push!(seen, p.angle)
        end
        if (p.angle > front(queue).angle)
            seen = Set{Float64}()
        end
    end

end

println(part2(points, best))
