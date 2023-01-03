# Intuition
Heaps

# Approach
The strategy here is to create a min heap from the input nums. Then, if the length of the heap is greater than k, we pop from the heap until there's k elements left. This is because popping will always pop the minimum element from the list, so if we have k elements left in the heap, then the value at the front of the list is guaranteed to by the kth largest element (with the greatest element being at the back of the heap)

When we add values to the heap, we will almost always have k + 1 elements. We can then pop once, and return the value at the front of the heap which will be the kth largest element. We have to ensure that there are more than k elements in the list before popping to handle the edge case where k = 1 and the list is initially empty (as all we need to do is push once and return that element, NOT immediately pop)

# Complexity
- Time complexity: This can be broken into two parts:
    - init(): Heapifying the list takes $O(n)$ time. Removing elements from the heap takes $O(n-k(log(n)))$ time, which worse case if k << n is $O(nlog(n))$. Adding these together gices us $O(nlog(n))$
    - add(): Worst case for every add call we'll have to make 1 push and 1 pop call, which is $O(log(k))$. If m of these calls are made, this is $O(mlog(k))$
    - This gives us a total of $O(nlog(n) + mlog(k))$

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(N)$, since our heap is of length N initiallyt
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

Note that alternatively we could use quick select to achieve $O(n)$ time, which is what I did in kth-largest-element-in-array

# Code
```python3
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
