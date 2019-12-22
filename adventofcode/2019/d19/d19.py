import os
from collections import defaultdict, deque

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    program = [int(x) for x in f.read().split(",")]


class VM:
    def __init__(self, program):
        self.pointer = 0
        self.program = defaultdict(int, enumerate(program))
        self.input = []
        self.output = []
        self.done = False
        self.base = 0

        self.op_params = {
            1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1
        }

    def add_input(self, input):
        self.input.append(input)
        self.run()

    def run(self):
        while True:
            opcode = self.program[self.pointer]
            code = opcode % 100
            if code == 99:
                self.done = True
                return
            if code == 3 and len(self.input) == 0:
                return

            num_params = self.op_params[code]
            modes = [(opcode // 10**i) %
                     10 for i in range(2, 2+num_params)]
            args = [self.program[self.pointer+x]
                    for x in range(1, 1+num_params)]
            reads = [(self.program[a], a, self.program[a+self.base])[m]
                     for a, m in zip(args, modes)]
            writes = [(a, None, a+self.base)[m]
                      for a, m in zip(args, modes)]

            self.pointer += num_params + 1
            if code == 1:
                self.program[writes[2]] = reads[0] + reads[1]
            elif code == 2:
                self.program[writes[2]] = reads[0] * reads[1]
            elif code == 3:
                self.program[writes[0]] = self.input.pop(0)
            elif code == 4:
                self.output.append(reads[0])
            elif code == 5:
                if reads[0] != 0:
                    self.pointer = reads[1]
            elif code == 6:
                if reads[0] == 0:
                    self.pointer = reads[1]
            elif code == 7:
                self.program[writes[2]] = int(reads[0] < reads[1])
            elif code == 8:
                self.program[writes[2]] = int(reads[0] == reads[1])
            elif code == 9:
                self.base += reads[0]


def plot_matrix(mat, map_chars=None, reverse=True, show_guide=True):
    if reverse:
        mat = reversed(mat)
    if show_guide:
        for x in range(len(mat[0])):
            print(x % 10, end='')
        print()
    for y, row in enumerate(mat):
        for x, char in enumerate(row):
            print(char, end='')
        if show_guide:
            print(f' {y % 10}', end='')
        print()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, num):
        return Point(self.x*num, self.y*num)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'({self.x},{self.y})'


def pulled(point):
    vm = VM(program)
    vm.add_input(point.x)
    vm.add_input(point.y)
    return vm.output[-1] == 1


Y = 50
X = 50
grid = [['.']*X for _ in range(Y)]
for y in range(50):
    for x in range(50):
        if pulled(Point(x, y)):
            grid[y][x] = '#'

# p1
print('part1: ', sum(char == '#' for row in grid for char in row))

# plot_matrix(grid, reverse=False)


# p2
# start at this point because of the discontinuity seen on the plot
start = Point(7, 4)
right = Point(1, 0)
down = Point(0, 1)

pt = start
target_size = 100
while True:
    if pulled(pt):
        bottom_left = pt + Point(-target_size+1, target_size-1)
        if bottom_left.x >= 0:
            if pulled(bottom_left):
                top_left = pt + Point(-target_size+1, 0)
                print('part2: ', top_left.x*10000 + top_left.y)
                break
        pt += right
    else:
        pt += down
