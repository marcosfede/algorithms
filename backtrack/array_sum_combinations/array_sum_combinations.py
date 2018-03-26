from collections import Counter
from itertools import product


# Can be improved via FFT
# https://cstheory.stackexchange.com/questions/32036/finding-witness-in-minkowski-sum-of-integers


def sum_combinations(target, *arrs):
    counter_last = Counter(arrs[-1])
    for combination in product(*arrs[:-1]):
        difference = target - sum(combination)
        if difference in counter_last:
            for repeated in range(counter_last[difference]):
                yield combination + (difference,)


A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [1, 2, 2, 2]
target = 7

solution = list(sum_combinations(target, A, B, C))

print(len(solution))
for combination in solution:
    print(combination)
