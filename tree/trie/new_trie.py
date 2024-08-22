"""
Implement a new Trie data structure with insert, search, and starts_with methods.

This implementation uses a TrieNode class to represent each node in the Trie.
Each TrieNode contains a dictionary of children nodes and a flag to indicate
if it represents the end of a word.

Note:
    - All inputs are assumed to consist of lowercase letters a-z.
    - This implementation aims to be more memory-efficient by using a regular
      dictionary instead of defaultdict for children nodes.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Args:
            word (str): The word to be inserted.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie, False otherwise.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            bool: True if any word starts with the given prefix, False otherwise.
        """
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        """
        Helper method to find the node corresponding to the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            TrieNode: The node corresponding to the last character of the prefix,
                      or None if the prefix is not found.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
