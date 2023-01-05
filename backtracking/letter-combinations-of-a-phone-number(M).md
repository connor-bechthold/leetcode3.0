# Intuition
Backtrackinggggg

# Approach
Make a map of digits to chars. Go through the digits and keep track of a current pos and the current letter combo. For each digit get the letter combo from the hashmap. Iterate over every letter and add it to the string one by one, recursively calling the function each time and incrementing the pos to get the next digit for the updated string.

# Complexity
- Time complexity: Since we may have a max of 4 choices for each digit, we may have up to $4^n$ combinations. For each of these, we have to concat our combo along the way which will be of length $n$. Thus the total is $O(n * 4^n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$ if we don't count the output, otherwise it's $O(n * 4^n)$ since each combo we store will have n chars. The hashmap is always constant
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        
        if not digits:
            return res

        def backtrack(pos, curr):

            if pos == len(digits):
                res.append(curr)
                return

            code = letters[digits[pos]]

            for char in code:
                backtrack(pos + 1, curr + char)

        backtrack(0, "")

        return res
```
