# Intuition
Binary search is hard to see here, but it's only an optimization

# Approach
The solution here is simple. We need to pay attention to the fact that the amount of hours Coco has to eat all piles is greater than or equal to the number of piles. In other words, the max value that k will ever be will be is the max number of bananas in one pile.

Keeping this in mind, the solution is to iterate from k = 1 to the max, and for each k, go through each pile and return the first k that allows for all the bananas to be eaten in the time alloted. However, this iteration to find the right k is $O(max(piles))$. We can do even better here with a binary search. We can binary search through $k = 1....max(p)$. The midpoint of a search will be our test k. If this k is valid, then we move the right pointer in to see if we can find a smaller k. If this k is not valid, then we must move the left pointer in to find a higher k. Repeat this until the search is finished, and return the lowest k found along the way (will be updated through the search)

# Complexity
- Time complexity: $O(nlog(max(piles)))$. The $log(max(piles))$ is the time it takes to binary search through the k's, and in order to test if a k is valid, we may have to iterate over every pile at worst case which is $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        def isValidK(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                if hours > h:
                    return False
            return True

        while l <= r:
            k = (l + r) // 2
            if isValidK(k):
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

```
