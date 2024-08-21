class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

# Example usage and test cases
if __name__ == "__main__":
    # Create the binary tree from the example
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Test case 1: p = 5, q = 1
    p, q = root.left, root.right
    result = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {result.val}")  # Expected output: 3

    # Test case 2: p = 5, q = 4
    p, q = root.left, root.left.right.right
    result = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {result.val}")  # Expected output: 5

    # Test case 3: p = 6, q = 4
    p, q = root.left.left, root.left.right.right
    result = lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {result.val}")  # Expected output: 5
