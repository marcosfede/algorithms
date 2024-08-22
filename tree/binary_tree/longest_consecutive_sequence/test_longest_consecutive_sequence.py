import unittest
from longest_consecutive_sequence import Node, longest_consecutive

class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_example_case(self):
        root = Node(1)
        root.right = Node(3)
        root.right.left = Node(2)
        root.right.right = Node(4)
        root.right.right.right = Node(5)
        self.assertEqual(longest_consecutive(root), 3)

    def test_empty_tree(self):
        self.assertEqual(longest_consecutive(None), 0)

    def test_single_node(self):
        root = Node(1)
        self.assertEqual(longest_consecutive(root), 1)

    def test_no_consecutive_sequence(self):
        root = Node(1)
        root.left = Node(3)
        root.right = Node(5)
        self.assertEqual(longest_consecutive(root), 1)

    def test_multiple_consecutive_sequences(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.right = Node(4)
        root.right.right = Node(5)
        root.right.right.right = Node(6)
        self.assertEqual(longest_consecutive(root), 3)

if __name__ == '__main__':
    unittest.main()
