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

    def test_common_prefixes(self):
        words = ["car", "card", "carpet", "carpool", "cat"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertTrue(self.trie.search("car"))
        self.assertFalse(self.trie.search("carp"))

    def test_delete_common_prefixes(self):
        words = ["car", "card", "carpet"]
        for word in words:
            self.trie.insert(word)

        self.assertTrue(self.trie.delete("card"))
        self.assertFalse(self.trie.search("card"))
        self.assertTrue(self.trie.search("car"))
        self.assertTrue(self.trie.search("carpet"))

    def test_prefix_search(self):
        words = ["apple", "app", "application", "apply"]
        for word in words:
            self.trie.insert(word)

        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("ap"))

    def test_single_character_words(self):
        words = ["a", "b", "c", "ab", "bc"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertTrue(self.trie.delete("a"))
        self.assertFalse(self.trie.search("a"))
        self.assertTrue(self.trie.search("ab"))

    def test_case_sensitivity(self):
        words = ["Apple", "apple", "APPLE", "bAnAnA"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertFalse(self.trie.search("aPpLe"))
        self.assertTrue(self.trie.delete("Apple"))
        self.assertFalse(self.trie.search("Apple"))
        self.assertTrue(self.trie.search("apple"))

    def test_special_characters(self):
        words = ["hello!", "@world", "#python", "$100"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertFalse(self.trie.search("hello"))
        self.assertFalse(self.trie.search("world"))

    def test_complex_operations(self):
        words = ["tree", "trie", "algo", "algorithm", "algorithms"]
        for word in words:
            self.trie.insert(word)

        self.assertTrue(self.trie.search("algo"))
        self.assertTrue(self.trie.delete("algorithm"))
        self.assertFalse(self.trie.search("algorithm"))
        self.assertTrue(self.trie.search("algorithms"))

        self.trie.insert("algorithmic")
        self.assertTrue(self.trie.search("algorithmic"))
        self.assertFalse(self.trie.search("algorithm"))

    def test_unicode_characters(self):
        words = ["café", "résumé", "über", "naïve"]
        for word in words:
            self.trie.insert(word)
        for word in words:
            self.assertTrue(self.trie.search(word))
        self.assertFalse(self.trie.search("cafe"))
        self.assertFalse(self.trie.search("resume"))

    def test_mixed_operations(self):
        self.trie.insert("programming")
        self.trie.insert("program")
        self.assertTrue(self.trie.search("program"))
        self.trie.delete("programming")
        self.assertFalse(self.trie.search("programming"))
        self.assertTrue(self.trie.search("program"))
        self.trie.insert("progress")
        self.assertTrue(self.trie.search("progress"))

    def test_empty_trie(self):
        self.assertFalse(self.trie.search("any"))
        self.assertFalse(self.trie.delete("any"))

if __name__ == "__main__":
    unittest.main()
