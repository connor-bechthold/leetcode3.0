# Intuition
Use the concepts behind two sum sorted

# Approach
This problem can be boiled down to picking one element from the list as a "target", taking its negative, and then performing two sum on the rest of the list with our target. 

The tricky part of this problem is avoiding duplicates. However, this can be avoided by sorting the input list first. When we do this, we can ensure that we never perform our two sum computation with the same target by simply checking if the current element we're looking at is the same as the previous element we looked at (as long as we're not at the 0th index)

Now that we know the list is sorted, it is clear to see that we just need to perform two sum sorted. However, the twist is that there may be more than one solution in each case we face. So, once we find a valid solution, we can increment the start pointer by one and repeat the algorithm. Note that there may be duplicates, so when we're incrementing start, we want to make sure we're not still pointing to the same value or we'll get duplicates.

# Complexity
- Time complexity: $O(n^2)$. Two sum sorted is $O(n)$ and at most we'll perform this $n - 2$ times, which is in total $O(n^2)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$. This is because worst case, sort takes $O(n)$ space
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[start] + nums[end]
                if total < target:
                    start += 1
                elif total > target:
                    end -= 1
                else:
                    output.append([target * -1, nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return output         

```
