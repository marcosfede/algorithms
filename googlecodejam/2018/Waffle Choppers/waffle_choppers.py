def count_chocs(board):
    sums_by_row = list(map(lambda row: sum([el == '@' for el in row]), board))
    return sum(sums_by_row)


def check_valid(board, hcuts, vcuts, expected_chocs):
    prevh = 0
    for hcut in hcuts:
        prevv = 0
        for vcut in vcuts:
            submatrix = [el[prevv:vcut] for el in board[prevh:hcut]]
            if count_chocs(submatrix) != expected_chocs:
                return False
            prevv = vcut
        prevh = hcut
    return True


def solve_horizontally(board, h, v, total_choc):
    sums_by_row = list(map(lambda row: sum([el == '@' for el in row]), board))
    choc_per_row = int(total_choc / (v + 1))

    counter = 0
    cuts = []
    for idx, s in enumerate(sums_by_row):
        if counter + s > choc_per_row:
            return False
        if counter + s == choc_per_row:
            counter = 0
            cuts.append(idx+1)
            continue
        counter += s
    if counter != 0:
        return False
    return cuts


def solve(board, h, v):
    transpose = list(zip(*board))
    total_choc = count_chocs(board)
    expected_choc = total_choc / ((v + 1) * (h + 1))
    if total_choc == 0:
        return True
    if not expected_choc.is_integer():
        return False
    hcuts = solve_horizontally(board, h, v, total_choc)
    if hcuts is False or len(hcuts) != h + 1:
        return False
    vcuts = solve_horizontally(transpose, v, h, total_choc)
    if vcuts is False or len(vcuts) != v + 1:
        return False
    return check_valid(board, hcuts, vcuts, expected_choc)


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        r, c, h, v = map(int, input().split(" "))
        board = []
        for ir in range(r):
            row = list(input())
            board.append(row)

        sol = 'POSSIBLE' if solve(board, h, v) else 'IMPOSSIBLE'
        print("Case #{}: {}".format(case, sol))


read_input()

# assert solve([list('.@@..@'), list('.....@'), list('@.@.@@')], 1, 1) is True
# assert solve([list('@@@'), list('@.@'), list('@.@'), list('@@@')], 1, 1) is False
# assert solve([list('.....'), list('.....'), list('.....'), list('.....')], 1, 1) is True
# assert solve([list('..@@'), list('..@@'), list('@@..'), list('@@..')], 1, 1) is False
# assert solve([list('@.@@'), list('@@.@'), list('@.@@')], 2, 2) is True
# assert solve([list('.@.@'), list('@.@.'), list('.@.@')], 1, 2) is False
