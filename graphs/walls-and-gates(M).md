# Intuition
Bfs

# Approach
This is very similar to the rotten oranges. The naive approach would be to do a dfs from every empty room and then update the square with the closest gate, keeping a counter along the way. However, we can be even more efficient by doing a bfs starting at every gate. We add all the coordinates of gates to a queue, and initiliaze a distance counter to keep track of how far we are from any gate at any time. Starting from each gate, each time we look around and see an empty room, we update that empty room to the current distance we're at, and then push that empty room onto the queue to further look at any surrounding empty rooms.

# Complexity
- Time complexity: $O(m * n)$, in the case that there's no walls
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(m * n)$, in the case that every square is a gate
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):

        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()
        distance = 1

        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while len(queue):            
            for i in range(len(queue)):
                row, col = queue.popleft()

                if row > 0 and rooms[row - 1][col] == INF:
                    rooms[row - 1][col] = distance
                    queue.append((row - 1, col))

                if row < m - 1 and rooms[row + 1][col] == INF:
                    rooms[row + 1][col] = distance
                    queue.append((row + 1, col))

                if col > 0 and rooms[row][col - 1] == INF:
                    rooms[row][col - 1] = distance
                    queue.append((row, col - 1))

                if col < n - 1 and rooms[row][col + 1] == INF:
                    rooms[row][col + 1] = distance
                    queue.append((row, col + 1))

            distance += 1

        return rooms
```
