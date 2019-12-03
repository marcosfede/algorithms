with open('./input.txt') as f:
    l1, l2 = [l.strip().split(',') for l in f.readlines()]

DIRS = {'U': 1j, 'D': -1j, 'R': 1, 'L': -1}


def manhattan(complex):
    return abs(complex.real) + abs(complex.imag)


def parse(line):
    d = {}
    pos = steps = 0
    for step in line:
        dir = DIRS[step[0]]
        moves = int(step[1:])
        for m in range(moves):
            pos += dir
            steps += 1
            d.setdefault(pos, steps)
    return d


a = parse(l1)
b = parse(l2)
x = set(a) & set(b)

# p1
print(min(manhattan(p) for p in x))
# p2
print(min(a[p]+b[p] for p in x))
