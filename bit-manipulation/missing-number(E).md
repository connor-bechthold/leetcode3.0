# Intuition
Requires no explanation

# Approach
This is the last Leetcode question my four eyes will be doing, so there will be no explanation, just vibes. I have no idea why I even did this question.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        total = 0
        for i in range(n + 1):
            total += i

        curr = 0
        for num in nums:
            curr += num

        return total - curr
```
