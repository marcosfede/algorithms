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

    def __len__(self):
        return len(self.data)


Party = namedtuple('Party', ['people', 'name'])
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Solver:
    def __init__(self, people):
        self.people = [Party(p, letters[i]) for i, p in enumerate(people)]
        self.heap = MaxHeap(self.people, lambda party: -1 * party[0])
        self.total = sum(people)
        self.solution = []

    def pop_senator(self):
        top = self.heap.pop()
        self.total -= 1
        if top.people > 1:
            new = Party(top.people - 1, top.name)
            self.heap.push(new)
        return top

    def evacuate_single_senator(self):
        senator = self.pop_senator()
        self.solution.append(senator.name)

    def evacuate_two_senators(self):
        senator1 = self.pop_senator()
        senator2 = self.pop_senator()
        self.solution.append(senator1.name + senator2.name)

    def solve(self):
        while self.total > 0:
            while len(self.heap) > 2:
                self.evacuate_single_senator()
            self.evacuate_two_senators()
        return " ".join(self.solution)


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        groups = int(input())
        people_per_group = list(map(int, input().split(" ")))
        plan = Solver(people_per_group).solve()
        print('CASE #{}: {}'.format(case, plan))


read_input()
