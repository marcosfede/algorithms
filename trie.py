from typing import Union

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def delete(self, word: str) -> bool:
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete_child = _delete_helper(node.children[char], word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            return False

        if not word:
            if self.root.is_end_of_word:
                self.root.is_end_of_word = False
                return True
            return False

        return _delete_helper(self.root, word, 0)

    def _traverse(self, word: str) -> Union[TrieNode, None]:
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
