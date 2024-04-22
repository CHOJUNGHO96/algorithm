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
# while True:
n = int(input())
# 행렬만들기
graph = []
for i in range(n):
    tmp_arr = list(map(int, input().split()))
    graph.append(tmp_arr)
    if max_value < max(tmp_arr):
        max_value = max(tmp_arr)

import copy

for mv in range(1, max_value + 1):
    tmp_graph = copy.deepcopy(graph)

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if tmp_graph[x][y] >= mv:
            tmp_graph[x][y] = 0
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        else:
            tmp_graph[x][y] = 0

    tmp = 0
    for i in range(n):
        for j in range(n):
            if tmp_graph[j][i] >= mv:
                dfs(j, i)
                tmp += 1
    if tmp > result:
        result = tmp

print(result)
