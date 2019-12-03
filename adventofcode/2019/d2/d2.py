with open('./input.txt') as f:
    program = [int(x) for x in f.read().split(',')]

def run(program):
    program = program[:]
    i = 0
    while True:
        operation = program[i:i+4]
        op = operation[0]
        if op == 99:
            return program[0]
        _ , a, b, to = operation
        if op == 1:
            program[to] = program[a] + program[b]
        elif op == 2:
            program[to] = program[a] * program[b]
        i += 4

# p1
p1 = program[:]
p1[1] = 12
p1[2] = 2
print(run(p1))

# p2
for x in range(100):
    for y in range(100):
        p2 = program[:]
        p2[1] = x
        p2[2] = y
        if run(p2) == 19690720: # replace this with the number you're given
            print(100*x + y)
