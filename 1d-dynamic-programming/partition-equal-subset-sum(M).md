# Intuition
I can't do dp I can't do dp I can't do dp I can't do dp I can't do dp I can't d

# Approach
The gigabrain thing to realize here is that in order to partition the array into equal subsets, the values in oth subsets must be the same. This means that when we add these up, they will equal to the sum of the entire array. Thus, we can find the target sum our subset needs to be by taking the sum of the array and then dividing by two. Note that if the sum is odd, we obviously can't divide by 2, thus, a solution is impossible.

From here, the problem boils down to finding some subset of numbers that add up to our calculated target. We can do this in a very similar fashion to coin change, but with a few key differences.

We use a dp array of size target + 1, with initially everything set to False, where dp[i] is True if we can make the sum i with the nums we have. We set a total of 0 to True, since if we have an amount of i and happen to subtract num = i from that amount, our difference will be 0 which is valid, so we always want a total of 0 to be True.

The key difference from coin change is we can only use each number ONCE for each subset. Take the case where one of our nums is 1. We first set amount = 1 to True since we subtract 1 and dp[0] is True. However, when we get to amount = 2, we will suctract 1 and see that dp[1] = True, which we just updated. However, this is wrong! This means that we used 1 to get an amount of 1, and then 1 again to get an amount of 2. So, to solve this, we instead iterate from the HIGHEST amount to the LOWEST amount. This way when we're looking at dp[i - num] when we subtract, it is guaranteed that we haven't already used this amount to make a smaller amount already.

# Complexity
- Time complexity: $O(n * sum(nums))$. We go through each number, and for each number we go through the dp array of length $sum / 2$ which is $O(sum)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(sum(nums))$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, 0, -1):
                if i - num >= 0:
                    dp[i] = dp[i] or dp[i - num]

        return dp[target]
```
