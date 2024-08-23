"""
Implement a trie data structure with insert, search, and delete operations.

This implementation provides an efficient tree-like data structure for storing and retrieving strings.
It is particularly useful for tasks such as prefix matching, autocomplete, and spell checking.

Structure:
- The trie is composed of TrieNodes, each representing a character in the stored words.
- Each TrieNode has a dictionary of children nodes and a boolean flag indicating if it's the end of a word.

Functions:
- insert: Adds a word to the trie by creating a path of nodes for each character.
- search: Checks if a word exists in the trie by traversing the path of nodes.
- delete: Removes a word from the trie, cleaning up any unnecessary nodes.

Performance:
- Time complexity for insert, search, and delete operations is O(m), where m is the length of the word.
- Space complexity is O(n*m), where n is the number of words and m is the average word length.

Note:
- This implementation assumes all inputs consist of lowercase letters a-z.
- For larger datasets or more complex use cases, additional optimizations may be necessary.
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
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word: str) -> None:
        """
        Removes a word from the trie if it exists.
        """
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
