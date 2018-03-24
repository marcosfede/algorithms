def map_board(func, board):
    return [[func(el) for el in row] for row in board]


def clone_board(board):
    return map_board(lambda x: x, board)


def print_board(board):
    print()
    for row in board:
        print(' '.join(row))


def solve_rooks(board):
    n = len(board)
    board = clone_board(board)
    av_rows = set(range(n))
    av_cols = set(range(n))
    for ir in range(n):
        for ic in range(n):
            if board[ir][ic] == 'x':
                av_cols.remove(ic)
                av_rows.remove(ir)
    for _ in range(len(av_rows)):
        r = av_rows.pop()
        c = av_cols.pop()
        board[r][c] = 'x'
    return board


def solve_bishops_small(board):
    n = len(board)
    board = clone_board(board)
    for i in range(n):
        board[0][i] = '+'
    if n > 1:
        for i2 in range(1, n - 1):
            board[-1][i2] = '+'
    return board


def merge_solutions(rook_solution, bishop_solution):
    n = len(rook_solution)
    solution = []
    for ir in range(n):
        row = []
        for ic in range(n):
            if rook_solution[ir][ic] == '.':
                row.append(bishop_solution[ir][ic])
            elif bishop_solution[ir][ic] == '+':
                row.append('o')
            else:
                row.append('x')
        solution.append(row)
    return solution


def solve(board):
    rook_board = map_board(lambda piece: 'x' if (piece == 'x' or piece == 'o') else '.', board)
    bishop_board = map_board(lambda piece: '+' if (piece == '+' or piece == 'o') else '.', board)
    rook_solution = solve_rooks(rook_board)
    bishop_solution = solve_bishops(bishop_board)
    solution = merge_solutions(rook_solution, bishop_solution)
    score = score_board(solution)
    insertions = diff_board(board, solution)
    return score, insertions


def score_board(board):
    scores = {'.': 0, '+': 1, 'x': 1, 'o': 2}
    score = 0
    for row in board:
        for el in row:
            score += scores[el]
    return score


def diff_board(original, new):
    n = len(original)
    insertions = []
    for rowidx in range(n):
        for colidx in range(n):
            if original[rowidx][colidx] != new[rowidx][colidx]:
                insertions.append((new[rowidx][colidx], rowidx + 1, colidx + 1))
    return insertions


def read_input():
    t = int(input())
    for case in range(1, t + 1):
        n, m = map(int, input().split(" "))
        board = [['.'] * n for _ in range(n)]
        for k in range(m):
            piece, row, col = input().split(" ")
            board[int(row) - 1][int(col) - 1] = piece
        score, insertions = solve(board)
        print(f'CASE #{case}: {score} {len(insertions)}')
        for insertion in insertions:
            print(f'{insertion[0]} {str(insertion[1])} {str(insertion[2])}')


# read_input()
for row in solve([['.', '.', '.'], ['+', '+', '+'], ['.', '.', '.']]):
    print(row)
