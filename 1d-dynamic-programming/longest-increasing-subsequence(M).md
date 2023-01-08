# Intuition
Dp

# Approach
This is a classic dp approach, where we start from the simplest solution in the back of the array and move forwards. In this case, we start by initializing a dp array where the ith index will represent the longest increasing subsequence starting at index i. Every value is initialized to 1, since the longest increasing subsequence with just one value in it is 1.

The process is as follows. We start by finding the length of the longest increasing subsequence starting from the back element. this is obviously just one. As we move backwards, we iterate through every element ahead of us. If we find that the element we're currently at is less than the element we're looking at, we know it can make a valid increasing subseqeunce. However remember - since we're working from the back, we've already computed the longest increasing subsequence starting at that value! So, all we need to do is add 1 to it, and update our current max if it's greater than what we already have. We repeat this starting at every element, and then simply return the max of the array because that will give us the max increasing subsequence that we found.

# Complexity
- Time complexity: $O(n^2)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
```
