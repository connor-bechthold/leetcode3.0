# Intuition
Backtracking and sorting

# Approach
Basically the same as before, however now we can't use the same element twice, so we always increment our current pos + 1 when recursively calling. To make up for this, there are duplicate elements, so we do the normal sorting strategy. In each iteration, if our current position is greater than where we started (pos), and we've already seen that element before, we skip over it otherwise we'll get duplicate solutions (see my explanation for subsets II, it's the exact same thing)

# Complexity
- Time complexity: At each step we can either choose to include the current number or not include the current number. We also sometimes copy() our curr array. Sorting is slow enough here to ignore. $O(n * 2^n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ worst case, if the list is full of 1's
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []

        candidates.sort()

        def backtrack(pos, total):

            if total == target:
                res.append(curr.copy())
                return
            elif total > target:
                return
            else:
                for i in range(pos, len(candidates)):
                    if i > pos and candidates[i] == candidates[i - 1]:
                        continue
                    curr.append(candidates[i])
                    backtrack(i + 1, total + candidates[i])
                    curr.pop()

        backtrack(0,0)
        return res
```
