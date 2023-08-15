# Intuition
Bitwise XOR

# Approach
If every number appears twice except for 1, XORing these numbers will give us 0. XORing with 0 gives us the number, thus, if we XOR everything in the list together, we're left with the unique number. 

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0

        for num in nums:
            res = res ^ num

        return res
```
