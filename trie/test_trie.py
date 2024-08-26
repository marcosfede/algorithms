import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        words = ["apple", "app", "apricot", "banana"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertFalse(self.trie.search("grape"))
        self.assertFalse(self.trie.search("ap"))

    def test_delete(self):
        words = ["apple", "app", "apricot", "banana"]
        for word in words:
            self.trie.insert(word)

        self.assertTrue(self.trie.delete("apple"))
        self.assertFalse(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))

        self.assertTrue(self.trie.delete("banana"))
        self.assertFalse(self.trie.search("banana"))

        self.assertFalse(self.trie.delete("grape"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.delete(""))
        self.assertFalse(self.trie.search(""))

    def test_long_word(self):
        long_word = "a" * 1000
        self.trie.insert(long_word)
        self.assertTrue(self.trie.search(long_word))
        self.assertTrue(self.trie.delete(long_word))
        self.assertFalse(self.trie.search(long_word))

if __name__ == "__main__":
    unittest.main()
