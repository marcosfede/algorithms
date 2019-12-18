import networkx as nx
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

    def __copy__(self):
        vm = VM(program.copy())
        vm.pointer = self.pointer
        vm.output = self.output[:]
        vm.input = self.input[:]
        vm.done = self.done
        vm.base = self.base
        return vm


def arr_to_matrix(arr):
    mat = []
    row = []

    for i, code in enumerate(arr):
        if code == 10:
            mat.append(row)
            row = []
        else:
            row.append(chr(code))
    # there is an extra newline at the end..
    return mat[0:-1]


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


# G = nx.Graph()
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
vm = VM(program)
vm.run()
matrix = arr_to_matrix(vm.output)

plot_matrix(matrix, reverse=False, show_guide=True)

G = defaultdict(set)
for y, row in enumerate(matrix):
    for x, char in enumerate(row):
        if char == '#' or char in '^><v':
            for dx, dy in dirs:
                xp, yp = x+dx, y+dy
                if 0 <= xp < len(matrix[0]) and 0 <= yp < len(matrix) and matrix[yp][xp] == '#':
                    G[(x, y)].add((xp, yp))
                    G[(xp, yp)].add((x, y))


# p1
intersections = set(x for x, neigh in G.items() if len(neigh) == 4)
print(sum(x*y for x, y in intersections))

# p2
pos = next((x, y) for y, row in enumerate(matrix)
           for x, char in enumerate(row) if char in '<>v^')
seen = set()
path = []
while True:
    seen.add(pos)
    path.append(pos)
    try:
        it = iter(G[pos])
        while True:
            nxt = next(it)
            if nxt not in seen:
                pos = nxt
                seen.add(nxt)
                break
    except StopIteration:
        nxt = next(iter(G[pos]))
        if nxt in intersections:
            pos = nxt
        else:
            break
print(pos)
print(G[pos])
print(path)

assert len(G) == len(seen)