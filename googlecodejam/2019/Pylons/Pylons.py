from collections import defaultdict


def can_move(p1, p2):
    if p1[0] == p2[0]:
        return False
    if p1[1] == p2[1]:
        return False
    if p1[0] - p1[1] == p2[0] - p2[1]:
        return False
    if p1[0] + p1[1] == p2[0] + p2[1]:
        return False
    return True


def check(sequence):
    for n1, n2 in zip(sequence, sequence[1:]):
        if not can_move(n1, n2):
            return False, None
    return True, sequence


def solve(r, c):
    edges = defaultdict(set)
    nodes = set((x, y) for y in range(1, c+1) for x in range(1, r+1))
    for node in nodes:
        for other in nodes:
            if other != node and can_move(node, other):
                edges[node].add(other)

    def dive(visited, path):
        last = path[-1]
        if len(path) == r*c:
            return True, path
        for edge in edges[last]:
            if edge not in visited:
                possible, _path = dive(visited | set([edge]), path + [edge])
                if possible:
                    return True, _path
        return False, None

    first = (1, 1)
    possible, path = dive(set([first]), [first])

    return possible, path


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        r, c = list(map(int, input().split(' ')))
        possible, moves = solve(r, c)
        if not possible:
            print("CASE #{}: IMPOSSIBLE".format(case))
        else:
            print("CASE #{}: POSSIBLE".format(case))
            for move in moves:
                print("{} {}".format(move[0], move[1]))


read_input()
# print(solve(2, 2))
# print(solve(2, 5))
