# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
n = int(input())
m = int(input())


graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)

result = 0


def dfs(v):
    visited[v] = 1
    global result
    result += 1
    for i in range(n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)
print(result - 1)
# print(sum(visited)-1) 이걸로 하면 result 없어도된다
