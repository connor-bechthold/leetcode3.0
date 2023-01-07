# Intuition
Dp moderate big brain

# Approach
This is a top down approach that is best demonstrated with an example that uses tabulization, but it will be fairly obvious to see how we can transfer the states we use to variables to achieve constant space

Take the string 2026. There are 2 ways to decode this - (20, 26) and (20, 2, 6). We start by making a DP array that is the length of the string + 1, and is set like this: $[0, 0, 0, 0, 1]$, where the very last spot is extra and set to a 1, which you will see why shortly.

We start by looking at the 6. Since this value is not a 0, it can be added onto any decoding sequence in front of it and still be valid. The number of decoding sequences we've made with the values in front of us will be stored in the index in front of us, so we set it equal to that (this is why we have the 1 stored at the end by default). We also check to see if we can make this a double digit number by looking at the number ahead of us, but we can't, so we finish. $[0, 0, 0, \textbf{1}, 1]$

We now look at the 2. 2 can be added to the 6 ahead of us, which is only 1 valid sequence as we look at the index ahead of us. We also notice that we can make 26 by adding the 6 ahead of us. Similar to before, we look at the value in the array two indexes ahead and see it's 1, so we add that one as well. $[0, 0, \textbf{2}, 1, 1]$

We now look at the 0. 0 is a special case, since if we add to any valid sequence ahead of us, it will make the sequence invalid. So, we leave this spot as 0. $[0, \textbf{0}, 2, 1, 1]$

We finally look at the 2. We see there are no valid sequences in the index before, so we leave it as 0. However, we see that we can add the 0 and make 20. So, we look 2 indexes ahead and see that after the 20 comes "26", and we can make 2 sequences with that. So, we increment by 2. $[\textbf{2},0, 2, 1, 1]$.

We then return the first valie in our array, which is two. Notice again that we only needed three states. The current state (dp[i] = curr), the state one ahead (dp[i + 1] = oneAhead), and the state two ahead (dp[i + 2] = twoAhead). Thus, we can remove the array completely and get the exact same solution as shown in the code below.



# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def numDecodings(self, s: str) -> int:

        curr = 0
        oneAhead = 1
        twoAhead = 0

        for i in range(len(s) - 1, -1, -1):

            if s[i] != "0":
                curr += oneAhead

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                curr += twoAhead

            twoAhead = oneAhead
            oneAhead = curr
            curr = 0

        return oneAhead
```
