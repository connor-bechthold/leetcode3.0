# Intuition
Bit pattern recognition

# Approach
Basically at intervals of 1, 2, 4, 8, etc... we add a MSB. Between these intervals, we can look $x$ spots back and the number of 1 bits is guaranteed to be 1 less than the current number. For example, for 3, we would look back 2 spots and see that 1 has 1 bit. Thus, 3 has 2 bits.

We keep track of an offset which is initially 1. Everytime we increment i, we check to see if we've reached 2 * offset. If we have, we increase the offset to this value and continue. We then use the offset pattern as explained earlier to fill out the DP array

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):

            if 2 * offset == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp  
```
