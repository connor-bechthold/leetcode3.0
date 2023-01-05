# Intuition
Dfs

# Approach
The idea here is to have two sets that store coordinates in which water can flow to the pacific and/or atlantic ocean. We can use the fact that all edges of the graph can flow to either ocean. For each of these edge squares, we can push the coordinates to the respective set, then perform a dfs off the square to determine any other squares than can also flow to the ocean it's against. To do this, all we need to verify is that the new square in question has a value greater then or equal to the previous square we were on. That way we know water can flow down towards the ocean that we were previously on. At the end, we can iterate over every coordinate and simply check if they're in both the pacific and atlantic sets.


Note that to perform dfs off of every edge, we first go down the first and last columns and pass in the respective set that the edge belongs to (ie. the first column is against the pacific, and the last column is against the atlantic). We repeat the same going across the top and bottom row. Note that for a prev value we pass in the value of the square to guarantee it is always added to the set, since it will pass the height condition.

# Complexity
- Time complexity: $O(m * n)$. When performing dfs, we only go over each square at most twice, which occurs if the square can go to the pacific and atlantic. Then, we loop over every square to get the result.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(m * n)$, which is the max length of the recursive call stack.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        pacific = set()
        atlantic = set()
        m, n = len(heights), len(heights[0])

        def dfs(row, col, prev, visited):
            if row < 0 or row == m or col < 0 or col == n:
                return
            if (row, col) in visited:
                return

            height = heights[row][col]
            if height < prev:
                return

            visited.add((row, col))

            dfs(row - 1, col, height, visited)
            dfs(row + 1, col, height, visited)
            dfs(row, col - 1, height, visited)
            dfs(row, col + 1, height, visited)

        for row in range(m):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, n - 1, heights[row][n - 1], atlantic)

        for col in range(n):
            dfs(0, col, heights[0][col], pacific)
            dfs(m - 1, col, heights[m - 1][col], atlantic)

        for row in range(m):
            for col in range(n):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res
```
