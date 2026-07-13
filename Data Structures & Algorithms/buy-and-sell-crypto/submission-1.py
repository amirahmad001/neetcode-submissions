class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_left = []
        max_right = []
        min_l,max_r = float('inf'),0
        for i in range(len(prices)):
            if prices[i] < min_l:
                min_l = prices[i]
            min_left.append(min_l)
        for i in range(len(prices)-1,-1,-1):
            if prices[i] > max_r:
                max_r = prices[i]
            max_right.append(max_r)
        max_right = list(reversed(max_right))
        for i in range(len(prices)):
            if max_right[i] - min_left[i] > max_profit:
                max_profit = max_right[i] - min_left[i]
        return max_profit

        