class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeTraversal:
    def inorder_traversal(self, root):
        result = []
        self._inorder(root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
    
    def preorder_traversal(self, root):
        result = []
        self._preorder(root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def postorder_traversal(self, root):
        result = []
        self._postorder(root, result)
        return result
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)

# Example usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    traversal = BinaryTreeTraversal()

    print("Inorder traversal:", traversal.inorder_traversal(root))
    print("Preorder traversal:", traversal.preorder_traversal(root))
    print("Postorder traversal:", traversal.postorder_traversal(root))
