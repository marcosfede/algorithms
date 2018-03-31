import heapq
from collections import namedtuple


class MaxHeap:
    def __init__(self, initial, key=lambda x: x):
        self.key = key
        self.data = [(key(item), item) for item in initial]
        heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self.data)[1]

    def peek(self):
        return self.data[0]


def solve(people_arr):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ngroups = len(people_arr)
    total = sum(people_arr)
    Party = namedtuple('Party', ['people', 'name'])
    people = [Party(p, letters[p]) for p in people_arr]
    heap = MaxHeap(people, lambda party: -1*party[0])
    while total > 0:
        top = heap.pop()
        


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        groups = int(input())
        people_per_group = map(int, input().split(" "))
        plan = solve(people_per_group)
        print('CASE #{}: {}'.format(case, plan))


# read_input()
print(solve([2, 2]))
print(solve([3, 2, 2]))
print(solve([1, 1, 2]))
print(solve([2, 3, 1]))
