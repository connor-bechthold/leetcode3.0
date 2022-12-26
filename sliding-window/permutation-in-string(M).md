# Intuition
Seems hard, but it's actually not that bad

# Approach
Keep two hashmaps that pertain to s1 and s2. The s1 hashmap will never change, and will store the numeric value of each char by ordinal of all 26 letters a-z (default 0). The s2 hashmap will store the characters of each "window" of length s1 that we examine, which will be compared each time the window slides one position over starting at the beginning window of length s1. 

One solution would be to compare all 26 values of the s2 hashmap with the s1 hashmap for each window, which is still linear time, but can be optimized by keeping a variable that tracks the number of matches. This matches variable is inialized when we compare the first window. Naturally if we have 26 matches, we have a solution. So, for every subsequent window, we will be removing one char to the hashmap and adding a new char to the hashmap. So, we are really only changes 2/26 values in the hashmap. We can check if after the update the chars still match or not, and update matches accordingly, which is much faster. We repeat this until the window goes out of bounds.

# Complexity
- Time complexity: $O(n)$, where $n$ is the length of $s2$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$, since both hashmaps with always store 26 characters
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = collections.defaultdict(int)
        s2_chars = collections.defaultdict(int)

        for i in range(len(s1)):
            s1_chars[ord(s1[i]) - ord("a")] += 1
            s2_chars[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if s1_chars[i] == s2_chars[i]:
                matches += 1

        l = 0
        r = len(s1) - 1

        while r + 1 < len(s2):
            if matches == 26:
                return True
        
            removed_char = s2[l]
            l += 1

            pos = ord(removed_char) - ord("a")
            prev_matched = s1_chars[pos] == s2_chars[pos]
            s2_chars[pos] -= 1

            if s2_chars[pos] == s1_chars[pos]:
                matches += 1
            elif prev_matched:
                matches -= 1

            r += 1
            added_char = s2[r]

            pos = ord(added_char) - ord("a")
            prev_matched = s1_chars[pos] == s2_chars[pos]
            s2_chars[pos] += 1

            if s2_chars[pos] == s1_chars[pos]:
                matches += 1
            elif prev_matched:
                matches -= 1
        
        return matches == 26
```
