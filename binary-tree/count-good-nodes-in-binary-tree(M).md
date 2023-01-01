# Intuition
Recursive dfs

# Approach
Standard dfs, but at each step we keep track of the maximum value that we've seen so for in our path from the root to a node. If the value of the current node is greater than or equal than the max value we've seen, we add it as a good node, and also set it to the max value we've seen on that path. This process is repeated for all nodes

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
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
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [0]

        def dfs(node, max_val):
            if node:
                if node.val >= max_val:
                    good_nodes[0] += 1
                    max_val = node.val
                dfs(node.left, max_val)
                dfs(node.right, max_val)

        dfs(root, root.val)
        return good_nodes[0]
```
