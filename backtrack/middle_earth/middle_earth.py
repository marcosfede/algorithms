from itertools import permutations


def score(solution, gold):
    counter = 0
    for town in solution:
        if gold - town[0] >= 0:
            counter += 1
            gold -= town[1]
        else:
            break
    return counter


def brute_force_checker(towns, gold):
    ntowns = len(towns)
    perms = permutations(range(ntowns))
    town_perms = ([towns[idx] for idx in perm] for perm in perms)
    return max(score(solution, gold) for solution in town_perms)


def solve(towns, gold):
    current_gold = gold
    counter = 0
    raided = []
    sorted_towns = sorted(towns, key=lambda town: town[1])
    for town in sorted_towns:
        if current_gold - town[0] >= 0:
            raided.append(town)
            current_gold -= town[1]
            counter += 1
        elif score(sorted([town] + raided, key=lambda x: x[0], reverse=True), gold) > counter:
            raided = [town] + raided
            counter += 1
        else:
            break
    return counter


# print(brute_force_checker([(10, 5), (7, 3), (7, 3)], 10))  # 2
# print(brute_force_checker([(10, 7), (5, 1), (9, 1), (1, 1)], 10))  # 3
# print(brute_force_checker([(10, 1), (9, 5), (4, 1), (3, 1), (2, 1)], 10))  # 5
# print(brute_force_checker([(10, 6), (1, 1), (1, 1), (1, 1)], 10))  # 4
# print(brute_force_checker([(10, 6), (9, 1), (1, 1), (1, 1), (5, 1)], 10))  # 4
# print(brute_force_checker([(10, 8), (2, 1), (2, 1)], 10))  # 2
# print(brute_force_checker([(10, 6), (9, 1), (1, 1), (1, 1)], 10))  # 3

# print(solve([(10, 5), (7, 3), (7, 3)], 10))  # 2
# print(solve([(10, 7), (5, 1), (9, 1), (1, 1)], 10))  # 3
print(solve([(10, 1), (9, 5), (4, 1), (3, 1), (2, 1)], 10))  # 5
# print(solve([(10, 6), (1, 1), (1, 1), (1, 1)], 10))  # 4
# print(solve([(10, 6), (9, 1), (1, 1), (1, 1), (5, 1)], 10))  # 4
# print(solve([(10, 8), (2, 1), (2, 1)], 10))  # 2
# print(solve([(10, 6), (9, 1), (1, 1), (1, 1)], 10))  # 3
