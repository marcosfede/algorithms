file = open("input")
lines = readlines(file)

function parse_line(line::String)
  regex = r"\#(?<c>\d+) \@ (?<x>\d+),(?<y>\d+): (?<w>\d+)x(?<h>\d+)"
  m = match(regex, line)
  return (m[:c], m[:x], m[:y], m[:w], m[:h]) .|> x -> parse(Int, x)
end

function solve(lines::Vector{String})
  d = Dict{Tuple{Int, Int}, Int}()
  for line in lines
    (claim,offsetx,offsety,width,height) = parse_line(line)
    for y in 1:height
      for x in 1:width
        pos = (offsetx + x, offsety + y)
        d[pos] = get(d, pos, 0) + 1
      end
    end
  end

  # search for claim
  for line in lines
    (claim,offsetx,offsety,width,height) = parse_line(line)
    if all(d[(offsetx + x, offsety + y)] == 1 for y in 1:height for x in 1:width)
      return claim
    end
  end
end

println(solve(lines))
