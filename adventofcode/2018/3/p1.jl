file = open("input")
lines = readlines(file)

function parse_line(line::String)
  regex = r"\#\d+ \@ (?<x>\d+),(?<y>\d+): (?<w>\d+)x(?<h>\d+)"
  m = match(regex, line)
  return (m[:x], m[:y], m[:w], m[:h]) .|> x -> parse(Int, x)
end

function solve(lines::Vector{String})
  d = Dict{Tuple{Int, Int}, Int}()
  for line in lines
    (offsetx,offsety,width,height) = parse_line(line)
    for y in 1:height
      for x in 1:width
        pos = (offsetx + x, offsety + y)
        d[pos] = get(d, pos, 0) + 1
      end
    end
  end

  sum([1 for v in values(d) if v > 1])
end

println(solve(lines))
