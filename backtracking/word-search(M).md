# Intuition
Dfs backtracking

# Approach
We want to iterate through every square in the board as a starting spot, and from that starting spot we want to perform a dfs and see if we can find a word. Along the way we will store are current row and col position, as well as the position we're currently at with our word. 

If pos equals the length of the word, we've found a valid word (since we increment it each successful time), If the row or col vals are out of bounds, then we can immediately return False since we're not even on a word. Now that we're on a valid sqaure, we verify that the square char matches the char at our current word pos, and return True if its not.

We now know that we have a valid square. There are 4 different directions to look at, so we call the function moving once to the left, up, down, and right. Note that we want to make sure that we aren't visiting a square twice. So, before we call the function, we mark that square with a '#'. After the dfs is done, we revert it back to what is was before. Also note that we or the result of calling it in each direction, since all we need is one direction to return True.

# Complexity
- Time complexity: Worst case we'll have to iterate through all squares as a starting square, which is $O(m * n)$. For each of these squares, we have 4 different options. The depth of the recursive call stack will be the length of the word (say this is w), so searching for the word is $O(4^w)$. Thus, the total time complexity is $O(m * n * 4^w)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: Worst case the length of the call stack is $O(w)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        def search(row, col, pos):
            if pos == len(word):
                return True
            if row < 0 or row == m or col < 0 or col == n:
                return False
            char = board[row][col]
            if char != word[pos]:
                return False

            board[row][col] = '#'
            pos += 1
            found = search(row + 1, col, pos) or search(row - 1, col, pos) or search(row, col + 1, pos) or search(row, col - 1, pos)
            board[row][col] = char
            return found

        for row in range(m):
            for col in range(n):
                if search(row, col, 0):
                    return True
        return False

```
