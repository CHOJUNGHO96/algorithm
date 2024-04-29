# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

t = int(input())


def dfs(x, y):
    if x < 0 or x > n or y < 0 or y > m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    return True


for _ in range(t):
    m, n, k = map(int, input().split())

    # 행렬 만들기
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # print(graph)

    result = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1

    print(result)
