# Intuition
Big brain indexing

# Approach
This is kinda DP in the sense that we just need to keep rotating squares by 90 degrees until there are no more squares to rotate 

![image info](/images/rotate-image.jpg)

Looking at the diagram above, we have 4 pointers, left(l), right(r), top, ands bottom. Left and right are initially set to the left and right boundaries, respectfully. Notice how at each level, we only need to do (right - left) rotations, which is the reason for the for loop. Once we're done, we move left and right in one until they overlap, at which point we're done

We first assign top and bottom to left and right, since it's just a square.We store the top left in a variable, and then do a reverse rotation (i.e. bottom left to top left, etc.) so we only need one temp variable. This is fine for the corners, but notice how we need to shift these to get the edges. This is why we offset by i in some places (you can look at the code, but for example the left pointer should be moving right across the top row as we rotate, hence we add i)

# Complexity
- Time complexity: $O(n^2)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range (r - l):

                top, bottom = l, r

                topLeft = matrix[top][l + i]

                #bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #top left to top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1
```
