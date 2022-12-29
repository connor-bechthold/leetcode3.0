# Intuition
Linked list

# Approach
We keep a prev and curr pointer and set them to None and the head of the linked list respectively. We loop as long as the curr pointer exists.

Each time we save the next node after the curr pointer. We set the curr node to point to the prev node, set the prev node to the curr node, and set the curr node to the next node.

After we're done the head of the new list will be the prev pointer, which is returned.

# Complexity
- Time complexity: $O(n)$ for each node
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
```
