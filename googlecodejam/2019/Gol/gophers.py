#!/usr/local/bin/python3
import sys


from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def log(*args):
    print(*args, file=sys.stderr)


def read_input():
    t, n, m = list(map(int, input().split(' ')))
    for case in range(1, t + 1):
        responses = []
        for prime in [2, 3, 5, 7, 11, 13, 17]:
            print(' '.join([str(x) for x in [prime]*18]))
            responses.append(sum(list(map(int, input().split(' ')))))
        print(chinese_remainder([2, 3, 5, 7, 11, 13, 17], responses))
        veredict = input()
        log('veredict', veredict)



read_input()
