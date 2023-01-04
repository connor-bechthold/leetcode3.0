# Intuition
Heap, queue, and hashmap??????????

# Approach
The strategy here is keeping track of the occurrences that each task appears. Naturally, we want to finish the tasks that have the most occurrences first because the delay will affect these the most. So we use a map to count the occurences and store these occurences in a priority queue. Note that we want a max heap, which is why the occurrences are negative. 

Another problem is once we pop a task from a queue and increment it, we have to account for the delay. We obviously can't put it back on the heap (unless n == 0), so we use a queue instead. The queue will store a tuple that will store a task's occurrence, and the time that it can be looked at again (this is set by adding n to the time when it was added to the queue). Every unit of time we check this queue for tasks that can be removed and added back to the heap.

This loop continues until there are no values in the queue AND the heap. We then return the time.

# Complexity
- Time complexity:
    - Adding to hashmap takes $O(n)$
    - Adding to heap is $O(26)$
    - Heapifying is $O(26)$
    - Going through every value in the heap/queue is $O(n)$, and each time we see a task we may push/pop a value onto the heap which is $O(log(26))$
    - Adding this all together gives us $O(n)$    
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: All data structures are $O(26)$, so this is $O(1)$ 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = collections.defaultdict(int)
        for task in tasks:
            hashmap[task] += 1

        heap = []
        for occurrence in hashmap.values():
            heap.append(occurrence * -1)

        heapq.heapify(heap)
        queue = collections.deque()
        time = 0

        while len(heap) or len(queue):

            time += 1

            if len(heap):
                occurrence = heapq.heappop(heap)
                occurrence += 1

                if occurrence < 0:
                    queue.append((occurrence, time + n))

            if len(queue) and time == queue[0][1]:
                 heapq.heappush(heap, queue.popleft()[0])

        return time
```
