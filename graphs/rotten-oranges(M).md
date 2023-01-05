# Intuition
Bfs

# Approach
Instead of doing dfs like every problem, the best solution to replicate the rotting process is to use a breadth first search. This is because rotten oranges will rot fresh oranges surrounding them in the current minute, so bfs makes sense since at each step we'll analyze the fresh oranges around the rotten oranges. We start by going through the grid once and adding the positions of all the rotten oranges, and also keep track of the number of fresh oranges. Then, while the queue has rotten oranges AND there's still fresh oranges left, we analyze every spot around each rotten orange. If there's a fresh orange, we make it rotten, decrement fresh and then add the position of the new rotton orange to the queue.

At the end, if there's still fresh oranges left, we return -1. Otherwise, we just return the number of minutes it took.

# Complexity
- Time complexity: $O(m * n)$, as we only iterate through each grid at max 2 times
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: Worst case $O(m * n)$, in the case that the entire grid is filled with rotten oranges which we need to initially add to the queue
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        fresh, minutes = 0, 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        while len(queue) and fresh > 0:            
            for i in range(len(queue)):
                row, col = queue.popleft()

                if row > 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
                    fresh -= 1

                if row < m - 1 and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                    fresh -= 1

                if col > 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
                    fresh -= 1

                if col < n - 1 and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                    fresh -= 1

            minutes += 1

        return -1 if fresh > 0 else minutes
```
