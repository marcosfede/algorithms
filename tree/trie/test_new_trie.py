import unittest
from new_trie import NewTrie

class TestNewTrie(unittest.TestCase):
    def setUp(self):
        self.trie = NewTrie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("appl"))

    def test_startswith(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("app"))
        self.assertTrue(self.trie.startsWith("appl"))
        self.assertFalse(self.trie.startsWith("b"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.startsWith(""))

    def test_single_character(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"))
        self.assertTrue(self.trie.startsWith("a"))
        self.assertFalse(self.trie.search("b"))

    def test_long_word(self):
        long_word = "abcdefghijklmnopqrstuvwxyz"
        self.trie.insert(long_word)
        self.assertTrue(self.trie.search(long_word))
        self.assertTrue(self.trie.startsWith("abcdef"))

    def test_case_sensitivity(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("Apple"))
        self.assertFalse(self.trie.startsWith("App"))

    def test_multiple_words(self):
        words = ["apple", "app", "apricot", "banana"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertTrue(self.trie.startsWith("ap"))
        self.assertTrue(self.trie.startsWith("ban"))
        self.assertTrue(self.trie.startsWith("banan"))

if __name__ == "__main__":
    unittest.main()
