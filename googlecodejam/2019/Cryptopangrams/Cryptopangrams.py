import random
from math import gcd
chars = 'abcdefghijklmnopqrstuvwxyz'.upper()


def solve(arr):
    primes = [0]*(len(arr)+1)
    for i in range(len(arr)):
        if arr[i] != arr[i+1]:
            break
    _gcd = gcd(arr[i], arr[i+1])
    primes[i] = arr[i] / _gcd
    primes[i+1] = _gcd
    j = i - 1
    while j >= 0:
        primes[j] = arr[j] / primes[j+1]
        j -= 1
    j = i + 2
    while j <= len(arr):
        primes[j] = arr[j-1] / primes[j-1]
        j += 1

    primefirst = arr[0] // primes[0]
    primelast = arr[-1] // primes[-1]
    sorted_primes = sorted(list(set(primes)))
    assert len(sorted_primes) == 26
    prime_to_char = {k: chars[i] for i, k in enumerate(sorted_primes)}
    return ''.join([prime_to_char[c] for c in primes])


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n, l = list(map(int, input().split(' ')))
        arr = list(map(int, input().split(' ')))
        message = solve(arr)
        print("CASE #{}: {}".format(case, message))


read_input()
# print(solve(10000, [3292937, 175597, 18779, 50429, 375469, 1651121, 2102, 3722, 2376497, 611683, 489059, 2328901,
#                     3150061, 829981, 421301, 76409, 38477, 291931, 730241, 959821, 1664197, 3057407, 4267589, 4729181, 5335543]))


# def gen_primes():
#     """ Generate an infinite sequence of prime numbers.
#     """
#     # Maps composites to primes witnessing their compositeness.
#     # This is memory efficient, as the sieve is not "run forward"
#     # indefinitely, but only as long as required by the current
#     # number being tested.
#     #
#     D = {}

#     # The running integer that's checked for primeness
#     q = 2

#     while True:
#         if q not in D:
#             # q is a new prime.
#             # Yield it and mark its first multiple that isn't
#             # already marked in previous iterations
#             #
#             yield q
#             D[q * q] = [q]
#         else:
#             # q is composite. D[q] is the list of primes that
#             # divide it. Since we've reached q, we no longer
#             # need it in the map, but we'll mark the next
#             # multiples of its witnesses to prepare for larger
#             # numbers
#             #
#             for p in D[q]:
#                 D.setdefault(p + q, []).append(p)
#             del D[q]

#         q += 1


# def k_primes_bellow_n(k, n):
#     gen = gen_primes()
#     primes = []
#     p = next(gen)
#     while p < n:
#         p = next(gen)
#         primes.append(p)
#     ans = []
#     while len(ans) < k:
#         nxt = random.choice(primes)
#         if nxt not in ans:
#             ans.append(nxt)
#     assert len(ans) == k
#     return sorted(ans)


# s = 'CJQUIZKNOWBEVYOFDPFIEJALSUQNAWJEJQJQKKKAJLUXALGORITHMS'
# for test in range(2000):
#     xprimes = k_primes_bellow_n(26, 10000)
#     char_to_prime = {char: xprimes[i] for i, char in enumerate(chars)}
#     s_in_primes = [char_to_prime[x] for x in s]
#     prods = [x*y for x, y in zip(s_in_primes, s_in_primes[1:])]
#     # print(s)
#     # print(solve(prods))
#     assert s == solve(prods)
