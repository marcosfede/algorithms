import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("apples"))

    def test_starts_with(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("apple"))
        self.assertFalse(self.trie.starts_with("apq"))

    def test_delete(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.delete("apple"))
        self.assertFalse(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertFalse(self.trie.delete("apple"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))
        self.assertTrue(self.trie.delete(""))

    def test_case_sensitivity(self):
        self.trie.insert("Apple")
        self.assertTrue(self.trie.search("Apple"))
        self.assertFalse(self.trie.search("apple"))

    def test_non_alphabetic_characters(self):
        self.trie.insert("hello123")
        self.assertTrue(self.trie.search("hello123"))
        self.assertFalse(self.trie.search("hello"))

    def test_overlapping_prefixes(self):
        self.trie.insert("car")
        self.trie.insert("carpet")
        self.assertTrue(self.trie.search("car"))
        self.assertTrue(self.trie.search("carpet"))
        self.assertTrue(self.trie.starts_with("car"))

    def test_delete_prefix(self):
        self.trie.insert("car")
        self.trie.insert("carpet")
        self.assertTrue(self.trie.delete("car"))
        self.assertFalse(self.trie.search("car"))
        self.assertTrue(self.trie.search("carpet"))

if __name__ == '__main__':
    unittest.main()
