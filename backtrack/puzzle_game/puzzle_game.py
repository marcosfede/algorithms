from collections import OrderedDict

primes = {3, 5, 7, 11, 13, 17, 19}
# full_neighbours_map = {
#     0: [1, 3],
#     1: [0, 2, 4],
#     2: [1, 5],
#     3: [0, 4, 6],
#     4: [1, 3, 5, 7],
#     5: [2, 4, 8],
#     6: [3, 7],
#     7: [4, 6, 8],
#     8: [5, 7]
# }
neighbours_map = {
    0: [1, 3],
    1: [2, 4],
    2: [5],
    3: [4, 6],
    4: [5, 7],
    5: [8],
    6: [7],
    7: [8],
    8: []
}


class Board:
    def __init__(self, board):
        self.board = tuple(board)

    def possible_moves(self):
        swaps = []
        for i, n in enumerate(self.board):
            neighbours = self.neighbours(i)
            for neighbour in neighbours:
                swaps.append((i, neighbour))
        return [self.swap(*swap) for swap in swaps]

    def neighbours(self, i1):
        return [n for n in neighbours_map[i1] if self.is_swappable(i1, n)]

    def is_swappable(self, i1, i2):
        return (self.board[i1] + self.board[i2]) in primes

    def swap(self, i1, i2):
        newboard = list(self.board)
        newboard[i1], newboard[i2] = newboard[i2], newboard[i1]
        return Board(newboard)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __str__(self):
        return str(self.board)


target = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def flatten(board):
    return [el for row in board for el in row]


def bfs(board):
    board = Board(flatten(board))
    q = OrderedDict({board: 0})
    visited = set()

    while q:
        current, distance = q.popitem(last=False)

        if current.board == target:
            return distance  # should be length of path

        for move in current.possible_moves():
            if move in visited:
                continue
            if move not in q:
                q[move] = distance + 1

        visited.add(current)
    return -1


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        blank = input()
        board = []
        for rowi in range(3):
            row = map(int, input().split(" "))
            board.append(row)
        solution = bfs(board)
        print(solution)


# read_input()
print(bfs([[2, 1, 3], [4, 5, 6], [7, 8, 9]]))  # should be 1
print(bfs([[7, 3, 2], [4, 1, 5], [6, 8, 9]]))  # should be 6
print(bfs([[9, 8, 5], [2, 4, 1], [3, 7, 6]]))  # should be -1
