class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_deepest_leaf(root):
    """
    Finds the deepest leaf node in a binary tree.

    :param root: TreeNode, the root of the binary tree
    :return: tuple (TreeNode, int), the deepest leaf node and its depth
    """
    if not root:
        return None, 0

    def dfs(node, depth):
        if not node.left and not node.right:
            return node, depth

        left_node, left_depth = dfs(node.left, depth + 1) if node.left else (None, depth)
        right_node, right_depth = dfs(node.right, depth + 1) if node.right else (None, depth)

        if left_depth >= right_depth:
            return left_node, left_depth
        else:
            return right_node, right_depth

    return dfs(root, 0)

# Example usage and test
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)

    deepest_node, depth = find_deepest_leaf(root)
    print(f"The deepest leaf node value is {deepest_node.val} at depth {depth}")

    # Additional test cases
    # Test case 1: Empty tree
    assert find_deepest_leaf(None) == (None, 0)

    # Test case 2: Tree with only root
    assert find_deepest_leaf(TreeNode(1)) == (TreeNode(1), 0)

    # Test case 3: Balanced tree
    balanced_root = TreeNode(1)
    balanced_root.left = TreeNode(2)
    balanced_root.right = TreeNode(3)
    balanced_root.left.left = TreeNode(4)
    balanced_root.left.right = TreeNode(5)
    balanced_root.right.left = TreeNode(6)
    balanced_root.right.right = TreeNode(7)
    assert find_deepest_leaf(balanced_root)[1] == 2

    print("All test cases passed!")
