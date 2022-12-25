# Intuition
Sliding window

# Approach
Left and right pointer which start at the first and second day. The left pointer will stay at the lowest stock price we can buy, and the right pointer will be on the price we sell at. If the right pointer is less than or equal to the left, we set the left equal to the right since it's a lower buy price. Otherwise, we can make a profit, and we update a global variable the price at the right pointer minus the left pointer.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                max_profit = max(prices[r] - prices[l], max_profit)
            r += 1
        
        return max_profit
```
