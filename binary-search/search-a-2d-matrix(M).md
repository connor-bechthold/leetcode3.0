# Intuition
Binary search twice

# Approach
Here we perform binary search twice - once to find the right row, and another time to find the right value in that row.

For choosing a row, the normal algortithm is performed with some key changes. When we select a row, we use the first and last value in that row. If the first value in that row is greater than our target, then we know our target is in a row further up, and move the bottom pointer up. If the last value in the row is less than the target, then we know our target is in a row further down, and move the top pointer down. If both these conditions pass, we're in the right row, and break.

When we break from searching the algorithm, we check to see if the search failed (with binary search, the search fails if the pointers completely cross), and return false if it did. If it didn't, we have the right row, and can perform binary search as normal to see if the value exists or not.

# Complexity
- Time complexity: $O(log(m)+log(n))$, since we'll perform binary search a max of two times
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:       

        t, b = 0, len(matrix) - 1

        while t <= b:
            row = (t + b) // 2
            if matrix[row][0] > target:
                b = row - 1
            elif matrix[row][-1] < target:
                t = row + 1
            else:
                break

        if t > b:
            return False

        target_row = (t + b) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            col = (l + r) // 2
            if matrix[target_row][col] == target:
                return True
            elif matrix[target_row][col] < target:
                l = col + 1
            else:
                r = col - 1

        return False
```
