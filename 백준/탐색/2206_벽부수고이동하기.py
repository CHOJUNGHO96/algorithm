from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    que = deque()
    que.append((0, 0, 0))

    visited[0][0][0] = 1

    while que:
        x, y, punch = que.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][punch]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 이동할곳이 벽이고, 벽을부순적이없는경우
            if graph[nx][ny] == 1 and punch == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                que.append((nx, ny, 1))

            # 이동할곳이 벽이아니고 한번도 방문안한경우
            elif graph[nx][ny] == 0 and visited[nx][ny][punch] == 0:
                visited[nx][ny][punch] = visited[x][y][punch] + 1
                que.append((nx, ny, punch))

    return -1


print(bfs())
