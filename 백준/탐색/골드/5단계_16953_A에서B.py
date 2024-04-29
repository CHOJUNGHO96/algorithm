"""`
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

2 162
2 → 4 → 8 → 81 → 162
5

4 42
-1

100 40021
100 → 200 → 2001 → 4002 → 40021
5
"""
# 2 162
# 2 → 4 → 8 → 81 → 162
# 5

from collections import deque

A, B = map(int, input().split())


def bfs():
    que = deque()
    que.append((A * 2, int(str(A) + "1"), 2))
    while que:
        left_v, right_v, count = que.popleft()
        if left_v == B or right_v == B:
            return count
        if left_v < B:
            que.append((left_v * 2, int(str(left_v) + "1"), count + 1))

        if right_v < B:
            que.append((right_v * 2, int(str(right_v) + "1"), count + 1))
    return -1


print(bfs())


# 다른사람풀이
count = 1

while A < B:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    count += 1

if A == B:
    print(count)
else:
    print(-1)
