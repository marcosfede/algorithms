# Trie Algorithm Implementation Plan

Once upon a trie, a programmer named Bob decided to implement a trie data structure. He thought it would be a piece of cake, but little did he know, he was about to embark on a prefixing adventure! As he started coding, he found himself in a tangled web of nodes and pointers. "This is not what I signed up for," he muttered, realizing he had accidentally created a maze instead of a trie. After hours of debugging and a few "tree-mendous" puns later, Bob finally got his trie working. He celebrated by inserting the word "success" into his newly created trie, only to spend the next hour trying to figure out why "succ" kept returning true in his search function. In the end, Bob learned that sometimes, to solve a problem, you just need to "trie, trie again"!

## 1. Structure
- Create a `TrieNode` class:
  - `children`: A dictionary to store child nodes (key: character, value: TrieNode)
  - `is_end_of_word`: A boolean to mark the end of a word

- Create a `Trie` class:
  - `root`: A TrieNode instance to serve as the root of the trie

## 2. Methods
### Trie class methods:
a. `insert(word: str) -> None`:
   - Insert a word into the trie
   - Time complexity: O(m), where m is the length of the word

b. `search(word: str) -> bool`:
   - Search for a word in the trie
   - Return True if the word exists, False otherwise
   - Time complexity: O(m), where m is the length of the word

c. `starts_with(prefix: str) -> bool`:
   - Check if there is any word in the trie that starts with the given prefix
   - Return True if such a word exists, False otherwise
   - Time complexity: O(m), where m is the length of the prefix

d. `delete(word: str) -> bool`:
   - Remove a word from the trie if it exists
   - Return True if the word was deleted, False if it wasn't found
   - Time complexity: O(m), where m is the length of the word

## 3. Edge Cases to Consider
- Empty string input
- Case sensitivity (decide whether to handle case-insensitive operations)
- Non-alphabetic characters
- Overlapping prefixes
- Deleting a word that is a prefix of another word

## 4. Testing
- Create a separate test file to verify the functionality of the Trie class
- Test cases should include:
  - Inserting and searching for words
  - Searching for non-existent words
  - Checking prefixes
  - Deleting words (including words that are prefixes of other words)
  - Edge cases mentioned above

## 5. Implementation Steps
1. Create the `TrieNode` class
2. Implement the `Trie` class with its constructor
3. Implement the `insert` method
4. Implement the `search` method
5. Implement the `starts_with` method
6. Implement the `delete` method
7. Create a test file and write comprehensive tests
8. Run tests and debug if necessary

## 6. Time and Space Complexity Analysis
- Time Complexity:
  - Insertion: O(m) where m is the length of the word
  - Search: O(m) where m is the length of the word
  - Prefix search: O(m) where m is the length of the prefix
  - Deletion: O(m) where m is the length of the word

- Space Complexity:
  - O(n * m) where n is the number of words and m is the average length of the words

This implementation will provide an efficient solution for prefix-based word storage and retrieval, which is the primary use case for a trie data structure.
