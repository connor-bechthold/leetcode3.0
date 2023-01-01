# Intuition
Inorder iterative dfs

# Approach
The idea here is to always go left when we can. If we can't go left, we go right as few times as possible until we can go left again. If we can't go right, we work back up the tree.

We use a stack for this iterative solution, and a curr variable to keep track of the node we're currently looking at. We loop while curr exists or there's still nodes in the stack. We start by setting curr to the root, pushing this, and moving left until we can't. Once we can't go left, we pop. The nth pop will represent the nth smallest element, which is what we keep track of as we pop, and once we pop the kth time, we return that value. If we pop and still need to look at smaller elements, we set curr to the right node, and go back to the start, where one of two things happen:

- If a right node does exist, we push it on the stack, and then continue to look for more left nodes off of the right node
- If a right node doesn't exist, then curr will be null, and we will pop off higher nodes from the stack, and continue the process

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        stack = []
        curr = root

        while len(stack) or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
```
