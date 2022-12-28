# Intuition
Painfully painful binary search

# Approach
This kind of binary search can be broken up into two different scenarios. Where the value at the midpoint of our search is greater than (or equal) to the value at the left of the list, and where the value at the midpoint is less than the value to the left of the list.

Consider the first scenario. This means that the beginning of the original sequence is somewhere past the current midpoint (eg. $[3,4,5,6,1,2]$). The cases are broke down as follows: 

- If our target is GREATER than the midpoint, we can shift the left pointer in (the sequence can only go higher until it hits the beginning again)
- If our target is LESS than the midpoint:
    - If our target is LESS than the leftmost value, we can shift the left pointer in (the target appears before the sequence wraps around)  
    - If our target is GREATER THAN or EQUAL to the leftmost value, we can shift the right pointer in (the target appears after the sequence wraps around)  

Consider the second scenario. This means that the beginning of the original sequence is somewhere before the current midpoint (eg. $[6,7,1,2,3,4]$). The cases are broke down as follows: 

- If our target is LESS than the midpoint, we can shift the left pointer in (the sequence can only go lower until it hits the end of the sequence)
- If our target is GREATER than the midpoint:
    - If our target is GREATER than the rightmost value, we can shift the right pointer in (the target appears after the sequence wraps around)  
    - If our target is LESS THAN or EQUAL to the rightmost value, we can shift the left pointer in (the target appears before the sequence wraps around)  

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
            print(mid)

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1 
            
```
