# Intuition
Hashmaps are life

# Approach
Our trie will consist of a root TrieNode, which will contain a hashmap of characters in any words we're storing and a boolean which will store whether the current letter we're storing marks the end of a word.

The storing process works as so:
- Each TrieNode will contain hashmap of children, which will contain letters as keys
- The values in these letters will contain another TrieNode, which will store future letters in future TrieNodes

Lets consider storing the word "cat". We iterate through each letter, starting in the root TrieNode. In the root TrieNode, we look for the letter "c". If c exists, we go into its corresponding TrieNode and look for "a", and the process repeats. If the letter does not exist, we create a new entry under that letter by creating an empty TrieNode, then going into that TrieNode and continuing.

Once we've stored "t" and gone into its TrieNode, we make sure to update the "is_end" var to True. This is used so we can tell the difference when searching for words and prefixes. If we're searching for "cat", we go through "c", "a", and "t", and then check if is_end is True, which it is, so the word exists. However, if we were searching for "ca", "c" and "a" would exist due to "cat", but the word "ca" itself would not exist. This would return True in a prefix search, but not a word search.

# Complexity
- insert(word): Time complexity $O(n)$, space complexity $O(n)$ (if we have to make a new entry for every letter)
- search(word): Time complexity $O(n)$, space complexity $O(1)$
- startsWith(prefix): Time complexity $O(n)$, space complexity $O(1)$

# Code
```python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
