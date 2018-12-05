using Dates
file = open("input")
lines = readlines(file)
parseInt = x -> parse(Int, x)

function parse_line(line::String)
  regex = r"\[(?<year>\d+)-(?<month>\d+)-(?<day>\d+) (?<hour>\d+):(?<minute>\d+)\] (?<wakes>wakes up)*(?<sleep>falls asleep)*(?<shift>Guard #(?<gid>\d+) begins shift)*"
  m = match(regex, line)
  date = DateTime(m[:year], m[:month], m[:day], m[:hour], m[:minute])
  return (date, m[:wakes], m[:sleep], m[:gid])
end

function solve(lines::Vector{String})

  for line in lines
    
  end
end

println(solve(lines))
