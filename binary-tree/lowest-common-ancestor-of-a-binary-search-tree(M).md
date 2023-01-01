# Intuition
Recursive logic

# Approach
Starting at the root of the tree, we essentially want to find the node where the two given nodes branch out into two different subtrees. The current node is then the lowest common ancestor and can be returned.

Starting at the root node, we consider these cases:

- If both nodes are less than the current node, both nodes are somewhere in the left subtree. So, we can recursively call the function with the left subtree
- If both nodes are greater than the current node, both nodes are somewhere in the right subtree. So, we can recursively call the function with the right subtree
- The last case covers these scenarios:
    - If one node is less than the current node and the other node is greater than the current node, the nodes are in different subtrees, and we can return the current node
    - If one of the two nodes is the current node, the other node is guaranteed to be in one of its two subtrees. Since a node can be a descendant of itself, we can return the current node

# Complexity
- Time complexity: $O(logn)$, since we may need to visit a node at each level of the tree. Given a tree with $n$ nodes, the worst case depth is $logn$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node

        return dfs(root)

```
