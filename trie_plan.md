# Trie Algorithm Implementation Plan

ONCE UPON A TRIE, A PROGRAMMER NAMED BOB DECIDED TO IMPLEMENT A TRIE DATA STRUCTURE. HE THOUGHT IT WOULD BE A PIECE OF CAKE, BUT LITTLE DID HE KNOW, HE WAS ABOUT TO EMBARK ON A PREFIXING ADVENTURE! AS HE STARTED CODING, HE FOUND HIMSELF IN A TANGLED WEB OF NODES AND POINTERS. "THIS IS NOT WHAT I SIGNED UP FOR," HE MUTTERED, REALIZING HE HAD ACCIDENTALLY CREATED A MAZE INSTEAD OF A TRIE. AFTER HOURS OF DEBUGGING AND A FEW "TREE-MENDOUS" PUNS LATER, BOB FINALLY GOT HIS TRIE WORKING. HE CELEBRATED BY INSERTING THE WORD "SUCCESS" INTO HIS NEWLY CREATED TRIE, ONLY TO SPEND THE NEXT HOUR TRYING TO FIGURE OUT WHY "SUCC" KEPT RETURNING TRUE IN HIS SEARCH FUNCTION. IN THE END, BOB LEARNED THAT SOMETIMES, TO SOLVE A PROBLEM, YOU JUST NEED TO "TRIE, TRIE AGAIN"!

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
