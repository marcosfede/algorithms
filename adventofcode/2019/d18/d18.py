from collections import deque, namedtuple

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
State = namedtuple('State', ['x', 'y', 'd', 'keys'])


matrix = []
with open('p1.input.txt') as f:
    for line in f:
        matrix.append(list(line.strip()))


def part1(matrix):
    all_keys = set(char for row in matrix for char in row if char.islower())
    numkeys = len(all_keys)
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == '@':
                start = (x, y)
    Q = deque([State(*start, 0, frozenset())])
    seen = set()
    while Q:
        s = Q.popleft()
        key = (s.x, s.y, s.keys)
        if key in seen:
            continue
        seen.add(key)
        char = matrix[s.y][s.x]
        keys = s.keys
        if char.isupper() and char.lower() in all_keys and not char.lower() in keys:
            continue
        if char.islower():
            keys = s.keys | frozenset([matrix[s.y][s.x]])
            if len(keys) == numkeys:
                return s.d
        for dir in dirs:
            dx, dy = dir
            xp, yp = s.x+dx, s.y+dy
            if matrix[yp][xp] != '#':
                Q.append(State(xp, yp, s.d+1, keys))


print('part1', part1(matrix))


matrix = []
with open('p2.input.txt') as f:
    for line in f:
        matrix.append(list(line.strip()))

# this is not valid for every case, it just adds up all the distances from
# each quadrant, ignoring doors for which the key is in another quadrant, but it works for my input


def part2(matrix):
    submatrices = [[row[x:x+41] for row in matrix[y:y+41]]
                   for y in range(0, 41, 40) for x in range(0, 41, 40)]
    return sum(part1(m) for m in submatrices)


print('part2: ', part2(matrix))
