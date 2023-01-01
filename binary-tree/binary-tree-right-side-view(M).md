# Intuition
Bfs

# Approach
Standard bfs, but the key thing to notice here is that we always keep track of the last node we see on each depth level, as this will always be the node seen from the right side of the tree

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        res = []
        length = 1

        while length:
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == length - 1:
                    res.append(node.val)
            length = len(queue)

        return res
```
