
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def find_deepest_left(root):
    best_depth = 0
    best_node = None

    # stack elements are [node, is_left, depth]
    stack = [[root, False, 0]]
    while stack:
        this, is_left, depth = stack.pop()
        if is_left and depth > best_depth:
            best_depth = depth
            best_node = this
        if this.right is not None:
            stack.append([this.right, False, depth+1])
        if this.left is not None:
            stack.append([this.left, True, depth+1])

    return best_node


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)
    root.left.left.right = Node(8)

    assert find_deepest_left(root).val == 4
