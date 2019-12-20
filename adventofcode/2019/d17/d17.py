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
start = None
for y, row in enumerate(matrix):
    for x, char in enumerate(row):
        if char in '#^><v':
            if char in '^><v':
                start = x + y*1j
            for dx, dy in dirs:
                xp, yp = x+dx, y+dy
                if 0 <= xp < len(matrix[0]) and 0 <= yp < len(matrix) and matrix[yp][xp] == '#':
                    G[x+y*1j].add(xp+yp*1j)
                    G[xp+yp*1j].add(x+y*1j)


# p1
intersections = set(x for x, neigh in G.items() if len(neigh) == 4)
print('part1', sum(i.real*i.imag for i in intersections))

# p2

cmd = []
pos = start
facing = -1j
count = 0
while True:
    neigh = G[pos]
    if pos + facing not in neigh:
        if count > 0:
            cmd.append(count)
            count = 0
        if pos + facing * -1j in neigh:
            facing *= -1j
            cmd.append('L')
        elif pos + facing * 1j in neigh:
            facing *= 1j
            cmd.append('R')
        else:
            break
    count += 1
    pos += facing


def replace_subarr(arr, sub, char):
    ans = []
    count = 0
    i = 0
    while i < len(arr):
        if arr[i:i+len(sub)] == sub:
            count += 1
            ans.append(char)
            i += len(sub)
        else:
            ans.append(arr[i])
            i += 1
    return ans


def find_subroutines(cmd):
    for a in range(1, 11):
        A = cmd[0:a]
        for c in range(1, 11):
            if cmd[-a:] == A:
                C = cmd[-c-a:-a]
            else:
                C = cmd[-c:]
            replaced = replace_subarr(replace_subarr(cmd, A, 'A'), C, 'C')
            fragments = []
            fragment = []
            i = 0
            while i < len(replaced):
                if replaced[i] == 'A' or replaced[i] == 'C':
                    if len(fragment) > 0:
                        fragments.append(fragment)
                        fragment = []
                else:
                    fragment.append(replaced[i])
                i += 1
            shortest_fragment = min(fragments, key=len)
            main = replace_subarr(replaced, shortest_fragment, 'B')
            if all(char in 'ABC' for char in ''.join(str(x) for x in main)):
                return A, shortest_fragment, C


A, B, C = find_subroutines(cmd)
main = replace_subarr(replace_subarr(
    replace_subarr(cmd, A, "A"), B, "B"), C, "C")
print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')
print(f'main: {main}')

program[0] = 2
vm = VM(program)


def asciify(cmd):
    return ','.join(str(x) for x in cmd) + '\n'


ascii_cmd = asciify(main) + asciify(A) + asciify(B) + asciify(C) + 'n' + '\n'
for char in ascii_cmd:
    vm.add_input(ord(char))

print('part2:', vm.output[-1])
