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

    def solve_algorithm(self):
        """
        Implement a level-order traversal (Breadth-First Search) of the binary tree.
        This algorithm visits all nodes of the tree level by level, from left to right.
        
        Returns:
        list: A list of node values in level-order traversal.
        """
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                result.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Basic binary tree
    tree1 = NewTreeAlgorithm()
    for value in [5, 3, 7, 1, 9]:
        tree1.insert(value)
    print("Test case 1 result:", tree1.solve_algorithm())
    # Expected output: [5, 3, 7, 1, 9]

    # Test case 2: Empty tree
    tree2 = NewTreeAlgorithm()
    print("Test case 2 result:", tree2.solve_algorithm())
    # Expected output: []

    # Test case 3: Tree with only right children
    tree3 = NewTreeAlgorithm()
    for value in [1, 2, 3, 4, 5]:
        tree3.insert(value)
    print("Test case 3 result:", tree3.solve_algorithm())
    # Expected output: [1, 2, 3, 4, 5]

    # Test case 4: Balanced binary tree
    tree4 = NewTreeAlgorithm()
    for value in [4, 2, 6, 1, 3, 5, 7]:
        tree4.insert(value)
    print("Test case 4 result:", tree4.solve_algorithm())
    # Expected output: [4, 2, 6, 1, 3, 5, 7]
