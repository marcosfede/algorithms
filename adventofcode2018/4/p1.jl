using Dates
using DataStructures

file = open("input")
lines = readlines(file)
parseInt = x -> parse(Int, x)

function parse_line(line::String)
  regex = r"\[(?<year>\d+)-(?<month>\d+)-(?<day>\d+) (?<hour>\d+):(?<minute>\d+)\] (?<wakes>wakes up)*(?<sleep>falls asleep)*(?<shift>Guard #(?<gid>\d+) begins shift)*"
  m = match(regex, line)
  return (parseInt(m[:minute]), m[:wakes] != nothing, m[:sleep] != nothing, m[:gid])
end

function solve(lines::Vector{String})
  # sort dates
  lines = sort(lines)
  minutes_sleep_per_guard = DefaultDict{Int, Int}(0)
  minute_data = Dict(x => Int[] for x in 0:59)

  current_guard = nothing
  sleep_start = nothing
  for line in lines
    (minute, wakes, sleep, gid) = parse_line(line)

    if gid != nothing
      current_guard = parseInt(gid)
    end
    if sleep
      sleep_start = minute
    end
    if wakes
        for i in sleep_start:minute-1
          push!(minute_data[i], current_guard)
          minutes_sleep_per_guard[current_guard] += 1
        end
    end
  end

  # find max sum ID
  max_minutes_slept = 0
  guard_id = nothing
  for (guard, minutes) in minutes_sleep_per_guard
    if minutes > max_minutes_slept
      max_minutes_slept = minutes
      guard_id = guard
    end
  end

  max_minute = 0
  max_minute_slept = 0
  for (minute, guards) in minute_data
    count = filter(gid -> gid == guard_id, guards) |> length
    if count > max_minute_slept
      max_minute_slept = count
      max_minute = minute
    end
  end

  return guard_id * max_minute
end

println(solve(lines))
