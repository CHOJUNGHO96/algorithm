"""
숨바꼭질 3
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	106236	27322	18202	24.099%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1
5 17
예제 출력 1
2

포인트
1. visited 에 방문횟수를 기록한다.
2. X * 2 나올때는 횟수를 증가시키면 안되므로 기존에있던 횟수 그대로 대입해준다.
3. X * 2는 횟수를증가시키지 않으므로  next_time 값이 방문할 노드의 횟수보다 적을수도있다 그래서 next_time값이 방몬할노드의 횟수(visited[next_val])
보다 적을때 visited[next_val]를 next_time으로 변경해줘야한다.
"""
from collections import deque

n, k = map(int, input().split())
MAX = 100001
visited = [-1 for _ in range(MAX)]  # 방문횟수 체크를위한 세팅


def bfs():
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        tmp = q.popleft()
        next_time = visited[tmp] + 1  # 해당노드 방문했을때 증가값
        for idx, next_val in enumerate([tmp - 1, tmp + 1, tmp * 2]):
            if 0 <= next_val < MAX:
                if visited[next_val] == -1 or visited[next_val] >= next_time:  # 처음 방문했을때와 next_time 더낮은값이 있을경우 bfs실행
                    if visited[next_val] == -1:
                        q.append(next_val)
                    if idx != 2:  # X * 2 가 아닐경우에는 next_time값 그대로 들어간다.
                        visited[next_val] = next_time
                    else:  # X * 2 일경우에는 -1을해줘서 기존 next_time값 그대로 들어가게한다.
                        visited[next_val] = next_time - 1


bfs()
print(visited[k])
