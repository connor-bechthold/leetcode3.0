# Intuition
Union find I cannot get my head around this so the explanation is going to awful I'm sorry future connor

# Approach
The goal with union find is to treat each node like its own disjoint set. When we see an edge between two nodes, we treat this as taking the union of those disjoint sets and combining them into one. The trick here to find the edge that causes a cycle is if we try and find the union of two values that are ALREADY in the same set (i.e. they're connected!). If they're already connected through some path and we're now trying to connect them directly, this is a cycle

The idea of the algorithm is this:
- We have an array called parents where all values are set to -1. It is important to note that the value of each node will be between 1 and the number of nodes in the graph. So, we can say that the $ith$ index in parent corresponds to the node with value $i$. For each node, accessing this parents array will tell us the parent of the node (which set it is in). If we find that a parent is -1, it is its own parent, or the ROOT of the set
- We use the rank array to rank each parent. These are initially all set to 1. We use this when we're trying to union two different parents (or sets). To decide which set to merge into the other, the parent with the lower rank will get merged into the parent with the higher rank (because this results in less subsequent updates to other parents who were pointing at this old root parent). After a parent has another parent merged into it, its rank increases by one.
- The find function recursively finds the parent of a given node. It recursively calls until the base case, which is when the parent is -1, then it returns the index. We then update every subsequent index that has this parent with that index (path shortening)
- The union function takes two edges. We find the parents of those two edges with find. If the parents are EQUAL, they are already in the same set, and we can return False since we can't take the union of the same set (this is where the cycle is detected). If the parents are different, we merge based on rank:
    - If edge one's parent's rank is greater than or equal to edge two's parent's rank, edge two is merged into edge one
    -  If edge two's parent's rank is greater than edge one's parent's rank, edge one is merged into edge two
    - Finally, we go through every edge (or disjoint set) and union them all. If we can't union two edges, that means they were already in the same set, and would create a loop, so we return them

# Complexity
- Time complexity: $O(v)$ - union find is linear time with ranking and path compression
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(v)$ for arrays
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [-1 for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

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

            return True


        for one, two in edges:
            if not union(one, two):
                return [one, two]
```
