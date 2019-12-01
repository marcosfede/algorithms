from dataclasses import dataclass
from typing import List
import re


@dataclass
class Sample:
    before: List[int]
    instructions: List[int]
    after: List[int]


regex = r'.+: +\[(\d), (\d), (\d), (\d)\]'
samples = []
with open('./16/input1') as f:
    lines = f.readlines()
    for index in range(0, len(lines), 4):
        m = re.match(regex, lines[index])
        before = [int(x) for x in m.groups()]
        instructions = [int(x) for x in lines[index+1].split(' ')]
        m = re.match(regex, lines[index+2])
        after = [int(x) for x in m.groups()]
        samples.append(Sample(before, instructions, after))


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

opcode_map = {k: set(opcodes) for k in range(16)}

# p1
sample_count = 0
for sample in samples:
    count = 0
    opcode_code, a, b, c = sample.instructions
    for opcode in opcodes:
        if apply_opcode(opcode, sample.before, a, b, c) == sample.after:
            count += 1
        elif opcode in opcode_map[opcode_code]:
            opcode_map[opcode_code].remove(opcode)
    if count >= 3:
        sample_count += 1

print(sample_count)


# p2

# there are codes with only one choice, remove those opcodes from the other keys
while True:
    unique_ops = set()
    for code, ops in opcode_map.items():
        if len(ops) == 1:
            unique_ops |= ops
    for code, ops in opcode_map.items():
        if len(ops) > 1:
            ops -= unique_ops
    if all(len(v) == 1 for v in opcode_map.values()):
        break

# set values to the only opcode remaining
opcode_map = {k: next(iter(v)) for k, v in opcode_map.items()}

# parse second part
instructions = []
with open('./16/input2') as f:
    for line in f:
        instructions.append([int(x) for x in line.split(' ')])

# run the program
current_state = [0, 0, 0, 0]
for instruction in instructions:
    code, a, b, c = instruction
    current_state = apply_opcode(opcode_map[code], current_state, a, b, c)
print(current_state[0])
