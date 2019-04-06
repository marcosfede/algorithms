def solve(n, way):
    if way[0] == way[-1]:
        if way[0] == 'E':
            for i, char in enumerate(way):
                if way[i] == way[i+1] and way[i] == 'S':
                    y = sum(ch == 'S' for ch in way[:i]) + 1
                    return 'S'*y + 'E'*n + 'S'*(n-y)
        elif way[0] == 'S':
            for i, char in enumerate(way):
                if way[i] == way[i+1] and way[i] == 'E':
                    y = sum(ch == 'E' for ch in way[:i]) + 1
                    return 'E'*y + 'S'*n + 'E'*(n-y)

    else:
        if way[0] == 'E':
            return 'S'*n + 'E'*n
        elif way[0] == 'S':
            return 'E'*n + 'S'*n


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n = int(input())
        way = input()
        path = solve(n-1, way)
        print("CASE #{}: {}".format(case, path))


read_input()
# print(solve(5, 'SEEEESSS'))
