# Intuition
DP

# Approach
Exact same approach as longest palindromic substring, but instead of storing pointers to keep track of the longest, everytime we build a valid palindrome from inside out, we increment a counter. Note that we have to do this for even AND odd substrings

# Complexity
- Time complexity: $O(n^2)$, if the string is something like "aaaaaaaa"
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def countSubstrings(self, s: str) -> int:

        palindromes = 0

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

        return palindromes
```
