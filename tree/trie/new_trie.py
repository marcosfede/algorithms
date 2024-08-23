"""
Implement a trie data structure with insert, search, and delete operations.

Note:
This implementation assumes that all inputs consist of lowercase letters a-z.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete_current_node = _delete_helper(node.children[char], word, index + 1)

            if should_delete_current_node:
                del node.children[char]
                return len(node.children) == 0

            return False

        _delete_helper(self.root, word, 0)

# Example usage
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "apricot", "banana"]
    for word in words:
        trie.insert(word)

    print(trie.search("apple"))  # True
    print(trie.search("app"))    # True
    print(trie.search("apricot"))  # True
    print(trie.search("banana"))   # True
    print(trie.search("grape"))    # False

    trie.delete("apple")
    print(trie.search("apple"))  # False
    print(trie.search("app"))    # True
    print(trie.search("apricot"))  # True
