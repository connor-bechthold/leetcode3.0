# Intuition
Two pointers

# Approach
Area can be maximized with width, so we put two pointers at each end of the array to do so. From there, we calculate the area using the smaller of the two walls, and update the global max everytime we find a larger area. After this, we move the two pointers in. At this point, we want to maximize height, so whichever pointer is at a smaller wall gets moved in one, and the process repeats until there's no more walls to compare.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_amount = float(-inf)

        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_amount = max(area, max_amount)

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        
        return max_amount
```
