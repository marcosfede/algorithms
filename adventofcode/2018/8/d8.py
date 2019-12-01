from collections import Counter

with open('input') as f:
    nums = list(map(int, f.readline().strip().split(' ')))


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata


def build_tree(tree, start=0):
    nchildren = tree[start+0]
    nmetadata = tree[start+1]
    offset = start + 2
    children = []
    for _ in range(nchildren):
        child, offset = build_tree(tree, start=offset)
        children.append(child)
    return Node(children, tree[offset:offset+nmetadata]), offset+nmetadata


def calc_sum(tree):
    return sum(tree.metadata) + sum(calc_sum(node) for node in tree.children)


def calc_value(tree):
    nchildren = len(tree.children)
    if nchildren == 0:
        return sum(tree.metadata)
    index_allowed_values = set(range(1, nchildren+1))
    indexes = Counter([i for i in tree.metadata if i in index_allowed_values])
    return sum(calc_value(tree.children[i-1])*times for i, times in indexes.items())


root = build_tree(nums)[0]

# p1
print(calc_sum(root))

# p2
print(calc_value(root))
