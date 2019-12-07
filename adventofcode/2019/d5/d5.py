with open("./adventofcode/2019/d5/input.txt") as f:
    program = [int(x) for x in f.read().split(",")]


mode_to_accesor = {
    0: lambda x, y: y[x],
    1: lambda x, y: x,
}


class Mult:
    params = 3

    @classmethod
    def run(cls, params, modes, vm):
        a, b, to = params
        accesors = [mode_to_accesor[c] for c in modes]
        acc_a, acc_b, acc_c = accesors
        vm.program[to] = acc_a(a, vm.program) * acc_b(b, vm.program)
        vm.pointer += cls.params + 1


class Add:
    params = 3

    @classmethod
    def run(cls, params, modes, vm):
        a, b, to = params
        accesors = [mode_to_accesor[c] for c in modes]
        acc_a, acc_b, acc_c = accesors
        vm.program[to] = acc_a(a, vm.program) + acc_b(b, vm.program)
        vm.pointer += cls.params + 1


class Input:
    params = 1

    @classmethod
    def run(cls, params, modes, vm):
        to = params[0]
        vm.program[to] = vm.input
        vm.pointer += cls.params + 1


class Output:
    params = 1

    @classmethod
    def run(cls, params, modes, vm):
        source = params[0]
        accesors = [mode_to_accesor[c] for c in modes]
        acc_source = accesors[0]
        print(acc_source(source, vm.program))
        vm.pointer += cls.params + 1


class JumpIfTrue:
    params = 2

    @classmethod
    def run(cls, params, modes, vm):
        bool, dest = params
        acc_bool, acc_dest = [mode_to_accesor[c] for c in modes]
        if acc_bool(bool, vm.program) != 0:
            vm.pointer = acc_dest(dest, vm.program)
        else:
            vm.pointer += cls.params + 1


class JumpIfFalse:
    params = 2

    @classmethod
    def run(cls, params, modes, vm):
        boolean, dest = params
        acc_bool, acc_dest = [mode_to_accesor[c] for c in modes]
        if acc_bool(boolean, vm.program) == 0:
            vm.pointer = acc_dest(dest, vm.program)
        else:
            vm.pointer += cls.params + 1


class LessThan:
    params = 3

    @classmethod
    def run(cls, params, modes, vm):
        first, second, dest = params
        acc_first, acc_second, acc_dest = [mode_to_accesor[c] for c in modes]
        if acc_first(first, vm.program) < acc_second(second, vm.program):
            vm.program[dest] = 1
        else:
            vm.program[dest] = 0
        vm.pointer += cls.params + 1


class Equals:
    params = 3

    @classmethod
    def run(cls, params, modes, vm):
        first, second, dest = params
        acc_first, acc_second, acc_dest = [mode_to_accesor[c] for c in modes]
        if acc_first(first, vm.program) == acc_second(second, vm.program):
            vm.program[dest] = 1
        else:
            vm.program[dest] = 0
        vm.pointer += cls.params + 1


code_to_operation = {1: Add, 2: Mult, 3: Input, 4: Output,
                     5: JumpIfTrue, 6: JumpIfFalse, 7: LessThan, 8: Equals}


class VM:
    def __init__(self, program, input):
        self.pointer = 0
        self.program = program[:]
        self.input = input

    def run(self):
        while True:
            opcode = self.program[self.pointer]
            code = opcode % 100
            if code == 99:
                return self.program
            operation = code_to_operation[code]
            modes = [(opcode // 10**i) %
                     10 for i in range(2, 2+operation.params)]
            params = self.program[self.pointer +
                                  1: self.pointer + 1 + operation.params]
            operation.run(params, modes, self)


# p1
VM(program, 1).run()

# p2
VM(program, 5).run()
