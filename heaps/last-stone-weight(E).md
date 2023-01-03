# Intuition
Max heap
# Approach
We can easily create a max heap by first converting the list of stone weights to a negative value and then creating a heap with heapify. Then we can loop and combine/destroy stones until there's 0 or 1 stones left.

# Complexity
- Time complexity: $O(nlog(n))$, because worst case we'll have to push/pop 3 times to remove a net of one stone, until there's 0 or 1 stones
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(stone * -1)
            
        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest, second_heaviest = heapq.heappop(heap), heapq.heappop(heap)
            if heaviest != second_heaviest:
                heapq.heappush(heap, heaviest - second_heaviest)

        if len(heap):
            return heap[0] * -1
        return 0
```
