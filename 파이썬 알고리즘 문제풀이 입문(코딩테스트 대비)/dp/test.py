"""
4 7
6 13
4 8
3 6
5 12

4 6
6 13
3 8
7 15
2 6
"""
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
dic = {}
dp = [0] * (m + 1)
for _ in range(n):
    _a, _b = map(int, input().split())
    if _a == 1 or _a == 2:
        dp[_a] = _b
    arr.append(_a)
    dic.update({_a: _b})
# 무게별로 정렬
arr.sort()


for i in range(3, m + 1):
    for j in range(i - 1, round(i // 2), -1):
        # 반으로 나눠서 가야함
        if j in arr and i - j in arr:
            dp[i] = max(dp[i], dic[i - j] + dic[j])

print(max(dp))
