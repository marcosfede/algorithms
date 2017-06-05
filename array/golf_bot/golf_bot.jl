
function calc_holes(moves::Vector{Int}, distances::Vector{Int})
    move_set = Set(moves)
    M = 2 * maximum(moves) - 1
    moves_poly = [ d in move_set for d in range(0, M)]
    moves_poly[1] = 1
    moves_transform = fft(moves_poly)
    conv = ifft(moves_transform .*  moves_transform)
    return sum(round(real(conv[d+1])) > 0 for d in distances)
end

n = parse(Int, readline())
moves = [parse(Int, readline()) for _ in range(1,n)]
m = parse(Int, readline())
distances = [parse(Int, readline()) for _ in range(1, m)]
print(calc_holes(moves, distances))