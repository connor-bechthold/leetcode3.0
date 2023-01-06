# Intuition
DP

# Approach
This approach is clearer to explain with an example: Take a cost array of $[10, 15, 30]$. We want to use an array to keep track of the min costs along the way, and we can reduce the need to create a separate array by using the array we're given.

We start by appending a 0 to the end of the array: $[10, 15, 30, 0]$. We then start our calculation at the **3rd last** index, which in this case is 15. We are still using the same approach as climbing stairs, except this time we are working BACKWARDS, which means we'll be pretending the previous two steps are AHEAD of us. 

At the second step (15), we can either take one step from step one (cost of 30), or take two steps from the floor (cost of 0). This is why we add the 0, since the cost of being on the floor is nothing. The min of $(15 + 0 = 15, 15 + 30 = 45)$ is obviously 15, so we update the min cost to get to that step as 15: $[10, 15, 30, 0]$. We do the same thing for the next step, which is the min of $(10 + 15 = 25, 10 + 30 = 40) = 25$. Thus, our final array looks like this: $[25, 15, 30, 0]$. 

To return, we take the min of the first two values, since from index 0 (25), we can take one step and reach the top, or from index 1 (15), we can take two steps and reach the top. This is obivously 15, so that's what we return.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])
```
