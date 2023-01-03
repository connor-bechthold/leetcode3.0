# Intuition
Basically quicksort, but quick SELECT

# Approach
We want to store the index in the array that the kth largest element would be at if the array was sorted as normal.

We keep a left and right pointer that initially are at the start and end of the list respectively. We choose a "pivot" point which is always the value on the right of our bounds. We also keep a pointer p that will start at the beginning of the bounds. We iterate through every value in the list. If a value is less than or equal to the pivot, we switch it with whatever is currently in p, and then increment p. When we're finished iterating, everything left of p will be less than the pivot, and everything right of p will be greater than the pivot. If we switch the values stored at the pivot and p, it is a guarantee that the pivot is now sorted in the correct spot.

Since it's in the right spot, we can check if it's the kth largest element by comparing the index of it with our target index. If the target index is further ahead, we move the left pointer in to p + 1. If it's behind us, we move the right pointer in to p - 1. We then repeat the process. If the indexes match, we can return the value. 

# Complexity
- Time complexity: On average case this is $O(n)$, but worst case it could be $O(n^2)$. This depends on our pivot point. We ideally want p to be in the middle so we can have iterations of $O(n) + O(n/2) + ... + = O(2n) = O(n)$, but if our p is at the start or end each time, it looks more like $O(n^2)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$, since we're modifying in place
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_p = len(nums) - k
        
        def quickSelect(l, r):
            p = l
            pivot = nums[r]

            for i in range(l , r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < target_p:
                return quickSelect(p + 1, r)
            elif p > target_p:
                return quickSelect(l, p - 1)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)

```
