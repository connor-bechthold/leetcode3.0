# Intuition
Recursive dfs

# Approach
We compare each aligning node of each tree one by one. If both nodes don't exist, they are the same node. If one node exists and one node doesn't, they are not the same node. If both nodes exist but their values are different, they are not the same node. Once it is verified two nodes are the same, we call the function again with both of their left and right subtrees. At the end, if both the root node's left and right subtrees align, they must be the same tree.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node_p, node_q):
            if not node_p and not node_q:
                return True
            if node_p and not node_q or not node_p and node_q:
                return False
            if node_p.val != node_q.val:
                return False
            return dfs(node_p.left, node_q.left) and dfs(node_p.right, node_q.right)

        return dfs(p, q)
```
