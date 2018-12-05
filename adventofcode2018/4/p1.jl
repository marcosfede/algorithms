using Dates
file = open("input")
lines = readlines(file)
parseInt = x -> parse(Int, x)

function parse_line(line::String)
  regex = r"\[(?<year>\d+)-(?<month>\d+)-(?<day>\d+) (?<hour>\d+):(?<minute>\d+)\] (?<wakes>wakes up)*(?<sleep>falls asleep)*(?<shift>Guard #(?<gid>\d+) begins shift)*"
  m = match(regex, line)

  date = (m[:year], m[:month], m[:day], m[:hour], m[:minute]) .|> parseInt |> x -> DateTime(x...)
  return (date, m[:wakes], m[:sleep], m[:gid])
end

function solve(lines::Vector{String})
  events = []
  by_id = Map()
  for line in lines
    (date, wakes, sleep, gid) = parse_line(line)
    push!(events, wakes, sleep, gid)
  end
  sort!(events, by=x->x[1])

  # group by id
  for event in events:
    (date, wakes, sleep, gid) = event
    if gid != nothing
      current_id = gid
    end
    push!(by_id[current_id], event)
  end

  # parse into bitarray

  # sum over bitarrays

  # find max sum ID

  # find num intersections between bitarrays

  # return ID * numintersections
end

println(solve(lines))
