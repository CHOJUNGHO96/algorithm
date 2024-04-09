# 4 5
# 00110
# 00011
# 11111
# 00000
"""
1. 이미 탐색한곳은 1로변경하여 다시 탐색안하도록
"""
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 종료조건 1
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    # 종료조건 2
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)
