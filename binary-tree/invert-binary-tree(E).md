# Intuition
Recursive switch

# Approach
Every node we see, the left child needs to become the right child and vice versa. So, starting at the root, we flip the children and then recursively call the function with the children's children. This continues until we reach a child/root that doesn't exist, in which case we do nothing and return

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if node:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
        
        invert(root)
        return root
```
