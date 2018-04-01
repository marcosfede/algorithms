function product(arr, repeat)
  arrs = [arr for _ in 1:repeat]
  Iterators.product(arrs...)
end

function solve(num, target)
    n = length(num)
    return Channel() do c
        for comb in product(["", "+", "*", "-"], n - 1)
            solution = []
            # interleave numbers with operators
            for i in 1:n - 1
                push!(solution, num[i])
                push!(solution, comb[i])
            end
            push!(solution, num[end])
            solution = join(solution, "")
            if eval(parse(solution)) == target
                push!(c, solution)
            end
        end
    end
end

# "123", 6 -> ["1+2+3", "1*2*3"]
println(collect(solve("123", 6)))

# "232", 8 -> ["2*3+2", "2+3*2"]
println(collect(solve("232", 8)))

# "123045", 3 -> ['1+2+3*0*4*5', '1+2-3*0*4*5', '1*2+3*0-4+5', '1*2-3*0-4+5', '1-2+3+0-4+5', '1-2+3-0-4+5']
println(collect(solve("123045", 3)))

println(collect(solve("105", 5)))
