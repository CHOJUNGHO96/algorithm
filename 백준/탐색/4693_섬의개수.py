import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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
