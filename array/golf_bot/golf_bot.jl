
function calc_holes(moves::Vector{Int}, distances::Vector{Int})
    move_set = Set(moves)
    M = 2 * maximum(moves) - 1
    moves_poly = [ d in move_set for d in 0:M]
    moves_poly[1] = 1
    moves_transform = fft(moves_poly)
    conv = ifft(moves_transform .* moves_transform)
    return sum(round(real(conv[d + 1])) > 0 for d in distances)
end

moves = [1, 3, 5]
distances = [2, 4, 5, 7, 8, 9]
expected_out = 4
println(calc_holes(moves, distances))
