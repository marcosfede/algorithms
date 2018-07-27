from itertools import product
import re


# alternative LAZY product impl
# def product(arr, repeat):
#     if repeat == 1:
#         for e in arr:
#             yield [e]
#     else:
#         for el in arr:
#             for prod in product(arr, repeat - 1):
#                 yield [el] + prod


def int2base(n, b):
    if n == 0:
        return [0]

    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


# alternative algo using base 4 numbers


def solve2(num, target):
    n = len(num)
    possibilities = 4 ** (n - 1)
    operator_map = ["", "+", "*", "-"]
    for comb_base10 in range(possibilities):
        comb_base4 = int2base(comb_base10, 4)
        comb_base4 = "".join(map(str, comb_base4)).zfill(n - 1)
        comb = list(map(lambda x: operator_map[int(x)], comb_base4))
        solution = []
        for i in range(n - 1):
            solution.append(num[i])
            solution.append(comb[i])
        solution.append(num[-1])
        solution = "".join(solution)
        if calc(solution) == target:
            yield solution


def calc(string):
    # hack to patch eval around leading zeroes
    stripped = re.sub(r"\b0+(?!\b)", "", string)
    return eval(stripped)


def solve(num, target):
    n = len(num)
    for comb in product(["", "+", "*", "-"], repeat=(n - 1)):
        solution = []
        # interleave numbers with operators
        for i in range(n - 1):
            solution.append(num[i])
            solution.append(comb[i])
        solution.append(num[-1])
        solution = "".join(solution)
        if calc(solution) == target:
            yield solution


# "123", 6 -> ["1+2+3", "1*2*3"]
print(list(solve("123", 6)))

# "232", 8 -> ["2*3+2", "2+3*2"]
print(list(solve("232", 8)))

# "123045", 3 -> ['1+2+3*0*4*5', '1+2-3*0*4*5', '1*2+3*0-4+5', '1*2-3*0-4+5', '1-2+3+0-4+5', '1-2+3-0-4+5']
print(list(solve("123045", 3)))

print(list(solve("105", 5)))
