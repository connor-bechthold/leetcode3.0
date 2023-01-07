# Intuition
Dp

# Approach
We can use the exact same approach as house robber 1, but now instead we call it twice on two different subarrays. Since the first and last house can't be robbed at the same time, we run house robber 1 on every house but the first house, and then we run it again on every house but the last house. To do this, we simply pass in start and end pointers to our normal house rob algorithm, and then simply return the max of the two passes. We also have to check for the special case where there's only one house, in which we just return the amount that house has.

Note that compared to the house robber 1 solution, we instead use a two pointer approach that is very similar to climbing stairs.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHouses(start, end):

            rob1 = 0
            rob2 = nums[start]

            for i in range(start + 1, end + 1):
                curr = max(rob2, nums[i] + rob1)
                rob1 = rob2
                rob2 = curr

            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(robHouses(0, len(nums) - 2,), robHouses(1, len(nums) - 1))
```
