# Intuition
Similar approach to search rotated sorted array

# Approach
It's important to note that the list can be sorted from 1 to n times. This means that the array may be out of order (if rotated 1, 3, etc.) times, or it may still be a normal increasing sequence.

If it's a normal increasing sequence (the left pointer is less than the right pointer), we can immediately return the value at the left pointer since it has to be the min (or start) of the sequence. 

If it's out of order (the left pointer is greater than the right pointer), then we once again compare the midpoint with the left pointer. If the midpoint val is greater than the left pointer val, then we move the left pointer in since the breakpoint is somewhere in front of us (which is where the min will be). If the midpoint val is less than the left pointer val, we are in front of or at the start of the sequence, and move the right pointer in.

Along the way we always keep track of of the min value we see, which we return at the end.

# Complexity
- Time complexity: $O(logn)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            mid = (l + r) // 2
            res = min(nums[mid], res)

            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res


```
