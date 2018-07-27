import sys
from collections import defaultdict


def out(s):
    sys.stdout.write(str(s) + '\n')
    sys.stdout.flush()


def err(s):
    sys.stderr.write('ERR' + str(s))
    sys.stderr.flush()


def read():
    return list(map(int, input().split(" ")))


def solve(N):
    sold = []
    probs = defaultdict(lambda: 0)
    for i in range(0, N):
        flavors = read()
        if flavors[0] == -1:
            return sys.exit(0)
        flavors = flavors[1:]
        for f in flavors:
            probs[f] += 1
        flavor = None
        prob_min = 500
        for f in flavors:
            if probs[f] <= prob_min and f not in sold:
                prob_min = probs[f]
                flavor = f
        if flavor is None:
            out(-1)
        else:
            out(flavor)
            sold.append(flavor)


def read_input():
    ncases = int(input())
    for case in range(0, ncases):
        N = int(input())
        solve(N)
    sys.exit(0)


read_input()
