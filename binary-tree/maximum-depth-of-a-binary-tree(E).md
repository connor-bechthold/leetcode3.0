# Intuition
Recursive dfs

# Approach
We can treat each node as its own tree. For each node, the max depth of it is the 1 + the max depth of the depths of its children. We recursively do this until a node doesn't exist (parent node has no child), in which case we just return 0 (base case)

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)
```
