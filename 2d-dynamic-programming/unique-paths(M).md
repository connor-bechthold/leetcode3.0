# Intuition
2D DP (But actually just 1D)

# Approach
We can take adavntage of the fact that the number of unique paths to any square is the sum of the number of unique paths to the sqaure above plus the the number of unique paths to the square to the left (since we can only move down and right). 

Notice for the first row, this will always be 1. For every subsequent row, this will be the value of the row val above in that column, and the value to the left in the current row. Thus, we can just keep a DP array for each row, and keep incrementing each square by the value to it's left (since the value above was already set from the previous row)

Then, the desired result is in the far right column in our DP array.
# Complexity
- Time complexity: $O(m * n)$

- Space complexity: $O(n)$


# Code
```python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [1] * n

        for row in range(1, m):
            for col in range(n):

                if col > 0:
                    dp[col] += dp[col - 1]

        return dp[n - 1] 
```
