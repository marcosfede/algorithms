import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"), "Should find 'apple'")
        self.assertFalse(self.trie.search("app"), "Should not find 'app'")

    def test_starts_with(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("app"), "Should find words starting with 'app'")

    def test_multiple_inserts(self):
        self.trie.insert("app")
        self.trie.insert("apricot")
        self.assertTrue(self.trie.search("app"), "Should now find 'app'")
        self.assertTrue(self.trie.startsWith("apr"), "Should find words starting with 'apr'")
        self.assertFalse(self.trie.search("apr"), "Should not find 'apr'")

if __name__ == "__main__":
    unittest.main()
