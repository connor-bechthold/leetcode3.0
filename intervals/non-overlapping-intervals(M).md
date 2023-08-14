# Intuition
Intervals

# Approach
Like most interval questions, we start by sorting the intervals based on the start date. Here, we always keep track of the end time of the last interval we went through. Initially, this is the first interval in the list.

For every subsequent interval, we check if it's overlapping. If it's not, we update the previous end time to the current interval. If it is overlapping, we want to remove the interval that runs longer.

For example, if we have $(1, 3)$ and $(1, 5)$, we want to remove the latter because it stretches longer and is more likely to cause overlap. Thus, we choose the MIN end time and update the previous end value to match that. We also increment the counter for removals, since this is what that action is replicating.

# Complexity
- Time complexity: $O(nlog(n))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[0])

        removals = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] < prevEnd:
                removals += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        
        return removals
```
