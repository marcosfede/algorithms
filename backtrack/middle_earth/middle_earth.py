from itertools import permutations


def score(solution, gold):
    counter = 0
    for town in solution:
        if gold - town[0] >= 0:
            counter += 1
            gold += town[1] - town[0]
        else:
            break
    return counter


def brute_force_checker(towns):
    print('brute force checking')
    easy_towns = [t for t in towns if t[0] <= t[1]]
    hard_towns = [t for t in towns if t[0] > t[1]]

    cost, revenue = map(sum, zip(*easy_towns))
    gold = revenue - cost
    
    best = 0
    best_sol = None
    town_perms = permutations(hard_towns)
    for p in town_perms:
        if score(p, gold) > best:
            best = score(p, gold)
            best_sol = p

    print('best', best)
    print('best sol', best_sol)
    return best + len(easy_towns)
    # return max(score(solution, gold) for solution in town_perms) + len(easy_towns)


def cost_to_raid(towns):
    cost, revenue = map(sum, zip(*towns))
    return cost - revenue


def are_raidable(towns, gold, K):
    if K == 1:
        return gold >= towns[0][0]
    for idx, town in enumerate(towns):
        others = [t for i, t in enumerate(towns) if i != idx]
        if are_raidable(others, gold, K-1):
            if gold - cost_to_raid(others) >= town[0]:
                return True
    return False


def solve(towns, gold):
    easy_towns = sorted([t for t in towns if t[0] <= t[1]], key=lambda x: x[0])
    hard_towns = [t for t in towns if t[0] > t[1]]

    # raid easy
    for t in easy_towns:
        if gold >= t[0]:
            gold += t[1] - t[0]
        else:
            break

    max_raidable = len(hard_towns)
    while max_raidable > 0:
        if are_raidable(hard_towns, gold, max_raidable):
            return max_raidable + len(easy_towns)
        max_raidable -= 1
    return len(easy_towns)


testcases = [
    [(0, 10), (10, 5), (7, 4), (7, 4)],  # [(cost, revenue)]
    [(0, 10), (10, 3), (5, 4), (9, 8), (1, 0)],
    [(0, 10), (10, 9), (9, 4), (4, 3), (3, 2), (2, 1)],
    [(0, 10), (10, 4), (1, 0), (1, 0), (1, 0)],
    [(0, 10), (10, 4), (9, 8), (1, 0), (1, 0), (5, 4)],
    [(0, 10), (10, 2), (2, 1), (2, 1)],
    [(0, 10), (10, 4), (9, 8), (1, 0), (1, 0)],
    [(0, 10), (7, 6), (3, 2), (3, 2), (8, 4)],
]
for testcase in testcases:
    print('new testcase')
    s1 = solve(testcase, 0)
    s2 = brute_force_checker(testcase)
    if s1 != s2:
        print(f'failed testcase {testcase}')
        print(f's1={s1} s2={s2}')
        print(' --- ')
    break
