# Intuition
Backtracking

# Approach
Keep track of a curr array that we can keep our current subset iteration. At each level, we keep track of the position we're at in the array. At each step, we create a shallow copy of our curr array and add the solution. At every step, we add an element to our curr array starting at pos and going up to the last element. We then call the function itself with the current position we're at + 1. When this returns, we pop the element we added, and continue adding other elements.

# Complexity
- Time complexity: For every value in the input list, we have the choice to include it or not include it. This means that each number has two different options, for a total of $2^n$ options. The copy at each step is also $O(n)$, for a total of $O(n*2^n)$

- Space complexity: Not counting the output, $O(n)$ for the curr array

# Code
```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(pos):
            res.append(curr.copy())
            for i in range(pos, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        backtrack(0)

        return res
```
