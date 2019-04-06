from math import ceil, sqrt

offset = 10


class Digger:
    def __init__(self, area):
        sqrta = sqrt(area)
        self.height = int(round(sqrta, 0))
        self.width = int(ceil(sqrta))
        self.board = [[0] * self.width for _ in range(self.height)]

    def nneigh(self, x, y):
        total = 0
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for move in moves:
            if self.board[y + move[1]][x + move[0]] == 0:
                total += 1
        return total

    def find_priority_square(self):
        return max([
            (x, y)
            for y in range(1, self.height - 1)
            for x in range(1, self.width - 1)
        ],
            key=lambda point: self.nneigh(point[0], point[1])
        )

    def dig(self):
        x, y = self.find_priority_square()
        return "{} {}".format(x + offset, y + offset)

    def set_hole(self, x, y):
        self.board[y - offset][x - offset] = 1


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        a = int(input())
        digger = Digger(a)
        guessed = False
        while not guessed:
            guess = digger.dig()
            print(guess)
            x, y = map(int, input().split(" "))
            if x == 0 and y == 0:
                guessed = True
            elif x == -1 and y == -1:
                return
            else:
                digger.set_hole(x, y)


read_input()
