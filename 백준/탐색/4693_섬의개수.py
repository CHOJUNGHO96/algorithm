import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 풀이법
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    def dfs(y, x):
        if x < 0 or x >= w or y < 0 or y >= h:
            return False

        if graph[y][x] == 1:
            graph[y][x] = 0
            # 상,하,좌,우
            dfs(y - 1, x)
            dfs(y + 1, x)
            dfs(y, x - 1)
            dfs(y, x + 1)

            # 대각선 위 좌,우
            dfs(y + 1, x - 1)
            dfs(y + 1, x + 1)

            # 대각선 아래 좌,우
            dfs(y - 1, x - 1)
            dfs(y - 1, x + 1)

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1

print(result)


# bfs 풀이법

from collections import deque

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = []
    for i in range(m):
        graph.append(list(map(int, input().split())))

    def bfs(x, y):
        que = deque([(x, y)])
        while que:
            move = que.popleft()
            if move[0] < 0 or move[0] >= n or move[1] < 0 or move[1] >= m:
                continue

            x = move[0]
            y = move[1]
            if graph[y][x] == 1:
                # 상하 좌우
                que.append((x + 1, y))
                que.append((x - 1, y))
                que.append((x, y + 1))
                que.append((x, y - 1))

                # 대각선
                que.append((x + 1, y + 1))
                que.append((x - 1, y + 1))
                que.append((x + 1, y - 1))
                que.append((x - 1, y - 1))

                graph[move[1]][move[0]] = 0

    result = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(j, i)
                result += 1
    print(result)
