class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NewTreeAlgorithm:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def algorithm(self):
        # Implement Depth-First Search (DFS) traversal
        def dfs(node):
            if node:
                print(node.value, end=' ')  # Visit the current node
                dfs(node.left)              # Traverse left subtree
                dfs(node.right)             # Traverse right subtree

        print("DFS traversal:")
        dfs(self.root)
        print()  # Add a newline after traversal

# Example usage
if __name__ == "__main__":
    tree = NewTreeAlgorithm()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(9)

    # Call and test the algorithm method
    tree.algorithm()
