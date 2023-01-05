# Intuition
Dfs reverse thinking

# Approach
We want to capture all the regions that aren't connected to an edge, but it's really easy to identify regions that are connected to an edge. We can simply go around the edges of the board, and if a square is a "O", we can perform a DFS and add all of the connected "O"'s coordinates to a set. All we have to make sure is any surrouning square hasn't been seen aleady, is in the board, and is an "O". Then at the end, we can loop through the enire board and capture all "O"'s that aren't in our set of edge regions.

# Complexity
- Time complexity: $O(m * n)$. Worst case is the dfs takes $O(m * n)$ if the entire board is an "O", and then we have to go over the entire board once to capture squares
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(m * n)$. In the case above we store every coordinate in the set, which is $O(m * n)$, and the max recursion depth is also $m * n
$<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        edgeRegions = set()
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row == m or col < 0 or col == n:
                return

            if (row, col) in edgeRegions:
                return

            if board[row][col] == "X":
                return

            edgeRegions.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)

        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "O" and (row, col) not in edgeRegions:
                    board[row][col] = "X"

        return board           
```
