# Intuition
Big brain hashmap with linked list map

# Approach
The main idea behind the solution here is we want to map each node in the old list ot its replica in the new list. So, we first iterate over the old list and for each node, we create a replica node with the same value, and then store it in a hashmap with its key being the old node.

We then iterate over the old list again, with the goal of linking the new nodes together. For each old node, we get its old next and random node, and map those to the new next and random nodes through the hashmap. Then, we get the old node's new node, and link the new next and random nodes there.

Note that we store the key value pair "None: None" in the map because not every old node has a next or random pointer. So, we want to make sure that if we come across this case, the mapped node also is None

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_new_map = {None: None}
        curr = head

        while curr:
            new_node = Node(curr.val, None, None)
            old_new_map[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = old_new_map[curr]

            new_node.next = old_new_map[curr.next]
            new_node.random = old_new_map[curr.random]

            curr = curr.next

        return old_new_map[head]
```
