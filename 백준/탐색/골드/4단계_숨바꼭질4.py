"""
숨바꼭질 4 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	47908	15982	11249	30.854%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1
5 17
예제 출력 1
4
5 10 9 18 17
예제 입력 2
5 17
예제 출력 2
4
5 4 8 16 17

포인트
1. visited 에 소요시간 지나쳤던 노드를넣어준다.
2. 출력이 5 10 9 18 17 이런식으로 지나쳤던 노드들을 출력해야하므로 while문으로 연결된 노드들을 따로 q에담아두고 reverse한후 출력한다.
"""
from collections import deque

n, k = map(int, input().split())
MAX = 100001
visited = [[-1, 0] for _ in range(MAX)]


def bfs():
    q = deque()
    q.append(n)
    visited[n][0] = 0
    while q:
        tmp = q.popleft()
        if tmp == k:
            break
        next_time = visited[tmp][0] + 1
        for next_val in [tmp - 1, tmp + 1, tmp * 2]:
            if 0 <= next_val < MAX:
                if visited[next_val][0] == -1:
                    q.append(next_val)
                    visited[next_val][0] = next_time
                    visited[next_val][1] = tmp  # 직전에 지나쳤던 노드값을 넣어준다


bfs()
q = deque()
q.append(k)

if n == k:  # 수빈이와 동생의 위치가같으면 이동할필요가 없으므로 바로 출력
    print(0)
    print(k)
else:  # 물려있는 노드들을 큐에 담고 역순으로 출력해준다.
    tmp = visited[k][1]
    q.append(tmp)
    while tmp != n:  # tmp와 수빈이의 위치가 다를때까지 루프진행
        tmp = visited[tmp][1]
        q.append(tmp)

    q.reverse()
    print(visited[k][0])
    print(*q)
