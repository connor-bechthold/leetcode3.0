# Intuition
Use a hashset!

# Approach
Iterate through the list. For each element, check if we've seen the element in the hashset. If we haven't, it's not a duplicate, and we can add it. Otherwise, if it is in the hashset, we've seen it, and can immediately return true.

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(n)$

# Code
```python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

```
