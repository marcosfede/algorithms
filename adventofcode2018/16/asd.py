import re, collections

*samples, _, program = open('16/input.txt').read().split('\n\n')

ops = {
    'addr': lambda regs, a, b: regs[a] + regs[b],
    'addi': lambda regs, a, b: regs[a] + b,
    'mulr': lambda regs, a, b: regs[a] * regs[b],
    'muli': lambda regs, a, b: regs[a] * b,
    'banr': lambda regs, a, b: regs[a] & regs[b],
    'bani': lambda regs, a, b: regs[a] & b,
    'borr': lambda regs, a, b: regs[a] | regs[b],
    'bori': lambda regs, a, b: regs[a] | b,
    'setr': lambda regs, a, b: regs[a],
    'seti': lambda regs, a, b: a,
    'gtir': lambda regs, a, b: 1 if a > regs[b] else 0,
    'gtri': lambda regs, a, b: 1 if regs[a] > b else 0,
    'gtrr': lambda regs, a, b: 1 if regs[a] > regs[b] else 0,
    'eqir': lambda regs, a, b: 1 if a == regs[b] else 0,
    'eqri': lambda regs, a, b: 1 if regs[a] == b else 0,
    'eqrr': lambda regs, a, b: 1 if regs[a] == regs[b] else 0,
}

indeterminate = 0

possible = {k: set(ops.keys()) for k in range(16)}

for sample in samples:
    before, op, after = map(lambda s: list(map(int, re.findall(r'-?\d+', s))), sample.splitlines())

    count = 0

    for opcode in ops:
        result = ops[opcode](before, op[1], op[2])

        if [*before[:op[3]], result, *before[op[3]+1:]] == after:
            count += 1
        elif opcode in possible[op[0]]:
            possible[op[0]].remove(opcode)

    if count >= 3:
        indeterminate += 1

print('part 1:', indeterminate)

print({k: sorted(s) for k, s in possible.items()})


mapping = {}

while any(possible.values()):
    for number, opcodes in possible.items():
        if len(opcodes) == 1:
            mapping[number] = op = opcodes.pop()
            for remaining in possible.values():
                remaining.discard(op)

regs = [0, 0, 0, 0]

for line in program.splitlines():
    op, a, b, c = [int(x) for x in line.split()]
    regs[c] = ops[mapping[op]](regs, a, b)

print('part 2:', regs[0])
