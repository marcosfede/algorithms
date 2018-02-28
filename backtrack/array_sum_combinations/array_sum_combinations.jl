function product(head:: Array{Int, 1})
    [[x] for x in head]
end

function product(head::Array{Int, 1}, tail::Array{Int, 1}...)
    subproducts = product(tail...)
    [[x, p...] for p in subproducts for x in head]
end

function Counter(iterable)
    hmap = Dict{Int, Int}()
    for el in iterable
        hmap[el] = get(hmap, el, 0) + 1
    end
    hmap
end

function sum_combinations(target, arrs...)
    counter_last = Counter(arrs[end])
    ans = []
    for combination in product(arrs...)
        difference = target - sum(combination)
        if difference in keys(counter_last)
            for _ in 0:counter_last[difference]
                push!(ans, [combination ; difference])
            end
        end
    end
    ans
end


A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [1, 2, 2, 2]
target = 7

println(sum_combinations(target, A, B, C))
