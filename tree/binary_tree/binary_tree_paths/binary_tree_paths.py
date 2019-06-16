class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def paths(root):
    res = []
    dfs(res, root, str(root.val))
    return res


def dfs(res, root, cur):
    if not root.left and not root.right:
        res.append(cur)
    if root.left:
        dfs(res, root.left, cur + '->' + str(root.left.val))
    if root.right:
        dfs(res, root.right, cur + '->' + str(root.right.val))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)
    print(paths(root))
