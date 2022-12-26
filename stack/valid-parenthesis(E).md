# Intuition
Ze stack

# Approach
Push all open brackets onto the stack. When we get a closing bracket, its matching open bracket should be on the top of the stack and is verified. If the stack is empty when we reach a closing bracket, there aren't enough open brackets. If we go through the input string and the stack isn't empty, there weren't enough open brackets

# Complexity
- Time complexity: $O(n)$, to go through input string
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$, worst case our stack stores an entire string of open brackets
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket not in bracket_map:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if bracket_map[bracket] != stack.pop():
                    return False
        return len(stack) == 0
```
