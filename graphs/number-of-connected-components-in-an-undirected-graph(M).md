# Intuition
Union find

# Approach
The whole reason why union find works is explained in redundent connections. We are literally doing the exact same here, except keeping track of the numnber of connected components that we have. Since we start with v vertices, we initially have v connected components. Everytime we merge two parents that aren't in the same set, we are combining connected components. Thus, the overall number of connected components we have decreases by 1 (which is why we return 1, and subtract from the overall count). If we are merging two edges which share the same parent, we're simply adding onto the existing connected component, so the overall number of connected components stays the same, and we return 0.

# Complexity
- Time complexity: $O(v)$ for union find with path compression and ranking
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(v)$ for arrays
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [-1 for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        count = len(edges)

        def find(val):
            if parents[val] == -1:
                return val
            parents[val] = find(parents[val])
            return parents[val]

        def union(one, two):
            parOne, parTwo = find(one), find(two)

            if parOne == parTwo:
                return 0

            if rank[parOne] >= rank[parTwo]:
                parents[parTwo] = parOne
                rank[parOne] += 1
            else:
                parents[parOne] = parTwo
                rank[parTwo] += 1

            return 1


        for one, two in edges:
            count -= union(one, two)

        return count
```
