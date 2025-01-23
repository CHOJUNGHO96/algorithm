import sys

sys.setrecursionlimit(10**6)


def solution1(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567
    return arr[-1]


def solution2(n):
    answer = [0, 1]

    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)

    return answer[-1]


def solution4(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def solution(n):
    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1234567

    return b


print(solution(100000))
