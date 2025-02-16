import math


def 소수판별기(n):
    if n in [1, 2]:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print(소수판별기(4))
print(소수판별기(3))
print(소수판별기(7))
