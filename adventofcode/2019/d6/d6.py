from collections import defaultdict

orbits = []

with open('./input.txt') as f:
    for i, line in enumerate(f):
        orbits.append((line[:3], line[4:7]))

children_by_key = defaultdict(set)
parent_by_key = {}
for orbit in orbits:
    parent, node = orbit
    children_by_key[parent].add(node)
    parent_by_key[node] = parent


def depth(node):
    if node not in parent_by_key:
        return 0
    return depth(parent_by_key[node]) + 1


def get_ancestors(node):
    if node in parent_by_key:
        parent = parent_by_key[node]
        return get_ancestors(parent) + [parent]
    else:
        return []


def common_ancestor(node1, node2):
    ancestors1 = get_ancestors(node1)
    ancestors2 = get_ancestors(node2)
    max_i = min(len(ancestors1), len(ancestors2))
    i = 0
    while i < max_i and ancestors1[i] == ancestors2[i]:
        i += 1
    if i == 0:
        return None
    return ancestors1[i-1]


def calc_moves(source, target):
    ancestor = common_ancestor(source, target)
    return depth(target) + depth(source) - 2*depth(ancestor)


# p1
print(sum(depth(node) for node in parent_by_key))

# p2
print(calc_moves('YOU', 'SAN')-2)
