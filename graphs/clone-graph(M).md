# Intuition
Dfs with hashmap

# Approach
The idea here is to have a hashmap where the key is a node in the graph, and the value is our deep copy node that needs to be exactly the same as the original. So, every node that is passed into dfs will first get a deep copy node stored in the hashmap. Then, we go through the original node's neighbors (if they exist). We want to go through the neighbors because we want to construct the adjacency list for the deep copy node. However, in order for this to happen, each one of the nodes in the adjacency list must exist in node map. This way we can construct the deep copy list by looking up each neighbor in node map and adding the deep copied version to the list. So, we first check if the adj node exists in node map, and if it doesn't we call dfs with the adj node to do so.

# Complexity
- Time complexity: $O(e + v)$, where $e$ is the number of edges and $v$ is the number of vertices
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(v)$ for the nodemap
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        nodeMap = {}

        def dfs(node):
            newNode = Node(node.val)
            nodeMap[node] = newNode

            if node.neighbors:
                adjList = []
                for adjNode in node.neighbors:
                    if adjNode not in nodeMap:
                        dfs(adjNode)
                    adjList.append(nodeMap[adjNode])
                nodeMap[node].neighbors = adjList

        if not node:
            return None

        dfs(node)
        return nodeMap[node]
```
