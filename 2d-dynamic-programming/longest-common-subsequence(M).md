# Intuition
2D DP

# Approach
This appraoch is better visualized with the DP table constructed, which is a bottom up constructed.

![IMG_0640](https://github.com/connor-bechthold/leetcode3.0/assets/64047863/d43f33af-808c-4b49-a5c3-4df2ac9f176f)

For this example, we use $ace$ and $abcde$. With this grid, any square value is going to the longest common subsequence between the two substrings (for example, the $(c, c)$ coordinate is the LCS between $ce$ and $cde$). There are two different cases:
- If the coordinates match (characters are the same), the LCS is 1 + the grid value down 1 and to the left one. In the case above, this is between $de$ and $e$ (which makes sense, as we're just breaking the problem down further)
- If the coordinates do not match (strings are not the same), we take the max of the grid below us or to the right of us. In the case of $ce$ and $de$, this is comparing between $e$ and $de$ or $e$ and $ce$ (again, breaking down the problem further)
- Note how the outer edge coordinates are set to 0, as te LCS between any string and the empty string is just 0

At the end, the LCS will be at position [0][0]

# Complexity
- Time complexity: $O(len(text1) * len(text2))$
- Space complexity: $O(len(text1) * len(text2))$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for pos1 in range(len(text1) -1, -1, -1):
            for pos2 in range(len(text2) -1, -1, -1):

                if text1[pos1] == text2[pos2]:
                    dp[pos1][pos2] = 1 + dp[pos1 + 1][pos2 + 1]
                else:
                    dp[pos1][pos2] = max(dp[pos1 + 1][pos2], dp[pos1][pos2 + 1])

        return dp[0][0]
```
