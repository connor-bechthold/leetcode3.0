# Intuition
Shtack

# Approach
Push the integers on the stack. Everytime we see an operator, pop the most 2 recent numbers off the stack, and perform the operation, pushing the result back onto the stack. At the end, the last integer in the stack will be the answer.

Note: The only tricky part here is that division needs to be always rounded towards 0 (ie. floor if +ve, ceil if -ve). Conveniently, doing float division and then casting to an int does this for us.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            match(token):
                case "+":
                    val_one, val_two = stack.pop(), stack.pop()
                    stack.append(val_two + val_one)
                case "-":
                    val_one, val_two = stack.pop(), stack.pop()
                    stack.append(val_two - val_one)
                case "*":
                    val_one, val_two = stack.pop(), stack.pop()
                    stack.append(val_two * val_one)
                case "/":
                    val_one, val_two = stack.pop(), stack.pop()
                    stack.append(int(val_two / val_one))
                case _:
                    stack.append(int(token))

        return stack.pop()
```
