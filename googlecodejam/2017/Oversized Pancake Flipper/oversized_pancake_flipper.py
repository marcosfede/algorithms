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


# O(n^2)
# each pancake needs to be flipped at some point and order does not matter
# flip from left to right and decide at the end
def solve_flipping(pancakes: str, k: int) -> int:
    i = 0
    n = len(pancakes)
    pancakes = list(pancakes)
    flips = 0
    while i <= n - k:
        if pancakes[i] == '-':
            flips += 1
            for idx in range(i, i + k):
                pancakes[idx] = flipmap[pancakes[idx]]
        i += 1
    if all(p == '+' for p in pancakes[i:n]):
        return flips
    return -1


# O(n)
# same as above but keeps a count of owed flips to avoid flipping each pancake
def solve(pancakes: str, k: int) -> int:
    i = 0
    n = len(pancakes)
    pancakes = list(pancakes)
    flips = 0
    flipaux = 0
    changeaux = set()

    def should_flip(index):
        return (pancakes[index] == '-' and flipaux % 2 == 0) or (pancakes[index] == '+' and flipaux % 2 == 1)

    while i <= n - k:
        if i in changeaux:
            flipaux += 1
        if should_flip(i):
            flips += 1
            flipaux += 1
            changeaux.add(i + k)
        i += 1

    for idx in range(i, n):
        if idx in changeaux:
            flipaux += 1
        if should_flip(idx):
            return -1
    return flips


def read_input():
    n = int(input())
    for case in range(1, n + 1):
        pancakes, size = input().split(" ")
        size = int(size)
        solution = solve(pancakes, size)
        if solution == -1:
            print(f"CASE #{case}: IMPOSSIBLE")
        else:
            print(f'CASE #{case}: {solution}')


if __name__ == '__main__':
    read_input()
