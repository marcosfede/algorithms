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

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""), "Should find empty string")
        self.assertTrue(self.trie.startsWith(""), "Should find words starting with empty string")

    def test_single_character(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"), "Should find single character 'a'")
        self.assertTrue(self.trie.startsWith("a"), "Should find words starting with 'a'")
        self.assertFalse(self.trie.search("b"), "Should not find 'b'")

    def test_overlapping_prefixes(self):
        self.trie.insert("car")
        self.trie.insert("carpet")
        self.assertTrue(self.trie.search("car"), "Should find 'car'")
        self.assertTrue(self.trie.search("carpet"), "Should find 'carpet'")
        self.assertFalse(self.trie.search("carp"), "Should not find 'carp'")
        self.assertTrue(self.trie.startsWith("car"), "Should find words starting with 'car'")

    def test_case_sensitivity(self):
        self.trie.insert("Apple")
        self.assertTrue(self.trie.search("Apple"), "Should find 'Apple'")
        self.assertFalse(self.trie.search("apple"), "Should not find 'apple' (case-sensitive)")

    def test_non_existent_word(self):
        self.trie.insert("hello")
        self.assertFalse(self.trie.search("world"), "Should not find non-existent word")
        self.assertFalse(self.trie.startsWith("wo"), "Should not find non-existent prefix")

if __name__ == "__main__":
    unittest.main()
