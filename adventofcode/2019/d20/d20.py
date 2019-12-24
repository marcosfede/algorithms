from collections import namedtuple
from itertools import groupby
import heapq
import networkx as nx


class PrioritizedItem:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        return (self.item, self.priority) == (other.item, other.priority)

    def __lt__(self, other):
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self, initial, key=lambda x: x):
        self.key = key
        self.data = [PrioritizedItem(item, key(item)) for item in initial]
        heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, PrioritizedItem(item, self.key(item)))

    def pop(self):
        return heapq.heappop(self.data).item

    def peek(self):
        return self.data[0]

    def __len__(self):
        return len(self.data)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __mul__(self, num):
        return Vec2d(self.x*num, self.y*num)

    def __eq__(self, other):
        return type(self) == type(other) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'({self.x},{self.y})'


right, up, left, down = Vec2d(1, 0), Vec2d(0, 1), Vec2d(-1, 0), Vec2d(0, -1)
deltas = [right, up, left, down]
Door = namedtuple('Door', ['name', 'outer'])

G = nx.Graph()
with open('./input.txt') as f:
    grid = [list(row) for row in f.readlines()]
    R = len(grid)
    C = max(len(row) for row in grid)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '.':
                p1 = Vec2d(x, y)
                for delta in deltas:
                    p2 = p1 + delta
                    p3 = p2 + delta
                    try:
                        p2c = grid[p2.y][p2.x]
                        if p2c == '#':
                            continue
                        if p2c == '.':
                            G.add_edge(p1, p2, weight=1)
                        else:
                            is_outer = (p2.y < 2) or (
                                p2.y >= R - 3) or (p2.x < 2) or (p2.x >= C - 3)
                            if delta == right:
                                n2 = p2c + grid[p3.y][p3.x]
                            elif delta == left:
                                n2 = grid[p3.y][p3.x] + p2c
                            elif delta == up:
                                n2 = p2c + grid[p3.y][p3.x]
                            elif delta == down:
                                n2 = grid[p3.y][p3.x] + p2c
                            if n2 == 'AA' or n2 == 'ZZ':
                                G.add_edge(p1, Door(n2, is_outer), weight=0)
                            else:
                                G.add_edge(p1, Door(n2, is_outer), weight=0.5)
                    except IndexError:
                        continue

doors = sorted([d for d in G.nodes() if isinstance(d, Door)],
               key=lambda d: d.name)
for name, drs in groupby(doors, lambda d: d.name):
    for d1 in drs:
        for d2 in drs:
            if d1 != d2:
                G.add_edge(d1, d2, weight=0)

# p1
start = Door('AA', True)
end = Door('ZZ', True)
print('part1: ', nx.shortest_path_length(G, start, end, weight='weight'))

# p2
State = namedtuple('State', ['node', 'distance', 'depth'])
Q = PriorityQueue([State(start, 0, 0)], key=lambda x: x.distance)
SEEN = set()

while Q:
    node, distance, depth = Q.pop()
    key = (node, depth)
    if key in SEEN:
        continue
    else:
        SEEN.add(key)
    if depth == 0 and node == end:
        print('part2: ', distance)
        break
    for nxt in G.neighbors(node):
        nxt_depth = depth
        if isinstance(node, Door) and isinstance(nxt, Door):
            nxt_depth += (-1 if node.outer else 1)
            if nxt_depth < 0:
                continue
        if (nxt, nxt_depth) not in SEEN:
            Q.push(State(nxt, distance + G.get_edge_data(node, nxt)
                         ['weight'], nxt_depth))
