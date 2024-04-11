# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y, cnt):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        result[cnt] += 1
        dfs(x - 1, y, cnt)
        dfs(x + 1, y, cnt)
        dfs(x, y - 1, cnt)
        dfs(x, y + 1, cnt)


result = {}
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            result.update({cnt: 0})
            dfs(i, j, cnt)
print(cnt)
for i in sorted(list(result.values())):
    print(i)
