# Intuition
Dfs

# Approach
This the exact same as number of islands, but instead of doing the dfs and returning nothing, we keep track of the area and return that. We can do this for any sqaure by returning 1 + the area of the rest of the island excluding that square recursively.

# Complexity
- Time complexity: $O(m * n)$ in the case that the whole grid is an island, and we never revisit a square
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(m * n)$ for the max call stack length if the whole grid is an island
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(row, col):
            if row < 0 or row == m or col < 0 or col == n:
                return 0
            if grid[row][col] != 1:
                return 0
            
            grid[row][col] = 0

            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))

        return maxArea
```
