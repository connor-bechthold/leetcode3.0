# Intuition
Two pointers

# Approach
<!-- Describe your approach to solving the problem. -->
Initialize two pointers, one at the start of the list, and one at the end. If the sum is less than what we need, move the start pointer up one spot (since ordered, this will increase sum). If the sum is more than we need, move the end pointer back one spot (since ordered, this will decrease sum).

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while(True):
            total = numbers[start] + numbers[end]
            if total == target:
                return [start + 1, end + 1]
            elif total < target:
                start += 1
            else:
                end -= 1
```
