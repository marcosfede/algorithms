masses = readlines("input.txt")

fuel(x)::Int = x ÷ 3 - 2
fuel(x::String)::Int = fuel(parse(Int64, x))

# p1
@show masses .|> fuel |> sum

# p2
function true_fuel(mass)::Int
    f = fuel(mass)
    f <= 0 ? 0 : f + true_fuel(f)
end

@show masses .|> true_fuel |> sum
