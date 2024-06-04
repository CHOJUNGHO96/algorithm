"""
음식물 피하기 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	21143	10075	7995	47.720%
문제
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다.
이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.

이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다.
참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다.

통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.

선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

입력
첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ N×M)이 주어진다.
그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.

좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.

출력
첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.

예제 입력 1
3 4 5
3 2
2 2
3 1
2 3
1 1
예제 출력 1
4
"""
import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[0] * (M + 1) for _ in range(N + 1)]
visted = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, K + 1):
    r, c = map(int, input().split())
    arr[r][c] = 1
result = 0

dy = [+1, -1, 0, 0]
dx = [0, 0, +1, -1]


def bfs(i, j):
    # 큐에 넣는다
    q = deque()
    q.append((i, j))

    # 방문체크
    visted[i][j] = 1

    # 쓰레기가 있는 카운트
    cnt = 0

    # while문 반복
    while q:
        y, x = q.popleft()
        cnt += 1

        # 상,하,좌,우로 탐색을 진행하여 쓰레기가 있는곳의 위치만 큐에넣기
        for i in range(4):
            ty = dy[i] + y
            tx = dx[i] + x

            if ty < 0 or ty > N or tx < 0 or tx > M:
                continue

            if arr[ty][tx] == 1 and visted[ty][tx] == 0:
                visted[ty][tx] = 1
                q.append((ty, tx))
    return cnt


for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i][j] == 1 and visted[i][j] == 0:
            result = max(result, bfs(i, j))

print(result)
