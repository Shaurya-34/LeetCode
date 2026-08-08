class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]

            if profit > max_profit:
                max_profit = profit
    
            elif profit <= 0:
                left =right

        return max_profit