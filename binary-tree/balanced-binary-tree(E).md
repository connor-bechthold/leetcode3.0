# Intuition
Recursive dfs

# Approach
Very similar approach to finding the max depth of a binary tree. At each node, we get the depth of the left and right tree. We then take the absolute value of the difference between the two depths. We than logical AND the assertion that the difference is less than or equal to 1 with our global balanced variable, and update it. Note that we assert this var as True originally, and in order for it to stay True, it must logically AND True with the depth difference of every node. If one node is not balanced, it turns to False and can never turn True again. Once this comparison is done, we return 1 + the max depth of the left and right subtrees for the parent node to use and the process is repeated

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = [True]

        def dfs(node):
            if not node:
                return 0

            left_depth, right_depth = dfs(node.left), dfs(node.right)
            difference = abs(left_depth - right_depth)
            balanced[0] = balanced[0] and difference <= 1

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return balanced[0]
```
