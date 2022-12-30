# Intuition
Fast and slow pointers

# Approach
Return false if the list is empty. Put a slow pointer on the head, and a fast pointer on the second node. If there isn't a cycle, the fast pointer will reach it, and we return false. Otherwise, the fast and slow pointers will eventually meet if the fast pointer moves twice the speed as the slow pointer, in which case we can return true.

# Complexity
- Time complexity: $O(n)$. This is called Floyd's algorithm. Take the fact that the fast pointer starts 1 spot ahead of the slow pointer. That means that if a cycle exists, the fast pointer has to close a distane of n - 1 (assuming there's n nodes). Each iteration, the fast pointer closes the distance by two, and the slow pointer increases the distance by 1. This means that the net distance closed is 1. So, after n - 1 iterations, the pointers will meet. Thus, this is $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```
