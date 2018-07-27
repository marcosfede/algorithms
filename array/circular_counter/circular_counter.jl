function circ_counter(l::Vector, skip::Int)
    skip = skip - 1
    idx = 0
    while length(l) > 0
        idx = (skip + idx) % length(l)
        println(splice!(l, idx + 1)) # julia indexes start at 1
    end
end

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
circ_counter(a, 3)
