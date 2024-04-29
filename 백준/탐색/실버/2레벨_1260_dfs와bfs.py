# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
n, m, v = map(int, input().split())

# 행렬 만들기
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (n + 1)


def dfs(v):
    visited1[v] = 1
    print(v, end=" ")
    for i in range(n + 1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)


def bfs(v):
    from collections import deque

    visited2 = [0] * (n + 1)
    visited2[v] = 1
    que = deque([v])
    while que:
        node = que.popleft()
        print(node, end=" ")
        for i in range(n + 1):
            if graph[node][i] == 1 and visited2[i] == 0:
                que.append(i)
                visited2[i] = 1


dfs(v)
print("")
bfs(v)
