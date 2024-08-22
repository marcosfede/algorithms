class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def new_tree_algorithm(root):
    """
    This function implements an inorder traversal algorithm.
    
    Args:
    root (TreeNode): The root node of the binary tree.
    
    Returns:
    list: The inorder traversal of the binary tree.
    """
    def inorder_traversal(node, result):
        if node:
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)
    
    result = []
    inorder_traversal(root, result)
    return result

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = new_tree_algorithm(root)
    print(f"Inorder traversal of the binary tree: {result}")
