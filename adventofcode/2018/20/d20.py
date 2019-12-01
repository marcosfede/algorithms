from collections import namedtuple, defaultdict, deque


class Vector(namedtuple('V2D', ['x', 'y'])):

    def __add__(self, other):
        return Vector(self.x + other.x, self.y+other.y)


up = Vector(0, 1)
down = Vector(0, -1)
right = Vector(1, 0)
left = Vector(-1, 0)

direction_map = {'N': up, 'S': down, 'E': right, 'W': left}


with open('./20/input.txt') as f:
    regex = f.read().strip()[1:-1]


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)

    def add_edge(self, a, b):
        for node in [a, b]:
            if node not in self.nodes:
                self.nodes.add(node)
        self.edges[a].add(b)

    def bfs(self, start):
        q = deque([(start, 0)])
        distances = {}
        distances[start] = 0
        distance = 0
        while q:
            this, distance = q.pop()
            for edge in self.edges[this]:
                if edge not in distances:
                    distances[edge] = distance + 1
                    q.appendleft((edge, distance+1))
        return distances


def parse(regex, graph):
    start = Vector(0, 0)
    stack = []
    fork_results = []
    heads = set([start])

    for char in regex:
        if char == '(':
            stack.append(heads)
            fork_results.append(set())
        elif char == '|':
            fork_results[-1].update(heads)
            heads = stack[-1]
        elif char == ')':
            fork_results[-1].update(heads)
            heads = fork_results.pop()
            stack.pop()
        else:
            newheads = set()
            for head in heads:
                newhead = head + direction_map[char]
                graph.add_edge(head, newhead)
                newheads.add(newhead)
            heads = newheads


graph = Graph()
start = Vector(0, 0)
graph = Graph()
parse(regex, graph)
distances = graph.bfs(start)
# p1
print(max(distances.values()))

# p2
print(sum(1 for pos, dist in distances.items() if dist >= 1000))
