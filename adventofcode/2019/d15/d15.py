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


dirs = {
    1: 4,
    -1: 3,
    1j: 1,
    -1j: 2
}
reverse = {
    1: -1,
    -1: 1,
    1j: -1j,
    -1j: 1j,
}

G = nx.Graph()

seen = {}
queue = deque([[]])
while len(queue):
    path = queue.popleft()
    pos = sum(path)
    vm = VM(program)
    for m in path:
        vm.add_input(dirs[m])
    for move in dirs.keys():
        next_pos = pos + move
        if next_pos in seen:
            continue
        vm.add_input(dirs[move])
        out = vm.output[-1]
        if out == 0:
            seen[next_pos] = 0
        else:
            seen[next_pos] = out
            queue.append(path + [move])
            vm.add_input(dirs[reverse[move]])
            G.add_edge(pos, next_pos)


def plot(seen):
    xs = [int(x.real) for x in seen.keys()]
    ys = [int(x.imag) for x in seen.keys()]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    print(f'x from {min_x} to {max_x}. y from {min_y} to {max_y}')
    arr = [[' ']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for coord, obj in seen.items():
        char = ['#', ' ', 'O'][obj]
        arr[int(coord.imag)-min_y][int(coord.real) - min_x] = char
        print(
            f'setting a {char} at {int(pos.real) - min_x}, {int(pos.imag) - min_y}')
    arr[0-min_y][0-min_x] = 'S'
    print('\n'.join(reversed([''.join(row) for row in arr])))


# p1
plot(seen)

oxi = next(pos for pos, obj in seen.items() if obj == 2)
print(nx.shortest_path_length(G, 0, oxi))

# p2
print(max(nx.shortest_path_length(G, oxi).values()))
