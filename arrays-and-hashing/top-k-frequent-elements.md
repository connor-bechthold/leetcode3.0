# Intuition
Bucket sorting

# Approach
Use a hashmap to store the number of occurrences of each input number. We know that given an input of size n, the max number of frequencies any given number can have is n. So, we make a separate array of of length n + 1, where index i corresponds to the input numbers that appeared a frequency of i times. We can go through our hashmap and add each number to a "bucket" accordingly (one index will store an array which may contain zero or more input numbers). Then, to determine the top k highest occurences, we can iterate from the back of the array to the front (highest to lowest frequencies), and add it to our output array until we reach a length of k.

# Complexity
- Time complexity: $O(n)$. For the last part, the worst case is we have an input array with n different numbers, meaning index 1 will have an array of length n. So, starting at the end of the array, we will iterate n times before iterating n more times through index 1. This is $nO(1) + O(n) = O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$. Hashmap is length n, and similar to above, worst case is we have n spots of our array storing an $O(1)$ empty array, and the first index storing an $O(n)$ size array, which is in total $O(n)$ space
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = collections.defaultdict(int)
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            seen[num] += 1
        for num, freq in seen.items():
            frequency[freq].append(num)
        output = []
        for i in range(len(nums), -1, -1):
            for j in range(len(frequency[i])):
                output.append(frequency[i][j])
                if len(output) == k:
                    return output

        
        
```
