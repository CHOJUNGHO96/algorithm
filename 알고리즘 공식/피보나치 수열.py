def 피보나치(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def 피보나치(n):
    arr = [0] * n
    arr[0], arr[1] = 1, 1
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1]


print(피보나치(5))


print(피보나치(5))
