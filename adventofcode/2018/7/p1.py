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

# p1

# number of incoming edges for each node
incomings = {k: 0 for k in nodes}
for src, neighbours in edges.items():
    for dest in neighbours:
        incomings[dest] += 1

result = []
# ready tasks
queue = [k for k in nodes if incomings[k] == 0]
heapq.heapify(queue)
while queue:

    curr = heapq.heappop(queue)
    result.append(curr)

    for dest in edges[curr]:
        incomings[dest] -= 1
        if incomings[dest] == 0:
            heapq.heappush(queue, dest)
order = ''.join(result)
print(order)
