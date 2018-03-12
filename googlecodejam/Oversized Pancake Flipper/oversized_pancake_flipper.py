from typing import List


# calculates all possible (2^n) substets of a set
def subsets(collection: List[int]):
    n = len(collection)
    for comb in range(2 ** n):
        indexes = bin(comb)[2:]
        ans = []
        for i, x in enumerate(reversed(indexes)):
            if x == '1':
                ans.append(collection[i])
        yield ans


flipmap = {'-': '+', '+': '-'}


# brute force solution  O(2^(N-K+1))
def solve_bruteforce(pancakes: str, k: int) -> int:
    pancakes = list(pancakes)
    n = len(pancakes)
    flips = list(range(0, n - k + 1))
    solutions = []
    for flipcombination in subsets(flips):
        turned_pancakes = pancakes[:]
        for flip in flipcombination:
            for index in range(flip, flip + k):
                turned_pancakes[index] = flipmap[turned_pancakes[index]]
        if all(x == "+" for x in turned_pancakes):
            solutions.append(len(flipcombination))
    if len(solutions) == 0:
        return -1
    return min(solutions)


def read_input():
    n = int(input())
    for case in range(1, n + 1):
        pancakes, size = input().split(" ")
        size = int(size)
        solution = solve_bruteforce(pancakes, size)
        if solution == -1:
            print(f"CASE #{case}: IMPOSSIBLE")
        else:
            print(f'CASE #{case}: {solution}')


read_input()
