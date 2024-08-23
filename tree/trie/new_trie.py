from collections import defaultdict
from typing import Union

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class NewTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, string: str) -> Union[TrieNode, None]:
        node = self.root
        for char in string:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
