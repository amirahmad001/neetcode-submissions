class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy_day,sell_day = 0,1
        while sell_day < len(prices):
            profit = prices[sell_day] - prices[buy_day]
            max_p = max(profit,max_p)
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
            else:
                sell_day += 1
        return max_p
                
        