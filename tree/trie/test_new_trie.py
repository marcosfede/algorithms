import unittest
from new_trie import Trie

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

    def test_multiple_words(self):
        words = ["apple", "app", "apricot", "banana", "bat"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("ba"))
        self.assertFalse(self.trie.starts_with("c"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))

if __name__ == "__main__":
    unittest.main()
