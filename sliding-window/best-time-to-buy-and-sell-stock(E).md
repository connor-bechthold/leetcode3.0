# Intuition
Slide that window

# Approach
Keep track of the lowest buy that we can make. By default, we will set this to the first day and start from the second day. If the current stock price is less than pr equal to our current buy, update the current buy to be that price since it saves us money wasted. Otherwise, the stock price is higher than our lowest buy, which means we can calculate the possible profit. We keep track of the max profit in a variable, and return it at the end.

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
        lowest_buy = prices[0]

        for i in range(1, len(prices)):
            stock_price = prices[i]
            if stock_price <= lowest_buy:
                lowest_buy = stock_price
            else:
                max_profit = max(stock_price - lowest_buy, max_profit)
        
        return max_profit
```
