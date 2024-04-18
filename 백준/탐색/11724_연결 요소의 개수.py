import sys

# 인접행렬 풀이방식
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

# 행렬구하기
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)


def dfs(v):
    visited[v] = 1
    for i in range(n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)


result = 0
for i in range(n + 1):
    if i == 0:
        continue
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)


# 인접리스트 풀이방식
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

# 행렬구하기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


# [[], [2,5],[5,1],[4],[3,6],[2,1],[4]]
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


result = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)
