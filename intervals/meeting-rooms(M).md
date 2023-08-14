# Intuition
Intervals

# Approach
Again, sort intervals by start date. This is very similar to non-overlapping intervals, where we keep track of the end of the previous interval, which is initially the first interval. As soon as the beginning of the next interval is less than the previous end, we return False, as there's overlap. If we make it through every interval, return True.

# Complexity
- Time complexity: $O(n^2log(n))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key: lambda x: x.start)

        prevEnd = intervals[0].end

        for i in range(1, len(intervals)):

            if intervals[i][0] < prevEnd:
                return False

            prevEnd = intervals[i][1]

        return True
```
