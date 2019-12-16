import os
import math
from collections import defaultdict

G = {}
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    for line in f:
        mats, outcome = line.strip().split('=>')
        outcome = outcome.strip().split(' ')
        mats = mats.strip().split(', ')
        mats = [mat.split(' ') for mat in mats]
        G[outcome[1]] = {"q": int(outcome[0]), "mats": [
            {"q": int(mat[0]), "mat": mat[1]} for mat in mats], "produces": outcome[1]}


recipies_used = defaultdict(int)


def ore_needed(fuel):
    needed = defaultdict(int)
    needed['FUEL'] = fuel
    waste = defaultdict(int)

    while not (len(needed) == 1 and 'ORE' in needed):
        for mat, q in needed.items():
            if mat == 'ORE':
                continue

            q -= min(waste[mat], q)
            waste[mat] -= min(waste[mat], q)

            if q > 0:
                recipe = G[mat]
                reactions_needed = math.ceil(q/recipe['q'])
                for child in recipe['mats']:
                    needed[child['mat']] += reactions_needed * child['q']
                waste[mat] += recipe['q'] * reactions_needed - q
            del needed[mat]
            break

    return needed['ORE']


# p1
print(ore_needed(1))


# p2
def binary_search(func, low, high):
    lo = low
    hi = high

    while lo <= hi:
        if lo == hi:
            return lo
        if lo + 1 == hi:
            return lo + 1 if func(lo + 1) else lo
        mid = (lo + hi) // 2
        if func(mid):
            lo = mid
        else:
            hi = mid - 1


arr = [1, 2, 3, 4, 5, 6]


print(binary_search(lambda fuel: ore_needed(fuel)
                    <= 1000000000000, low=1, high=10000000))
