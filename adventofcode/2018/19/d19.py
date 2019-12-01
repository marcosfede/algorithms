
def addr(r, a, b):
    return r[a]+r[b]


def addi(r, a, b):
    return r[a]+b


def mulr(r, a, b):
    return r[a]*r[b]


def muli(r, a, b):
    return r[a] * b


def banr(r, a, b):
    return r[a] & r[b]


def bani(r, a, b):
    return r[a] & b


def borr(r, a, b):
    return r[a] | r[b]


def bori(r, a, b):
    return r[a] | b


def setr(r, a, b):
    return r[a]


def seti(r, a, b):
    return a


def gtir(r, a, b):
    return 1 if a > r[b] else 0


def grti(r, a, b):
    return 1 if r[a] > b else 0


def gtrr(r, a, b):
    return 1 if r[a] > r[b] else 0


def eqir(r, a, b):
    return 1 if a == r[b] else 0


def eqri(r, a, b):
    return 1 if r[a] == b else 0


def eqrr(r, a, b):
    return 1 if r[a] == r[b] else 0


def apply_opcode(opcode, registers, a, b, c):
    newregisters = registers[:]
    newregisters[c] = opcode(registers, a, b)
    return newregisters


opcodes = [addr, addi, mulr, muli, banr, bani, borr,
           bori, setr, seti, gtir, grti, gtrr, eqir, eqri, eqrr]

opcodes_by_name = {op.__name__: op for op in opcodes}

program = []
with open('./19/input.txt') as f:
    pregister = int(f.readline()[4])
    for line in f:
        op, a, b, c = line.split(' ')
        program.append((op, int(a), int(b), int(c)))

# p1
pointer = 0
registers = [0, 0, 0, 0, 0, 0]
while 0 <= pointer < len(program):
    registers[pregister] = pointer
    op, a, b, c = program[pointer]
    registers = apply_opcode(opcodes_by_name[op], registers, a, b, c)
    pointer = registers[pregister]
    pointer += 1

print(registers[0])

# p2
# for p2 running the instructions would take a shitload of time
# the idea is to reverse eng the intructions to find what's the code doing
# the code initializes some variables and then runs a double loop to find the divisiors
# of some number. register 0 holds the value of the sum of all divisors
# in my case it was the sum of divisors of the last register = 10551367  ==> 10557936
