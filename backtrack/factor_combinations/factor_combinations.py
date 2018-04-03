from functools import reduce
from math import sqrt, floor


# Iterative:

def getFactors(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n // i]),
                todo.append([n // i, i, combi + [i]])  # python3: n // i
            i += 1
    return combis


# Recursive:

def getFactorsR(n):
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n // i]),
                factor(n // i, i, combi + [i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])


print(getFactorsR(16))
