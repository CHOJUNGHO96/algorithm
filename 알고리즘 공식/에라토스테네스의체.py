import math


def 에라토스테네의체(n):
    """
    1. 제곱근까지 루프실행
    2. 자기를 제외한 해당 인덱스의 배수들이 소수인지 판별
    """
    arr = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if not arr[i]:
            continue
        count = 2
        while i * count < n:
            arr[i * count] = False
            count += 1

    for i in range(2, n):
        if arr[i]:
            print(i)


에라토스테네의체(10)
