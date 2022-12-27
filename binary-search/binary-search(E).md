# Intuition
Binary search

# Approach
Standard binary search using two pointers. Keep finding midpoint and close bounds until the value is found or the pointers fully cross each other (which means the value does not exist). Remember to use floor division.

# Complexity
- Time complexity: $O(logn)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
```
