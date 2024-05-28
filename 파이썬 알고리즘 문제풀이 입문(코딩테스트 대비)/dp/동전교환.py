"""
동전교환
다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환
해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.
 ▣입력설명
첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종
류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
각 동전의 종류는 100원을 넘지 않는다.
 ▣출력설명
첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
 ▣입력예제 1
3
1 2 5
15

 ▣출력예제 1
 3

▣입력예제 1
5
1 5 7 11 15
39

▣출력예제 1
5

풀이과정
납색알고리즘을 사용하여 dp에 거슬러야할 동전만큼 list만든다.
해당 금액을 거슬러야하는 동전의 최소개수를 값으로 넣는다
"""
# 내풀이
N = int(input())
K = list(map(int, input().split()))
V = int(input())
dp = [0] * (V + 1)
for i in range(N):
    for j in range(K[i], V + 1):
        # 현재금액(dp[j])을 달성할수있는 최소동전개수를 넣어줘야한다
        if dp[j] != 0:
            dp[j] = min(dp[j - K[i]] + 1, dp[j])
        else:
            dp[j] = dp[j - K[i]] + 1

print(dp[V])

# 강의풀이
import sys

sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dy = [1000] * (m + 1)
    dy[0] = 0
    for i in range(n):
        for j in range(coin[i], m + 1):
            dy[j] = min(dy[j], dy[j - coin[i]] + 1)
    print(dy[m])
