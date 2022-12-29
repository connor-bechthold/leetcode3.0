# Intuition
Linked list with two pointers and dummy node

# Approach
We create a dummy node which will point the head of the list. We set our first pointer to this dummy node, and the second pointer to the head of the list. We move the second pointer n spots from the head. Then, we move both pointers by one spot until the second pointer is past the end of the list. At this point, the first pointer is guaranteed to be pointing to one spot before the node to be removed (in the case that we're removing the head, the first pointer will stay on the dummy node). To remove that node, it's as simple as setting the first pointer's next to the node after the node to remove. Finally, we can return the head by returning the node the dummy node's next is pointing to.

# Complexity
- Time complexity: $O(n)$
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        end = head

        offset = 0
        while offset < n:
            end = end.next
            offset += 1

        while end:
            prev = prev.next
            end = end.next

        prev.next = prev.next.next
        return dummy.next
```
