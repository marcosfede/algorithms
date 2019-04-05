def solve(arr):
    n = len(arr)
    evens = arr[::2]
    odds = arr[1::2]
    sorted_evens = sorted(evens)
    sorted_odds = sorted(odds)
    flat = []
    for x in range(n // 2):
        flat.append(sorted_evens[x])
        flat.append(sorted_odds[x])
    if n % 2 == 1:
        flat.append(sorted_evens[-1])

    for i in range(n - 1):
        if flat[i] > flat[i + 1]:
            return i
    return 'OK'


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        size = input()
        arr = list(map(int, input().split(" ")))
        sol = solve(arr)
        print("CASE #{}: {}".format(case, sol))


read_input()
