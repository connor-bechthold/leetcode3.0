# Intuition
Prefix and suffix

# Approach
At any given index in the output array, the value is the product of multiplying the product of everything on the left side if the index by the right side of the index. So, we can iterate through the input array twice - once forwards and once backwards, keeping track of our product along the way

When moving forwards, the cumulative product at index i goes towards the value of the output array at index i + 1. When going backwards, the same is true, except it corresponds to the value of the output array at index i - 1. At each index of the output array, multiplying the forward and backward products together gives us the correct number

# Complexity
- Time complexity: $O(n)$. We're iterating through the input array two times, which is $O(n)$.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$ if we don't count the output array.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums) - 1):
            left *= nums[i]
            output[i + 1] *= left

        right = 1
        for i in range(len(nums) - 1, 0, -1):
            right *= nums[i]
            output[i - 1] *= right

        return output
```
