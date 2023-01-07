# Intuition
Dp

# Approach
The approach to this is extremely similar to decode ways. We keep a dp array of size length of the word + 1, initialize all the values to false, then set the last value to True. The idea here is that the ith index in dp corresponds to the ith character in the string. If we can find a word in the word dictionary starting at the ith character, then we set it to True ONLY IF the spot ahead of where the word ends is also True. This is because the words that we find to make up our string should have no gaps between them.

For example, if the word is "connor" and the dictionary contains ["onno"], we will find a match once we iterate back to the first o, but we will also need to ensure that the REST OF THE STRING AHEAD OF IT has also been covered by a word in the dictionary, otherwise it isn't valid. In this case, "r" is not in the dictionary, so the dp array will be false at this character. This is also why we set the last value in the dp array to True, because if we find a word that reaches the end of our string, it is clearly valid up until the character it starts at. At the end, the boolean value in the first index will store the result of the problem.

# Complexity
- Time complexity: $O(n^3)$, where n is the length of the input string. This is because we have a nested for loop, and also are slicing the string each time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) -1, -1, -1):

            for word in wordDict:
                length = len(word)
                if i + length <= len(s) and s[i : i + length] == word and dp[i + length]:
                    dp[i] = True
                    break
        
        return dp[0]
```
