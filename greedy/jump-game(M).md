# Intuition
Greedy

# Approach
The idea here is to keep track of a target, which the closest index we have to reach in order to jump to the end. Obviously, this is initialized to the last index. We then work backwards from there, and move the target to the current index if the current index plus the number is greater than or equal to the target (since we don't need to jump the full distance). At the end, we simply need to check if the target is at the 0th index, and return True if it is, and False if it isn't.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1

        for i in range (len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0
```
