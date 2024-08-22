import unittest
from .novel_tree_algorithm import TreeNode, find_deepest_leaf

class TestNovelTreeAlgorithm(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(find_deepest_leaf(None), (None, 0))

    def test_single_node_tree(self):
        root = TreeNode(1)
        node, depth = find_deepest_leaf(root)
        self.assertEqual(node.val, 1)
        self.assertEqual(depth, 0)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        node, depth = find_deepest_leaf(root)
        self.assertIn(node.val, [4, 5, 6, 7])
        self.assertEqual(depth, 2)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.left = TreeNode(6)
        node, depth = find_deepest_leaf(root)
        self.assertEqual(node.val, 6)
        self.assertEqual(depth, 3)

    def test_left_heavy_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        node, depth = find_deepest_leaf(root)
        self.assertEqual(node.val, 4)
        self.assertEqual(depth, 3)

    def test_right_heavy_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        node, depth = find_deepest_leaf(root)
        self.assertEqual(node.val, 4)
        self.assertEqual(depth, 3)

if __name__ == '__main__':
    unittest.main()
