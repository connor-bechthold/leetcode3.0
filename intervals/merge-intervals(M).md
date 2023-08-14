# Intuition
Intervals

# Approach
This is a similar approach to insert interval with a few key details. The first key step is to first sort the interval list by the start value, which makes it easier to merge intervals later.

After this is done, we add the first interval to the result list. For each following interval, we simply check to see if the interval comes after the interval at the end of the list. If it is, we add it and move on. If it's not, there's overlap. However, since the start values or sorted, we simply only update the max of the end values.

# Complexity
- Time complexity: $O(n^2log(n))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ for the sort
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):

            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])

            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])

        return res
```
