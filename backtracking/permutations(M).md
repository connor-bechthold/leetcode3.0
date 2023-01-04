# Intuition
Backtracking

# Approach
Same as usual, except we keep an array of booleans where index i of the array is true if we've used that value already, and false otherwise. Each recursive step we iterate through each value in nums, but only actually add it to our current solution if it hasn't been used yet. Once the recursice call finishes, we set it back to false and continue going through the loop.

# Complexity
- Time complexity: There are $n!$ permutations, and at some steps we may have to copy() the curr array into our result array which is $O(N)$. So in total, this is $O(n * n!)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ if we don't count the output array. If we do, it's the same as the time complexity
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        seen = [False] * len(nums)

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
            else:
                for i in range(len(nums)):
                    if not seen[i]:
                        seen[i] = True
                        curr.append(nums[i])
                        backtrack()
                        curr.pop()
                        seen[i] = False

        backtrack()
        return res
```
