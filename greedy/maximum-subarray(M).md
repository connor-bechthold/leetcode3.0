# Intuition
Greedy

# Approach
We keep track of a current max and a global max. The current max will be updated as follows:
- The current number is added onto the subarray if its value is not greater than the value of the current total summed with it
- If it is greater, then we're starting a new subarray

We then keep updating the global max with the greatest current max we're seeing.

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(1)$

# Code
```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currMax, globalMax = 0, float(-inf)

        for num in nums:
            currMax = max(num + currMax, num)
            globalMax = max(currMax, globalMax)

        return globalMax
```
