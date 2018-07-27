def solve(n, w):
    accum = 0
    indexes = set()
    for i in range(n):
        slice = [w[idx] if idx in indexes else 0 for idx in range(i)] + [w[i]]
        can_support = w[i]*6 - accum
        if can_support < 0:
            max = 0
            for idx, el in enumerate(slice):
                if el > max:
                    max = el
                    idxmax = idx
            if idxmax in indexes:
                indexes.remove(idxmax)
                indexes.add(i)
                accum = accum - w[idxmax] + w[i]

        else:
            indexes.add(i)
            accum += w[i]
    return len(indexes)


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n = int(input())
        w = list(map(int, input().split(" ")))
        sol = solve(n, w)
        print('CASE #{}: {}'.format(case, sol))


read_input()
# print(solve(2, [9, 1]))
# print(solve(3, [8, 4, 100]))
# print(solve(9, [10, 10, 10, 10, 10, 10, 10, 10, 100]))
# print(solve(12, [1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 10]))
# print(solve(13, [1, 1, 1, 1, 1, 1, 1, 30, 40, 8, 8, 8, 8]))
# print(solve(13, [1, 1, 1, 1, 1, 1, 1, 1, 40, 3, 2, 1, 10]))
# ARR = [1, 1, 1, 3, 4, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,100, 2, 2, 3, 4, 30, 3, 4, 4, 5, 6, 3, 2, 7, 8, 9, 11, 13, 15]
# print(solve(len(ARR), ARR ))