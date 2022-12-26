# Intuition
Big brain sliding window

# Approach
We essentially always want to keep track of the character that appears the most in a given window. Then, when we take the length of the window and subtract the amount of times this character appears, the result should be less than or equal to k (i.e. this gives us the amount of other characters we need to replace).

So, we keep moving the right pointer until this occurrs. Before we move the right pointer, we note that we've seen the character the right pointer is at by incrementing its occurrence in a hashmap. To find the character that appears the most, take the max of all the values in the hashmap. If we need to make more than k replacements after subtracting this value from the length, we bring the left pointer in. Everytime we bring the left pointer in, we remove the char it was at from the hashmap. Repeat this until the right pointer reaches the end of the string, updating the global longest along the way.

# Complexity
- Time complexity: $O(n)$. The left and right pointer will worse case go over every element once each, which is still $O(n)$ We also get the max value of the hashmap, which is worse case $O(26)$ (letters in alphabet), and still keeps the time complexity at $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$, which is because it is actually $26O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = collections.defaultdict(int)
        longest = 0
        l,r = 0, 0

        while r < len(s):
            seen[s[r]] += 1

            while (r - l + 1) - (max(seen.values())) > k:
                seen[s[l]] -= 1
                l += 1

            longest = max(r - l + 1, longest)
            r += 1

        return longest
```
