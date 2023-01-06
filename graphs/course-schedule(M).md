# Intuition
Topological sort

# Approach
This is a more condensed version of a topological sort. A topological sort is defined as:

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
![image info](/images/Topological-Sort.png.webp)

So in this case, we can take each node of the graph to be a course, and there will be a directed edge from course A to course B if course B is a prereq of course A. If a topological sort exists, then there is obviously a way to take all required courses. Note that if a cycle exists in the graph, topological sort fails, which also means that we can't take all courses.

So, we start by making an adjacency list graph from the list of pre-reqs using the course as the key, and the value being a list of prereqs for that course. 

We do a topological sort with a dfs like so:
- Start at any node and add it to a visited set
- Do a dfs on all its connected edges 
- If a node we visit is already in our set of visited nodes, return False, as a topological sort can not be done with cycles
- The first node that we get to that has no children will be added to our finished set. This is because since it has no children, it will be at the END of our topological sort, as there are no further nodes that come after it. We can also remove it from our visited set, since we won't be looking at in anymore
- We then go back up the dfs and repeat the same steps. If we happen to re-visit any node that is already in finished, we can immediately return True as we know it's valid in the sort

We call this dfs with every node in the graph, since our graph may be disconnected and doing it on one node may not cover all nodes. We don't need to worry about performing a dfs on a node that's already been looked at, since we'll immediately return True if it's in finished. Once very node has returned True, we know there's a valid sequence of courses to take, and can return True. 

# Complexity
- Time complexity: $O(e + v)$, since we're visiting every node and edge once
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(v)$ for the sets
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        finished = set()

        hashmap = collections.defaultdict(list)
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)

        def dfs(course):
            
            if course in finished:
                return True

            if course in visited:
                return False

            visited.add(course)

            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            finished.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
```
