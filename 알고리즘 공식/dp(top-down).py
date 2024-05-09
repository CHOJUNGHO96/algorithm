"""
네트워크 선자르기
현수는 네트워크 선을 1m, 2m 길이르 갖는 선으로 자르려고 합니다.
예를 들어 4m의 네트워크 선이 주어진다면
1) 1m + 1m + 1m + 1m
2) 2m + 1m + 1m
3) 1m + 2m + 1m
4) 1m + 1m + 2m
5) 2m + 2m
의 5가지 방법을 생각할 수 있습니다. (2)와 (3)과 (4)의 경우 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각한다.
그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?

입력설명
첫째 줄은 네트워크 선의 총 길이인 자연수 N(3<= N <= 100)이 주어집니다

출력설명
첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.

입력에제 1
7

출력예제 1
21

포인트
1m, 2m 길이로 자른다는 조건을토대로 점화식을 만들어 진행한다.
점화식 f(n) = f(n-1) + f(n-2)
top-down 방식이므로 재귀, 메모제이션을 통하여 dfs방식으로 접근한다
재귀가 끝나는 경우는 이미 메모리에 적재했을때 끝낸다
"""


def dfs(v):
    if arr[v] != -1:
        return arr[v]

    arr[v] = dfs(v - 1) + dfs(v - 2)
    return arr[v]


N = int(input())
arr = [-1] * (N + 1)
arr[1] = 1
arr[2] = 2
print(dfs(N))
