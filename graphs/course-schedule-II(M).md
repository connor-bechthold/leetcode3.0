# Intuition
Topological sort

# Approach
Exact same as course schedule, but we actually want to keep track of the nodes that we mark as finished and return the order. We don't want to return False if we have a cycle, so instead we keep a global variable called cycle that we update if a node we're at was already visited. If at any point we see that a cycle exists, we return nothing because we can't complete the sort successfully

We use a stack to push all of our finished node on (remember that the first finished node will have no children and thus be at the end of the list, which works with a stack since it's First In Last Out). We also have to call dfs on every node in the graph in case the graph is disconnected in some places.

At the end of this loop, we return an empty list if there's a cycle, otherwise we return the stack we created.

# Complexity
- Time complexity: $O(e + v)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(v)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        cycle = [False]
        visited = set()
        finished = set()
        stack = []

        hashmap = collections.defaultdict(list)
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)

        def dfs(course):

            if cycle[0] or course in finished:
                return

            if course in visited:
                cycle[0] = True
                return

            visited.add(course)

            for prereq in hashmap[course]:
                dfs(prereq)

            visited.remove(course)
            finished.add(course)
            stack.append(course)

        for course in range(numCourses):
            dfs(course)

        return [] if cycle[0] else stack
```
