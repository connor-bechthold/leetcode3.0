# Intuition
Big brain indexing 

# Approach
Once again, we use the approach where we have top and left pointers initialized to 0, and bottom and right pointers initialized to the number of rows and columns, respectively.

Our loop condition is while the left and right as well as the top and bottom haven't crossed each other. If they have, then we've completed the spiral.

We first go from top left to top right. We move the top pointer down after because we're done with that row and don't want to start on it again.

We do the same for top to bottom, noting that we're indexing $right - 1$ because right is out of bounds. Move the right in since we're done with that column

We then do a check for our condition again. This is because there's a chance we just went over a matrix (or inner matrix) with a single row or column, in which case, we're done.

We then repeat the same pattern for the bottom row and left column, moving the bottom pointer up and left pointer in after we're done. 

This is repeated for a any inner squares until the spiral pattern is complete.

# Complexity
- Time complexity: $O(m * n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while left < right and top < bottom:

            #Top left to top right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #Top right to bottom right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            #In case we have nothing left now, break immediately
            if top >= bottom or left >= right:
                break

            #Bottom right to bottom left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            #Bottom left to top left
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
```
