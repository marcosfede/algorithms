import os
from itertools import permutations

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    program = [int(x) for x in f.read().split(",")]


class VM:
    def __init__(self, program):
        self.pointer = 0
        self.program = program[:]
        self.input = []
        self.output = []
        self.done = False
        self.base = 0

        self.op_params = {
            1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3
        }

    def get_param(self, param, mode):
        if mode == 0:
            return self.program[param]
        if mode == 1:
            return param
        if mode == 2:
            return self.program[self.base+param]

    def get_params(self, params, modes):
        return [self.get_param(p, m) for p, m in zip(params, modes)]

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
            raw_params = self.program[self.pointer +
                                      1: self.pointer + 1 + num_params]
            params = self.get_params(raw_params, modes)

            self.pointer += num_params + 1
            if code == 1:
                _, _, to = raw_params
                a, b, _ = params
                self.program[to] = a + b
            elif code == 2:
                _, _, to = raw_params
                a, b, _ = params
                self.program[to] = a * b
            elif code == 3:
                to = raw_params[0]
                self.program[to] = self.input.pop(0)
            elif code == 4:
                source = params[0]
                self.output.append(source)
            elif code == 5:
                boolean, dest = params
                if boolean != 0:
                    self.pointer = dest
            elif code == 6:
                boolean, dest = params
                if boolean == 0:
                    self.pointer = dest
            elif code == 7:
                _, _, dest = raw_params
                first, second, _ = params
                self.program[dest] = int(first < second)
            elif code == 8:
                _, _, dest = raw_params
                first, second, _ = params
                self.program[dest] = int(first == second)
            elif code == 9:
                pass


def run_amplifiers(program, phases):
    vms = [VM(program) for _ in range(5)]
    for phase, vm in zip(phases, vms):
        vm.add_input(phase)
    vms[0].add_input(0)

    while vms[4].done is False:
        for i, vm in enumerate(vms):
            vms[(i+1) % 5].add_input(vm.output[-1])

    return vms[4].output[-1]


# p1
print(max(run_amplifiers(program, phases)
          for phases in permutations(range(5))))
# p2
print(max(run_amplifiers(program, phases)
          for phases in permutations(range(5, 10))))
