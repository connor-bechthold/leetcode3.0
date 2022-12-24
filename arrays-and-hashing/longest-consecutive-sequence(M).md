# Intuition
Hashset, global max

# Approach
Convert the input list to a hashset to remove all duplicate elements. We want to go through every unique value in the set, but in order to count the length of all subsequences, we want to make sure that the element we're on is the first one in the sequence. So, check that num -  1 does not exist. Once verified, we can count the length of the subsequence, and then continously update a global max length.

# Complexity
- Time complexity: $O(n)$. Worst case scenario is we have a subsequence of length n and go through every n value of the subsequence but the first value. Once we reach the first value, we go over n values again. However, $2O(n) = O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in hashset:
            if num - 1 in hashset:
                continue
            curr = 1
            next_val = num + 1
            while next_val in hashset:
                curr += 1
                next_val += 1
            longest = max(curr, longest)
        return longest
```
