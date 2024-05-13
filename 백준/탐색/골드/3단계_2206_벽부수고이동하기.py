"""
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데,
이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1
6 4
0100
1110
1000
0000
0111
0000

예제 출력 1
15

예제 입력 2
4 4
0111
1111
1111
1110

예제 출력 2
-1

포인트
3차원 배열로 부셨을떄와 안부셨을때글 구분하여 진행한다.
"""


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


"""
2024-05-13 복습
"""
from collections import deque

N, M = map(int, input().split())
graph = []
dy = [-1, +1, 0, 0]
dx = [0, 0, +1, -1]

for i in range(N):
    graph.append(list(map(int, input().rstrip())))
vistied = [[[0, 0] for _ in range(M)] for _ in range(N)]


def bfs(y, x):
    q = deque()
    q.append((x, y, 0))
    vistied[y][x][0] = vistied[y][x][1] = 1

    while q:
        y, x, punch = q.popleft()
        if y == N - 1 and x == M - 1:
            return vistied[y][x][punch]
        for i in range(4):
            ty = dy[i] + y
            tx = dx[i] + x

            if ty < 0 or ty >= N or tx < 0 or tx >= M:
                continue

            # 이미벽을 부순상태에서 또 벽을 만났을때
            if graph[ty][tx] == 1 and punch == 1:
                continue

            # 이동할곳이 벽이아니고 방문안했으면
            if graph[ty][tx] == 0 and vistied[ty][tx][punch] == 0:
                vistied[ty][tx][punch] = vistied[y][x][punch] + 1
                q.append((ty, tx, punch))

            # 처음 벽을 부셨을때
            elif graph[ty][tx] == 1 and vistied[ty][tx][1] == 0:
                vistied[ty][tx][1] = vistied[y][x][0] + 1
                q.append((ty, tx, 1))
    return -1


print(bfs(0, 0))
