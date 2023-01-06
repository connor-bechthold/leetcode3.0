# Intuition
DP

# Approach
We first define our base cases. The number of ways to go one step is 1, and the number of ways to go two steps is 2. If n equals 1 or 2, we can immediately return. Otherwise, we start looping from n = 3, to whatever n is. The key here is working from the bottom up. At any step, the number of unique ways to get to that step is the number of ways to get to two steps before that step plus the number of ways to get to one step before that step. Remember that we can only take steps of 1 or 2. So, for each of the ways we can get to two steps behind the current step, we can take another two step climb to reach the current step. For each of the ways we can get one step behind the current step, we can take another one step to get to the current step. 

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def climbStairs(self, n: int) -> int:

        twoStepBehindWays = 1
        oneStepBehindWays = 2

        if n == 1:
            return twoStepBehindWays
        if n == 2:
            return oneStepBehindWays

        for step in range(3, n + 1):
            currStepWays = twoStepBehindWays + oneStepBehindWays
            twoStepBehindWays = oneStepBehindWays
            oneStepBehindWays = currStepWays

        return oneStepBehindWays
```
