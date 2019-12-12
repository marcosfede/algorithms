import os
from collections import defaultdict

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


def paint(start_color):
    ship = defaultdict(int)
    vm = VM(program)
    pos = 0
    ship[pos] = start_color
    direction = 1j
    while vm.done is False:
        vm.add_input(ship[pos])
        color, turn = vm.output[-2:]
        ship[pos] = color
        direction = direction * (1j if turn == 0 else -1j)
        pos += direction
    return ship


# p1
print(len(paint(0)))


def plot(ship):
    min_x, max_x = int(min(x.real for x in ship.keys())), int(
        max(x.real for x in ship.keys()))
    min_y, max_y = int(min(x.imag for x in ship.keys())), int(
        max(x.imag for x in ship.keys()))

    arr = [[' ']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for pos, paint in ship.items():
        arr[int(pos.imag)-min_y][int(pos.real) -
                                 min_x] = ' ' if paint == 0 else '#'

    print('\n'.join(reversed([''.join(row) for row in arr])))


# p2
ship = paint(1)
plot(ship)
