# Intuition
Bfs

# Approach
Standard bfs. We first check to see if the tree is empty. If it isn't, we push the root node onto the queue. We loop while there are still items in the queue. We make sure that for each level, we only iterate through the nodes on that level (since we'll also be pushing children on the list at the same time). We only push each node's children on the list if it exists. We also push each node's value onto a list. At the end of each level, we push the created list onto our result list.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$. For a binary tree, there will be a max of $n/2$ nodes on one level (queue) at once
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while len(queue):
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)

            res.append(level)

        return res
```
