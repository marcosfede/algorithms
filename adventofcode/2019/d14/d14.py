import os
import math
from collections import defaultdict, deque

G = {}
with open(os.path.join(os.path.dirname(__file__), 'input1.txt')) as f:
    for line in f:
        mats, outcome = line.strip().split('=>')
        outcome = outcome.strip().split(' ')
        mats = mats.strip().split(', ')
        mats = [mat.split(' ') for mat in mats]
        G[outcome[1]] = {"q": int(outcome[0]), "mats": [
            {"q": int(mat[0]), "mat": mat[1]} for mat in mats], "produces": outcome[1]}


recipies_used = defaultdict(int)


def part1():
    queue = deque([[1, 'FUEL']])
    waste = defaultdict(int)
    ore = 0

    while len(queue) > 0:
        q, mat = queue.popleft()
        # print(f'need {q} of {mat}')
        if mat == 'ORE':
            ore += q
            # print(f'adding for a total of {ore} ORE needed')
            # print()
            continue

        # get from waste first
        # print(f'there is {waste[mat]} in wastes')
        q -= min(waste[mat], q)
        waste[mat] -= min(waste[mat], q)
        # print(f'so i need to produce an extra {q}')

        if q > 0:
            recipe = G[mat]
            # print(
            #     f'using recipe {", ".join([str(mat["q"])+ " " + mat["mat"] for mat in recipe["mats"]])} => {recipe["q"]} {mat}')
            reactions_needed = math.ceil(q/recipe['q'])
            # print(f'reaction will be used {reactions_needed} times, leaving {recipe["q"] * reactions_needed - q} waste')
            for child in recipe['mats']:
                queue.append([reactions_needed * child['q'], child['mat']])
            waste[mat] += recipe['q'] * reactions_needed - q
        # print()

    return ore


print(part1())
