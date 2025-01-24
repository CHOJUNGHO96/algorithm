from itertools import permutations
import math

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            if is_prime_number(num):
                answer.add(num)
    return len(answer)


# Test
print(solution("011"))
# print(solution("17"))
