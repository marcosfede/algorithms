file = open("input")
lines = readlines(file)

function solve(lines)
    for line1 in lines
        for line2 in lines
            if sum(collect(line1) .!= collect(line2)) == 1
                return collect(line1)[collect(line1) .== collect(line2)] |> join
            end
        end
    end
end

println(solve(lines))
