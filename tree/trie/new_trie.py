"""
Implement a new trie algorithm with insert and search functions.

Note:
This implementation assumes all inputs consist of lowercase letters a-z.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class NewTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
