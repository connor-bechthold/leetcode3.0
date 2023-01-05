# Intuition
Backtracking

# Approach
Normal backtracking apporach where at each step we keep adding characters to our substring starting from pos up to the end of the word. If the current word we're building is a palindrome, we add it to curr and recursively call the function with the position after the substring ends. If the position equals the length of s, then we have a valid partition and can add it to our response.

Note: It wasn't needed here, but we could easily optimize the palindrome checking by keeping a set of words that we've seen are palindromes and aren't palindromes.

# Complexity
- Time complexity: When we're going through the string, we can choose to cut it into substrings or do nothing, for a max of n times. This is $O(2^n)$. For each one of these substrings we have to check if it's a palindrome, which is $O(n)$. We also sometimes have to shallow copy. Thus total is $O(n^2*2^n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ for max length of call stack excluding output
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        curr = []

        def backtrack(pos):
            if pos == len(s):
                res.append(curr.copy())
                return
            
            substring = ""
            for i in range(pos, len(s)):
                substring += s[i]
                if isPal(substring):
                    curr.append(substring)
                    backtrack(i + 1)
                    curr.pop()

        backtrack(0)

        return res
```
