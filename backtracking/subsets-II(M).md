# Intuition
Backtracking + sorting

# Approach
The big idea here is that we need to handle the duplicate values so we don't get duplicate subsets. In order to do this, we check to see if we've already seen a duplicate value previously when we're iterating. To make sure all the duplicate values are beside each other, we need to sort the list first. 

For example, take the set $[1,2,2,3]$. We first begin by recursively calling with $[1]$, and then $[2]$. When we get to 2 again, we obviously don't want to call with $[2]$ again as we've already seen that value. So, since we saw that element one spot behind us, we can skip ahead. We make sure that this is only checked for elements BEYOND the position we're starting iteration from. For ex. when we recursively call with the first $[2]$, pos will be at the second 2. We don't want to skip this 2, as $[2,2,3]$ is still valid. 

# Complexity
- Time complexity: Same as normal even with sorting (since $nlog(n)$ is faster), $O(n*2^n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        nums.sort()

        def backtrack(pos):
            res.append(curr.copy())

            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return res

```
