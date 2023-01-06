# Intuition
Union find

# Approach
A valid tree is one that is one entirely connected component and has no loops. Conveniently, both of those things can be accoomplished and checked by union find at the same! See redundant connection for the loops and number of connected components in an undirected graph for more detail. Essentially all we're doing is decrementing count everytime we merge two DIFFERENT parents (as this combines 2 components into 1), and also returning True. We immediately return False if we see a loop. If there are no loops, we also need to verify at the end that the number of connected components is 1.

Note: To make the arrays, we use $n$, as this is the number of nodes in the array. We don't use edges like usualy since there may be less edges than nodes if the graph isn't connected.

# Complexity
- Time complexity: $O(v)$ for union find with path compression and ranking
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(v)$ for arrays
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [-1 for i in range(n)]
        rank = [1 for i in range(n)]

        count = [n]

        def find(val):
            if parents[val] == -1:
                return val
            parents[val] = find(parents[val])
            return parents[val]

        def union(one, two):
            parOne, parTwo = find(one), find(two)

            if parOne == parTwo:
                return False

            if rank[parOne] >= rank[parTwo]:
                parents[parTwo] = parOne
                rank[parOne] += 1
            else:
                parents[parOne] = parTwo
                rank[parTwo] += 1

            count[0] -= 1
            return True

        for one, two in edges:
            if not union(one, two):
                return False

        return count[0] == 1
```
