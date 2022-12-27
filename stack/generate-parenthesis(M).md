# Intuition
This should be under backtracking but we use a stack anyways

# Approach
The stack will keep track of our current combination at any time. They key here is to always keep track of the number of open and closed brackets. A valid combination will have $n$ opening and $n$ closed brackets. We start by adding as many open brackets as we can up to n. Everytime we recursively call, we push an open bracket onto the stack, and then pop it after the function returns (ie. all combinations were exhausted). Once we're done adding open brackets on our current combination, we add closing brackets and the process repeating.

Ex. algo progression for $n = 2$
(, ((, ((), (()), (), ()(, ()()


# Complexity
- Time complexity: $O(2^{2n})$ roughly as an upper bound. Think of this as a binary string of length $2n$. The number of different combinations would be $2 * 2 * 2 * .....$ up to $2n$ times. So if we replace 0's and 1's with open and closing brackets, we'd roughly have that many stops in our algorithm (not exact because not all combination are valids, eg. those with more closing brackets)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ for the stack
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open, close):
            if open == n and close == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
            
```
