class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf(node):
    return node and not node.left and not node.right

def add_left_boundary(root, result):
    current = root.left
    while current:
        if not is_leaf(current):
            result.append(current.val)
        if current.left:
            current = current.left
        else:
            current = current.right

def add_leaves(root, result):
    if is_leaf(root):
        result.append(root.val)
    else:
        if root.left:
            add_leaves(root.left, result)
        if root.right:
            add_leaves(root.right, result)

def add_right_boundary(root, result):
    current = root.right
    temp = []
    while current:
        if not is_leaf(current):
            temp.append(current.val)
        if current.right:
            current = current.right
        else:
            current = current.left
    result.extend(temp[::-1])

def boundary_traversal(root):
    result = []
    if not root:
        return result

    if not is_leaf(root):
        result.append(root.val)

    add_left_boundary(root, result)
    add_leaves(root, result)
    add_right_boundary(root, result)

    return result

# Example usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.right.right.left = TreeNode(10)
    root.right.right.right = TreeNode(11)

    # Perform boundary traversal
    print("Boundary traversal:", boundary_traversal(root))
