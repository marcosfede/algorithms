from collections import deque, Iterable
from itertools import chain

def count(iter):
    return sum(1 for _ in iter)

def flatten(x):
    if isinstance(x, Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

class Game():

    def __init__(self, board):
        self.board = [row.split(" ") for row in board.split("\n")]

    def open(self, y, x):
        v = self.board[y][x]
        if v == 'x':
            raise ValueError('Upss! a mine is there')
        return v

    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])


gamemap = """
? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ?
? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? ? ? ? ?
? ? ? ? 0 0 ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 0 0
""".strip()
result = """
1 2 x 1 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 1 1 1 1 x 1
1 x 2 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 1 1 1 x 1 1 1 1
1 2 2 1 0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 x 2 2 1 1 0 0 0
0 1 x 2 1 2 2 x 2 1 0 0 0 0 0 0 0 0 1 3 x 3 1 1 0 0 0
0 1 1 2 x 2 x 3 x 1 0 0 0 0 0 0 0 0 0 2 x 3 x 1 0 0 0
""".strip()
game = Game(result)


class Cell:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.adjacents = []

    def ismine(self):
        return self.v == 'x'

    def isund(self):
        return self.v == '?'

    def isnotmine(self):
        return self.v == 'n'

    def isnumber(self):
        return str(self.v) in '012345678'

    def open(self):
        v = game.open(self.y, self.x)
        self.v = v

    def set_mine(self):
        self.v = 'x'

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.v)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y, self.v) == (other.x, other.y, other.v)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    def __init__(self, gamemap, mines):
        self.board = [[Cell(ei, ri, e) for ei, e in enumerate(r.split(' '))]
                      for ri, r in enumerate(gamemap.split('\n'))]
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.mines_left = mines
        self.directions = [Point(0, 1), Point(1, 1), Point(1, 0), Point(1, -1),
                           Point(0, -1), Point(-1, -1), Point(-1, 0), Point(-1, 1)]
        self.discovered = {
            el for row in self.board for el in row if el.isnumber()}
        # self.set_adjacents()

    def set_adjacents(self):
        for row in self.board:
            for cell in row:
                cell.adjacents = self.adjacents(cell)

    def adjacents(self, cell):
        return [self.get(direc.x + cell.x, direc.y + cell.y) for direc in self.directions if self.get(direc.x + cell.x, direc.y + cell.y) is not None]

    def celliterator(self):
        return (el for row in self.board for el in row)

    def unknowns(self):
        return count(self.unknowniterator)

    def unknowniterator(self):
        return (el for el in self.celliterator() if el.isund())

    def mineiterator(self):
        return (el for el in self.celliterator() if el.ismine())

    def notmineiterator(self):
        return (el for el in self.celliterator() if el.isnotmine())

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.board[y][x]
        return None

    def near_notmine(self, cell):
        return filter(lambda c: c.isnotmine(), self.adjacents(cell)) 

    def near_mines(self, cell):
        return filter(lambda c: c.ismine(), self.adjacents(cell))

    def near_und(self, cell):
        return filter(lambda c: c.isund(), self.adjacents(cell))

    def near_discovered(self, cell):
        return filter(lambda c: c.isnumber(), self.adjacents(cell))

    def safe_moves_arround(self, cell):
        near_und = list(self.near_und(cell))
        near_mines = list(self.near_mines(cell))
        if int(cell.v) == len(near_mines):
            for c in near_und:
                yield c

    def find_mines_arround(self, cell):
        near_und = list(self.near_und(cell))
        near_mines = list(self.near_mines(cell))
        if int(cell.v) - len(near_mines) == len(near_und):
            for mine in near_und:
                yield mine

    def issolved(self):
        for e in self.discovered:
            if int(e.v) != count(self.near_mines(e)):
                return False
        for n in chain(self.unknowniterator(), self.notmineiterator()):
            if count(self.near_mines(n)) == 0:
                return False
        return True

    def safe_moves(self):
        queue = deque(self.discovered)
        while queue and self.mines_left > 0:
            cell = queue.popleft()

            for mine in self.find_mines_arround(cell):
                self.set_mine(mine)
                for neigh in self.near_discovered(mine):
                    if neigh not in queue:
                        queue.append(neigh)

            for safe in self.safe_moves_arround(cell):
                self.open(safe)
                queue.append(safe)
        
        if self.mines_left == 0:
            for notmine in self.unknowniterator():
                self.open(notmine)
            return True
        return False

    def safe_moves_between_boards(self, boards):
        common = []
        for y in range(self.height):
            for x in range(self.width):
                compare = [ board.get(x,y) for board in boards ]
                if all(c.isund() or c.isnotmine() for c in compare):
                    common.append((x,y))
        return common

    def find_subblock():
        

    def solve(self):
        while True:
            self.safe_moves()
            done = self.safe_moves()
            if done:
                return str(self)
            
            subblock = self.find_subblock()
            solvable, boards = sublblock.speculate()
            boards = flatten(boards)

            if not solvable:
                return '?'
            if len(boards) == 1:
                board = boards[0].board
                for notmine in chain(board.notmineiterator(), board.unknowniterator()):
                    self.open_at(notmine.x, notmine.y)
                return str(self)
            safe_moves = subblock.safe_moves_between_boards(boards)
            if not safe_moves:
                return '?'
            for safe in safe_moves:
                self.open_at(safe[0], safe[1])

    def speculate(self):
        queue = deque(filter(lambda x: count(self.near_mines(x))
                             > 0 and count(self.near_und(x)) > 0, self.discovered))
        while queue and self.mines_left >= 0:
            cell = queue.popleft()
            near_und = list(self.near_und(cell))
            near_mines = count(self.near_mines(cell))
            remaining_mines = int(cell.v) - near_mines
            if remaining_mines < 0:
                return None, None
            if remaining_mines == len(near_und):
                for mine in near_und:
                    self.set_mine(mine)
                    for neigh in self.near_discovered(mine):
                        if neigh not in queue:
                            queue.append(neigh)
            if int(cell.v) == near_mines:
                for safe in near_und:
                    safe.v = 'n'
                    for neigh in filter(lambda c: c != cell and count(self.near_und(c)) > 0, self.near_discovered(safe)):
                        queue.append(neigh)

        if self.mines_left < 0:
            return None, None        
        if self.mines_left == 0:
            if self.issolved():
                return True, self
            return None, None

        sols = []
        for fruta in filter(lambda x: count(self.near_discovered(x)) + count(self.near_notmine(x)) > 0, self.unknowniterator()):
            board_cp = [[Cell(e.x, e.y, e.v) for e in row]
                        for row in self.board]
            board_cp[fruta.y][fruta.x].set_mine()
            s = '\n'.join([' '.join([str(c.v) for c in row])
                           for row in board_cp])
            b = Board(s, self.mines_left - 1)
            solvable, board = b.speculate()
            if solvable is not None:
                sols.append(board)
        if len(sols) == 0:
            return None, None
        return True, sols

    def open(self, cell):
        cell.open()
        self.discovered.add(cell)

    def open_at(self, x, y):
        cell = self.get(x, y)
        self.open(cell)

    def set_mine(self, cell):
        cell.set_mine()
        self.mines_left -= 1

    def __str__(self):
        return '\n'.join([' '.join([str(c.v) for c in row]) for row in self.board])

    def __eq__(self, other):
        return all(x == y for x, y in zip(self.celliterator(), other.celliterator()))


def solve_mine(gamemap, n):
    board = Board(gamemap, n)
    sol = board.solve()
    return sol

print(solve_mine(gamemap, result.count('x')))