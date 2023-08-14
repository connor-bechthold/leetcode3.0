# Intuition
Intervals

# Approach
This is actually decievingly difficult, but can be broken down into 3 different cases which are outlined below. We iterate through the intervals given and construct a return list.

There are two cases for when the new interval doesn't overlap:
- End of new interval is less than the start of the current interval. This means that the new interval can simply be appended to the list, and the rest of the intervals can then be copied over
- Start of new interval is less than the end of the current interval. This means the current interval can be appended to the list, however, we keep iterating since the new interval could have overlap with a following interval

The third case is only reached when the first two are passed, meaning that there's an overlap. We perform the following algorithm to merge:
- The start of the interval is the min of the starts of the merging intervals
- The end of the interval is the max of the ends of the merging intervals

We also don't add this to the res list, as there may be overlap further on. Thus, if the iterating finishes and we haven't returned, we append the new interval.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)

        return res
```
