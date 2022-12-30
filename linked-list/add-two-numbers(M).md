# Intuition
Linked list moment

# Approach
Standard addition while keeping track of carry. Only trick is that one of the numbers may be shorter, so to avoid writing down the same logic with only one of the lists and a carry, we set the value to zero so we can continue. Also note the case where we completely finish addition but there's still a carry - the carry then needs its own node

# Complexity
- Time complexity: $O(max(m, n))$
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        prev = dummy

        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            node = ListNode(total, None)
            prev.next = node
            prev = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next   
```
