# Intuition
Bit Shift
# Approach
In order to count the 1 bits, we can and the LSB with 1, and if it's 1, we can add that as a 1 saw. Then, we simply bit shift to the right to get other possible 1 bits, until the number reaches 0.

# Complexity
- Time complexity: $O(nbits)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0

        while n != 0:
            res += n & 1
            n = n >> 1

        return res
```
