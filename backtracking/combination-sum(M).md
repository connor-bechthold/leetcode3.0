# Intuition
Trackbacking

# Approach
Pretty classic backtracking approach where we keep track of a pos variable and a total sum. If we reach a sum that equals the target, we can add it to our output and break. We can also simply break if our sum is greater than the target. Otherwise we iteratively add elements from our pos up to the length of the array and recursively call the function again. An important note is that we can use the same element more than once, so when we're recursively calling the function we pass in the current pos we're at. All the numbers in the input are unique, so we don't need to worry about seeing duplicates in the future. 

# Complexity
- Time complexity: At each node we can make a max of $n$ decisions (n-ary tree). We can do this up to the depth of the tree, which can worse case be $t$ if there is a 1 in our input. This is probably an overestimate, so we can disregard the copy() call that occurs for a total of $O(n^t)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: The depth of the recursive stack depends on the min element: $O(t / min(c))$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []

        def backtrack(pos, total):
            if total == target:
                res.append(curr.copy())
            elif total > target:
                return
            else:
                for i in range(pos, len(candidates)):
                    num = candidates[i]
                    curr.append(num)
                    backtrack(i, total + num)
                    curr.pop()

        backtrack(0, 0)

        return res      
```
