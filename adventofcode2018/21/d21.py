
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
with open('./21/input.txt') as f:
    pregister = int(f.readline()[4])
    for line in f:
        op, a, b, c = line.split(' ')
        program.append((op, int(a), int(b), int(c)))

# p1
pointer = 0
registers = [0, 0, 0, 0, 0, 0]
seen = set()
while 0 <= pointer < len(program):
    registers[pregister] = pointer
    op, a, b, c = program[pointer]
    registers = apply_opcode(opcodes_by_name[op], registers, a, b, c)
    pointer = registers[pregister]
    pointer += 1
    if pointer == 28:
        if registers[5] in seen:
            print(registers[5])
            break
        seen.add(registers[5])
        print(registers[5])

print(registers[0])

###
# so basically inspecing the assembly code you realize that the only line where register 0 is used is on line 28 which sets a termination condition.
# when r[0] == r[5] the program halts
# p1 is the value of r[5] when it first reaches l28,
# p2 is the last value of r[5] before it cycles indefinitely
