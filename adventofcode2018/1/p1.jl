file = open("input")
lines = readlines(file)
lines = parse.(Float64,lines)
println(sum(lines))
