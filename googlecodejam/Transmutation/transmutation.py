from collections import Counter


def ingredients(this, quantities, dict, blacklist):
    if this in blacklist:
        return None
    if quantities[this] > 0:
        return [this]
    newset = set(blacklist)
    newset.add(this)
    left = ingredients(dict[this][0], quantities, dict, newset)
    right = ingredients(dict[this][1], quantities, dict, newset)
    if left is None or right is None:
        return None
    return left + right

def is_possible(ing_counter, quantities):
    for key, value in ing_counter.items():
        if value > quantities[key]:
            return False

    return True

def solve(dict, quantities):
    counter = 0
    while True:
        ings = ingredients(1, quantities, dict, set())
        if ings is None:
            return counter
        ing_counter = Counter(ings)
        if not is_possible(ing_counter, quantities):
            break
        while is_possible(ing_counter, quantities):
            flag = True
            for key, value in ing_counter.items():
                quantities[key] -= ing_counter[key]
            counter += 1

    return counter


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n = int(input())
        dict = {}
        for i in range(1, n + 1):
            dict[i] = list(map(int, input().split(" ")))
        quantities = [0] + list(map(int, input().split(" ")))
        sol = solve(dict, quantities)
        print('CASE #{}: {}'.format(case, sol))


read_input()
# print(solve({1: [3, 4], 2: [3, 4], 3: [4, 5], 4: [3, 5], 5: [1, 3]}, [0, 0, 8, 6, 2, 4]))
#
