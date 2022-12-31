# Intuition
Recursive dfs

# Approach
This is very similar to same tree. We can bascially perform a dfs through every node, and for each of these nodes, perform same tree with the subtree. If it returns True, then we've found a successful subtree

# Complexity
- Time complexity: $O(ST)$, where S is the number of nodes in the root tree, and T is the number of nodes in the subtree
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(node_p, node_q):
            if not node_p and not node_q:
                return True
            if node_p and not node_q or not node_p and node_q:
                return False
            if node_p.val != node_q.val:
                return False
            return isSameTree(node_p.left, node_q.left) and isSameTree(node_p.right, node_q.right)

        def dfs(node):
            if not node:
                return False
            left_result, right_result = dfs(node.left), dfs(node.right)
            return isSameTree(node, subRoot) or left_result or right_result

        return dfs(root)

```
