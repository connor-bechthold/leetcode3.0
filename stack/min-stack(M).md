# Intuition
So many stacks

# Approach
We do the normal stack operations without changing any functionality. We need to be aware of the fact that we have to return the min value from the stack at any time. It seems simple enough to just store a variable with this value, but if that min value is popped off the stack, how can we find the next best min in constant time without looping through the stack? This is where another stack comes in handy - one that always has the min value at the top. If a new lowest min is added to the stack, we also push that onto our min stack. That way once that lowest min is popped, we still have the next lowest min stored and available.

# Complexity
- Time complexity: All functions are $O(1)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$. Worst case all push operations
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class MinStack:

    def __init__(self):
        self.values = []
        self.minimums = []
        
    def push(self, val: int) -> None:
        if len(self.minimums) == 0 or val <= self.minimums[-1]:
            self.minimums.append(val)
        self.values.append(val)
        
    def pop(self) -> None:
        if self.values[-1] == self.minimums[-1]:
            self.minimums.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
