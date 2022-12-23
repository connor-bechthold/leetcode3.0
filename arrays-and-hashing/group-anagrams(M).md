# Intuition
Ordinals 

# Approach
Anagrams have one to one correspodence between the characters they contain. Since we know the characters range from a-z, we cab group anagrams by their character occurrences. To do so, we can store groups in a hashmap, where the key is a tuple of 26 integers long (a-z is 26 letters), where "a" is index 0, "b" index 1, etc. Then, we can return a list of the hashmap values

# Complexity
- Time complexity: $O(mn)$. We define "n" as the number of input words, and "m" as the max number of chars a word will have
<!-- Add your time complexity here, e.g. $O(n)$ -->

- Space complexity: $O(mn)$. Our hashmap will store at worse case $n * O(1) = O(n)$ key tuples and $n$ words of max $m$ characters which is $O(mn)$. In total this is $O(n + mn)$ which is $O(mn)$.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for word in strs:

            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - ord("a")] += 1
            hashmap[tuple(char_count)].append(word)

        return hashmap.values()
        
```
