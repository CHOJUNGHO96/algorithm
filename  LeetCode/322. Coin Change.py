"""
서로 다른 액면가의 동전을 나타내는 정수 배열의 동전과 총 금액을 나타내는 정수가 주어집니다.

해당 금액을 구성하는 데 필요한 가장 적은 수의 동전을 반환합니다. 어떤 동전 조합으로도 해당 금액을 채울 수 없으면 -1을 반환합니다.

각 종류의 동전이 무한대로 있다고 가정해도 됩니다.



예제 1:
입력: 동전 = [1,2,5], 금액 = 11
출력 3
설명 11 = 5 + 5 + 1

예제 2:
입력: 동전 = [2], 금액 = 3
출력 -1

예제 3:
입력: 코인 = [1], 금액 = 0
출력 0
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        sort_coins = coins
        for coin in sort_coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


# [1, 1, 3, 2, 1, 3, 7, 4, 9, 2, 11]
a = Solution()
print(a.coinChange([186, 419, 83, 408], 6249))
print(a.coinChange([1, 2, 5], 11))
print(a.coinChange([2], 3))
print(a.coinChange([1], 0))
