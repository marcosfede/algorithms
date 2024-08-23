import unittest
from edit_distance import edit_distance

class TestEditDistance(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("horse", "ros"), 3)
        self.assertEqual(edit_distance("intention", "execution"), 5)

    def test_edge_cases(self):
        self.assertEqual(edit_distance("", ""), 0)
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("abc", ""), 3)
        self.assertEqual(edit_distance("abc", "abc"), 0)

    def test_single_character_operations(self):
        self.assertEqual(edit_distance("a", "b"), 1)  # substitution
        self.assertEqual(edit_distance("a", "ab"), 1)  # insertion
        self.assertEqual(edit_distance("ab", "a"), 1)  # deletion

    def test_long_strings(self):
        self.assertEqual(edit_distance("pneumonoultramicroscopicsilicovolcanoconiosis",
                                       "ultramicroscopically"), 27)

if __name__ == '__main__':
    unittest.main()
