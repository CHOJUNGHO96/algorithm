import math


def 소수찾기(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def solution1(n):
    정답 = 0
    for i in range(2, n + 1):
        if 소수찾기(i):
            정답 += 1
    return 정답


def solution(n):
    # 에라토스테네의체 사용
    배열 = [True for _ in range(n + 1)]
    정답 = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if 배열[i]:
            카운트 = 2
            while i * 카운트 <= n:
                배열[i * 카운트] = False
                카운트 += 1

    for i in range(2, n + 1):
        if 배열[i]:
            정답 += 1
    return 정답


# print(solution(10))
print(solution(5))
