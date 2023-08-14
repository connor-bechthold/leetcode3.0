# Intuition
Intervals

# Approach
Little bit different than the classic intervals approach, but still the same idea. We get two sorted lists, one with the start times and one with the end times. We keep two pointers, one that goes across each list, and they both start at index 0 of their respective list. We also keep track of a current and global room count

The key here is that we compare the first start and first end times together. If a meeting starts before it ends (obviously) it will need a room. So, we increment the rooms needed, and increment the pointer to go the meeting that starts next. If it's also less than the first end time, we'll need another room, as that one needs to start before it finishes. The same pattern continues.

If a meeting ends before the next one starts, we decrement the number of rooms needed and move the end pointer up one. This repeats until all meetings have started. At each step, we update the local room count with the global room count.

# Complexity
- Time complexity: $O(nlog(n))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:

        startTimes, endTimes = [], []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)

        startTimes.sort()
        endTimes.sort()

        s, e = 0, 0
        globalMax, currMax = 0, 0

        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                currMax += 1
                s += 1
            else:
                currMax -= 1
                e += 1

            globalMax = max(currMax, globalMax)

        return globalMax
```
