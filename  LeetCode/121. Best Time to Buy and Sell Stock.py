from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit


a = Solution()
# print(a.maxProfit(prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))
# print(a.maxProfit(prices=[2, 4, 1]))
print(a.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
# print(a.maxProfit(prices=[7, 6, 4, 3, 1]))
