# Intuition
Max heap

# Approach
Convert each point to a tuple that stores the distance from the origin (in negative) and the point itself. If the heap size is less than k, we simply add it to the heap. Otherwise we perform a push pop. We can perform a push pop because the distances are negative, when we pop after pushing, the most negative (largest) distance will be popped off the heap. At the end, the k values on the heap will be the k closest distances to the origin

# Complexity
- Time complexity: $O(Nlog(k))$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(k)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance_point = ((point[0] ** 2 + point[1] ** 2) * -1, point)
            if len(heap) < k:
                heapq.heappush(heap, distance_point)
            else:
                heapq.heappushpop(heap, distance_point)

        res = []
        for dist, point in heap:
            res.append(point)

        return res
```
