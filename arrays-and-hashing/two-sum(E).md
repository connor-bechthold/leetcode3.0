# Intuition
Hashmap!

# Approach
Iterate through the list, storing the difference of subtracting each value from the target value in the hashmap of the form difference : index. For each value we go over, check if that value is in the hashmap as a difference. If the difference exists, then we've found a number that when added with our current number sums to the target. From there, we can return the two indexes.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        for index, num in enumerate(nums):
            if num in hashmap:
                return [index, hashmap[num]]
            else:
                difference = target - num
                hashmap[difference] = index
```
