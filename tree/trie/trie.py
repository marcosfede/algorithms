"""
Implement a trie (prefix tree) with insert, search, and startsWith methods.

A trie is an efficient information retrieval data structure. It's commonly
used to store and search strings in a space and time efficient way.

Note:
You may assume that all inputs consist of lowercase letters a-z.
"""
from collections import defaultdict


class TrieNode:
    """
    A node in the trie structure.

    Attributes:
        children (defaultdict): Child nodes, keyed by characters.
        is_word (bool): Marks end of a word.
    """
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    """
    Trie data structure for efficient string storage and retrieval.

    A trie, also called a prefix tree, is an ordered tree data structure used to store a dynamic set or associative
    array where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key
    associated with that node; instead, its position in the tree defines the key with which it is associated.

    Time Complexity:
        - Insert: O(m) where m is the length of the word
        - Search: O(m) where m is the length of the word
        - StartsWith: O(m) where m is the length of the prefix

    Space Complexity:
        - O(n * m) where n is the number of words and m is the average length of the words

    Methods:
        insert(word): Inserts a word into the trie.
        search(word): Returns True if the word is in the trie, False otherwise.
        startsWith(prefix): Returns True if there is any word in the trie that starts with the given prefix.

    Use cases:
        - Autocomplete
        - Spell checkers
        - IP routing (longest prefix matching)
        - T9 predictive text
        - Solving word games
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Args:
            word (str): The word to be inserted.
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie, False otherwise.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists in the trie, False otherwise.
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            bool: True if any word starts with the given prefix, False otherwise.
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
