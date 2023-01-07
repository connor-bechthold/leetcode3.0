# Intuition
DP

# Approach
The tricky part here is that we may come across negatives in our subarray. Remember that two negatives make a positive, so we can't just disregard them and only take positives. Instead, we always keep track or a current maximum value AND a current minimum value.

For example, take the array $[-3, 3, 4, -1]$. We start with all of our variables set to -3, since it's the first value in the array. When we get to the second value we want to compute the new current min and current max. We first calculate the current max, which is the max of $(3, -9, -9) = 3$. Because we need the current max to calculate the current min, we save the value first before updating it. The current min is the min of $(3,-9, -9) = -9$. Then, we update the global max to be the max of the current max and. the global max.

It may not be clear to see why this is done until we get to the last value. At this point, the currMin is $-9 * 4 = -36$, and the currMax is $3 * 4 = 12$. Note how when we're updating the current max, we use the current min in this calculation. This situation is why. When we multiply $-1$ by the current min, we get a large positive value, which happens to the max product we can get. If we didn't store the min along the way, we would've never gotten this value.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        globalMax = currMin = currMax = nums[0]

        for i in range(1, len(nums)):

            temp = currMax
            currMax = max(nums[i], currMax * nums[i], currMin * nums[i])
            currMin = min(nums[i], temp * nums[i], currMin * nums[i])

            globalMax = max(currMax, globalMax)

        return globalMax
```
