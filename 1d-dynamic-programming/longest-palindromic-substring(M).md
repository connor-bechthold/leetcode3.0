# Intuition
Dp

# Approach
The idea here is to go through the string character by character and construct palindromes from the inside out. Note that there are 2 types of palindromes:
- Odd length: "bab"
- Even length: "bb"

We want to work from the center out on these palindromes. So, for each character we test for an even or odd palindrome. 

An odd palindrome is tested by starting two pointers at the same character, and moving one pointer left and one right one by one. As long as the chars at these pointers are equal as we move outwards, we have a valid palindrome.

An even palindrome is tested by starting the right pointer a position ahead of the left pointer and repeating the same process.

For each step, we compare the current length of our palindrome with the max length we've seen so far by using max left and right pointers. With these max pointers, we can compare the length of our longest palindrome so far and the current palindrom we've seen, and then easily splice the substring from the full string at the end.

# Complexity
- Time complexity: $O(n^2)$, since we may have to go as outwards as far as we can for each char if the string is something like "aaaaaaaaa"
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestL, longestR = 0, 0
        
        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longestR - longestL + 1:
                    longestL, longestR = l, r
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longestR - longestL + 1:
                    longestL, longestR = l, r
                l -= 1
                r += 1

        return s[longestL:longestR+1]
```
