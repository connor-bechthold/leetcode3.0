# Intuition
Slide that window

# Approach
We start with two pointers both on the first character of the string. We only really care about moving the right pointer here. In order to keep track of the characters that we've seen, we always add whatever character the right pointer is at before moving it forwards to a hashset. 

When the right pointer reaches a character that we've already seen we can make an observation. We know all chars between the left and right pointer - 1 are unique. So, in order to gain that uniqueness back, we can move the left pointer up until the duplicate character is out of the window. Each time we move the left pointer up, we remove it from the hashset. Then, we can update the global longest subsequence using the positions of the left and right pointers.

# Complexity
- Time complexity: $O(n)$. Worst case both pointers go over every element, which is still $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ due to the size of the hashset
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l, r = 0, 0

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

            longest = max(r - l + 1, longest)
            seen.add(s[r])
            r += 1
     
        return longest    
```
