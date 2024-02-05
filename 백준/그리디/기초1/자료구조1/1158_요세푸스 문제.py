from collections import deque

n, k = map(int, input().split())
정답 = []

# (1, 2, 3, 4, 5, 6, 7)
큐 = deque(range(1, n + 1))
while 큐:
    for _ in range(k - 1):
        큐.append(큐.popleft())
    정답.append(큐.popleft())

# <3, 6, 2, 7, 5, 1, 4>
print("<{}>".format(", ".join(map(str, 정답))))
