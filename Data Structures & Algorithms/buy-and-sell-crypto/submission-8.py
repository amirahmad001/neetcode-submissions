class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        for j in range(1,len(prices)):
            curr_price = prices[j]
            max_profit = max(max_profit,curr_price-lowest_price)
            if curr_price < lowest_price:
                lowest_price = curr_price
        return max_profit
        