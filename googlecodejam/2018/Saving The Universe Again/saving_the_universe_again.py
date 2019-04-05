def calculate_damage(p, d):
    damage = 1
    total = 0
    for i in range(len(p)):
        if p[i] == 'C':
            damage *= 2
        else:
            total += damage
    return total <= d


def is_impossible(p, d):
    counter = 0
    for c in p:
        if c == 'S':
            counter += 1
    return counter > d


def swap(string, i, j):
    lst = list(string)
    lst[i], lst[j] = lst[j], lst[i]
    return "".join(lst)


def solve(p, d):
    swap_count = 0
    i = len(p) - 1
    if calculate_damage(p, d):
        return swap_count
    if is_impossible(p, d):
        return 'IMPOSSIBLE'
    while i >= 0:
        while p[i] == 'C' and i >= 0:
            i -= 1
        while p[i] == 'S' and i >= 0:
            i -= 1
        j = i
        while True:
            if j == len(p) - 1 or p[j + 1] == 'C':
                break
            p = swap(p, j, j + 1)
            j += 1
            swap_count += 1
            if calculate_damage(p, d):
                return swap_count


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        d, p = input().split(" ")
        d = int(d)
        moves = solve(p, d)
        print("CASE #{}: {}".format(case, moves))


read_input()
