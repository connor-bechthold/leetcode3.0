# Intuition
Stack

# Approach
We bascially want the stack to keep track of prev day temps that are waiting for a future day where the temp is higher. Every temp will be pushed on the stack, along with its index so we know where it's positoned which allows us to count the number of days. Before we push a temp on the stack, we check to see if there's any prev temps on the stack that we can satisfy. We pop a temp off the stack if the current temp is greater than that prev temp. We then calculate the number of days it took for this increase, and update the res list. This loops until there are no more temps we can satisfy, or they've all been satisifed. Then, we push the current temp, and the process repeats.

# Complexity
- Time complexity: $O(n)$. Worst case is the last temp satisifies every prev temp, which means every element in gone over twice, which is still $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$, which is the max number of temps that will be on the stack at once (same situation as above)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > stack[-1][0]:
                prev_temp, prev_temp_index = stack.pop()
                res[prev_temp_index] = i - prev_temp_index
            stack.append((temp, i))

        return res 
```
