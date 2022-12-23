# Intuition
Use a hashmap!

# Approach
First of all, anagrams must be the same length, so do that check first. 

For the string s, iterate through each character and add it to the hashmap to keep track of how many times we've seen each character (this will be represented as an integer, with a default value of 0). Then, do the same for the t string, but instead subtract the value associated with the character in the hashmap. If the value at this character is already 0, then we've already either used up all instances of that character in s, or have never seen that character. Either way, we can immediately return false. If we make it through t without returning, we've seen a valid anagram, and can return true.

# Complexity
- Time complexity: $$O(s)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(s)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Follow Up
If asked for $$O(1)$$ space, we could sort first, which is $$O(nlog(n))$$ time, and then compare each character.

# Code
```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = collections.defaultdict(int)
        for letter in s:
            hashmap[letter] += 1
        for letter in t:
            if hashmap[letter] == 0:
                return False
            hashmap[letter] -= 1
        return True
```
