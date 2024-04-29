"""
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다.
그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다.
(단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

4
9
"""

import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[False] * (M) for _ in range(N)]
graph = []
dx = [0, 0, +1, -1]
dy = [+1, -1, 0, 0]
for i in range(N):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    visited[y][x] = True
    que = deque([])
    que.append((x, y))
    count = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            _x = dx[i] + x
            _y = dy[i] + y
            if _x < 0 or _x >= M or _y < 0 or _y >= N:
                continue
            if graph[_y][_x] == 1 and not visited[_y][_x]:
                que.append([_x, _y])
                visited[_y][_x] = True
                count += 1
    return count


def dfs(x, y):
    global tmp
    tmp += 1
    visited[y][x] = True
    for i in range(4):
        _x = dx[i] + x
        _y = dy[i] + y
        if _x < 0 or _x >= M or _y < 0 or _y >= N:
            continue

        if graph[_y][_x] == 1 and not visited[_y][_x]:
            dfs(_x, _y)


bfs_result = [0, 0]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs_result[0] += 1
            bfs_result[1] = max(bfs_result[1], bfs(j, i))

visited = [[False] * (M) for _ in range(N)]
dfs_result = [0, 0]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            tmp = 0
            dfs_result[0] += 1
            dfs(j, i)
            dfs_result[1] = max(dfs_result[1], tmp)


print(f"bfs정답\n{bfs_result[0]}\n{bfs_result[1]}\n")
print(f"dfs정답\n{dfs_result[0]}\n{dfs_result[1]}\n")
