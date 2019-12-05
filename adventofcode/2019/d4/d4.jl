function Counter(iter::String)::Dict{Char,Int64}
    d = Dict()
    for elem in iter
        d[elem] = get(d, elem, 0) + 1
    end
    return d
end

function valid(code::Int64, pred::Function)
    scode = string(code)
    if !all(b >= a for (a, b) in zip(scode[1:end - 1], scode[2:end]))
        return false
    end
    # 599922 => ('5', '9', '2'), (1, 3, 2)
    c = Counter(scode)
    digits, counts = collect(keys(c)), collect(values(c))
    return pred(counts)
end

a, b = 284639, 748759
# p1
println(sum(valid(code, counts->any(count > 1 for count in counts))
          for code in a:b))
# p2
println(sum(valid(code, counts->any(count == 2 for count in counts)) for code in a:b))
