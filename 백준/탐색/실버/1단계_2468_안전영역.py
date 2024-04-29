# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
result = 0
max_value = 0
n = int(input())

# 행렬만들기
graph = []
for i in range(n):
    tmp_arr = list(map(int, input().split()))
    graph.append(tmp_arr)
    if max_value < max(tmp_arr):
        max_value = max(tmp_arr)


for mv in range(1, max_value + 1):
    visited = [[False] * n for _ in range(n)]

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if graph[x][y] >= mv and not visited[x][y]:
            visited[x][y] = True
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

    tmp = 0
    for i in range(n):
        for j in range(n):
            if graph[j][i] >= mv and not visited[j][i]:
                dfs(j, i)
                tmp += 1
    if tmp > result:
        result = tmp

print(result)
