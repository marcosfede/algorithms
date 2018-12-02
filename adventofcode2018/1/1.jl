file = open("1.in")
lines = readlines(file)
lines = parse.(Float64,lines)
println(sum(lines))
