class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie.
        Time complexity: O(m), where m is the length of the word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the trie.
        Returns True if the word is found, False otherwise.
        Time complexity: O(m), where m is the length of the word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        """
        Delete a word from the trie.
        Returns True if the word was deleted, False if it wasn't found.
        Time complexity: O(m), where m is the length of the word.
        """
        if not word:
            if self.root.is_end_of_word:
                self.root.is_end_of_word = False
                return True
            return False

        stack = [(self.root, 0)]
        last_node_with_branch = None
        last_index_with_branch = 0

        while stack:
            node, index = stack.pop()

            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                break

            char = word[index]
            if char not in node.children:
                return False

            if len(node.children) > 1 or node.is_end_of_word:
                last_node_with_branch = node
                last_index_with_branch = index

            stack.append((node.children[char], index + 1))

        if not node.children:
            if last_node_with_branch:
                del last_node_with_branch.children[word[last_index_with_branch]]
            else:
                self.root.children.pop(word[0], None)

        return True

# Example usage
if __name__ == "__main__":
    trie = Trie()

    # Insert words
    words = ["apple", "app", "apricot", "banana"]
    for word in words:
        trie.insert(word)

    # Search words
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # True
    print(trie.search("apricot"))  # True
    print(trie.search("banana"))   # True
    print(trie.search("grape"))    # False

    # Delete words
    print(trie.delete("apple"))    # True
    print(trie.search("apple"))    # False
    print(trie.search("app"))      # True

    print(trie.delete("banana"))   # True
    print(trie.search("banana"))   # False
