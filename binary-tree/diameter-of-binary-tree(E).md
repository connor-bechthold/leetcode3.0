# Intuition
Recursive dfs

# Approach
At any given node, the diameter is the max depth of the left tree + the right tree + 2 (where 2 accounts for the 2 edges connecting the node to each of its children). So, starting at the bottom of the tree and moving up, we can continously find and update diameters.

At any leaf node, the depths of the child nodes are zero. So, when the leaf node gets these depths, it will calculate its max diameter by adding 2 to these depths, which is obviously wrong. To avoid this, we can instead return -1. Once the diameter at that level is calculated, it is compared with the global diameter (stored in a list so it can be updated through the function), and updated if necessary. Finally, the max depth of the max depths is returned, so the parent node can perform the same calculation and ensure that the diameter is using the sum of the deepest depths. 

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]

        def dfs(node):
            if not node:
                return -1
            max_depth_left, max_depth_right = dfs(node.left), dfs(node.right)
            diameter[0] = max(2 + max_depth_left + max_depth_right, diameter[0])
            return 1 + max(max_depth_left, max_depth_right)

        dfs(root)
        return diameter[0]
```
