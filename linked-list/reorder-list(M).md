# Intuition
Massive brain activity involving reversing list

# Approach
Split the list in half and reverse the second part. Then, we can simply merge the two lists together starting at the ends and moving inwards. This gives us the desired pattern.

To split the list in half, use fast and slow pointers. Wherever this slow pointer stops is the end of the first list, so we set the next pointer equal to null. It's important note that since odd lists can't be split in half, the first list may sometimes be greater.

We then reverse the second list as normal. Once this is done, we can start moving the heads of the two lists in, connecting them along the way. Since the second list may be shorter than the first, our final while loop condition is the second list's head.

# Complexity
- Time complexity: $O(n)$, as we only iterate over the nodes twice each
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        back_head = slow.next
        slow.next = None

        prev = None
        while back_head:
            temp = back_head.next
            back_head.next = prev
            prev = back_head
            back_head = temp
        
        front_head = head
        back_head = prev

        while back_head:
            temp = front_head.next
            front_head.next = back_head
            front_head = temp

            temp = back_head.next
            back_head.next = front_head
            back_head = temp
               
```
