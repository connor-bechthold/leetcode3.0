# Intuition
Dfs with trie

# Approach
Normal trie operations, acceot we have to handle a case where we're looking for a word that has periods in it. This function is recursive in nature, where each call we keep track of the position in the word we're at and the current trie node we're at. When the pos var is past the word, we know we've reached the end, and can simply return whether it's the end of a word or not. When we reach a period, we can loop through every available character in the node until one call returns True, which is when we can simply return True

# Complexity
- Time complexity (search): $O(m)$, where $m$ is the sum of the number of characters that we add in the trie (ex. in the case we only get periods we may have to search through every node) 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(m)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(pos, node):
            if pos == len(word):
                return node.is_end
            elif word[pos] == ".":
                for node in node.children.values():
                    if dfs(pos + 1, node):
                        return True
                return False
            elif word[pos] not in node.children:
                return False
            else:
                return dfs(pos + 1, node.children[word[pos]])

        return dfs(0, self.root)
```
