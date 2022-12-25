# Intuition
Don't overthink this

# Approach
Convert the entire string to lowercase to remove uppercase letters. Have a pointer start at the front and back of the string. Keep moving the start pointer until we reach a valid character, OR we reach the end pointer, at which point we are done. The same goes for the end pointer, but instead moving it backwards until we reach a valid character, OR reach the start pointer. If the pointers are both valid, compare the characters. If they're different, it's not a palindrome, and we return False

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1
        while (start < end):
            while(not s[start].isalnum() and start < end):
                start += 1
            while(not s[end].isalnum() and start < end):
                end -= 1
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

```
