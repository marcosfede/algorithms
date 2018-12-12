import heapq
from collections import defaultdict
import re

nodes = set()
edges = defaultdict(set)

with open('input') as f:
    for line in f:
        regex = r'Step (.) must be finished before step (.) can begin\.'
        match = re.match(regex, line)
        src, dest = match.group(1), match.group(2)
        nodes.add(src)
        nodes.add(dest)
        edges[src].add(dest)


def score(x): return ord(x) - 4


timeremaining = {k: score(k) for k in nodes}
# build incoming connections map
incomings = {k: 0 for k in nodes}
for src, neighbours in edges.items():
    for dest in neighbours:
        incomings[dest] += 1

time = 0
queue = [k for k in nodes if incomings[k] == 0]
heapq.heapify(queue)
processing = set()
while queue or processing:
    time += 1
    idle = 5 - len(processing)
    if idle > 0:
        for worker in range(min(idle, len(queue))):
            processing.add(heapq.heappop(queue))

    done = set()
    for task in processing:
        timeremaining[task] -= 1
        if timeremaining[task] == 0:
            done.add(task)
            for dest in edges[task]:
                incomings[dest] -= 1
                if incomings[dest] == 0:
                    heapq.heappush(queue, dest)
    processing -= done

print(time)
