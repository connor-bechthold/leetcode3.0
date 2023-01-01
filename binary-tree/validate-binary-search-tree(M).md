# Intuition
Search tree tings

# Approach
The idea behind this approach is at each node, we want to be able to access a lower and upper bound in which is the node's value has to fall between. So, at the beginning of the function, we first check that the node falls within the bounds, and if not, return False (note that initially the bounds are infinite). If we have a left child, all the nodes in that subtree must be LESS than the MIN of the max value the node could be and the current node. If we have a right child, all the nodes in that subtree must be GREATER than the MAX of the minimum value the node could be and the current node. These bounds are updated as so when the function is recursively called, and the process repeats

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, minimum, maximum):

            if node.val <= minimum or node.val >= maximum:
                return False

            left_valid = right_valid = True
            if node.left:
                left_valid = validate(node.left, minimum, min(node.val, maximum))
            if node.right: 
                right_valid = validate(node.right, max(node.val, minimum), maximum)
            return left_valid and right_valid


        return validate(root, float("-inf"), float("inf"))
        
```
