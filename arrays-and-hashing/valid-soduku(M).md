# Intuition
Hashsets and floor division

# Approach
<!-- Describe your approach to solving the problem. -->
Iterate through each value in the board. We keep three hashsets - one for the rows, cols, and squares. The key of the rows and boards correspond to the current row and col we're currently on, and the values are sets to keep track of the numbers. For the squares, we use floor division to distuinguish each square by row and col. This gives us squares of (0, 0), (0, 1), (1, 0) etc....

# Complexity
- Time complexity: $O(9^2)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(9^2)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                val = board[r][c]
                if val == ".":
                    continue

                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
        
        return True
                
```
