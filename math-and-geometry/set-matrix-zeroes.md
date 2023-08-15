# Intuition
Indexing magic and edge cases

# Approach
The idea here is to iterate through the entire matrix once, and everytime we see a zero, we set the first row/col the square occupies to zero. After we do this, we simply go through each outer row/col, and for every zero we come across, we zero out the entire column/row.

However, there's an edge case. Let's say we have a zero on the first column. This will zero out the top left square, which will as a result zero out the entire top row, which is not what we want. So, to fix this issue, we keep a variable colZero which is set to True when this occurs. We DON'T zero out the column this occupies in this case, which is when col == 0.

We also need to be careful when going around the edges at the end. If the corner is zero, it's because we had a zero across the top row. If we start with that zero, we'll zero out the entire top row, which may cause out to zero some columns we don't want to. Thus, we leave that square (and the colZero) for last, and go over the other edges first.

# Complexity
- Time complexity: $O(m * n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])

        colZero = False

        for row in range(m):
            for col in range(n):

                if matrix[row][col] == 0:

                    matrix[row][0] = 0

                    if col == 0:
                        colZero = True
                    else:
                        matrix[0][col] = 0

        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0

        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(n):
                matrix[0][col] = 0

        if colZero:
            for row in range(m):
                matrix[row][0] = 0
```
