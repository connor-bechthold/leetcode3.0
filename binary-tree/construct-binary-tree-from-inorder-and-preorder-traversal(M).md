# Intuition
Big brain traversing

# Approach
The big idea here is identifying the relationship between preorder and inorder traversal. Preorder traversal travels the root node, left subtree, and then right subtree. Inorder traversal travels the left subtree, root node, and then right subtree. 

The first element in the preorder list will be the root node of the entire tree. All node values are unique, so we can find this value in the inorder list. Lets say for example the first element was 4, and the inorder traveral looked something like this: $[1,2,\textbf{4},8,3]$

All the values to the LEFT of 4 are in the LEFT subtree of 4, and all the values of the RIGHT of 4 are in the RIGHT subtree of 4. Also remember that preorder and inorder traversal are virtually the same, except for the fact that preorder visits the root node FIRST.

So, with this and mind we can perform the following algorithm:
- Keep a map of all the values in the inorder list as keys, and the indexes of these keys as values
- Keep a global index of the current preorder node we are at 
- Keep start and end pointers that will signify the range of nodes that we still need to add to a node's subtree
- First we access the first preorder value (the global root node) and create a TreeNode with it
- We then find that value's index in the inorder list
- We recursively set the node's left and right subtrees as follows:
    - For the left subtree (node.left), we want to keep going left as long as there are nodes to add in the left subtree. **Remember we increase the global preorder index by one each time. Preorder will keep going left until it can't, and then it goes right. This is why the inorder is important. At each step, it will tell us whether we need to keep adding to the left subtree, or add to the right subtree.** Hence, when we go left, we change the bounds to (start, mid - 1) which covers the number of nodes that still need to be added to the LEFT of that preorder node.
    - The same goes for the right subtree (node.right). Keep in mind that once we get here, **the preorder index is already in the right spot since we went left BEFORE right**. The bounds change to cover the values in the RIGHT subtree of the node, which is (mid + 1, end)

An example:
![image info](/images/tree.jpg)

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        preorder_index = [0]
        
        def rec(start, end):
            if end < start:
                return None

            root = TreeNode(preorder[preorder_index[0]], None, None)
            mid = inorder_map[root.val]

            preorder_index[0] += 1

            root.left = rec(start, mid - 1)
            root.right = rec(mid + 1, end)

            return root

        return rec(0, len(inorder) - 1)            
```
