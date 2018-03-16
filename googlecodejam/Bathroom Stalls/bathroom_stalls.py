import heapq
from math import ceil, floor
from collections import Counter
from decimal import Decimal


# python heapq is a min heap so we need to invert the signs

# O(k*log(k))
def solve2(n, k):
    heap = [-1 * n]

    for step in range(1, k + 1):
        x = -1 * heapq.heappop(heap)
        x0 = ceil((x - 1) / 2)
        x1 = floor((x - 1) / 2)
        if step == k:
            return x0, x1
        heapq.heappush(heap, -1 * x0)
        heapq.heappush(heap, -1 * x1)


# using decimal cause of float precision
# there can only be 4 elements in the set or counter at the same time
# so the max op is bounded by constant time. steps are the number of times
# it goes through the loop which is  O(log(n))
def solve(n, k):
    s = {Decimal(n)}
    counter = Counter()
    counter[n] = 1
    p = 0
    while True:
        x = max(s)
        x0 = Decimal(ceil((x - 1) / 2))
        x1 = Decimal(floor((x - 1) / 2))
        cx = counter[x]
        p += cx
        if p >= k:
            return int(x0), int(x1)
        s.remove(x)
        counter.pop(x)
        s.add(x0)
        s.add(x1)
        counter[x0] += cx
        counter[x1] += cx


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n, k = map(int, input().split(" "))
        mx, mn = solve(n, k)
        print(f'CASE #{case}: {mx} {mn}')


read_input()
