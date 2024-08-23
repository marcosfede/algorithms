"""
Implement a new trie algorithm with insert and search functions.

This implementation provides a basic trie data structure, which is an efficient
tree-like data structure for storing and retrieving strings. It is particularly
useful for tasks such as prefix matching, autocomplete, and spell checking.

Structure:
- The trie is composed of TrieNodes, each representing a character in the stored words.
- Each TrieNode has a dictionary of children nodes and a boolean flag indicating if it's the end of a word.

Functions:
- insert: Adds a word to the trie by creating a path of nodes for each character.
- search: Checks if a word exists in the trie by traversing the path of nodes.

Performance:
- Time complexity for both insert and search operations is O(m), where m is the length of the word.
- Space complexity is O(n*m), where n is the number of words and m is the average word length.

Note:
- This implementation assumes all inputs consist of lowercase letters a-z.
- The trie does not support deletion or prefix searching in its current form.
- For larger datasets or more complex use cases, additional optimizations may be necessary.
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
