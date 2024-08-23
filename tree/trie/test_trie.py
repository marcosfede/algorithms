import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("orange")
        self.assertTrue(self.trie.search("orange"))
        self.assertFalse(self.trie.search("ora"))
        self.assertFalse(self.trie.search("orang"))

    def test_startswith(self):
        self.trie.insert("orange")
        self.assertTrue(self.trie.startsWith("ora"))
        self.assertTrue(self.trie.startsWith("orang"))
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
        self.trie.insert("orange")
        self.assertFalse(self.trie.search("Orange"))
        self.assertFalse(self.trie.startsWith("Ora"))

    def test_multiple_words(self):
        words = ["orange", "ora", "orchard", "banana"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertTrue(self.trie.startsWith("or"))
        self.assertTrue(self.trie.startsWith("ban"))
        self.assertTrue(self.trie.startsWith("banan"))

if __name__ == "__main__":
    unittest.main()
