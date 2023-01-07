# Intuition
Dp

# Approach
The whole idea here is we have dp array where th ith index corresponds the min amount of coins it takes to make an amount of i. In order to get the min coins for amount, we work our way from the bottom up,

We first create a dp array filled with -1 of length amount + 1, to account for 0. We then set the min coins for 0 to 0, since it takes 0 coins to make an amount of 0. We start iterating from an amount of 1 up to our target amount. 

If that amount is in the coins we have, we can immediately set the min coins to 1 since we can literally just use that coin. Otherwise, we iterate through each coin we have and SUBTRACT the value from our current amount (if we can of course). If we see the new value we have has value over 0 in the dp array, we know that we can make that value with that amount of coins. That means we can take that value and the coin value we subtracted to get the min coins for our current value. 

Note that we go through every coin and keep track of the min coins we see. We set this value initially to amount + 1, since it is impossible to make that amount with more than amount coins. This just guarantees that any valid value we see is smaller than the default. We only update the index in the dp array if we find a valid value, otherwise it stays at -1.

This process repeats until the end, where the min number of coins will be at index amount.  

# Complexity
- Time complexity: $O(n * amount)$, where n is the number of coins that we have to look through for each amount we come across.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(amount)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):

            if i in coins:
                dp[i] = 1
            else:
                minCoins = amount + 1
                for coin in coins:
                    if i - coin >= 0 and dp[i - coin] > 0 and dp[i - coin] < minCoins:
                        minCoins = dp[i - coin]

                if minCoins != amount + 1:
                    dp[i] = 1 + minCoins

        return dp[amount]
```
