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
        children (defaultdict): A dictionary of child nodes, where keys are characters
                                and values are TrieNode objects.
        is_word (bool): Flag to mark the end of a word.
    """
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    """
    Trie data structure for efficient string storage and retrieval.

    Methods:
        insert(word): Inserts a word into the trie.
        search(word): Returns True if the word is in the trie, False otherwise.
        startsWith(prefix): Returns True if there is any word in the trie that starts with the given prefix.
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


# Test cases
if __name__ == "__main__":
    trie = Trie()

    # Test insert and search
    trie.insert("apple")
    assert trie.search("apple") == True, "Should find 'apple'"
    assert trie.search("app") == False, "Should not find 'app'"

    # Test startsWith
    assert trie.startsWith("app") == True, "Should find words starting with 'app'"

    # Insert more words
    trie.insert("app")
    trie.insert("apricot")

    assert trie.search("app") == True, "Should now find 'app'"
    assert trie.startsWith("apr") == True, "Should find words starting with 'apr'"
    assert trie.search("apr") == False, "Should not find 'apr'"

    print("All test cases passed!")
