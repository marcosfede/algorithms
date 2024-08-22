class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def new_tree_algorithm(root):
    """
    This function calculates the sum of all nodes at each level of a binary tree.
    
    Args:
    root (TreeNode): The root node of the binary tree.
    
    Returns:
    list: A list where each element is the sum of node values at the corresponding level.
    """
    if not root:
        return []
    
    level_sums = []
    current_level = [root]
    
    while current_level:
        level_sum = sum(node.val for node in current_level)
        level_sums.append(level_sum)
        
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        current_level = next_level
    
    return level_sums

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = new_tree_algorithm(root)
    print(f"Sum of nodes at each level: {result}")
