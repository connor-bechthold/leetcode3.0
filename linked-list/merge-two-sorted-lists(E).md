# Intuition
In place linked list magic

# Approach
We create a dummy head to return, and set a curr node to connect the two lists together. We iterate as long as both of the lists still have nodes left.

We compare the first values of the two lists. If list1's node val is less than or equal to list2's node val, we use the curr node to connect our current list's next to the list1 node. We move curr up to the new node we connected, and list1 up to the next node in its list.

This process continues between the two nodes until one of the lists has been fully connected to ours. At that point, we can simply connect the rest of our list to the rest of the remaining list, and return our list.

# Complexity
- Time complexity: $O(n + m)$, where n is the length of list1 and m is the length of list2
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        curr = newHead

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1

        return newHead.next                
```
