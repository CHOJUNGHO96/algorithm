from collections import deque


def 방향탐색(열, 행, 맵, 좌표, 방문):
    # [1, 0, 1, 1, 1]
    # [1, 0, 1, 0, 1]
    # [1, 0, 1, 1, 1]
    # [1, 1, 1, 0, 1]
    # [0, 0, 0, 0, 1]

    n, m = len(맵), len(맵[0])  # 맵의 크기를 동적으로 계산
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향

    for d열, d행 in directions:
        next_열, next_행 = 열 + d열, 행 + d행
        # 맵 범위 안에 있고, 벽이 아니며, 아직 방문하지 않은 곳인지 체크
        if 0 <= next_열 < n and 0 <= next_행 < m and 맵[next_열][next_행] == 1 and not 방문[next_열][next_행]:
            좌표.append((next_열, next_행))
            맵[next_열][next_행] = 맵[열][행] + 1  # 거리 증가
            방문[next_열][next_행] = True  # 방문 체크


def solution(맵):
    n, m = len(맵), len(맵[0])  # 맵의 크기를 동적으로 계산
    방문 = [[False] * m for _ in range(n)]  # 방문한 위치를 저장할 리스트 초기화
    좌표 = deque([(0, 0)])
    방문[0][0] = True  # 시작점 방문 체크

    while 좌표:
        열, 행 = 좌표.popleft()
        방향탐색(열, 행, 맵, 좌표, 방문)

    return 맵[-1][-1] if 맵[-1][-1] != 1 else -1  # 목적지에 도달했는지 체크


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
