"""
아기 상어 2
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	11843	5825	4383	47.374%
문제
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고,
이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자.

입력
첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다.
빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

출력
첫째 줄에 안전 거리의 최댓값을 출력한다.

예제 입력 1
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
예제 출력 1
2
예제 입력 2
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
예제 출력 2
2
"""
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 8방향 좌표설정
dy = [-1, +1, 0, 0, -1, -1, +1, +1]
dx = [0, 0, +1, -1, +1, -1, +1, -1]
res = 0


def bfs(y, x):
    q = deque()
    q.append((y, x))
    flag = False
    visited[y][x][0] = 1

    while q:
        _y, _x = q.popleft()

        for i in range(8):
            ty = dy[i] + _y
            tx = dx[i] + _x

            if ty < 0 or ty >= N or tx < 0 or tx >= M:
                continue

            # 방문하지않았다면 방문체크하고 큐에넣는다
            if visited[ty][tx][0] == 0:
                visited[ty][tx][0] = 1
                visited[ty][tx][1] = visited[_y][_x][1] + 1
                q.append((ty, tx))

                # 상어를 만나면 리턴
                if graph[ty][tx] == 1:
                    return visited[ty][tx][1]
    return 0


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
            _res = bfs(i, j)
            if res < _res:
                res = _res
print(res)
