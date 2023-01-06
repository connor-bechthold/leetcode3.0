# Intuition
DP

# Approach
This is basically the same approach as min cost climbing stairs. We work backwards, adding a 0 to represent that before robbing the first house, we can get nothing. We start at the second last house. We can either take what we got from the house before the first house (which in this case is nothing) plus what we're going to get from this house, or we can take the amount we got from the first house. Whatever is the max gets updated as the max value we can make at the second house, and we continue until we finsih the first house. At the end, the max value we can get will be at the first index.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def rob(self, nums: List[int]) -> int:

        nums.append(0)

        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i + 1], nums[i] + nums[i + 2])

        return nums[0]
```
