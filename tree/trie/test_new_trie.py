import unittest
from new_trie import NewTrie

class TestNewTrie(unittest.TestCase):
    def setUp(self):
        self.trie = NewTrie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("apples"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))

    def test_common_prefix(self):
        self.trie.insert("cat")
        self.trie.insert("car")
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("car"))
        self.assertFalse(self.trie.search("ca"))

    def test_non_existent_word(self):
        self.trie.insert("hello")
        self.assertFalse(self.trie.search("world"))

if __name__ == "__main__":
    unittest.main()
