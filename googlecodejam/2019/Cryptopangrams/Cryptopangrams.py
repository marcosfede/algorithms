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
