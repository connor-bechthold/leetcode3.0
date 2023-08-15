# Intuition
Bit shift

# Approach
We basically loop through each of the 32 bits of the input string. This is done by shifting by i, and then extracting the bit with an and. Then, we left shift this but 31 - i times, and or it with the current res to update that bit in its reverse spot

# Complexity
- Time complexity: $O(32)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):

            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res
```
