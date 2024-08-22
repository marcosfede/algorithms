import unittest
from binary_tree_traversal import TreeNode, BinaryTreeTraversal

class TestBinaryTreeTraversal(unittest.TestCase):
    def setUp(self):
        self.traversal = BinaryTreeTraversal()

    def test_empty_tree(self):
        self.assertEqual(self.traversal.inorder_traversal(None), [])
        self.assertEqual(self.traversal.preorder_traversal(None), [])
        self.assertEqual(self.traversal.postorder_traversal(None), [])

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(self.traversal.inorder_traversal(root), [1])
        self.assertEqual(self.traversal.preorder_traversal(root), [1])
        self.assertEqual(self.traversal.postorder_traversal(root), [1])

    def test_sample_tree(self):
        # Create a sample binary tree
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(self.traversal.inorder_traversal(root), [4, 2, 5, 1, 3])
        self.assertEqual(self.traversal.preorder_traversal(root), [1, 2, 4, 5, 3])
        self.assertEqual(self.traversal.postorder_traversal(root), [4, 5, 2, 3, 1])

if __name__ == '__main__':
    unittest.main()
