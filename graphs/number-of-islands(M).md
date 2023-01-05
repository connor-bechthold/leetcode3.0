# Intuition
Dfs

# Approach
Pretty straighttforward dfs. We iterate through every square in the grid, and if we see a one, we increment the number of islands seen and we perform a dfs starting at that square. The goal with the dfs is to change all the 1's on the current island to 0's, so when we continue our iteration, we don't count any 1's connected to the first 1 we saw as an extra island. We check if the row and col is in bounds and that the current val is a 1, and if both are satisfied, we change the 1 to a 0 on the board and repeat with the 4 surrounding directions.

# Complexity
- Time complexity: This is actually $O(m * n)$. Worst case scenario is the entire grid is full of ones, which would mean on the first 1 we see, we would visit every other 1 once, convert it to a 0, and never go over it again in the loop. We'd have 1 $O(m * n)$ call and $m * n - 1$ $O(1)$ calls, which is $O(m * n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: The max depth of the call stack is $m * n$ in the situation that the board is all 1's, so we have $O(m * n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row == m or col < 0 or col == n:
                return
            if grid[row][col] != "1":
                return
            
            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands
```
