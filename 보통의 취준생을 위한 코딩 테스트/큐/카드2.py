import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()


def soultion(n):
    for i in range(1, n + 1):
        queue.append(i)

    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())


soultion(n)
print(queue[0])
