# Intuition
Fast and slow pointer Floyd algo magic

# Approach
Note that every value in the array is within an index in the array so it replicates a linked list (omitting the index 0, which can be seen as the starting point). We can then reference this fast and slow pointer diagram to derive Floyd's algo used, where slow pointer starts on the second value in the list (nums[0]) and the fast pointer starts at the third (nums[1])

In this example, the duplicate entry is 1 (the start of the cycle). Take the distance from the start of the list to the start of the cycle as $p$, the distance from where the two pointers meet to the start of the cycle as $x$, and the length of the cycle of $C$.

We the know the fast pointer moves at twice the speed of the slow pointer so the distances travelled are this:
$2 * slow = fast$

More specifically if we look at the distance travelled for the slow pointer to the meeting point:

$p + C -x$

The fast pointer has to go 1 time around the cycle to catch the slow pointer, and then meets the slow pointer somewhere in the loop for a total distance of:

$p + C + C - x$

$p + 2C - x$

Subbing in the equation above:

$2(p + C - x) = p + 2C - x$

$2p + 2C - 2x = p + 2C - x$

$p = x$

We see that the meeting point is the same distance from the start of the cycle as the start of the list to the start of the cycle. So once we find the meeting point, we can put the slow pointer to the start of the list. We can move the slow pointer and fast pointer simultaneously until they equal, which will be the start of the cycle, and we can then return the duplicate 

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```
