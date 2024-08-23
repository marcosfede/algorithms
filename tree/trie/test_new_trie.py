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

    def test_words_with_common_prefixes(self):
        words = ["tree", "trie", "try", "triangle", "trap"]
        for word in words:
            self.trie.insert(word)
        for word in words:
            self.assertTrue(self.trie.search(word))
        self.assertFalse(self.trie.search("tr"))
        self.assertFalse(self.trie.search("tria"))

    def test_prefix_search(self):
        self.trie.insert("programming")
        self.assertTrue(self.trie.search("programming"))
        self.assertFalse(self.trie.search("program"))
        self.assertFalse(self.trie.search("prog"))

    def test_single_character_words(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.trie.insert(char)
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(self.trie.search(char))
        self.assertFalse(self.trie.search(""))

    def test_similar_non_existent_words(self):
        self.trie.insert("hello")
        self.trie.insert("world")
        self.assertFalse(self.trie.search("hell"))
        self.assertFalse(self.trie.search("worl"))
        self.assertFalse(self.trie.search("he"))
        self.assertFalse(self.trie.search("wo"))

if __name__ == "__main__":
    unittest.main()
